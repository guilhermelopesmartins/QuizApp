<template>
  <h2 class="text-center">{{ question.question_text }}</h2>
  <div
    v-for="(choice, index) in props.question.options.split(',')"
    :key="index"
    class="flex justify-content-center mt-3"
  >
    <RadioButton
      v-model="state.selectedChoice"
      :inputId="index"
      name="dynamic"
      :value="choice"
    />
    <label :for="index" class="ml-2 text-xl text-center">{{ choice }}</label>
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

</script>
