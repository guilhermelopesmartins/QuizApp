<template>
  <div class="text-center mb-2 text-2xl">Select Quiz</div>
  <div class="text-center">
    <SelectButton text raised rounded class="large" severity="info" v-model="state.selectQuiz"  :options="quizStore.quizzes.map(q => q.title)" aria-labelledby="basic" />
  </div>
</template>

<script setup>
import { reactive, watch } from 'vue';
import { useQuiz } from '@/store/modules/quiz';

const quizStore = useQuiz();

const state = reactive({
    selectQuiz: null,
});

watch(
  () => state.selectQuiz,
  async (value) => {
    const q = quizStore.quizzes.find(q => q.title === value)
    console.log(q)
    quizStore.setSelectedQuiz(q);
  }
);

</script>
