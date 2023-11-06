<template>
  <div class="mb-2 text-center text-2xl">Difficulty</div>
  <div class="grid text-center">
    <div class="col" v-for="difficulty in state.difficulties">
      <Button text raised rounded class="large" severity="info" @click="selectDifficulty(difficulty)" :label="difficulty" />
    </div>
  </div>
</template>

<script setup>
import { reactive } from 'vue';
import { useQuiz } from '@/store/modules/quiz';

const quizStore = useQuiz();

const state = reactive({
    difficulties: ["Easy", "Medium", "Hard"],
});

const selectDifficulty = (difficulty) => {
  quizStore.setDifficulty(difficulty);
};
</script>
