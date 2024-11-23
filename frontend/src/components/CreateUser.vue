<template>
    <div class="text-center">
        <h1>Login</h1>
    </div>
    <div class="form">
        <label for="username">User name</label>
        <input v-model="username" id="username" type="text">
        <label for="email">Email</label>
        <input v-model="email" id="email" type="email">
        <label for="password">Password</label>
        <input v-model="password" id="password" type="password">
        <Button @click="createUser()" label="Create"></Button>
    </div>
</template>

<script setup>
    import { ref } from 'vue';
    import { useSession } from "@/store/modules/session";

    const sessionStore = useSession();
    const username = ref('');
    const email = ref('');
    const password = ref('');

    const createUser = () => {
        const user = {
            username: username.value,
            email: email.value,
            password: password.value
        }
        sessionStore.createUser(user)
    };
</script>

<style scoped>
    .form {
        display: flex;
        flex-direction: column; /* Stack elements vertically */
        gap: 15px; /* Space between elements */
        max-width: 400px; /* Limit the width for better readability */
        margin: 0 auto; /* Center the form horizontally */
        padding: 20px; /* Add some padding around the form */
        font-size: 1.5rem;
    }
</style>