<template>
    <div id="questions">
        <div class="question-list">
            <div 
                class="question-btn"
                v-for="(opt, index) in questions" 
                :key="index" 
                @click="setQuizToEdit(index)"
            >
                {{ index + 1 }}
                <button @click="deleteQuestion(index)">X</button>
            </div>
        </div>
    </div>
    <div class="form">
        <label for="question">Question</label>
        <input v-model="question" id="question" type="text">

        <label for="options">Options</label>
        <div id="options">
            <div v-for="(opt, index) in options" :key="index" class="option-item">
                <span>{{ opt }}</span>
                <button @click="prepareEditOption(index)">Edit</button>
                <button @click="deleteOption(index)">Delete</button>
            </div>
        </div>

        <div class="add-option">
            <input v-model="option" id="option" type="text" :placeholder="editMode ? 'Edit option' : 'Add an option'">
            <button @click="editMode ? confirmEdit() : addOption()">
                {{ editMode ? 'Edit option' : 'Add option' }}
            </button>
        </div>
        <div class="answer-select">
            <label for="answer">Answer</label>
            <select v-model="selectedAnswer" id="answer">
                <option v-for="(opt, index) in options" :key="index" :value="opt">{{ opt }}</option>
            </select>
        </div>
        <div class="text-left">
            <Button @click="editModeQuestion ? confirmEditQuestion() : addQuestionToQuiz()">
                {{ editModeQuestion ? 'Edit question' : 'Add question' }}
            </Button>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';

const question = ref('');
const option = ref('');
const options = ref([]);
const editMode = ref(false);
const editModeQuestion = ref(false);
const editIndex = ref(null);
const editIndexQuestion = ref(null);
const selectedAnswer = ref('');
const questions = ref([]);

const addOption = () => {
    if (option.value.trim()) {
        options.value.push(option.value);
        option.value = ''; // Limpa o campo de input
    }
};

const prepareEditOption = (index) => {
    editMode.value = true;
    editIndex.value = index;
    option.value = options.value[index]; // Preenche o campo de input com o valor atual
};

const confirmEdit = () => {
    if (option.value.trim() && editIndex.value !== null) {
        options.value[editIndex.value] = option.value; // Atualiza a opção
        option.value = ''; // Limpa o campo de input
        editMode.value = false;
        editIndex.value = null;
    }
};

const deleteOption = (index) => {
    options.value.splice(index, 1);
    if (editIndex.value === index) {
        editMode.value = false; // Sai do modo de edição se a opção for excluída
        option.value = '';
    }
};

const addQuestionToQuiz = () => {
    if (!question._value.trim() || options.value.length < 2 || !selectedAnswer._value.trim()) {
        return;
    }
    questions.value.push({
        question: question._value, 
        options: options._value,
        answer: selectedAnswer._value
    });
    clearForm();
}

const confirmEditQuestion = () => {
    if (!question._value.trim() || options.value.length < 2 || !selectedAnswer._value.trim()) {
        return;
    }
    questions.value[editIndexQuestion.value] = {
        question: question._value, 
        options: options._value,
        answer: selectedAnswer._value
    }
    clearForm();
    editModeQuestion.value = false;
    editIndexQuestion.value = null;
};

const prepareEditQuestion = (index) => {
    editModeQuestion.value = true;
    editIndexQuestion.value = index;
};


const clearForm = () => {
    options.value = [];
    question.value = '';
    option.value = '';
    editMode.value = false;
    editIndex.value = null;
};

const getAllQuestions = () => {
    return questions._rawValue;
};

const setQuizToEdit = (index) => {
    const data = questions._value[index];
    options.value = data.options;
    question.value = data.question;
    selectedAnswer.value = data.answer;
    prepareEditQuestion(index);
};

const deleteQuestion = (index) => {
    questions.value.splice(index, 1);
};

const deleteAllQuestions = () => {
    questions.value = [];
};

defineExpose({
    getAllQuestions,
    deleteAllQuestions
});
</script>

<style scoped>
/* Estilização geral do formulário */
.form {
    display: flex;
    flex-direction: column;
    gap: 15px;
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    font-size: 1.2rem;
}

/* Estilização dos botões e inputs na seção de adicionar opção */
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
    background-color: gray;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.add-option button:hover {
    background-color: #585858;
}

/* Estilização das opções */
#options {
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.option-item {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: black;
    font-size: 1rem;
    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.05);
}

.option-item span {
    flex: 1;
    padding-right: 10px;
}

.option-item button {
    margin-left: 10px;
    padding: 5px 10px;
    font-size: 0.9rem;
    cursor: pointer;
    border: none;
    border-radius: 3px;
    transition: background-color 0.3s ease;
}

.option-item button:first-child {
    background-color: #007bff;
    color: white;
}

.option-item button:first-child:hover {
    background-color: #0056b3;
}

.option-item button:last-child {
    background-color: #dc3545;
    color: white;
}

.option-item button:last-child:hover {
    background-color: #a71d2a;
}

/* Estilização da lista de perguntas */
.question-list {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    margin: 10px 0;
}

.question-btn {
    padding: 10px 20px;
    font-size: 1rem;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    background-color: #18af31;
    color: white;
    transition: background-color 0.3s ease;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.question-btn:hover {
    background-color: #119427;
}

/* Estilização do seletor de resposta */
.answer-select {
    display: flex;
    flex-direction: column;
    gap: 5px;
}

.answer-select select {
    padding: 8px;
    font-size: 1rem;
    border-radius: 5px;
    border: 1px solid #ccc;
}

/* Estilização de labels */
label {
    font-weight: bold;
    font-size: 1rem;
}

/* Estilização geral dos inputs */
input {
    padding: 10px;
    font-size: 1rem;
    border: 1px solid #ccc;
    border-radius: 5px;
    width: 100%;
}

/* Alinhamento de botão à direita */
.text-left {
    display: flex;
    flex-direction: row-reverse;
}
</style>
