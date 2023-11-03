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
                                <button class="submit-btn">
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
 
    export default {
        name: 'roleApplication',
        components: {
            VueMultiselect,
        },
        mounted() {
            document.title = "All in One";
        },
        created() {
            console.log("working")
        },

        data() {
            return {
                selected: [
                    { name: 'Audit Compliance', code: 'Audit Compliance' },
                    { name: 'Audit Frameworks', code: 'Audit Frameworks' },
                    { name: 'Budgeting', code: 'Budgeting' }
                ],
                options: [
                    { name: 'Audit Compliance', code: 'Audit Compliance' },
                    { name: 'Audit Frameworks', code: 'Audit Frameworks' },
                    { name: 'Budgeting', code: 'Budgeting' }
                ],
                input: {
                    roleName: 'Account Manager',
                    department: 'Sales',
                    roleDescription: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla euismod, nisl vitae aliquam ultricies, nunc nisl ultricies nunc, vitae aliquam nisl nisl vitae aliquam ultricies, nunc nisl ultricies nunc, vitae aliquam nisl',
                    requiredSkills: ['Audit Frameworks', 'Budgeting', 'Business Acumen'],
                    
                    // joel plz take note i need the input dates like this for it to display properly
                    startDate: '2023-10-10',
                    endDate: '2023-10-20',
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
        }
    }
</script>

<style src="vue-multiselect/dist/vue-multiselect.css"></style>

<style @scoped>
    @import '@/assets/styling/staff_role_application.css';
    @import '@/assets/styling/hr_new_listing.css';
</style>