<template>
    <v-app>
        <v-container>
            <StaffNavbar v-if="role === 'staff'" />
            <HRNavbar v-if="role === 'hr'" />

            <div style="padding-top: 80px; padding-bottom: 80px;">
                <div class="container ms-auto">
                    <div class="page-head">
                        <p class="page-heading">All Roles.</p>
                        <p class="page-subheading">Browse all existing Roles.</p>
                    </div>
                </div>

                <br>

                <div class="container ms-auto">
                    <div class="search-and-filter row">
                        <div class="col-6">
                            <div class="input-box">
                                <i class="uil uil-search"></i>
                                <input v-model="searchText" type="text" placeholder="Search" />
                            </div>
        
                        </div>
        
                        <div class="col-3">
                            <div class="active-check">
                                <input type="checkbox" v-model="activeOnly" id="activeCheckbox" class="form-check-input">
                                <label for="activeCheckbox" class="form-check-label">Active</label>
                            </div>
                        </div>

                        <div class="col-3 create-new">
                            <router-link :to="{ name: 'newListingHR' }">
                                <button class="create-new-btn">Create New</button>
                            </router-link>
                        </div>
                    </div>
                </div>

                <br>

                <div class="container ms-auto">
                    <table class="table table-striped">
                    <thead>
                        <tr>
                            <th>No.</th>
                            <th>Role Name</th>
                            <th>Department</th>
                            <th>Start Date</th>
                            <th>End Date</th>
                            <th>Status</th>
                            <th>Action</th>
                        </tr>
                    </thead>

                    <tbody>
                        <tr v-for="(role, index) in filteredRoles" :key="index">
                        <td>{{ index + 1 }}</td>
                        <td>{{ role.role_name  }}</td>
                        <td>{{ role.department }}</td>
                        <td>{{ formatDate(role.start_date) }}</td>
                        <td>{{ formatDate(role.end_date) }}</td>
                        <td>{{ role.status }}</td>
                        <td>
                            <router-link :to="{ name: 'roleListingHR', params: { roleName: role.role_name, role: 'hr' } }">
                                <img class="table-actions" src="../assets/icons/view.png" />
                                <!-- <img class="table-actions" src="../assets/icons/view.png" @click="viewApplication(index)" /> -->
                            </router-link>

                            <router-link :to="{ name: 'editListingHR', params: { roleName: role.role_name, role: 'hr' }}">
                                <img class="table-actions" src="../assets/icons/edit.png" />
                            </router-link>

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
        name: 'overallListingHR',

        components: {
            StaffNavbar,
            HRNavbar
        },

        mounted() {
            document.title = "All in One";
            this.fetchRoles();
        },

        created() {
            console.log("working")
        },

        data() {
            return {
                allRoles: [],
                searchText: '',
                activeOnly: false,
            };
        },

        computed: {
            filteredRoles() {
                let filteredRoles = this.allRoles;

                if (this.activeOnly) {
                    filteredRoles = filteredRoles.filter(role => role.status === 'active');
                }

                if (this.searchText !== '') {
                    filteredRoles = filteredRoles.filter(role => {
                    return role.role_name.toLowerCase().includes(this.searchText.toLowerCase());
                });
                }

                return filteredRoles;
                },

            role() {
                return this.$route.params.role;
            }
        },

        methods: {
            // Function to format the date string without the time
            formatDate(dateString) {
                if (!dateString || dateString === 'null') {
                    return 'N/A'; // Handle cases where the date is null or empty
                }
                const date = new Date(dateString);
                return date.toLocaleDateString(); // Convert the date to a locale string
            },

            fetchRoles() {
                // Make an HTTP GET request to fetch roles from the API
                axios.get('http://localhost:5018/HR/role_admin')
                    .then(response => {
                        // Extract the roles from the response and set them to allRoles
                        console.log(response.data.roles)
                        this.allRoles = response.data.roles; // Assuming the API response has a "Roles" key
                    })

                    .catch(error => {
                        console.error('Failed to fetch roles:', error);
                    })
            },
    },
    }
</script>

<style scoped>
    @import '@/assets/styling/staff_overall_application.css';
    @import '@/assets/styling/hr_overall_listing.css';
</style>