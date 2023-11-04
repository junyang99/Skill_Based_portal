<template>
    <router-link :to="{ name: 'overallListing'}">
        <button>Staff</button>
    </router-link>

    <br><br><br>

    <button>HR</button>

    <main>
        <div>
            <router-view></router-view>
        </div>
    </main>
</template>

<script>
export default {
        name: 'loginTest'
    }
</script>