<template>
  <div class="text-center mb-2 text-2xl">Select Quiz</div>
  <div class="text-center">
    <SelectButton text raised rounded class="large" severity="info" v-model="state.selectQuiz"  :options="state.categories" aria-labelledby="basic" />
  </div>
</template>

<script setup>
import { reactive, watch } from 'vue';
import { useQuiz } from '@/store/modules/quiz';

const quizStore = useQuiz();

const state = reactive({
    categories: ["test", "adsf", "asdf", "as"],
    selectQuiz: null,
});

watch(
  () => state.selectQuiz,
  async (value) => {
    quizStore.setCategory(value);
  }
);

</script>
