<template>
    <div class="main-container">
      <div v-if="quizStore.quizCreation !== null">
        <Button @click="goHome()" class="logout" label="<- Home"></Button>
      </div>
      <div class="text-center">
        <h1>{{ user_name }}, you are playing QUIZ</h1>
      </div>
      <div id="quiz">  
        <div class="text-center" v-if="quizStore.quizCreation === null">
          <div class="text-center mt-6 space-between">
            <Button @click="startCreation()" label="Create a Quiz"></Button>
            <Button @click="startQuiz()" label="Take a Quiz"></Button>
          </div>
        </div>
        <div v-if="quizStore.quizCreation === true">
            <CreateQuiz />
        </div>
        <div v-if="quizStore.quizCreation === false">
            <TakeQuiz />
        </div>
      </div>
    </div>
</template>

<script setup>

    import { useQuiz } from "@/store/modules/quiz";
    import { useSession } from "@/store/modules/session";
    import CreateQuiz from "@/components/CreateQuiz.vue";
    import TakeQuiz from "@/components/TakeQuiz.vue";

    const quizStore = useQuiz();
    const sessionStore = useSession();
    const user_name = sessionStore.getUserName();

    const startCreation = () => {
      quizStore.setQuizCreation(true);
    };
    const startQuiz = () => {
      quizStore.setQuizCreation(null);
    };

    const goHome = () => {
      quizStore.setQuizCreation(null);
    }
</script>