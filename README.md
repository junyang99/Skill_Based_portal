# Skill_Based_portal

Our Vue.js application, Skill_Based_Portal, helps our organization find the right people for job openings. We encourage our staff to learn and grow. This app lets staff apply for jobs they like and shows how their skills match the job. Managers and HR can use it to find good candidates. It makes it easier for our staff to grow and for our organization to find the right talent.

## Table of Contents
    - Features
    - Getting Started
    - Prerequisites 
    - Installation
    - Usage
    - Contributions

## Feature
The key features of our applications are
    1. CRU of Role Listings
    2. View skills of role applicants
    3. Browse and Filter Role Listing
    4. View Role-Skill Match
    5. Apply for role

## Prerequisites

The following list of software and/or dependencies must be installed in your device before running the application
1. Flask
2. Sqlalchemy
3. Flask-cors
4. Requests
5. Unittest
6. Flask_Testing
7. mysql-connector-python

## Installation
To install and run the app, run the following command after you have downloaded the application

## Step 1 - Run Mamp/Wamp
## Step 2 -  Global search and replace database uri as required
### 1. **Changing the variables:**

   To change the username to `newuser`, password to `newpassword` and port to `8889` modify the URI like this:

   ```python
   app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://newuser:newpassword@localhost:8889/hr_portal" 
   ```
## Step 3 - Import.sql to local sql server and import sql file in the following sequence
1. access_control 
2. role
3. skill
4. staff
5. role_skill
6. staff_skill
7. open_position
8. application

# Step 4 - Running the application
### Running the Application on Windows

## Method 1: Using the Terminal
1. Open your preferred terminal.
2. Navigate to the `Skill_based_portal` directory:
    - cd path\to\Skill_based_portal
3. Execute the provided `run.bat` script:
    - .\run.bat

## Method 2: Opening via File Explorer
1. Navigate to your project folder and locate the `run.bat` file.
2. Double-click the `run.bat` file.

### Running the Application on Mac/Linux
1. Open your preferred terminal.
2. Navigate to the `Skill_based_portal` directory:
    - cd path/to/Skill_based_portal/
3. To give permission for the `run_utils.sh` script to be executed, run the following command:
    - chmod +x run_utils.sh
4. Execute the provided `run_utils.sh` script:
    - ./run_utils.sh
  

