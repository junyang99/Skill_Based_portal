<template>
    <v-app>
        <v-container>
            <StaffNavbar v-if="role === 'staff'" />
            <HRNavbar v-if="role === 'hr'" />

            <div style="padding-top: 80px; padding-bottom: 80px;">
                <div class="container ms-auto">
                    <div class="row">
                        <div class="col">
                            <p class="page-heading">My Profile.</p>
                        </div>

                        <div class="col">
                            <button class="application-btn float-end">
                                <img src="../assets/icons/edit.svg">
                                <p>EDIT</p>
                            </button>
                        </div>
                    </div>

                    <div class="row">
                        <div class="col">
                            <p class="page-subheading">View My Profile.</p>
                        </div>
                    </div>
                </div>

                <br>

                <div class="container ms-auto">
                    <div class="row">
                        <div class="col-lg-6">
                            <div class="form-group">
                                <label for="staff_id">Staff ID:</label>
                                <input type="text" name="staff_id" id="staff_id" disabled :placeholder="applicationData.staffID">
                            </div>
                        </div>
                        
                        <div class="col-lg-6">
                            <div class="form-group">
                                <label for="staff_name">Staff Name:</label>
                                <input type="text" name="staff_name" id="staff_name" disabled :placeholder="applicationData.staffName">
                            </div>
                        </div>
                    </div>

                    <br>

                    <div class="row">
                        <div class="col-lg-6">
                            <div class="form-group">
                                <label for="email">Email Address:</label>
                                <input type="text" name="email" id="email" disabled :placeholder="applicationData.staffEmail">
                            </div>
                        </div>
                        
                        <div class="col-lg-6">
                            <div class="form-group">
                                <label for="country">Country:</label>
                                <input type="text" name="country" id="country" disabled :placeholder="applicationData.staffCountry">
                            </div>
                        </div>
                    </div>

                    <br>

                    <div class="row">
                        <div class="col-lg-6">
                            <div class="form-group">
                                <label for="current_dept">Current Department:</label>
                                <input type="text" name="current_dept" id="current_dept" disabled :placeholder="applicationData.staffDepartment">
                            </div>
                        </div>
                        
                        <div class="col-lg-6">
                            <div class="form-group">
                                <label for="current_role">Current Job Role:</label>
                                <input type="text" name="current_role" id="current_role" disabled :placeholder="applicationData.staffRole">
                            </div>
                        </div>
                    </div>

                    <br>

                    <div class="row">
                        
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
    import StaffNavbar from '@/components/staff_navbar.vue';
    import HRNavbar from '@/components/hr_navbar.vue';

    import axios from 'axios';
    export default {
        name: 'myProfile',
        mounted() {
            document.title = "All in One";
            axios.get('http://127.0.0.1:5008/Staff/140001')
                .then(response => {
                    var data = response.data.data

                    this.applicationData.staffID = data.Staff_ID
                    this.applicationData.staffName = data.Staff_FName + " " + data.Staff_LName
                    this.applicationData.staffEmail = data.Email
                    this.applicationData.staffCountry = data.Country
                    this.applicationData.staffDepartment = data.Dept
                })
                .catch(error => {
                    console.log(error)
                })
                axios.get('http://127.0.0.1:5012/Staff_Skill/140001')
                .then(response => {
                    console.log(response.data.data)
                    var data = response.data.data

                    this.applicationData.staffSkills = data['Staff-Skill'].map(skill => skill.Skill_Name)
                })
                .catch(error => {
                    console.log(error)
                })
        },
        created() {
            console.log("working")
        },

        data() {
            return {
                applicationData: {
                    staffID: "000123",
                    staffName: "Alice Tan",
                    staffEmail: "alice@gmail.com",
                    staffCountry: "Singapore",
                    staffDepartment: "Marketing",
                    staffRole: "Content Strategist",
                    staffSkills: ['Audit Frameworks', 'Budgeting', 'Business Acumen']
                },
            }
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
    @import '@/assets/styling/staff_profile.css';
    @import '@/assets/styling/staff_view_application.css';
    @import '@/assets/styling/staff_role_listing.css';
</style>