<template>
    <router-link :to="{ name: 'overallListing', params: { role: 'staff' }}">
        <button type="button" class="btn btn-outline-primary">Staff Login</button>
    </router-link>

    <br><br><br>

    <router-link :to="{ name: 'overallListing', params: { role: 'hr' }}">
        <button type="button" class="btn btn-outline-primary">HR Login</button>
    </router-link>
    <main>
        <div>
            <router-view></router-view>
        </div>
    </main>
</template>

<script>
export default {
        name: 'loginPage'
    }
</script>