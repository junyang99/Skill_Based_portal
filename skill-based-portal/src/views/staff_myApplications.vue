<template>
    <v-app>
        <v-container>
            <StaffNavbar v-if="role === 'staff'" />
            <HRNavbar v-if="role === 'hr'" />

            <div style="padding-top: 80px; padding-bottom: 80px;">
                <div class="container ms-auto">
                    <div class="page-head">
                        <p class="page-heading">My Applications.</p>
                        <p class="page-subheading">Review your submitted Applications.</p>
                    </div>
                </div>

                <br>

                <div class="container ms-auto">
                    <table class="table table-striped">
                    <thead>
                        <tr>
                        <th>No.</th>
                        <th>Role Applied</th>
                        <th>Department</th>
                        <th>Date Submitted</th>
                        <th>Status</th>
                        <th>Action</th>
                        </tr>
                    </thead>

                    <tbody>
                        <tr v-for="(application, index) in applications" :key="index">
                        <td>{{ index + 1 }}</td>
                        <td>{{ application.roleApplied }}</td>
                        <td>{{ application.department }}</td>
                        <td>{{ application.dateSubmitted }}</td>
                        <td>
                            <span class="table-status" :style="{ backgroundColor: getStatusColor(application.status) }">
                                {{ application.status }}
                            </span>
                        </td>
                        <td>
                            <router-link :to="{ name: 'viewApplication'}">
                                <img class="table-actions" src="../assets/icons/view.png" />
                                <!-- <img class="table-actions" src="../assets/icons/view.png" @click="viewApplication(index)" /> -->
                            </router-link>
                            <img class="table-actions" src="../assets/icons/edit.png" />
                            <img class="table-actions" src="../assets/icons/delete.png" />
                        </td>
                        </tr>
                    </tbody>
                    </table>
                </div>
            </div>
        </v-container>
    </v-app>
</template>
<script>
    import StaffNavbar from '@/components/staff_navbar.vue';
    import HRNavbar from '@/components/hr_navbar.vue';

    export default {
        name: 'myApplications',
        mounted() {
            document.title = "All in One";
        },
        created() {
            console.log("working")
        },

        data() {
            return {
            applications: [
                {
                    id: 1,
                    roleApplied: "Account Manager",
                    department: "Sales",
                    dateSubmitted: "15 October 2023",
                    status: 'Pending'
                },
                {
                    id: 1,
                    roleApplied: "Account Manager",
                    department: "Sales",
                    dateSubmitted: "15 October 2023",
                    status: 'Rejected'
                },{
                id: 1,
                roleApplied: "Account Manager",
                department: "Sales",
                dateSubmitted: "15 October 2023",
                status: 'Accepted'
                }
            ],
            };
        },

        methods: {
            getStatusColor(status) {
            if (status == 'Pending') {
                return 'var(--status-pending)';
            } else if (status == 'Accepted') {
                return 'var(--status-accepted)';
            } else {
                return 'var(--status-rejected)';
            }
            },
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
<style scoped>
    @import '@/assets/styling/staff_overall_application.css';
</style>