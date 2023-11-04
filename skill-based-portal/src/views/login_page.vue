<template>
    <div style="padding: 80px;">
        <div class="d-flex justify-content-center">
            <img src="../assets/logo.svg" class="login-logo"/>
        </div>

        <br><br><br>

        <div class="d-flex justify-content-center">
            <p class="login-txt">Please select your User Type:</p>
        </div>

        <div class="d-flex justify-content-center">
            <router-link :to="{ name: 'overallListing', params: { role: 'staff' }}">
                <button type="button" class="btn btn-outline-primary login-btn">Staff Login</button>
            </router-link>

            <br><br><br>

            <router-link :to="{ name: 'overallListing', params: { role: 'hr' }}">
                <button type="button" class="btn btn-outline-primary login-btn">HR Login</button>
            </router-link>
        </div>

        <main>
            <div>
                <router-view></router-view>
            </div>
        </main>

    </div>
</template>

<script>
export default {
        name: 'loginPage'
    }
</script>

<style>
    .login-btn {
        margin: 30px;
    }

    .login-logo {
        width: 250px;
        height: auto;
    }

    .login-txt {
        font-family: text-medium;
        font-size: 23px;
        margin-bottom: 0px;
    }
</style>