<template>
    <v-app>
        <v-container>
            <div style="padding-top: 80px; padding-bottom: 80px;">

                <div class="container ms-auto">
                    <div class="page-head">
                        <div class="centered-svg">
                            <svg viewBox="0 0 26 26" xmlns="http://www.w3.org/2000/svg" style="color: var(--application-success)">
                            <g stroke="currentColor" stroke-width="2" fill="none" fill-rule="evenodd" stroke-linecap="round" stroke-linejoin="round">
                                <path class="circle" d="M13 1C6.372583 1 1 6.372583 1 13s5.372583 12 12 12 12-5.372583 12-12S19.627417 1 13 1z"/>
                                <path class="tick" d="M6.5 13.5L10 17 l8.808621-8.308621"/>
                            </g>
                            </svg>
                        </div>

                        <p class="page-heading" style="text-align: center;">Success!</p>

                        <br>

                        <p class="page-subheading" style="text-align: center;">Your Application has been successfully submitted.</p>
                    </div>

                    <br><br>

                    <div style="text-align: center;">
                        <router-link :to="{ name: 'myApplications'}">
                            <button class="card-apply-btn">View My Applications</button>
                        </router-link>
                    </div>
                </div>

                <!-- <div class="container ms-auto">
                    <div class="page-head">
                        <div class="centered-svg">
                            <svg viewBox="0 0 26 26" xmlns="http://www.w3.org/2000/svg" style="color: var(--application-failure)">
                            <g stroke="currentColor" stroke-width="2" fill="none" fill-rule="evenodd" stroke-linecap="round" stroke-linejoin="round">
                                <path class="circle" d="M13 1C6.372583 1 1 6.372583 1 13s5.372583 12 12 12 12-5.372583 12-12S19.627417 1 13 1z"/>
                                <path class="cross" d="M7 7, L19 19, M7 19, L19 7"/>
                            </g>
                            </svg>
                        </div>

                        <p class="page-heading" style="text-align: center;">Error!</p>

                        <br>
                        
                        <p class="page-subheading" style="text-align: center;">An Error was encountered when attempting to submit.</p>
                        <p class="page-subheading" style="text-align: center;">Please try again later.</p>

                    </div>

                    <br><br>

                    <div style="text-align: center;">
                        <router-link :to="{ name: 'myApplications'}">
                            <button class="card-apply-btn">View My Applications</button>
                        </router-link>
                    </div>
                </div> -->

            </div>
        </v-container>
    </v-app>
</template>

<script>
</script>

<style @scoped>
    @import '@/assets/styling/staff_application_confirmation.css';
</style>