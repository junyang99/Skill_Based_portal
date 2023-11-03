<template>
    <v-app>
        <v-container>
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
                                <input type="text" placeholder="Search" />
                            </div>
        
                        </div>
        
                        <div class="col-3">
                            <div class="active-check">
                                <input type="checkbox" id="active" name="active" value="active">
                                <label for="active">Active</label>
                            </div>
                        </div>

                        <div class="col-3 create-new">
                            <!-- <router-link :to="{ name: 'roleApplication', params: { id: roleData[0].id } }"> -->
                            <router-link :to="{ name: 'newListingHR'}">
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
                        <tr v-for="(role, index) in allRoles" :key="index">
                        <td>{{ index + 1 }}</td>
                        <td>{{ role.roleName }}</td>
                        <td>{{ role.department }}</td>
                        <td>{{ role.dateStart }}</td>
                        <td>{{ role.dateEnd }}</td>
                        <td>{{ role.status }}</td>
                        <td>
                            <router-link :to="{ name: 'roleListingHR'}">
                                <img class="table-actions" src="../assets/icons/view.png" />
                                <!-- <img class="table-actions" src="../assets/icons/view.png" @click="viewApplication(index)" /> -->
                            </router-link>

                            <router-link :to="{ name: 'editListingHR'}">
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
    export default {
        name: 'overallListingHR',
        mounted() {
            document.title = "All in One";
        },
        created() {
            console.log("working")
        },

        data() {
            return {
            allRoles: [
                {
                    id: 1,
                    roleName: "Account Manager",
                    department: "Sales",
                    dateStart: "10 October 2023",
                    dateEnd: "20 October 2023",
                    status: "Active"
                },
                {
                    id: 2,
                    roleName: "Account Manager",
                    department: "Sales",
                    dateStart: "",
                    dateEnd: "",
                    status: "Inactive"
                },
                {
                    id: 3,
                    roleName: "Account Manager",
                    department: "Sales",
                    dateStart: "",
                    dateEnd: "",
                    status: "Inactive"
                }
            ],
            };
        },
    }
</script>
<style scoped>
    @import '@/assets/styling/staff_overall_application.css';
    @import '@/assets/styling/hr_overall_listing.css';
</style>