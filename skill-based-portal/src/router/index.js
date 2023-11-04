import {createRouter, createWebHistory} from "vue-router";

const routes = [
    {
        path: "/",
        name: "loginPage",
        component: () => import("@/views/login_page.vue")
    },
    
    {
        path: "/overallListing/:role",
        name: "overallListing",
        component: () => import("../views/staff_overall_listing.vue"),
        props: true,
    },
    {
        path: "/My-Applications/:role",
        name: "myApplications",
        component: () => import("../views/staff_myApplications.vue"),
        props: true,
    },
    {
        path: "/My-Profile/:role",
        name: "myProfile",
        component: () => import("../views/staff_myProfile.vue"),
        props: true,
    },
    {
        path: "/Role-Listing/:role",
        name: "roleListing",
        component: () => import("../views/staff_role_listing.vue"),
        props: true,
    },
    {
        path: "/Role-Application/:role",
        name: "roleApplication",
        component: () => import("../views/staff_role_application.vue"),
        props: true,
    },
    {
        path: "/Application-Confirmation/:role",
        name: "applicationConfirmation",
        component: () => import("../views/staff_application_confirmation.vue"),
        props: true,
    },
    {
        path: "/View-Application/:role",
        name: "viewApplication",
        component: () => import("../views/staff_view_application.vue"),
        props: true,
    },
    {
        path: "/overallListing-HR/:role",
        name: "overallListingHR",
        component: () => import("../views/hr_overall_listing.vue"),
        props: true,
    },
    {
        path: "/Role-Listing-HR/:roleName/:role",
        name: "roleListingHR",
        component: () => import("../views/hr_role_listing.vue"),
        props: true,
    },
    {
        path: "/New-Listing-HR/:role",
        name: "newListingHR",
        component: () => import("../views/hr_new_listing.vue")
    },
    {
        path: "/Edit-Listing-HR/:roleName/:role",
        name: "editListingHR",
        component: () => import("../views/hr_edit_listing.vue")
    },
    // {
    //     path: "/Create-Confirmation",
    //     name: "createConfirmation",
    //     component: () => import("../views/hr_create_confirmation.vue")
    // },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
  });
  
export default router;