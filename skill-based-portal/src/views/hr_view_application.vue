<template>
    <v-app>
        <v-container>
            <div style="padding-top: 80px; padding-bottom: 80px;">
                <div class="container ms-auto">
                    <div class="row">
                        <div class="col">

                            <router-link :to="{ name: 'roleListingHR'}">
                                <div id="back-group" class="d-flex align-center">
                                    <img class="back-button" src="../assets/icons/back.png" />
                                    <p id="back-text">Back to Role Listing</p>
                                </div>
                            </router-link>

                        </div>

                    </div>

                    <br><br>
                    
                    <p class="header-btn">Submitted Application</p>

                    <br><br>

                    <p class="page-heading">{{ applicationData.roleName }}.</p>
                    <p class="page-subheading">{{ applicationData.roleDepartment }} Department</p>

                    <br>

                </div>
                    
                    <div class="container ms-auto">
                        <div class="row">
                            <div class="col-lg-6">
                                <div class="form-group">
                                    <label for="staff_id">Staff ID:</label>
                                    <input type="text" name="staff_id" id="staff_id" disabled :placeholder="applicationData.staffID" />
                                </div>
                            </div>

                            <div class="col-lg-6">
                                <div class="form-group">
                                    <label for="staff_name">Staff Name:</label>
                                    <input type="text" name="staff_name" id="staff_name" disabled :placeholder="applicationData.staffName" />
                                </div>
                            </div>
                        </div>
                    
                    <br>

                    <div class="row">
                        <div class="col-lg-6">
                            <div class="form-group">
                                <label for="email">Email Address:</label>
                                <input type="text" name="email" id="email" disabled :placeholder="applicationData.staffEmail" />
                            </div>
                        </div>

                        <div class="col-lg-6">
                            <div class="form-group">
                                <label for="country">Country:</label>
                                <input type="text" name="country" id="country" disabled :placeholder="applicationData.staffCountry" />
                            </div>
                        </div>
                    </div>

                    <br>

                    <div class="row">
                        <div class="col-lg-6">
                            <div class="form-group">
                                <label for="current_dept">Current Department:</label>
                                <input type="text" name="current_dept" id="current_dept" disabled :placeholder="applicationData.staffDepartment" />
                            </div>
                        </div>

                        <div class="col-lg-6">
                            <div class="form-group">
                                <label for="current_role">Current Job Role:</label>
                                <input type="text" name="current_role" id="current_role" disabled :placeholder="applicationData.staffRole" />
                            </div>
                        </div>
                    </div>

                    <br>

                    <div class="row">
                        <div class="col-lg-6">
                            <div class="form-group">
                                <label for="cover_letter">Cover Letter (optional):</label>
                                <textarea name="cover_letter" id="cover_letter" cols="30" rows="8" disabled :placeholder="applicationData.staffCoverLetter" ></textarea>
                            </div>
                        </div>

                        <div class="col-lg-6">
                            <div class="form-group">
                                <label for="skills_profile">Skills Profile:</label>
                                <div class="skills_profile">
                                    <div v-for="(skill, index) in applicationData.staffSkills" :key="index" class="user_skill">{{ skill }}</div>
                                </div>
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        </v-container>
    </v-app>
</template>
<script>
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
                applicationData: {
                    roleName: 'Account Manager',
                    roleDepartment: 'Sales',

                    staffID: "000123",
                    staffName: "Ben Tan",
                    staffEmail: "ben@gmail.com",
                    staffCountry: "Singapore",
                    staffDepartment: "Marketing",
                    staffRole: "Content Strategist",
                    staffCoverLetter: "hello this is test cover letter",
                    staffSkills: ['Audit Frameworks', 'Budgeting', 'Business Acumen'],
                },
            }
        },
    }
</script>
<style scoped>
    @import '@/assets/styling/staff_view_application.css';
    @import '@/assets/styling/staff_role_listing.css';

</style>