<template>
    <v-app>
        <v-container>
            <StaffNavbar v-if="role === 'staff'" />
            <HRNavbar v-if="role === 'hr'" />
            
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
                            placeholder="Select Department"
                            @click="filterRoles">
                        </VueMultiselect>
                        
                        <!-- <button @click="filterRoles">Test</button> -->
                        
                    </div>
                </div>
            </div>
            
            <br>
            
            <div class="container ms-auto">
                <div class="row">
                    <div class="row">
                        <div class="col-lg-4 col-md-6 col-12" v-for="card in filteredCardData" :key="card.id">
                            <div class="listing-card">
                                <p class="card-heading">{{ card.title }}</p>
                                <p class="card-subheading">{{ card.department }}</p>
                                <p class="card-deadline">Deadline: {{ card.deadline }}</p>
                                <p class="card-description">{{ card.description }}</p>
                                <router-link :to="{ name: 'roleListing', query: { id: card.id } }">
                                    <button class="card-find-btn">Find Out More</button>
                                </router-link>
                                <router-link :to="{ name: 'roleApplication', params: { id: card.id } , query: {id: card.id}}">
                                    <button class="card-apply-btn">APPLY</button>
                                </router-link>
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
import axios from 'axios';
// import { handleDropdown } from "../assets/js/dropdown.js";
import VueMultiselect from 'vue-multiselect'
import StaffNavbar from '@/components/staff_navbar.vue';
import HRNavbar from '@/components/hr_navbar.vue';

export default {
    name: 'overallListing',
    methods: {
        // handleDropdown,
        // Function to format the date string without the time
        formatDate(dateString) {
            if (!dateString || dateString === 'null') {
                return 'N/A'; // Handle cases where the date is null or empty
            }
            const date = new Date(dateString);
            return date.toLocaleDateString(); // Convert the date to a locale string
        },
        async searchRoles() {
            const url = "http://127.0.0.1:5006/Open_Position/Search";
            // console.log(this.cardData);
            try {
                const response = await axios.get(url, {
                    params: {
                        search_input: this.searchInput
                    }
                })
                
                console.log(response);
                if (response.status === 200) {
                    console.log("testing search");
                    console.log(response.data.data);
                    var openPositions = response.data.data.open_positions;
                    // console.log(openPositions[0]);
                    var filteredData = [];
                    for (var i = 0; i < openPositions.length; i++) {
                        console.log(openPositions[i]);
                        let id = openPositions[i].Position_ID;
                        let title = openPositions[i].Role_Name;
                        let department = openPositions[i].Department;
                        let deadline = this.formatDate(openPositions[i].Ending_Date);
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
        },
        async filterRoles() {
            console.log("filter");
            console.log(this.selectedDepartments);
            const filterURL = "http://127.0.0.1:5006/Open_Position/Dept"
            console.log(this.selectedDepartments);
            let deptParam = this.selectedDepartments.join(",");
            
            try {
                const response = await axios.get(filterURL, {
                    params: {
                        departments: deptParam
                    }
                });
                
                console.log(response);
                if (response.status === 200) {
                    console.log("testing filter");
                    console.log(response.data.data);
                    var openPositions = response.data.data.open_positions;
                    var filteredData = [];
                    for (var i = 0; i < openPositions.length; i++) {
                        console.log(openPositions[i]);
                        let id = openPositions[i].Position_ID;
                        let title = openPositions[i].Role_Name;
                        let department = openPositions[i].Department;
                        let deadline = this.formatDate(openPositions[i].Ending_Date);
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
                    this.filteredData = filteredData;
                }
                
                
            } catch (error) {
                console.log(error);
                console.log("error");
            }
        }
    },
    components: {
        VueMultiselect,
        StaffNavbar,
        HRNavbar
    },
    mounted() {
        document.title = "All in One";
        // On mount, get open role listing data from flask app and store in cardData
        axios.get('http://127.0.0.1:5013/All_Role_Listing')
        .then(response => {
            var roleData = response.data.data.Role_Listing; 
            this.cardData = [];
            for (var i = 0; i < roleData.length; i++) {
                let id = roleData[i].Position_ID;
                let title = roleData[i].Role_Name;
                let department = roleData[i].Department;
                let deadline = this.formatDate(roleData[i].Ending_Date);
                let description = roleData[i].Role_Desc;
                
                this.cardData.push({
                    id: id,
                    title: title,
                    department: department,
                    deadline: deadline,
                    description: description
                })
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    },
    created() {
        console.log("working")
    },
    data() {
        return {
            searchInput: "",
            selectedDepartments: [],
            filteredData: null,
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
            if (this.searchInput || this.selectedDepartments.length > 0) {
                console.log("returning filteredData");
                console.log(this.filteredData);
                return this.filteredData;
            } else {
                return this.cardData;
            }
        },   
        
        role() {
            return this.$route.params.role;
        }
    }
}
</script>

<style src="vue-multiselect/dist/vue-multiselect.css"></style>

<style @scoped>
@import '@/assets/styling/staff_overall_listing.css';
</style>