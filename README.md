
# Be-Be-Boba - Portfolio project 4

Be-Be-Boba is a restaurant that serves bubble tea. The website is a system that gives customers the ability to make/cancel bookings, check out the menu as well as read about the history of Be-Be-Boba. Furthermore staff has access to login and manage bookings where they are able to see the bookings and have a list of cancelations.
The manager login has access to edit the menu.

You can access the deployed system/web page here: <a href="https://bookboba.herokuapp.com/" target="_blank">Be-Be-Boba Home Page</a>

![IMAGE ALT TEXT HERE](/docs/screenshots/responsive_header.png)

# Contents
- [Project Aim](#project-aim)
- [User Experience](#user-experience)
    - [Site Aims](#site-aims)
    - [User Stories](#user-stories)
- [Agile Method](#agile-method)
- [Features](#features)
    - [Reservation feature](#reservation-feature)
    - [Cancelation Form](#cancelation-form)
    - [Staff Page](#staff-page)
    - [Navigation bar](#navigation-bar)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
    - [PEP8 Validator Extensions](#pep8-validator-extension)
    - [Manual Testing](#manual-testing)
    - [Bug Fixes](#bug-fixes)
- [Deployment](#deployment)
- [Credits](#credits)

# Project Aim

The aim of this project has been to build a full-stack site based on business logic used to control a centrally-owned dataset. Features such as user authentication, role based accessability to request and manipulate data as well as create a booking system where data is stored, updated and editable with the concept of 'CRUD' for (in this case) a bubble tea restaurant.

# User Experience

## Site Aims

* To provide an interactive website/web-app/system that is accessible from desktops and mobile devices for booth potential customers & staff.

* Customers: To provide a webpage where the customer can see the menu, make and cancel a booking as well as read about the restaurant.

* Staff User: To see and edit bookings and cancelations.
* Staff Manager User: To see and edit bookings, cancelations and the menu which is displayed for the customers that visit the home page.

## User Stories

|  |  |  |   |
|-----------------|:-------------|:---------------:|:---------------:|
| 1 | User | As a user, I want to see a menu of the bubble tea that the restaurant offer | So I can choose if they have exciting flavours that I'd like to try|
| 2 | User | As a user, I want to be able to book a table at the restaurant | So I can assure to get a table if I plan to visit the restaurant |
| 3 | User | As a user, I want to be able to read about the history of the restaurant | So I can learn about the background of the restaurant |
| 4 | User | As a user, I want to be able to cancel a booking and have access to contact information | So I can easerly get in touch if I have questions or need to cancel a booking |
| 5 | User | As a staff user, I want to have the ability to see/edit and delete all the bookings that have come in | So I can have an overview of guests and adept the day accordingly |
| 6 | User | As a staff user, I want to be able see all cancelations that have come in | So I can remove the reservations that have been cancelled |
| 7 | User | As a manager user, I want be able to edit the menu | So I can add and remove items when the menu has to be updated |
|  | User | As a  user, I want to have a clear overview of how to navigate through the web page through the nav bar | So I can have a clear user navigation experience |

# Agile Method

For the project back-log I have used the built in board feature that can be found inside github (canban similarities). I made user stories in order to have a structured overview of which features I wanted for the system and website.

The process has made it clear of what has to be done but also been iterative in forms of that I have adjusted the user stories when I realized that I had articulated in a different way than what turned out to be the final result for the page.

Some user stories have been removed as the deadline was coming closer. Among the user stories that I did not have time to finish were: to limit booking slots to 30 min slots, prevent double bookings and refine the cancelation form so staff doesn't have to remove these "manually" on the staff page.

![IMAGE ALT TEXT HERE](/docs/screenshots/agile_canban_user_stories.png)

# Features

## Reservation feature

When the user enters the home page they see the menu followed by a reservation form.

![IMAGE ALT TEXT HERE](/docs/screenshots/reserve_table.png)

When the form is filled out the user is notified and redirected to the 'about us page'. What happens in the background is that the reservation is stored in the data base and can now be seen bu the staff in the staff page, where staff can edit & delete the reservation. 

## Cancelation form

If a user/customer has made a booking and wants to cancel a booking that can fill out the following form on the 'contact us' page. This cancelation will then be reflected on the staff page for the staff to see.

![IMAGE ALT TEXT HERE](/docs/screenshots/cancelation_form.png)

## Staff Page

On the staff page the user has to be signed in in order to access the content. Depending on if the user is a super-user (manager user) or a staff user they will see the following features on the page. Since staff has not access to manipulate data that is desplayed to customers they can edit and manage bookings & cancelations.

If the menu has to be updated a manger user needs to be logged in, in order to make edits.

![IMAGE ALT TEXT HERE](/docs/screenshots/staff_page.png)

When the user clicks on the edit buttons they will be redirected to the according pages where they can fill out what they wish to edit, which then will be reflected in the data-base and displayed.

![IMAGE ALT TEXT HERE](/docs/screenshots/edit_menu_reservations.png)

## Navigation bar

The navigation bar offer a clear way to navigate through the different pages of the web page. Depending on if a user is logged in they will see different navigation bars.

Furthermore a hamburger menu feature has been added in order to give a cleaner experience when using smaller screen sized devices.

![IMAGE ALT TEXT HERE](/docs/screenshots/nav_bar.png)

# Technologies Used
* <a href="https://en.wikipedia.org/wiki/HTML5">HTML5</a> - to provide structure to the templates that are loaded for the user.
* <a href="https://en.wikipedia.org/wiki/CSS">CSS3</a> - styling the templates
* <a href="https://en.wikipedia.org/wiki/JavaScript">JavaScript</a> - Manipulate the dom and build an interactive user expereience
* <a href="https://www.python.org/">Python</a> - to build functionality to the system
* <a href="https://www.djangoproject.com/">Django</a> - framework that is used for this project
* <a href="https://developer.chrome.com/docs/devtools/">Google Chrome DevTools</a> - Debugging
* <a href="https://www.gitpod.io/">Gitpod</a> - Used to create, edit and write the code for the program
* <a href="https://dashboard.heroku.com/">Heroku</a> - Used to deploy the page
* <a href="https://www.elephantsql.com/">PostgreSQL</a> - Data base system used for this project
* <a href="https://cloudinary.com/">Cloudinary</a> - Cloud based image management service used for the project

# Testing

## PEP8 Validator Extension
Running the pep8 validator extension within gitpod showed a number of errors and warnings. Among these where syntax errors such as 2 blank lines after classes, trailing white spaces, function etc. Furthermore, long lines have been shortened and class names have been changed to camel cased, starting with a capital letter. 

Regarding a few long lines I could not shorten all of these because another pep8 warning came up as a result. Therefore I have kept these long and ignored that warning. 

![IMAGE ALT TEXT HERE](/docs/screenshots/pep8_validator.png)

## Manual Testing

Manual testing has been carried out accordingly:

* Tested all forms, through different web browsers (Firefox, Chrome & Safari).
* Tested that all forms post their data to the data base and that these are displayed where intended.
* That restricted content only is displayed to the correct users when authenticated.
* Tested CRUD features on the staff page and that these work and update the data base. 