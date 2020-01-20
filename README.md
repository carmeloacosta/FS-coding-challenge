# Yoga Solo -  Full Stack code challenge

Congratulations! You’re nearly there to join our team as Full Stack developer! 

We have a really big issue in our office and we need you to solve it. We are trying to practice Yoga, but we are not able to remember the different postures, and we need your superpowers as Full Stack to provide us a solution for it! 

# Install dependencies

It is possible to simply install dependencies and run it. Simply run the following commands from 
the root directory (where is located requirements.txt file) to install dependencies:

    python3 -m pip install -r requirements.txt
    cd yoga
    python3 manage.py makemigrations
    python3 manage.py migrate --run-syncdb
    
And then run the HTTP server, exposing the API, running the following command

    python3 manage.py runserver

# Run all tests

First, install dependencies (see prior section)
Then, from the root directory (where is located manage.py file) run

    python manage.py test

# Run a single test

From the root directory (where is located manage.py file) run

    python manage.py test yoga.tests.<test_file_name>.<test_class_name>.<test_name>

Example:

    python manage.py test yoga.tests.tests_models.ModelsTestCase.test__new_posture__ok


## What we need? 

Here you have the user stories we would need:

- **[YS-1]** As a user, I should be able to see all the postures that are in the system

## What you should do?

Create a project, install dependencies needed and run a web server using your favourite tech stack.

### Backend

- Design a SQL or NoSQL database
- The system should have the following features:
    - Be able to add Yoga postures
        - A posture has a name, image and a description
    - Given a list of postures generate a list of entries in the database
    - Login / Registration (Plus)
        - User registration:
            - A user would need to enter a name, email and password
        - Login with email and password
- API RESTful. Generate routes and use cases to get the list of available postures (login and register routes too, if the bonus points are done)

Due that this is not a real case, we don't need a complex registration / login system, for the scope of this challenge we are happy with a register / login system that stores the data directly to the database and just compares the username and password to check if the user is registered and can go to their private area. 

### Frontend

Create a view or use a template to present the list of postures, consuming the above API. Also, the user should be able to see a text field showing his name when he is logged in.

### Bonus Points

- **[YS-2]** As a user, If I want to add a new posture in the system, this posture would be available for all the users
- **[YS-3]** As a user, I should be able to Register/Log In to the system
- **[YS-4]** As a user, when I Log In, I would enter to my private space (where I would see my name and all the postures that are in the system)
- **[YS-5]** As a user, I can see the design in different devices and it has to be responsive

## General Advice and Tips:

- We like code that is simple, but [simple is different from easy](https://www.infoq.com/presentations/Simple-Made-Easy).
- Keep in mind the [SOLID principles](https://en.wikipedia.org/wiki/SOLID_(object-oriented_design)) when doing the project.
- Testing is very important for us. Even if you don't write a single test (for instance, because of time constraints), your app should be easy to test (we love [Dependency injection](https://en.wikipedia.org/wiki/Dependency_injection)).
- Error scenarios should be taken into consideration and it should be easy to add them, even if you don't explicitly handle them.
- Although UI and UX are important, we are more concerned in this demo with your thought process and with how you architect your solution. 
- Your demo should take into consideration features that might be added in the future.
- You can use any 3rd party libraries you wish but be prepared to justify why you did so.
- Be consistent in your code. 
- Be opinionated regarding any architecture you use and take your time to make it a reflection of your thought process.
- A good documentation is always welcome, if there’s something that needs to be documented in order to run the project or whatever that you thing is not clear enough (or something that you would do better in a real project, but for time constraints your doing it in a faster way, just justify it and let us know how it would be the good solution)

## Submitting your solution

- Create a fork of this project
- Do your code
- Commit frequently, we would love to see how you work and how you create your solution
  - Don't be afraid of not perfect code on pushed commits, we would check the final code that appears in the Pull Request
- Remember to use descriptive commit messages
- Use the README.md file to explain what you did
  - Hand in your solution along with any notes, comments, and assumptions you have made while working on the solution


This technical test is **NOT** time boxed, but time is taken into consideration just as any other factor when reviewing your solution.

## Data

Here you have some postures in JSON format that you can use to fill your DB:

```json
[
    {
      "id": "5df111bd23f72ffeefe0fa31",
      "name": "Inversion on block",
      "picture": "https://loremflickr.com/320/320/yoga,asana",
      "description": "The posture inversion on block lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    },
    {
      "id": "5df111bd3b1537fd3ed6a94a",
      "name": "Stretch with strap",
      "picture": "https://loremflickr.com/320/320/yoga,asana",
      "description": "The posture stretch with strap lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    },
    {
      "id": "5df111bde6b47a0cdfb264e9",
      "name": "Arm Pose",
      "picture": "https://loremflickr.com/320/320/yoga,asana",
      "description": "The posture arm pose lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    },
    {
      "id": "5df111bde57dcfa0bdcdcec1",
      "name": "Sphinx rotation",
      "picture": "https://loremflickr.com/320/320/yoga,asana",
      "description": "The posture sphinx rotation lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    },
    {
      "id": "5df111bdbbaf1a0d62492bbe",
      "name": "Inverted pose",
      "picture": "https://loremflickr.com/320/320/yoga,asana",
      "description": "The posture inverted pose lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    },
    {
      "id": "5df111bda3f02dd8a3b143c1",
      "name": "Lying down on block",
      "picture": "https://loremflickr.com/320/320/yoga,asana",
      "description": "The posture lying down on block lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
    },
    {
      "id": "5df111bd06b2ec5a2e0ba268",
      "name": "Simple twist",
      "picture": "https://loremflickr.com/320/320/yoga,asana",
      "description": "The posture simple twist lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    },
    {
      "id": "5df111bd4e67358b133d42fe",
      "name": "Turtle pose",
      "picture": "https://loremflickr.com/320/320/yoga,asana",
      "description": "The posture turtle pose lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    },
    {
      "id": "5df111bd836c69d124cb25e3",
      "name": "Hip Pose",
      "picture": "https://loremflickr.com/320/320/yoga,asana",
      "description": "The posture hip pose lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    },
    {
      "id": "5df111bd95e020c3a7019779",
      "name": "Rotated wheel pose",
      "picture": "https://loremflickr.com/320/320/yoga,asana",
      "description": "The posture rotated wheel pose lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    },
    {
      "id": "5df111bd2c1f5cbc414ef3d2",
      "name": "Archer",
      "picture": "https://loremflickr.com/320/320/yoga,asana",
      "description": "The posture archer lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    },
    {
      "id": "5df111bd10ded18b8400e585",
      "name": "Horse pose",
      "picture": "https://loremflickr.com/320/320/yoga,asana",
      "description": "The posture horse pose lorem ipsum dolor sit amet, consectetur adipiscing elit."
    }
  ]
```

## Thanks

The structure of this README has been inspired by:
https://github.com/luvotels/fs-hiring-test





