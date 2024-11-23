<template>
    <div class="text-center">
        <h1>Create your user</h1>
    </div>
    <div class="form">
        <label for="name">User name</label>
        <input id="name" type="text">
        <label for="password">Password</label>
        <input id="password" type="password">
        <Button onclick="" label="Login"></Button>
    </div>
</template>

<script>

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