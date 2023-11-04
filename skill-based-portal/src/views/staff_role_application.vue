<template>
    <v-app>
        <v-container>
            <StaffNavbar v-if="role === 'staff'" />
            <HRNavbar v-if="role === 'hr'" />

            <div style="padding-top: 80px; padding-bottom: 80px;">
                    <div class="container ms-auto">
                        <p class="header-btn">APPLY</p>
                        <br /><br />
                        <p class="page-heading">{{ applicationData[0].title }}.</p>
                        <p class="page-subheading">{{ applicationData[0].department }} Department</p>
                    </div>

                    <br>

                    <div class="container ms-auto">
                        <div class="row">
                            <div class="col-lg-6">
                            <div class="form-group">
                                <label for="staff_id">Staff ID:</label>
                                <input type="text" name="staff_id" id="staff_id" disabled :placeholder="applicationData[0].staffID" />
                            </div>
                            </div>

                            <div class="col-lg-6">
                            <div class="form-group">
                                <label for="staff_name">Staff Name:</label>
                                <input type="text" name="staff_name" id="staff_name" disabled :placeholder="applicationData[0].staffName" />
                            </div>
                            </div>
                        </div>

                        <br />

                        <div class="row">
                            <div class="col-lg-6">
                            <div class="form-group">
                                <label for="email">Email Address:</label>
                                <input type="text" name="email" id="email" disabled :placeholder="applicationData[0].staffEmail" />
                            </div>
                            </div>

                            <div class="col-lg-6">
                            <div class="form-group">
                                <label for="country">Country:</label>
                                <input type="text" name="country" id="country" disabled :placeholder="applicationData[0].staffCountry" />
                            </div>
                            </div>
                        </div>

                        <br />

                        <div class="row">
                            <div class="col-lg-6">
                            <div class="form-group">
                                <label for="current_dept">Current Department:</label>
                                <input type="text" name="current_dept" id="current_dept" disabled :placeholder="applicationData[0].staffDepartment" />
                            </div>
                            </div>

                            <div class="col-lg-6">
                            <div class="form-group">
                                <label for="current_role">Current Job Role:</label>
                                <input type="text" name="current_role" id="current_role" disabled :placeholder="applicationData[0].staffRole" />
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
                                    <div v-for="(skill, index) in applicationData[0].staffSkills" :key="index" class="user_skill">{{ skill }}</div>
                                </div>
                            </div>
                            </div>
                        </div>

                        <br /><br />
                        
                        <div class="d-flex">
                            <router-link :to="{ name: 'applicationConfirmation'}">
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
    import StaffNavbar from '@/components/staff_navbar.vue';
    import HRNavbar from '@/components/hr_navbar.vue';

    import axios from 'axios';

    export default {
        name: 'roleApplication',
        props: ['applications'],
        methods: {
            getResponse(){
                const path = 'http://127.0.0.1:5000/Role-Application';
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
                console.log("sending cover letter")
                // Send the cover letter text to the Python backend
                axios.post('http://127.0.0.1:5000/api/send-cover-letter', { coverLetter: this.coverLetter })
                    .then(response => {
                    // Handle the response from the Python backend
                    const successMessage = response.data.message; // Access the message property
                    console.log('Response from Python:', successMessage);
                    console.log(this.coverLetter)
                    console.log('Cover Letter sent to Python:', response.data);
                    })
                    .catch(error => {
                    // Handle errors
                    console.error('Error sending Cover Letter to Python:', error);
                    });
                },
        },

        mounted() {
            console.log("mounted")
            this.getResponse();
            document.title = "All in One";
        },
        created() {
            console.log("created")
            this.getResponse();
            console.log("working")
        },

    data() {
        return {
        applicationData: [
            {
                id: '',
                title: '',
                department: '',
                staffID: '',
                staffName: '',
                staffEmail: '',
                staffCountry: '',
                staffDepartment: '',
                staffRole: '',
                staffSkills: '',
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
    @import '@/assets/styling/staff_role_application.css';
</style>