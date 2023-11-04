<template>
    <v-app>
        <v-container>
            <div style="padding-top: 80px; padding-bottom: 80px;">
                    <div class="container ms-auto">
                        <p class="header-btn">APPLY</p>
                        <br /><br />
                        <p class="page-heading">{{ applicationData.title }}.</p>
                        <p class="page-subheading">{{ applicationData.department }} Department</p>
                    </div>

                    <br>

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

                        <br />

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

                        <br />

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

                        <br />

                        <div class="row">
                            <div class="col-lg-6">
                            <div class="form-group">
                                <label for="cover_letter">Cover Letter (optional):</label>
                                <textarea v-model="coverLetter" name="cover_letter" id="cover_letter" cols="30" rows="8"></textarea>
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

                        <br /><br />
                        
                        <div class="d-flex">
                            <router-link :to="{ name: 'applicationConfirmation', query: { id: cardid } }">
                                    <button class="submit-btn" @click="sendCoverLetter">
                                    SUBMIT
                                    </button>
                            </router-link>

                            <router-link :to="{ name: 'overallListing'}">
                                <button class="cancel-btn">
                                    CANCEL
                                </button>
                            </router-link>
                        </div>

                    </div>
            </div>
        </v-container>
    </v-app>
</template>

<script>
import axios from 'axios';
export default {
    name: 'roleApplication',
    methods: {
        getResponse(){
            const path = 'http://127.0.0.1:5016/Role-Application';
            axios.get(path)
            .then ((res) => {
                console.log(res.data)
                this.applicationData = res.data;
            })
            .catch ((err) => {
                console.error(err);
            });
        },
        
        sendCoverLetter() {
            // Prepare the application data to be sent in the request
            const cardid = this.$route.query.id;
            const applicationData = {
                "Position_ID":  cardid,
                "Staff_ID": this.applicationData.staffID,
                "Application_Date": "2023-11-04",
                "Cover_Letter": this.coverLetter,
                "Application_Status": 1
            }

            // Send a POST request to the Flask API to submit the application
            console.log("sending")
            axios.post('http://127.0.0.1:5016/create_application', applicationData)
            .then(() => {
            // Handle the successful submission, e.g., show a success message
            console.log('Application submitted successfully');
        })
            .catch(error => {
                // Handle errors, e.g., display an error message
                console.error('Error submitting application:', error);
            });
        },

    },
    mounted() {
        console.log("mounted")
        console.log(this.$route.query.id)
        axios.get('http://127.0.0.1:5016/Staff/160065')
                .then(response => {
                    var data = response.data.data
                    // console.log(this.$route.query.id)
                    const position_id = this.$route.query.id
                    this.cardid = position_id
                    this.applicationData.staffID = 160065
                    this.applicationData.staffName = data.Staff_FName + " " + data.Staff_LName
                    this.applicationData.staffEmail = data.Email
                    this.applicationData.staffCountry = data.Country
                    this.applicationData.staffDepartment = data.Dept
                })
                .catch(error => {
                    console.log(error)
                })
        // this.getResponse();
        document.title = "All in One";
    },
    created() {
        console.log("created")
        // this.getResponse();
        console.log("working")
    },

    data() {
        return {
        applicationData: {
                id: '1',
                title: 'Account Manager',
                department: 'Sales',
                staffID: '000123',
                staffName: 'Alice Tan',
                staffEmail: 'alice@gmail.com',
                staffCountry: 'Singapore',
                staffDepartment: 'Marketing',
                staffRole: 'Content Strategist',
                staffSkills: ['Audit Frameworks', 'Budgeting', 'Business Acumen'],
                },
        };
    },

}
</script>

<style @scoped>
    @import '@/assets/styling/staff_role_application.css';
</style>