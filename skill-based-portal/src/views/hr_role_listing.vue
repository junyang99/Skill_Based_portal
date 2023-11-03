<template>
    <v-app>
        <v-container>
            <div style="padding-top: 80px; padding-bottom: 80px;">

                <div class="container ms-auto">
                    <div class="row">
                        <div class="col">
                            <router-link :to="{ name: 'overallListingHR'}">
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

                        <div class="col">
                            <router-link :to="{ name: 'editListingHR'}">          
                                <button class="application-btn float-end" style="background-color: var(--hr-actions);">
                                    <img src="../assets/icons/edit.svg">
                                    <p>EDIT</p>
                                </button>
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
                            <div class="skills-text">
                                Skills Required
                            </div>
                            <div class="page-skills">
                                <div v-for="(skill, index) in roleData[0].skills" :key="index" class="user_skill">{{ skill }}</div>
                            </div>

                            <br><br>

                            <div class="openingPeriod" v-if="roleData[0].startDate && roleData[0].endDate">
                                <p>Start Date: {{ roleData[0].startDate }}</p>
                                <p>End Date: {{ roleData[0].endDate }}</p>
                            </div>
                        </div>
                    </div>

                    <br><br>

                    <div class="row" v-if="roleData[0].startDate && roleData[0].endDate">
                        <div class="col">
                            <p class="page-subheading">View Applicants</p>
                        </div>
                    </div>

                    <br>

                    <div class="row" v-if="roleData[0].startDate && roleData[0].endDate">
                        <table class="table table-striped">
                            <thead>
                                <tr>
                                    <th>No.</th>
                                    <th>Applicant Name</th>
                                    <th>Skills</th>
                                    <!-- <th>Date Submitted</th> -->
                                    <th>Action</th>
                                </tr>
                            </thead>

                            <tbody>
                                <tr v-for="(applicant, index) in allApplicants" :key="index">
                                <td>{{ index + 1 }}</td>
                                <td>{{ applicant.applicantName }}</td>
                                <td>{{ applicant.applicantSkills }}</td>
                                <!-- <td>{{ applicant.dateSubmitted }}</td> -->
                                <td>
                                    <router-link :to="{ name: 'viewApplicationHR'}">
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
                </div>

        </v-container>
    </v-app>
</template>

<script>
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
                    skills: ['Audit Frameworks', 'Budgeting', 'Business Acumen'],
                    startDate: "10 October 2023",
                    endDate: "20 October 2023",
                    // startDate: "",
                    // endDate: ""
                }
            ],

            allApplicants: [
                {
                    applicantName: "Ben Tan",
                    applicantSkills: "Audit Frameworks, Budgeting, Business Acumen",
                    // dateSubmitted: "10 October 2023"
                }
            ]
            };
        },
    }
</script>

<style @scoped>
    @import '@/assets/styling/staff_role_listing.css';
    @import '@/assets/styling/staff_view_application.css';
    @import '@/assets/styling/hr_role_listing.css';
    @import '@/assets/styling/staff_overall_application.css';
    @import '@/assets/styling/hr_overall_listing.css';
</style>