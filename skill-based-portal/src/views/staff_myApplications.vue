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
                        <td>{{ application.role_name }}</td>
                        <td>{{ application.dept }}</td>
                        <td>{{ formatDate(application.application_date) }}</td>
                        <td>
                            <span class="table-status" :style="{ backgroundColor: getStatusColor(application.status) }">
                                {{ application.status }}
                            </span>
                        </td>
                        <td>
                            <router-link :to="{ name: 'viewApplication' ,query: { id: application.id } }" >
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
import axios from 'axios';
import StaffNavbar from '@/components/staff_navbar.vue';
import HRNavbar from '@/components/hr_navbar.vue';

    export default {
        name: 'myApplications',
        mounted() {
            document.title = "All in One";
        },
        created() {
            axios.get('http://127.0.0.1:5016/Staff/applications/140001') 
            .then(response => {
                response = response.data.data;
                console.log(response);
                this.applications = response;
                for (let i = 0; i < response.length; i++) {
                    if (response[i].application_status == 0) {
                        this.applications[i].status = 'Pending';
                    } else if (response[i].application_status == 1) {
                        this.applications[i].status = 'Accepted';
                    } else {
                        this.applications[i].status = 'Rejected';
                    }
                }
            
            })
            .catch(error => {
                console.error('Error fetching staff applications:', error);
            });
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

            formatDate(dateString) {
                if (!dateString || dateString === 'null') {
                    return 'N/A'; // Handle cases where the date is null or empty
                }
                const date = new Date(dateString);
                return date.toLocaleDateString(); // Convert the date to a locale string
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