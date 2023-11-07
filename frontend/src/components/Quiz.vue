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

const quizStore = useQuiz();
const questions = quizStore.selectedQuiz.questions;

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
  quizStore.setQuizStatus("NOT_STARTED");
};
</script>
