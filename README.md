
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
    - [Wire Frames](#wire-frames)
- [Agile Method](#agile-method)
- [Features](#features)
    - [Reservation feature](#reservation-feature)
    - [Cancelation Form](#cancelation-form)
    - [Staff Page](#staff-page)
    - [Navigation bar](#navigation-bar)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
    - [PEP8 Validator Extensions](#pep8-validator-extension)
    - [Lighthouse](#lighthouse)
    - [Manual Testing](#manual-testing)
    - [JsHint Validation](#jshint-validation)
    - [W3C Validator](#w3c-validator)
    - [Bug Fixes](#bug-fixes)
    - [Mentor Session](#mentor-session)
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

## Wire Frames

For the design thinking and briefing my layout in the early stages I made my own wireframes inside the mac os program 'pages'. These have helped me to structure the basics of my website and keep a consistant goal of where I'm heading with the UX in the early stages.

![IMAGE ALT TEXT HERE](/docs/screenshots/wireframes.png)

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

## Lighthouse
Furthermore, testing has been carried out on Performance, Accessibility, Best Practices, and SEO via Lighthouse testing in Chrome DevTools. 

![IMAGE ALT TEXT HERE](/docs/screenshots/lighthouse.png)
![IMAGE ALT TEXT HERE](/docs/screenshots/lighthouse_desktop.png)
## Manual Testing

Manual testing has been carried out accordingly:

* Tested all forms, through different web browsers (Firefox, Chrome & Safari).
* Tested that all forms post their data to the data base and that these are displayed where intended.
* That restricted content only is displayed to the correct users when authenticated.
* Tested CRUD features on the staff page and that these work and update the data base. 
* Testing that all alerts trigger when intended to notify the user
* All links have been tested that they work both on smal screen devices and desktop sized screens

## JsHint Validation

The Javascript file was validated with JSHint. There were warnings such as: couple of undefined variables, missing semicolons.

## W3C Validator

When it comes to the testing of the code, an outcome of errors were detected when running the W3C Validator for CSS and HTML. These were errors regarding the syntax used for the Built-in template tags ( '{% %}'  ). Therefore I ignored these errors since I did not find any way to let the test ignore these.

In the CSS there was an operator error found which has been resolved.

![IMAGE ALT TEXT HERE](/docs/screenshots/w3c_validation.png)

## Bug Fixes 

All bugs that I've found have been resolved. Among these were the following:
- Forms filled out not posting and adding the data to database.
    - Solution: In the 'Action' tag inside the HTML I had linked the page I wanted the user to be redirected to. This blocked the the data somehow and caused that no data was posted to the DB. I realized that I could put the redirect request inside the 'views.py' in order to redirect the user to the page I wanted. Once I did that, the data was finally posted to the database.

- No static files were loaded upon deployment.
    - I missunderstood how the 'load static' worked and thought that css stylesheet and JS as well as pictures were loaded without the {% static %} implementation. Once I deployed the project and removed the "DEBUG = False", I realized that no styling or media was loaded. Eventually I understood the mistake while searching on google for hours and realized how to link the files properly.

- Calendar picker loading previous dates.
    - When I added the calendar picker to the form it displayed previous dates. I didn't want that to happen and with some javascript manipulation I finally was able to set the min attribute on the date element.

- Model fields (Textfield, datefield, timefield), not user friendly.
    - The default model.models for the form fields of reserving tables model was just a textfield and said that the input was unvalid if not written with 'yyyy-mm-dd'. After lots of googling I found out that I could set attributes inside the forms.py file and managed to set the type to date and time. These loaded the calendar and time picker. I also added the min and max time for the time field so a user could not book slots before 12:00 and after 21:00.

- Among the major bugs mentioned above there were tons of smaller once such as the hamburger menu not being triggered properly, images not loading etc etc.. These were rooted in syntax errors and were often discoreved as I was going through the code and realized I had misspelled something etc.

## Mentor Session

- As time for dedline was closing up I realized I had to many feature ideas for the project and that I won't be able to code the detail features such as double bookings, 30 min time slot bookings etc. My mentor advices me to focus on what I had, make that code ready and then leave these "good to have features for another project". I deleted a few templates that I had made in the befinning and focused on what I had and to finish that. I'm very satified with the result but I also realize that there can be more done in terms of making the web app/system more effective for the user. However the main purpose and aim that I had for this project has been reached and my learning outcome has been huge. I feel a lot more confident and if I would have had more time to finish this project I know that I could have implemented the features that I had originally planned to have.

# Deployment

## Deploy locally

1. Create repository from code institutes template.
2. Installing Django and supporting libraries
3. Install Django, gunicorn, dj3-cloudinary-storage, dj_database_url psycopg2
4. Create requirements file -> pip3 freeze --local > requirements.txt
5. Terminal: django-admin startproject 'Name of project ."
6. Terminal: python3 manage.py startapp 'Name of app"
7. Go to settings.py and update INSTALLED_APPS=['Add your app name here']
8. Migrate changes -> Terminal: python3 manage.py migrate
9. Run server for testing if django is setup etc - > python3 manage.py runserver

## Deploying an app to Heroku

1. Create a new external database (For this project I chose to do this inside Heroku directly and pay the 5$). But here are the steps for free user:
    - On elephantsql.com
    - Log in to your ElephantSQL account
    - Click “Create New Instance”
    - Set up your plan (name, tiny-turtle(free).) 
    - Click “Select 
    - Click “Review”
    - Return to the ElephantSQL dashboard and click on the database instance name for this project
    - Copy your ElephantSQL database URL using the Copy icon. It will start with postgres://
2. Create the Heroku app
    - Go to heroku.com and login
    - Create new Heroku App
    - Open the settings tab
    - Click Reveal Config Vars
    - Add a Config Var called DATABASE_URL
4. Attach the database
    - Create new env.py file on top level directory
    - In env.py file: Import os library ("import os")
    - Set environment variables ("os.environ["DATABASE_URL"] = "Paste in ElephantSQL database URL"")
    - Add in secret key ("os.environ["SECRET_KEY"] = "Make up your own randomSecretKey"")
    - Add Secret Key to Config Vars at heroku.com 
5. Prepare our environment and settings.py file
    - Reference env.py ("from pathlib import Path import os [import dj_database_url
if os.path.isfile("env.py"):
   import env
]")
    - Remove the insecure secret key and replace it with ("SECRET_KEY")
    - Comment out the old DataBases Section
    - Add new DATABASES Section (DATABASES = {
   'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}")
    - Terminal: Save all files and Make Migrations
6. Get our static and media files stored on Cloudinary.
    - Go to cloudinary.com and log in.
    - Copy your CLOUDINARY_URL e.g. API Environment Variable.
    - in env.py file -> Add Cloudinary URL
    - heroku.com -> Add Cloudinary URL to Heroku Config Vars - be sure to paste in the correct section of the link
    - Add DISABLE_COLLECTSTATIC to Heroku Config Vars (temporary step for the moment, will be removed before deployment)
    - In settings.py -> Add Cloudinary Libraries to installed apps
    - Tell Django to use Cloudinary to store media and static files, place under the Static files note 
    (STATIC_URL = '/static/'

STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
)
