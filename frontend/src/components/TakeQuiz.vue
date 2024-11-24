<template>
    <!-- <SelectDifficulty v-if="quizStore.quizStatus !== 'STARTED' && quizStore.quizStatus !== 'FINISHED'" /> -->
    <div class="text-center">
        <Button v-if="quizStore.quizStatus !== 'STARTED' && quizStore.quizStatus !== 'FINISHED'" :disabled="isLoading" @click="generateQuiz" label="Generate Quizzes"></Button>
    </div>
    <div v-if="quizStore.quizStatus !== 'STARTED' && quizStore.quizStatus !== 'FINISHED'" class="mt-6">
        <SelectCategories />
    </div>
    <div v-if="quizStore.quizStatus !== 'STARTED' && quizStore.quizStatus !== 'FINISHED' && quizStore.selectedCategory" class="mt-6">
        <SelectQuiz />
    </div>
    <div v-if="quizStore.quizStatus !== 'STARTED' && quizStore.quizStatus !== 'FINISHED'" class="text-center mt-6">
        <Button @click="() => setQuizStatus('STARTED')" raised text label="Start!"></Button>
    </div>
    <div v-if="quizStore.quizStatus === 'STARTED' || quizStore.quizStatus === 'FINISHED'" class="mt-6">
        <Quiz />
    </div>
</template>

<script setup>
    import { ref, onMounted } from "vue";
    import SelectCategories from "@/components/SelectCategories.vue";
    import SelectDifficulty from "@/components/SelectDifficulty.vue";
    import SelectQuiz from "@/components/SelectQuiz.vue";
    import Quiz from "@/components/Quiz.vue";
    
    import QuizApi from "@/api/quiz";
    const quizApi = new QuizApi();
    
    import UserApi from "@/api/user";
    const userApi = new UserApi();

    import { useQuiz } from "@/store/modules/quiz";
    import { useSession } from "@/store/modules/session";

    const sessionStore = useSession(); 

    const quizStore = useQuiz();

    const setQuizStatus = (status) => {
        quizStore.setQuizStatus(status);
    };

    const isLoading = ref(false);

    const generateQuiz = async() => {
        isLoading.value = true;
        const generatedQuestion = await quizApi.getGeneratedQuestions();
        const quizData = {
                title: `Quiz generated ${quizStore.quizzes.length + 1}`,
                description: '',
                category_id: 100,
                difficulty: 'Easy',
                owner_id: sessionStore.getUserId(),
            };
        const newQuiz = await quizApi.createQuiz(quizData);
        console.log(generatedQuestion);
        await generatedQuestion.data._value?.results.forEach(async(g) => {
            g.incorrect_answers.push(g.correct_answer);
            const question = {
                    question_text: g.question,
                    options: g.incorrect_answers.join(','),
                    correct_answer: g.correct_answer,
                    quiz_id: newQuiz.data._value.id
            };
            await quizApi.createQuestion(question);
        });
        const quizzesResponse = await quizApi.getAllQuizzes();
        await quizStore.setQuizzes(quizzesResponse.data.value);
        isLoading.value = false;
    }

    onMounted(async () => {
        const quizzesResponse = await quizApi.getAllQuizzes();
        const usersResponse = await userApi.getAllUsers();

        const categories = quizzesResponse.data.value.map((quiz) => quiz.category);

        quizStore.setQuizzes(quizzesResponse.data.value);
        quizStore.setCategories(categories);
        quizStore.setUsers(usersResponse.data.value)
    });

</script>