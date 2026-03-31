
<template>
    <div class="container">
        <div class="section">
            <h3>Connexion admin</h3>
            <button @click="$router.push('/connexion/')">Se connecter</button>
        </div>
        <div class="section">
            <h3>Faire le quizz</h3>
            <button @click="$router.push('/quiz/')"> Jouer</button>
        </div>
    </div>

</template>
<style scoped>
.container {
    display: flex;
    justify-content: space-between;
    gap: 2rem;
}

.section {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
}
</style>
