<template>
    <v-app>
        <v-container>
            <StaffNavbar v-if="role === 'staff'" />
            <HRNavbar v-if="role === 'hr'" />

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

                            <!-- <div class="col-lg-6">
                            <div class="form-group">
                                <label for="current_role">Current Job Role:</label>
                                <input type="text" name="current_role" id="current_role" disabled :placeholder="applicationData.staffRole" />
                            </div>
                            </div> -->
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
import StaffNavbar from '@/components/staff_navbar.vue';
import HRNavbar from '@/components/hr_navbar.vue';
export default {
    name: 'roleApplication',
    methods: {
        sendCoverLetter() {
            // Prepare the application data to be sent in the request
            const cardid = this.$route.query.id;
            const applicationData = {
                "Position_ID":  cardid,
                "Staff_ID": this.applicationData.staffID,
                "Application_Date": "2023-11-04",
                "Cover_Letter": this.coverLetter,
                "Application_Status": 0
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

        const idToFetch = this.role === 'staff' ? this.staffID : this.hrID;
        const url = `http://127.0.0.1:5008/Staff/${idToFetch}`;

        axios.get(url)
                .then(response => {
                    var data = response.data.data
                    const position_id = this.$route.query.id
                    this.cardid = position_id
                    this.applicationData.staffID = idToFetch
                    this.applicationData.staffName = data.Staff_FName + " " + data.Staff_LName
                    this.applicationData.staffEmail = data.Email
                    this.applicationData.staffCountry = data.Country
                    this.applicationData.staffDepartment = data.Dept

                    console.log(data)
                })
                .catch(error => {
                    console.log(error)
                })
        document.title = "All in One";
        axios.get('http://127.0.0.1:5003/Role/' +this.$route.query.roleName)
        .then(response => {
            console.log(response.data.data['Role'][0]['Department']);
            this.applicationData.department = response.data.data['Role'][0]['Department'];
            this.applicationData.title = response.data.data['Role'][0]['Role_Name'];
        })
        .catch(error => {
            console.log(error);
        });
        axios.get(`http://127.0.0.1:5012/Staff_Skill/${idToFetch}`)
        .then(response => {
            console.log(response.data.data);
            response = response.data.data['Staff-Skill']
            for (let i = 0; i < response.length; i++) {
                this.applicationData.staffSkills.push(response[i].Skill_Name)
            }
        })
    },
    created() {
        console.log("created")
        console.log("working")
    },

    data() {
        return {
            applicationData: {
                id: '',
                title: '',
                department: '',
                staffID: '',
                staffName: '',
                staffEmail: '',
                staffCountry: '',
                staffDepartment: '',
                staffRole: '',
                staffSkills: [],
            },

            staffID: '140001',
            hrID: '160065'
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
    @import '@/assets/styling/staff_role_application.css';
</style>