<template>
    <div class="main-container">
      <div class="header" >
        <div>
          <Button @click="goHome()" v-if="quizStore.quizDisplay !== null" class="logout" label="<- Home"></Button>
        </div>
        <div>
          <h1>{{ user_name }}</h1>
        </div>
      </div>
      <div id="quiz">  
        <div class="text-center" v-if="quizStore.quizDisplay === null">
          <h1>Quizzz</h1>
          <div class="text-center mt-6 space-between">
            <Button @click="startCreation()" label="Create a Quiz"></Button>
            <Button @click="startQuiz()" label="Take a Quiz"></Button>
            <Button @click="quizResults()" label="Quiz Results"></Button>
          </div>
        </div>
        <div v-if="quizStore.quizDisplay === 'CREATION'">
            <CreateQuiz />
        </div>
        <div v-if="quizStore.quizDisplay === 'PLAY'">
            <TakeQuiz />
        </div>
        <div v-if="quizStore.quizDisplay === 'RESULTS'">
            <ViewResults />
        </div>
      </div>
    </div>
</template>

<script setup>

    import { useQuiz } from "@/store/modules/quiz";
    import { useSession } from "@/store/modules/session";
    import CreateQuiz from "@/components/CreateQuiz.vue";
    import TakeQuiz from "@/components/TakeQuiz.vue";
    import ViewResults from "@/components/ViewResults.vue";
    

    const quizStore = useQuiz();
    const sessionStore = useSession();
    const user_name = sessionStore.getUserName();

    const startCreation = () => {
      quizStore.setQuizDisplay('CREATION');
    };
    const startQuiz = () => {
      debugger
      quizStore.setQuizDisplay('PLAY');
    };
    const quizResults = () => {
      quizStore.setQuizDisplay('RESULTS');
    };

    const goHome = () => {
      quizStore.setQuizDisplay(null);
      quizStore.setQuizStatus('NOT_STARTED');
      quizStore.setCategory(null);
    }
</script>