<template>
    <div class="main-container">
      <div class="header" v-if="quizStore.quizCreation !== null">
        <Button @click="goHome()" class="logout" label="<- Home"></Button>
        <h1>{{ user_name }}</h1>
      </div>
      <div id="quiz">  
        <div class="text-center" v-if="quizStore.quizCreation === null">
          <h1>Quizzz</h1>
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
      quizStore.setQuizCreation(false);
    };

    const goHome = () => {
      quizStore.setQuizCreation(null);
    }
</script>