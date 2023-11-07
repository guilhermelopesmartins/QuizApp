<template>
  <div class="text-center mb-2 text-2xl">Select Category</div>
  <div class="text-center">
    <SelectButton text raised rounded class="large" severity="info" v-model="state.selectCategory"  :options="quizStore.categories.map(c => c.name)" aria-labelledby="basic" />
  </div>
</template>

<script setup>
import { reactive, watch } from 'vue';
import { useQuiz } from '@/store/modules/quiz';

const quizStore = useQuiz();

const state = reactive({
    selectCategory: null,
});

watch(
  () => state.selectCategory,
  async (value) => {
    quizStore.setCategory(value);
  }
);

</script>
