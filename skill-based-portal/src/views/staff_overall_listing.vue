<template>
    <v-app>
        <v-container>
            <div style="padding-top: 80px; padding-bottom: 80px;">

                <div class="container ms-auto">
                    <div class="page-head">
                        <p class="page-heading">All Role Listings.</p>
                        <p class="page-subheading">Browse all available Role Listings.</p>
                    </div>
                </div>

                <br>
        
                <div class="container ms-auto">
                    <div class="search-and-filter row">
                        <div class="col-6">
        
                            <div class="input-box">
                                <i class="uil uil-search"></i>
                                <input type="text" v-model="searchInput" @input="searchRoles" placeholder="Search" />
                                <!-- <button class="button">Search</button> -->
                            </div>
        
                        </div>
        
                        <div class="col-6">
                            <!-- <div class="select-btn" @click="handleDropdown">
                                <span class="btn-text">Select Department</span>
                                <span class="arrow-dwn">
                                    <i class="fa-solid fa-chevron-down"></i>
                                </span>
                            </div> -->

                            <!-- <ul class="list-items"> -->
                                <!-- Use v-for to loop through departments and generate list items -->
                                <!-- <li class="item" v-for="(department, index) in departments" :key="index">
                                    <span class="checkbox">
                                    <i class="fa-solid fa-check check-icon"></i>
                                    </span>
                                    <span class="item-text">{{ department }}</span>
                                </li>
                            </ul> -->

                            <VueMultiselect
                                v-model="selectedDepartments"
                                :options="departments"
                                :close-on-select="false"
                                :multiple="true"
                                placeholder="Select Department">
                            </VueMultiselect>
                            
                        </div>
                    </div>
                </div>
        
                <br>
        
                <div class="container ms-auto">
                    <div class="row">

                        <router-link class="router-link-custom" :to="{ name: 'roleListing'}">
                        <!-- <router-link :to="{ name: 'specificListing', params:{ id: 1 }}"> -->
                            <a href="./views/specific_listing.vue"></a>

                            <div class="row">
                                <div class="col-lg-4 col-md-6 col-12" v-for="card in filteredCardData" :key="card.id">
                                    <div class="listing-card">
                                    <p class="card-heading">{{ card.title }}</p>
                                    <p class="card-subheading">{{ card.department }}</p>
                                    <p class="card-deadline">Deadline: {{ card.deadline }}</p>
                                    <p class="card-description">{{ card.description }}</p>
                                    <router-link :to="{ name: 'roleListing', params: { id: card.id } }">
                                        <button class="card-find-btn">Find Out More</button>
                                    </router-link>
                                    <router-link :to="{ name: 'roleApplication', params: { id: card.id } }">
                                        <button class="card-apply-btn">APPLY</button>
                                    </router-link>
                                    </div>
                                </div>
                                </div>

                        </router-link>

                    </div>
                </div>
            </div>
        </v-container>
    </v-app>
</template>

<script>
    import axios from 'axios';
    import { handleDropdown } from "../assets/js/dropdown.js";
    import VueMultiselect from 'vue-multiselect'

    export default {
        name: 'overallListing',
        methods: {
            handleDropdown,
            async searchRoles() {
                const url = "http://127.0.0.1:5006/Open_Position/Search";
                console.log(this.cardData);
                try {
                    const response = await axios.get(url, {
                            params: {
                                search_input: this.searchInput
                            }
                    })
                    
                    console.log(response);
                    if (response.status === 200) {
                        console.log("testing");
                        console.log(response.data.data);
                        var openPositions = response.data.data.open_positions;
                        // console.log(openPositions[0]);
                        var filteredData = [];
                        for (var i = 0; i < openPositions.length; i++) {
                            console.log(openPositions[i]);
                            let id = openPositions[i].Position_ID;
                            let title = openPositions[i].Role_Name;
                            let department = openPositions[i].Department;
                            let deadline = openPositions[i].Ending_Date;
                            let description = openPositions[i].Role_Desc;

                            filteredData.push({
                                id: id,
                                title: title,
                                department: department,
                                deadline: deadline,
                                description: description
                            })
                        }

                        console.log(filteredData);
                        // return filteredData;
                        this.filteredData = filteredData;
                    }


                } catch (error) {
                    console.log(error);
                    console.log("error");
                }
            }
        },
        components: {
            VueMultiselect
        },
        mounted() {
            document.title = "All in One";
        },
        created() {
            console.log("working")
        },
        data() {
            return {
            searchInput: "",
            cardData: [
                {
                id: 1,
                title: "Account Manager",
                department: "Sales",
                deadline: "15 October 2023",
                description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc quis faucibus est. Proin tristique dolor et tortor venenatis, auctor vestibulum risus consequat. Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                },

                {
                id: 2,
                title: "Finance Manager",
                department: "Finance",
                deadline: "15 October 2023",
                description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc quis faucibus est. Proin tristique dolor et tortor venenatis, auctor vestibulum risus consequat. Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                },

                {
                id: 3,
                title: "Developer",
                department: "IT",
                deadline: "15 October 2023",
                description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc quis faucibus est. Proin tristique dolor et tortor venenatis, auctor vestibulum risus consequat. Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                },

                {
                id: 1,
                title: "Account Manager",
                department: "Sales",
                deadline: "15 October 2023",
                description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc quis faucibus est. Proin tristique dolor et tortor venenatis, auctor vestibulum risus consequat. Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                },

                {
                id: 2,
                title: "Account Manager",
                department: "Sales",
                deadline: "15 October 2023",
                description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc quis faucibus est. Proin tristique dolor et tortor venenatis, auctor vestibulum risus consequat. Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                },

                {
                id: 3,
                title: "Account Manager",
                department: "Sales",
                deadline: "15 October 2023",
                description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc quis faucibus est. Proin tristique dolor et tortor venenatis, auctor vestibulum risus consequat. Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                },
            ],
            selectedDepartments: null,

            departments: [
                // {name: 'Chairman', code: 'CH'},
                // {name: 'CEO', code: 'CEO'},
                // {name: 'Sales', code: 'SA'},
                // {name: 'Engineering', code: 'EN'},
                // {name: 'HR', code: 'HR'},
                // {name: 'Finance', code: 'FIN'},
                // {name: 'Consultancy', code: 'CO'},
                // {name: 'Solutioning', code: 'SO'},
                // {name: 'IT', code: 'IT'}
                "Chairman",
                "CEO",
                "Sales",
                "Engineering",
                "HR",
                "Finance",
                "Consultancy",
                "Solutioning",
                "IT"
            ],
            };
        },
        computed: {
            filteredCardData() {
                if (this.searchInput) {
                    return this.filteredData;
                } else {
                    return this.cardData;
                }
            }   
        }
    }
</script>

<style src="vue-multiselect/dist/vue-multiselect.css"></style>

<style @scoped>
    @import '@/assets/styling/staff_overall_listing.css';
</style>