<template>
  <h2 class="text-center">{{ question }}</h2>
  <div
    v-for="(choice, index) in props.choices"
    :key="index"
    class="flex justify-content-center mt-3"
  >
    <RadioButton
      v-model="state.selectedChoice"
      :inputId="choice.key"
      name="dynamic"
      :value="choice.name"
    />
    <label :for="choice.key" class="ml-2 text-xl text-center">{{ choice.name }}</label>
  </div>
</template>

<script setup>
import { reactive } from "vue";

const props = defineProps({
  question: {
    type: String,
    required: true,
  },
  choices: {
    type: Array,
    required: true,
  },
  onAnswer: {
    type: Function,
    required: true,
  },
});

const state = reactive({
  selectedChoice: null,
});

const question = "What is the capital of France?";
</script>
