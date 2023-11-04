<template>
    <v-app>
        <v-container>
            <StaffNavbar v-if="role === 'staff'" />
            <HRNavbar v-if="role === 'hr'" />

            <div style="padding-top: 80px; padding-bottom: 80px;">
                    <div class="container ms-auto">
                        <p class="header-btn">Role Listing</p>
                        
                        <br><br>

                        <p class="page-heading">New Role Listing</p>
                    </div>

                    <br>

                    <div class="container ms-auto">
                        <div class="row">
                            <div class="col-lg-6">
                                <div class="form-group">
                                    <label for="role_name">Role Name:</label>
                                    <input v-model="title" type="text" name="role_name" id="role_name" placeholder="Role Name" />
                                </div>
                            </div>

                            <div class="col-lg-6">
                                <div class="form-group">
                                    <label for="new_department">Department:</label>
                                    <input v-model="department_name" type="text" name="new_department" id="new_department" placeholder="Department" />
                                </div>
                            </div>
                        </div>

                        <br>

                        <div class="row">
                            <div class="col-lg-6">
                                <div class="form-group">
                                    <label for="role_description">Role Description:</label>
                                    <textarea v-model="description" name="role_description" id="role_description" cols="30" rows="8"></textarea>
                                </div>
                            </div>

                            <div class="col-lg-6">
                                <div class="form-group">
                                    <label>Required Skills:</label>
                                    <VueMultiselect
                                        v-model="selected"
                                        :options="options"
                                        :multiple="true"
                                        :taggable="true"
                                        placeholder="Search for a skill"
                    
                                    ></VueMultiselect>
                                </div>
                            </div>
                        </div>

                        <br>

                        

                        
                        
                        <div class="d-flex">
                            <router-link :to="{ name: 'overallListingHR'}">
                                <button class="submit-btn" @click="submitForm">
                                    SAVE
                                </button>
                            </router-link>

                            <router-link :to="{ name: 'overallListingHR'}">
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
    import VueMultiselect from 'vue-multiselect'
    import axios from 'axios'
    import StaffNavbar from '@/components/staff_navbar.vue';
    import HRNavbar from '@/components/hr_navbar.vue';

 
    export default {
        name: 'roleApplication',
        components: {
            VueMultiselect,
            StaffNavbar,
            HRNavbar
        },
        mounted() {
            document.title = "All in One";
        },
        created() {
            console.log("working");
            this.fetchSkills();
        },

        computed: {
            role() {
                return this.$route.params.role;
            }
        },

        data() {
            return {
                selected: [],
                options:[],
                taggingOptions: [], 
                taggingSelected: [],
                title: '',            // Add data properties for form fields
                department_name: '',
                description: '',
                skills: [],
                start_date: '',
                end_date: ''
            };
        },

        methods: {
            fetchSkills() {
                axios.get('http://localhost:5011/Skill')
                .then(response => {
                    const skillList = response.data.data.Skill; // Correct the object path

                    // Extract all skill names and populate the options array
                    // this.options = skillList.map(item => {
                    //     return {
                    //         label: item.Skill_Name,
                    //     };
                    // });

                    this.options = skillList.map(item => item.Skill_Name);

                    console.log('Options:', this.options);
                })
                .catch(error => {
                    console.error('Failed to fetch skills:', error);
                });
            },

            addTag (newTag) {
            const tag = {
                name: newTag,
                code: newTag.substring(0, 2) + Math.floor((Math.random() * 10000000))
            };
            this.taggingOptions.push(tag)
            this.taggingSelected.push(tag)
            },
            submitForm() {
                // Create an object to represent the data you want to send to the API
                const postData = {
                    role_name: this.title,
                    department: this.department_name,
                    description: this.description,
                    skills: this.selected,
                    start_date: this.start_date,
                    end_date: this.end_date
                };

            // Make the API request using Axios
            axios.post("http://localhost:5018/HR/role_admin", postData)
                .then(response => {
                    // Handle the API response here (e.g., show a success message)
                    console.log("API response:", response.data);
                    window.alert("Role created successfully!");

                    console.log(postData)

                    axios.post("http://localhost:5015/HR/add_open_position", postData)

                    .then(response2 => {
                        // Handle the API response here (e.g., show a success message)
                        console.log("API response:", response2.data);
                        window.alert("Role created successfully!");
                    })

                    .catch(error2 => {
                        // Handle API request errors (e.g., show an error message)
                        if (error2.response && error2.response.status === 400 && error2.response.data.message) {
                            // Handle the 400 Bad Request error with an error message
                            window.alert("Error creating role: " + error2.response.data.message);
                        } else {
                            // Handle other errors
                            window.alert("Error creating role: " + error2.message);
                        }
                    })

                })

                

                .catch(error => {
                    // Handle API request errors (e.g., show an error message)
                    if (error.response && error.response.status === 400 && error.response.data.message) {
                        // Handle the 400 Bad Request error with an error message
                        window.alert("Error creating role: " + error.response.data.message);
                    } else {
                        // Handle other errors
                        window.alert("Error creating role: " + error.message);
                    }
                })
            },
        }
    }
</script>

<style src="vue-multiselect/dist/vue-multiselect.css"></style>

<style @scoped>
    @import '@/assets/styling/staff_role_application.css';
    @import '@/assets/styling/hr_new_listing.css';
</style>