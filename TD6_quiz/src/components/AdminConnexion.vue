<script>
export default {
    data() {
        return {
            username: "Toto",
            password: "1234",
            form_username: "",
            form_password: "",
        };
    },
    methods: {
        adminco: function () {
            if (this.form_password == this.password && this.form_username == this.username) {
                localStorage.setItem("admin-auth", "true");
                const redirect = this.$route.query.redirect;
                this.$router.push(typeof redirect === "string" ? redirect : "/quizz");
            }
        },
    },
};
</script>


<template>
    <div>
        <label>
            Nom utilisateur
        </label>
        <input type="text" placeholder="username" v-model="form_username" />
    </div>
    <div>
        <label>
            Password
        </label>
        <input type="password" placeholder="password" v-model="form_password" />
    </div>

    <button @click="adminco"> Envoyer </button>
</template>