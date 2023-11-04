import {createRouter, createWebHistory} from "vue-router";

// const routes = [
//     // {
//     //     path: "/",
//     //     name: "loginPage",
//     //     component: () => import("../views/login_page.vue")
//     // },

//     {
//         path: "staff",
//         name: "staffPages",
//         component: () => import("../views/staff_navbar.vue"),
//         children: [
//             {
//                 path: "/overallListing",
//                 name: "overallListing",
//                 component: () => import("../views/staff_overall_listing.vue")
//             },
//             {
//                 path: "/My-Applications",
//                 name: "myApplications",
//                 component: () => import("../views/staff_myApplications.vue")
//             },
//             {
//                 path: "/My-Profile",
//                 name: "myProfile",
//                 component: () => import("../views/staff_myProfile.vue")
//             },
//             {
//                 path: "/Role-Listing",
//                 name: "roleListing",
//                 component: () => import("../views/staff_role_listing.vue")
//             },
//             {
//                 path: "/Role-Application",
//                 name: "roleApplication",
//                 component: () => import("../views/staff_role_application.vue")
//             },
//             {
//                 path: "/Application-Confirmation",
//                 name: "applicationConfirmation",
//                 component: () => import("../views/staff_application_confirmation.vue")
//             },
//             {
//                 path: "/View-Application",
//                 name: "viewApplication",
//                 component: () => import("../views/staff_view_application.vue")
//             },
//         ]
//     }
// ]

const routes = [
    {
        path: "/",
        name: "loginPage",
        component: () => import("../views/login_page.vue")
    },
    {
        path: "/overallListing",
        name: "overallListing",
        component: () => import("../views/staff_overall_listing.vue")
    },
    {
        path: "/My-Applications",
        name: "myApplications",
        component: () => import("../views/staff_myApplications.vue")
    },
    {
        path: "/My-Profile",
        name: "myProfile",
        component: () => import("../views/staff_myProfile.vue")
    },
    {
        path: "/Role-Listing",
        name: "roleListing",
        component: () => import("../views/staff_role_listing.vue")
    },
    {
        path: "/Role-Application",
        name: "roleApplication",
        component: () => import("../views/staff_role_application.vue")
    },
    {
        path: "/Application-Confirmation",
        name: "applicationConfirmation",
        component: () => import("../views/staff_application_confirmation.vue")
    },
    {
        path: "/View-Application",
        name: "viewApplication",
        component: () => import("../views/staff_view_application.vue")
    },
    {
        path: "/overallListing-HR",
        name: "overallListingHR",
        component: () => import("../views/hr_overall_listing.vue")
    },
    {
        path: "/Role-Listing-HR/:roleName",
        name: "roleListingHR",
        component: () => import("../views/hr_role_listing.vue")
    },
    {
        path: "/New-Listing-HR",
        name: "newListingHR",
        component: () => import("../views/hr_new_listing.vue")
    },
    // {
    //     path: "/View-Application-HR/:positionID",
    //     name: "viewApplicationHR",
    //     component: () => import("../views/hr_view_application.vue")
    // },
    {
        path: "/Edit-Listing-HR/:roleName",
        name: "editListingHR",
        component: () => import("../views/hr_edit_listing.vue")
    },
    {
        path: "/Create-Confirmation",
        name: "createConfirmation",
        component: () => import("../views/hr_create_confirmation.vue")
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
  });
  
export default router;