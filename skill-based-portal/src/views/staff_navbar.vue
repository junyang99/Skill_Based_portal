<template>
    <div id="app">
        <link rel="stylesheet" href="https://unicons.iconscout.com/release/v4.0.0/css/line.css" />
            <nav>
              <ul style="margin-bottom: 0;">
                  <li> <img src="@/assets/logo.png" class="logo"> </li>
  
                  <div class="staff-links">
  
                      <li class="nav-link">
                      <router-link :to="{ name: 'overallListing'}">
                          <a href="./views/overall_listing.vue">Role Listing</a>
                      </router-link>
                      </li>
  
                      <li class="nav-link">
                      <router-link :to="{ name: 'myApplications'}">
                          <a href="./views/myApplications.vue">My Applications</a>
                      </router-link>
                      </li>
  
                      <li class="nav-link">
                      <router-link :to="{ name: 'myProfile'}">
                          <a href="./views/myProfile.vue">My Profile</a>
                      </router-link>
                      </li>
  
                  </div>
  
                  <div class="left-align">
                    <div id="nav-user">
                        <li id="nav-user">
                        <img src="@/assets/icons/user.png" style="height: 40px; width: auto;">
                        </li>
    
                        <li id="nav-user">
                        <div> {{ userName }} </div>
                        <div> {{ userRole }} </div>
                        </li>
                    </div>
                  </div>
                  
              </ul>
            </nav>
  
        <main>
        <div>
            <router-view></router-view>
        </div>
        </main>
    </div>
  </template>
  
  <script>
  import "bootstrap/dist/css/bootstrap.min.css";
  import "bootstrap/dist/js/bootstrap.min.js";
  import '@fortawesome/fontawesome-free/css/all.css';
  
  export default {
  data() {
    return {
      userName: "Alice Tan",
      userRole: "Staff",
    };
  },
  };
  </script>
  
  <style>
    @import '../assets/styling/nav.css';
    @import '../assets/styling/styles.css';
    @import '../assets/styling/staff_search.css';
    @import '../assets/styling/staff_filter.css';
    @import '../assets/styling/staff_overall_listing.css';
    @import '../assets/styling/staff_role_listing.css';
    @import url('https://unicons.iconscout.com/release/v4.0.0/css/line.css');
  </style>