<template>
    <div class="results-container">
        <h1 class="results-title">Result of your quizzse</h1>
        <div class="result-item" v-for="(result, index) in results">
            <ul class="result-details">
                <li><strong>Score:</strong> {{ result.score }} / {{ result.quiz.questions.length }}</li>
                <li><strong>Time taken:</strong> {{ result.time_taken }}</li>
                <li><strong>Quiz:</strong> {{ result.quiz.title }}</li>
            </ul>
        </div>
    </div>
</template>

<script setup>
    import { ref, onMounted } from 'vue';
    import { useQuiz } from "@/store/modules/quiz";
    const quizStore = useQuiz();

    const results = ref([]);

    results.value = quizStore.getAllResults();

    onMounted(async () => {
        results.value = await quizStore.getAllResults();
    });
</script>

<style scoped>
.results-container {
    display: flex;
    flex-direction: column;
    gap: 15px;
    max-width: 600px;
    margin: 0 auto 50px;
    padding: 20px;
    font-size: 1.2rem;
}

.results-title {
    text-align: center;
    font-size: 1.5rem;
    font-weight: bold;
    margin-bottom: 15px;
}

.result-item {
    display: flex;
    flex-direction: column;
    gap: 10px;
    padding: 15px;
    border: 1px solid #ddd;
    border-radius: 8px;
    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.05);
}

.result-details {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: 8px;
}

.result-details li {
    font-size: 1rem;
    color: white;
}

.result-details strong {
    font-weight: bold;
}

</style>
