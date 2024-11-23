<template>
    <div class="form">
        <label for="title">Title</label>
        <input v-model="title" id="title" type="text">
        <label for="description">Description</label>
        <input v-model="description" id="description" type="text">
        <label for="category">Select Category</label>
        <select v-model="category" id="category">
            <option value="" disabled>Select a category</option>
            <option v-for="cat in categories" :key="cat.id" :value="cat.id">
                {{ cat.name }}
            </option>
        </select>
        <label for="difficulty">Select Difficulty</label>
        <select v-model="difficulty" id="difficulty">
            <option value="" disabled>Select an option</option>
            <option value="easy">Easy</option>
            <option value="medium">Medium</option>
            <option value="hard">Hard</option>
        </select>
        <label for="questions">Questions</label>
        <div >
            <AddQuestion ref="addQuestion"/>
        </div>
        <div>
            <Button @click="addQuiz()" label="Add quiz"></Button>
        </div>
    </div>
</template>

<script setup>
    import { ref } from 'vue';
    import AddQuestion from "@/components/AddQuestion.vue";
    import { useQuiz } from "@/store/modules/quiz";
    import { useSession } from "@/store/modules/session";

    const addQuestion = ref(null);

    const quizStore = useQuiz();
    const sessionStore = useSession();

    const title = ref('');
    const description = ref('');
    const category = ref('');
    const categories = ref([]);
    const difficulty = ref('');
    const user_id = sessionStore.getUserId();
    
    quizStore.getAllCategories().then((result) => {
        categories.value = result;
    });

    const cleanForm = () => {
        title.value = '';
        description.value = ''; 
        category.value = '';
        difficulty.value = ''; 
    }

    const addQuiz = () => {
        let questions = []; 
        addQuestion.value.getAllQuestions().forEach(a => {
            const currentOption = a.options.join(', ');
            questions.push({
                question: a.question,
                options: currentOption,
                answer: a.answer
            });
        });
        const data = {
            quiz: {
                title: title.value,
                description: description.value,
                category: category.value,
                difficulty: difficulty.value,
                owner_id: user_id
            },
            questions: questions,
        }
        try {
            quizStore.createNewQuiz(data);
            cleanForm();
            addQuestion.value.deleteAllQuestions();
            alert('your quiz saved')
        } catch (err) {
            console.log('error when savin quiz: ', err)
        }
    }

</script>

<style scoped>
.form {
    display: flex;
    flex-direction: column;
    gap: 15px;
    max-width: 400px;
    margin: 0 auto 50px; /* Centraliza horizontalmente e adiciona margem inferior */
    padding: 20px;
    font-size: 1.2rem;
    border: 1px solid #ddd;
    border-radius: 8px;
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
}

label {
    font-weight: bold;
    font-size: 1rem;
}

input {
    padding: 10px;
    font-size: 1rem;
    border: 1px solid #ccc;
    border-radius: 5px;
    width: 100%;
}

.text-left {
    display: flex;
    flex-direction: row-reverse;
}

.question-list {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    margin: 10px 0;
}

.question-list .question-btn {
    padding: 10px 20px;
    font-size: 1rem;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    background-color: #007bff;
    color: white;
    display: flex;
    align-items: center;
    justify-content: space-between;
    transition: background-color 0.3s ease;
}

.question-list .question-btn:hover {
    background-color: #0056b3;
}

.option-item {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px;
    font-size: 1rem;
    background-color: #ffffff;
    border: 1px solid #ddd;
    border-radius: 5px;
    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.05);
}

.option-item span {
    flex: 1;
    padding-right: 10px;
}

.add-option {
    display: flex;
    gap: 10px;
}

.add-option input {
    flex: 1;
    padding: 10px;
    font-size: 1rem;
    border: 1px solid #ccc;
    border-radius: 5px;
}

.add-option button {
    padding: 10px 12px;
    font-size: 1rem;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.add-option button:hover {
    background-color: #0056b3;
}

select {
  padding: 10px;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 5px;
  width: 100%;
}

select:focus {
  outline: none;
  border-color: #007bff;
  box-shadow: 0 0 4px rgba(0, 123, 255, 0.5);
}
</style>
