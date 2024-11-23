<template>
  <div>
    <div v-if="quizStore.quizStatus !== 'FINISHED'">
      <h1 class="text-center">Quiz</h1>
      <p class="text-center" v-if="currentQuestionIndex < questions.length">
        {{ currentQuestionIndex + 1 }} / {{ questions.length }}
      </p>

      <ViewQuestion
        v-for="(question, index) in questions"
        :question="question"
        :choices="question.choices"
        :onAnswer="handleAnswer"
      />

      <div  class="text-center mt-6">
        <Button
          @click="finishQuiz"
          class="text-2xl"
          raised
          text
          label="Finish!"
        ></Button>
      </div>
    </div>

    <div v-if="quizStore.quizStatus === 'FINISHED'" class="text-center">
      <h2>Quiz Completed!</h2>
      <p>Your Score: {{ score }} / {{ questions.length }}</p>
      <div class="form-group">
        <textarea
          placeholder="Leave your feedback here..."
          class="custom-textarea"
          v-model="feedback"
        ></textarea>
      </div>
      <Button
        @click="backToQuizSelection"
        class="text-2xl"
        raised
        text
        label="Back to Quiz Selection"
      ></Button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import ViewQuestion from "./ViewQuestion.vue";
import { useQuiz } from "@/store/modules/quiz";
import { useSession } from "@/store/modules/session";

const quizStore = useQuiz();
const sessionStore = useSession();
const questions = quizStore.selectedQuiz.questions;

const feedback = ref('');

const currentQuestionIndex = 0;
const score = ref(0);

const handleAnswer = (isCorrect) => {
  if (isCorrect) {
    score.value++;
  }

  if (currentQuestionIndex.value < questions.length - 1) {
    currentQuestionIndex.value++;
  }
};

const finishQuiz = () => {
  quizStore.setQuizStatus("FINISHED");
};

const backToQuizSelection = () => {
  const data = 
    {
      feedback_text: feedback.value,
      user_id: sessionStore.getUserId()
    }
  quizStore.sendFeedBack(data);
  quizStore.setCategory(null);
  quizStore.setQuizStatus("NOT_STARTED");
};

// const questions = ref([
//   {
//     question: "What is the capital of France?",
//     choices: [
//       { name: "Accounting", key: "A" },
//       { name: "Marketing", key: "M" },
//       { name: "Production", key: "P" },
//       { name: "Research", key: "R" },
//     ],
//     correctAnswer: "Paris",
//   },
//   {
//     question: "What is the capital of Spain?",
//     choices: [
//       { name: "Accounting", key: "A" },
//       { name: "Marketing", key: "M" },
//       { name: "Production", key: "P" },
//       { name: "Research", key: "R" },
//     ],
//     correctAnswer: "Madrid",
//   },
//   {
//     question: "What is the capital of Germany?",
//     choices: [
//       { name: "Accounting", key: "A" },
//       { name: "Marketing", key: "M" },
//       { name: "Production", key: "P" },
//       { name: "Research", key: "R" },
//     ],
//     correctAnswer: "Berlin",
//   },
//   {
//     question: "What is the capital of Italy?",
//     choices: [
//       { name: "Accounting", key: "A" },
//       { name: "Marketing", key: "M" },
//       { name: "Production", key: "P" },
//       { name: "Research", key: "R" },
//     ],
//     correctAnswer: "Rome",
//   },
//   {
//     question: "What is the capital of Portugal?",
//     choices: [
//       { name: "Accounting", key: "A" },
//       { name: "Marketing", key: "M" },
//       { name: "Production", key: "P" },
//       { name: "Research", key: "R" },
//     ],
//     correctAnswer: "Lisbon",
//   },
//   {
//     question: "What is the capital of Poland?",
//     choices: [
//       { name: "Accounting", key: "A" },
//       { name: "Marketing", key: "M" },
//       { name: "Production", key: "P" },
//       { name: "Research", key: "R" },
//     ],
//     correctAnswer: "Warsaw",
//   },
//   {
//     question: "What is the capital of Sweden?",
//     choices: [
//       { name: "Accounting", key: "A" },
//       { name: "Marketing", key: "M" },
//       { name: "Production", key: "P" },
//       { name: "Research", key: "R" },
//     ],
//     correctAnswer: "Stockholm",
//   },
// ]);
</script>

<style scoped>

.custom-textarea {
  width: 100%; /* Largura total para se alinhar com outros inputs */
  max-width: 400px; /* Limita a largura, semelhante aos inputs */
  height: 120px; /* Altura maior que o input padrão */
  padding: 10px;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 5px;
  resize: vertical; /* Permite redimensionar verticalmente */
  box-sizing: border-box; /* Inclui padding na largura */
}

.custom-textarea:focus {
  outline: none;
  border-color: #007bff; /* Altera a cor da borda no foco */
  box-shadow: 0 0 5px rgba(0, 123, 255, 0.5);
}
</style>