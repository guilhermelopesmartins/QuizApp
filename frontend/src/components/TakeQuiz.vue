<template>
    <!-- <SelectDifficulty v-if="quizStore.quizStatus !== 'STARTED' && quizStore.quizStatus !== 'FINISHED'" /> -->
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
    import { onMounted } from "vue";
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

    const quizStore = useQuiz();

    const setQuizStatus = (status) => {
        quizStore.setQuizStatus(status);
    };

    onMounted(async () => {
        const quizzesResponse = await quizApi.getAllQuizzes();
        const usersResponse = await userApi.getAllUsers();

        const categories = quizzesResponse.data.value.map((quiz) => quiz.category);

        quizStore.setQuizzes(quizzesResponse.data.value);
        quizStore.setCategories(categories);
        quizStore.setUsers(usersResponse.data.value)
    });

</script>