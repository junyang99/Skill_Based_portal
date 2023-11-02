<template>
    <v-app>
        <v-container>
            <div style="padding-top: 80px; padding-bottom: 80px;">
                    <div class="container ms-auto">
                        <p class="header-btn">Role Listing</p>
                        
                        <br><br>

                        <p class="page-heading">Edit Role Listing</p>
                    </div>

                    <br>

                    <div class="container ms-auto">
                        <div class="row">
                            <div class="col-lg-6">
                                <div class="form-group">
                                    <label for="role_name">Role Name:</label>
                                    <input type="text" name="role_name" id="role_name" v-model="input.roleName" /> 
                                </div>
                            </div>

                            <div class="col-lg-6">
                                <div class="form-group">
                                    <label for="new_department">Department:</label>
                                    <input type="text" name="new_department" id="new_department" v-model="input.department" />
                                </div>
                            </div>
                        </div>

                        <br>

                        <div class="row">
                            <div class="col-lg-6">
                                <div class="form-group">
                                    <label for="role_description">Role Description:</label>
                                    <textarea name="role_description" id="role_description" cols="30" rows="8" v-model="input.roleDescription"></textarea>
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
                                        label="name"
                                        track-by="code"
                                        >
                                    </VueMultiselect>
                                </div>
                            </div>
                        </div>

                        <br>

                        <div class="row">
                            <div class="col-lg-6">
                                <div class="form-group">
                                    <label for="start_date">Start Date:</label>
                                    <input type="date" name="start_date" id="start_date" v-model="input.startDate"/>
                                </div>
                            </div>

                            <div class="col-lg-6">
                                <div class="form-group">
                                    <label for="end_date">End Date:</label>
                                    <input type="date" name="end_date" id="end_date" v-model="input.endDate"/>
                                </div>
                            </div>
                        </div>

                        <br /><br />
                        
                        <div class="d-flex">
                            <router-link :to="{ name: 'overallListingHR'}">
                                <button class="submit-btn" @click="saveData">
                                    SAVE
                                </button>
                            </router-link>

                            <!-- joel where do u want this to lead back to? the specific role listing can? -->
                            <router-link :to="{ name: 'roleListingHR'}">
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
import axios from 'axios';
 
    export default {
        name: 'roleApplication',
        components: {
            VueMultiselect,
        },
        mounted() {
            document.title = "All in One";
        },
        created() {
            console.log("working");
            this.fetchRoleDetails();
            this.fetchOptions();
        },

        data() {
            return {
                selected: [],
                options: [],
                input: {
                    roleName: '',
                    department: '',
                    roleDescription: '',
                    requiredSkills: [],
                    startDate: '',
                    endDate: '',
                }
            };
        },

        methods: {
            addTag (newTag) {
            const tag = {
                name: newTag,
                code: newTag.substring(0, 2) + Math.floor((Math.random() * 10000000))
            }
            this.taggingOptions.push(tag)
            this.taggingSelected.push(tag)
            },
            formatDate(dateString) {
                if (!dateString || dateString === 'null') {
                    return 'N/A'; // Handle cases where the date is null or empty
                }
                const date = new Date(dateString);
                const year = date.getFullYear();
                const month = (date.getMonth() + 1).toString().padStart(2, '0'); // Add 1 to month because it's zero-based
                const day = date.getDate().toString().padStart(2, '0');
                return `${year}-${month}-${day}`;
                },
                revertToSQLDateFormat(dateString) {
                    if (!dateString || dateString === 'null') {
                        return null; // Handle cases where the date is null or empty
                    }

                    // Split the "yyyy-mm-dd" string into year, month, and day
                    const [year, month, day] = dateString.split('-');

                    // Create a new Date object with the year, month, and day
                    const date = new Date(year, month - 1, day);

                    // Get the date in SQL format (e.g., "YYYY-MM-DD")
                    const sqlDate = date.toISOString().slice(0, 10);

                    return sqlDate;
                },
            fetchRoleDetails() {
                // Get the roleName from the route's parameters
                const roleName = this.$route.params.roleName;
                console.log("Role Name:", roleName);

                if (roleName) {
                    // Make an Axios GET request with the roleName parameter
                    axios.get(`http://localhost:5018/HR/role_admin?role_name=${roleName}`)
                    .then(response => {
                        // Handle the response and update the input data
                        const roleData = response.data.roles[0];
                        this.input.roleName = roleData.role_name;
                        this.input.department = roleData.department;
                        this.selected = roleData.skills.map(skill => ({ name: skill, code: skill }));
                        this.input.roleDescription = roleData.description;
                        this.input.startDate = this.formatDate(roleData.start_date);
                        this.input.endDate = this.formatDate(roleData.end_date);
                        console.log(this.input)
                        console.log(this.selected)
                    })
                    .catch(error => {
                        console.error('Failed to fetch role details:', error);
                    });
                }
                },
            fetchOptions() {
                axios.get('http://localhost:5011/Role_Skill')
                    .then(response => {
                        // Extract and set the options data to the options array
                        const roles = response.data.data['Roles-Skill'];
                        const uniqueRoleDesc = Array.from(new Set(roles.map(role => role.Role_Desc)));

                        // Create an array of objects with the unique Role_Desc values
                        this.options = uniqueRoleDesc.map(roleDesc => ({
                        name: roleDesc,
                        code: roleDesc
                        }));
                    })
                    .catch(error => {
                        console.error('Failed to fetch options:', error);
                    });
            },
            saveData() {
                // Here you can implement your Axios POST request to save the data
                const startDateSQL = this.revertToSQLDateFormat(this.input.startDate);
                const endDateSQL = this.revertToSQLDateFormat(this.input.endDate);

                // Here you can implement your Axios POST request to save the data
                axios.put('http://localhost:5018/HR/role_admin', {
                    role_name: this.input.roleName,
                    department: this.input.department,
                    description: this.input.roleDescription,
                    skills: this.selected.map(skill => skill.name),
                    start_date: startDateSQL,
                    end_date: endDateSQL,
                })
                .then(response => {
                    // Handle the response (e.g., show a success message)
                    console.log('Data saved successfully:', response.data);
                })
                .catch(error => {
                    // Handle errors (e.g., show an error message)
                    console.error('Failed to save data:', error);
                });
            }
        }
};
</script>

<style src="vue-multiselect/dist/vue-multiselect.css"></style>

<style @scoped>
    @import '@/assets/styling/staff_role_application.css';
    @import '@/assets/styling/hr_new_listing.css';
</style>