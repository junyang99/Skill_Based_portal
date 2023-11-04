<template>
    <v-app>
        <v-container>
            <StaffNavbar v-if="role === 'staff'" />
            <HRNavbar v-if="role === 'hr'" />

            <div style="padding-top: 80px; padding-bottom: 80px;">

                <div class="container ms-auto">
                    <div class="row">
                    <div class="col">
                        <router-link :to="{ name: 'overallListing'}">
                            <div id="back-group" class="d-flex align-center">
                                <img class="back-button" src="../assets/icons/back.png" />
                                <p id="back-text">Back to All Role Listings</p>
                            </div>
                        </router-link>
                    </div>
                    </div>

                    <br>

                    <div class="row">
                    <div class="col">
                        <p class="page-heading">{{ roleData[0].title }}.</p>
                        <p class="page-subheading">{{ roleData[0].department }} Department</p>
                    </div>

                    <div class="col right-align">
                        <!-- <router-link :to="{ name: 'roleApplication', params: { id: roleData[0].id } }"> -->
                        <router-link :to="{ name: 'roleApplication'}">
                            <button class="card-apply-btn">APPLY</button>
                        </router-link>

                    </div>
                    </div>

                    <br>

                    <div class="row">
                    <div class="col-7">
                        <p class="page-description">
                            {{ roleData[0].description }}
                        </p>
                    </div>

                    <div class="col-1"></div>

                    <div class="col-4">
                        <div class="rs-card">
                        <p class="rs-heading">Your Role-Skill Match</p>
                        <p class="rs-percentage">{{ roleData[0].match }}%</p>
                        </div>

                        <br>

                        <div class="page-skills">
                            <div v-for="(skill, index) in roleData[0].skillMatch" :key="index" class="matching-skill">{{ skill }}</div>
                            <div v-for="(skill, index) in roleData[0].skillMiss" :key="index" class="missing-skill">{{ skill }}</div>
                        </div>
                    </div>
                    </div>
                </div>
                </div>

        </v-container>
    </v-app>
</template>

<script>
    import StaffNavbar from '@/components/staff_navbar.vue';
    import HRNavbar from '@/components/hr_navbar.vue';

    export default {
        name: 'specificListing',
        mounted() {
            document.title = "All in One";
        },
        created() {
            console.log("working")
        },

        data() {
            return {
            roleData: [
                {
                id: 1,
                title: "Account Manager",
                department: "Sales",
                deadline: "15 October 2023",
                description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc quis faucibus est. Proin tristique dolor et tortor venenatis, auctor vestibulum risus consequat. Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc quis faucibus est. Proin tristique dolor et tortor venenatis, auctor vestibulum risus consequat. Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc quis faucibus est. Proin tristique dolor et tortor venenatis, auctor vestibulum risus consequat. Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc quis faucibus est. Proin tristique dolor et tortor venenatis, auctor vestibulum risus consequat. Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc quis faucibus est. Proin tristique dolor et tortor venenatis, auctor vestibulum risus consequat. Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc quis faucibus est. Proin tristique dolor et tortor venenatis, auctor vestibulum risus consequat. Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc quis faucibus est. Proin tristique dolor et tortor venenatis, auctor vestibulum risus consequat. Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                match: 75,
                skillMatch: ['Audit Frameworks', 'Budgeting', 'Business Acumen'],
                skillMiss: ['Audit Compliance']
                }
            ],
            };
        },

        components: {
            StaffNavbar,
            HRNavbar
        },

        computed: {
            role() {
                return this.$route.params.role;
            }
        }
    }
</script>

<style @scoped>
    @import '@/assets/styling/staff_role_listing.css';
    @import '@/assets/styling/staff_view_application.css';
</style>