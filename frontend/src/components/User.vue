<template>
    <div class="main-container">
        <div v-if="sessionStore.sessionStatus !== null">
            <Button @click="goBack()" class="logout" label="<- Back"></Button>
        </div>
    <div class="text-center" v-if="sessionStore.sessionStatus === null">
        <h1>Welcome to the quiz</h1>
        <div class="space-between">
            <Button @click="() => setSessionStatus('LOGIN')" label="Login"></Button>
            <Button @click="() => setSessionStatus('CREATE')" label="Create new user"></Button>
            <!-- <Button @click="() => setSessionStatus('START')" label="Start with a guest"></Button> -->
        </div>
    </div>
    <div v-if="sessionStore.sessionStatus === 'CREATE'">
        <CreateUser />
    </div>
    <div v-if="sessionStore.sessionStatus === 'LOGIN'">
        <Login />
    </div>
    </div>
</template>

<script setup>
    import Login from "@/components/Login.vue";
    import CreateUser from "@/components/CreateUser.vue";

    import { useSession } from "@/store/modules/session";

    const sessionStore = useSession();

    const setSessionStatus = (status) => {
        sessionStore.setSessionStatus(status);
    };
    const goBack = () => {
        sessionStore.setSessionStatus(null);
    }
</script>

<style>
    .space-between {
        display: flex;
        gap: 30px;
        justify-content: center;
    }

    .logout {
        color: white;
        background-color: black;
    }
</style>