PRIDE PARK

![Main Mockup](static/images/mockupB.png)

[Link to Live Website](https://pride-park.herokuapp.com/)

[GitHub Repo](https://github.com/mika-sims/pride-park)
Happy blogging!


*** 

## About  
Welcome to Pride park, a webapp to helps bloggers with similar interest interact with each other! 
This is a Python Flask app using MongoDB to produce a social blogging  application.

Pride Park brings bloggers together and allows them to interact and share their interests in similar subjects! 
Anyone can write on Pride Park . Thought-leaders, journalists, experts, and individuals with unique perspectives can share their thinking here.
The application lets users create a profile that allows them to add their  details, add photos, let other users know when they last posted,how many followers they have add comments both  and private message each other.
The site offers the additional functionality; reset passwords, change passwords contact us, editing and deleting comments, backend validation. Please look at the [features](#features) section for a more detailed description. 

 
## Index – Table of Contents

- [User Experience (UX)](#user-experience--ux-)
- [Strategy](#strategy)
  * [User Stories](#user-stories)
- [Scope](#scope)
- [Structure](#structure)
- [Database](#database)
- [Validation](#validation)
  * [Backend Validation](#backend-validation)
  * [Front End Validation](#front-end-validation)
- [Security](#security)
- [Features](#features)
- [Design](#design)
- [Skeleton](#skeleton)
  * [Layout](#layout)
- [Surface](#surface)
  * [Typography](#typography)
  * [Call to Action](#call-to-action)
  * [Imagery](#imagery)
- [Technologies](#technologies)
    + [Languages & Frameworks](#languages---frameworks)
    + [Front End](#front-end)
    + [Backend](#backend)
    + [Helpers](#helpers)
    + [Planning](#planning)
  * [Flask](#flask)
    + [Testing Tools](#testing-tools)
    + [Technology Configuration](#technology-configuration)
    + [MongoDB](#mongodb)
  * [Flask Mail](#flask-mail)
- [Testing](#testing)
- [Deployment](#deployment)
  * [Configuration](#configuration)
    + [Local Environment](#local-environment)
  * [Adding and Committing files](#adding-and-committing-files)
  * [Deploying](#deploying)
  * [Forking](#forking)
  * [Cloning](#cloning)
- [Known Bugs](#known-bugs)
- [Acknowledgements](#acknowledgements)
  * [Credit](#credit)
      - [People](#people)
      - [Additional Testers](#additional-testers)
      - [Tools and Docs](#tools-and-docs)
  * [Code:](#code-)
  * [Content:](#content-)
  * [Inspiration & Research:](#inspiration---research-)


*** 

## User Experience (UX)
## Strategy
Everyone has got something interesting to say or even full depth of knowledge about a particular subject.
Pride Park enables people to blog about anything and everything and also provides users with a way to communicate with others and attain information about a particular subject.


### User Stories 

### A typical user of this site would:
 - Have an interest in writing blogs
 - Reading blogs from other bloggers
 - Have an interest in being part of a blogging community.
 - Have an interest in gaining knowledge far beyond his/ her neighbourhood or circle.
 - connect with fellow bloggers from around the world.


#### New User
1. As a new user to the website, I want to understand the purpose of the site and how to interact with it.
2. As a new user,i want to explore blogposts written by other bloggers easily without registering
3.  As a new user ,I would like to easily register 



#### Existing User
1.As an existing user to the website, I want to be able to easily sign in.
2.As an existing user to the website, I would like to be able to delete my account
3.As an existing user to the website, i would like to be able to reset my password incase i forgot my previous password
4.As an existing user to the website, I would like to be able to add/read/edit and delete my blogposts.
5.As an existing user to the website,I would like to see the blogs by other people to decide which blog I would like to read.
6.As an existing user to the website, I would like to easily add new blogs.
7.As an existing user to the website, I would like to be able to upload a profile photo or change my profile photo. 
i.  If I don’t have a profile photo, I'd like to have a choice of placeholder (default avatar). 


## Scope 
Create a simple, intuitive, and responsive website that acts as a respository of blogs that users can browse and contribute to. 

The structure should adhere to convention and be simple and intuitive, ensuring the user always knows where they are, how they got there and how to get back to 
where they started.

The design should be simple, utilising the same colour palette, 

Any addition features or functionally are out of scope at this stage.

### User Goals:
- To find blogs from different authors and various categories.
- To be able to write , read, edit and delete blogs.
- To be part of a social blogging platform.

### Website Owner's goals:
 - To build on and expand the community for bloggers and readers around the world.
 - To create a safe and welcoming platform for users to share their passion for blogging.
 - To encourage bloggers to create their own blogs for other readers.
 - The ability for admin to edit and delete any inappropriate blogs to keep the platform safe and welcome for bloggers.


## Features
 
### Existing Features
- User Registration: allows new users to create an account so they can log in.
- User Log-in: allows existing users to log in using their username or email and password. Passwords are hashed for security reasons. Log-in is required to read , post your own blogs and give feedback. 
- User Profiles: allow users to tell others about themselves, provide a username, and users can see blogs created by themselves of their profiles 
- A user must be logged in to edit their own profile. A user cannot edit someone else's profile. 
- A user must be logged in to view messages and interact with other members.
- Password reset page- allows users to reset their password incase they had forgotten it.
- Expore: This allows both non registered and registered users to explore blogposts in the system that all the users have written.
- Search: allows a registed bloggers  to search for blogposts by simple words and more complex phrases
- Logout : allows a user to securely logout of the page.


### admin
- Admin role - The admin can Create ,Read ,Update and Delete blog categories.
- Admin may also delete blogs written by users that is considered inappropriate. 

### Features Left to Implement
- Allow users to upload their own cover image for a blog.
- Allow bloggers to rate other people's blogposts.
- Allow bloggers to search for blogposts based on other users' ratings.
- Allow admins to block/suspend users when necessary.
- follower feature
- comments feature
- upload profile pic
- incoporate a blog editor in the write new blog page.
- implement a better editor in the write a blog page to ensure proper paragraghing/ design and possibly add symbols and image
***

## Site implemented Features
##### Every page on this site also incorporates the following features:
- A logo in the top left hand corner, that not only forms part of the branding and design of the site but also as is consistent with a user's expectations, clicking the logo will return the user to the home page of the site.

- A responsive, collapsible navigation bar, allowing users to easily navigate the site on any device.
## Pages
 ### All users

#### Home
The home page introduced users to the site and with a call to action button to direct thm to register. users may also contact the site owner incase of any unforeseen issues.

#### Explore
  Here the both unregisstered and registered users may view and read blogs created by registered logged in users.
  The user can also search for a blog based on  single words or text phrases.

#### Register
The registration page allows a user to register an account. To register a user is required provide a username, email and password. Validation has been added to form. The Registration page also provides a link to the Log In page if a user has already registered and simply needs to log in, once a user is registered , he or she is redirected to the log in page.

#### Log In
  The Log in page allows registered user to log in to their account in order to view their own blogss, add a new blog, edit or delete one of their own blogs. The Log In page also provides a link to the Registration page if a user hasn't yet registered.

#### Write a new blog
  This page displays a form to the user to enable them to create a new blog. The user first selects a category from a dropdown list, then enter the title of their blog, content,publish_date ,read_time, created_by and hashtags
  the content/text area allows up to 2000 words and is expandable. The user then clicks submit and their blog is saved in MongoDB and visible on the site.
  This page is not accessible to users that are not logged in.

#### Edit Blog
    This page displays a form to the user to enable them to edit their blogs. The same form that is used to add blogs is shown again and is prefilled with the original information. The user can then edit their blog and click the edit button to update their blog, there is also is the option to click cancel if they have changed their mind and no longer want to make any edits.
    This page is specific to the blog that has been seleted to edit and is only available to the creater of the blog when they are logged in.
#### Admin Only
  ##### Categories
  This is an admin only area and allows an admin to create, edit and delete categories on the front end. This page displays a list of categories available to users, the categories have an edit and delete icons to allow an admin to either make edits to a category or to delete one. The page also has an 'Add Category' button to allow an admin to create a new category.


## Database Design
  All user generated content is stored in mongo db. There are three collections for blogit db.
  1. users
  2. categories 
  3. blogs

## Technologies
#### Languages & Frameworks 
* HTML5 - Mark-up language using semantic structure.
* CCS3 - Cascading style sheet used to style.
* JavaScript - Programming language.  
* Python - Programming language
* [Flask](#flask) - Framework + Extensions
* [Materialize](https://materializecss.com/) - CSS Framework for structure, buttons, and some styling
* [jQuery](https://jquery.com/) - Materialize initialising
* [Favicon](https://favicon.io/) - was used for creating the favicon
* Gitpod.io - for writing the code. Using the command line for committing and pushing to Git Hub
* GitHub - hosting repositories
* GIT - Pushing code to repositories

#### Front End
* [Google fonts](https://fonts.google.com/)  - for the font
* [Font Awesome](https://fontawesome.com/) - for icons used

#### Backend 
* [MongoDB](https://www.mongodb.com/)
* [Heroku](https://dashboard.heroku.com/)

#### Helpers
* [Beautifier](https://beautifier.io/) - for helping to keep code tidy 
* [Random Key Gen](https://randomkeygen.com/) - to generate a random secret key
* [Power Mapper](https://www.powermapper.com/) to check for browser compatibility
* [Temp Mail](https://temp-mail.org/en/)

#### Planning
[wireframes](https://lucidchart/app/dashboard/) - for planning of site flow, creating wire frames and general mind mapping


### Flask
The application was built using the [Flask](https://flask.palletsprojects.com/en/1.1.x/) Framework which is reliant on the [Jinja](https://www.palletsprojects.com/p/jinja/) templating language. The application was written in python. 

I used the following Extensions:
* [Flask Mail](https://pythonhosted.org/Flask-Mail/) - For emailing users
* [Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/) - For interacting with the MongoDB database
* [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/utils/) - For providing security’s, password_hash, check_password_hash

# Testing 
I tested the site in the following ways:
- I used the inspector tool to test the site in all the screen sizes and devices available in the Chrome developer tool. In addition to this I also tested it on live devices, including but not limited to iPhone, iPad, MacBook Pro, MotoG7.

- I also viewed my site in multiple browsers including, Chrome, Firefox and Safari in terms of design, responsiveness and functionality

#### Testing Tools
* [HTML Validator](https://validator.w3.org/) - checking the validity of code
* [CSS Validator](https://validator.w3.org/) - checking the validity of code
* [JSHint](https://jshint.com/)- Testing and checking JS.  - checking for errors in code
* [Pep8 Online](http://pep8online.com/) - Testing and checking PEP8 compliance 
* [Am I Responsive](http://ami.responsivedesign.is/#) - checking whether the site is responsive. 
* DEV Tools - Lighthouse

#### Validation reports
  - All links were tested to ensure there were no broken links and that all links to external sites open in a new tab.
  - In addition to testing with the inspector tool, real devices and validation tools, I also work through a series of test cases, to ensure that the site met the users stories and that any functionality that was added worked as intended.

### User Story Test Cases

#### New Visitors

1.  As a new visitor to the website, I want to understand the purpose of the site and how to interact with it.
- The home page of the site features a title and an introduction with an explanation of the purpose of the site and how to interact with it.
2. As a new visitor to the website, I want to find blogs easily from fellow blogggers without the need to register.
- There is no requirement to register to view blogs. The blogss are the main feature of the site and are visible from the explore page for all visitors to view.
4. As a new visitor to the website, I want to be able to register easily.
- The nagvigation is clear and has a item named 'Register', when a user clicks on this nav item they are brought to a simple form, with clearly labelled fields, placehold text and a clearly marked 'Register' button.

#### Logged In Visitors

1. As a logged in visitor to the website, I want to be able to easily add a blog..
- When a user logs into the site there are now options available to them in the navigation bar. When a users click 'write a blog' in the navigation bar, they are taken to the add_blog page. This page displays a form to the user to enable them to create a blog, The user first selects a category from a dropdown list, then enter the title,content,date,created_by, read_time and tags, and finally selected a . The user then clicks submit and their blog is saved in MongoDB and visible in the site.
2. As a logged in visitor to the website, I want to be able to easily edit my blogs.
- When a user logs into the site there are taken to their blogs, from there they can easily view, or select to edit or delete their blogs. If they click on the edit button within a blog listings they are taken to a page that consists of a form that is prepopulated with the orginal blog data. The user can then then edit their blog and click the edit button to update the blog , there is also the option to click cancel if they have changed their mind and no longer want to make any edits.
3. As a logged in visitor to the website, I want to be able to easily delete my blogs.
- When a user logs into the site there are taken to their blogs, from there they can easily view, or select to edit or delete their blogs. If they click on the delete button within a blog listings a pop up modal appears asking the user to verify that they want to delete their blog. If the users click the delete button on the modal, their blog is delete from the database and no longer appears in the site.
4. As a logged in visitor to the website, I want to be given visual confirmation when I edit or delete my blog that the update has been successful.
When a user is logged in and and adds, edits or deletes a blog, a message is flashed to confirm that the action has been carried out successfully.

#### Admin

1. As an admin, I want to be able to edit or delete any blogs to remove any inappropriate content.
When an admin is logged in, the edit and delete buttons are available to them on all blogs allowing then to edit or delete any inappropriate blogs- an orange delete button is present to show its a blog not written by admin.
2. As an admin, I want to be able to easily add, edit or delete categories within in the site rather than having to access MongoDB.
3. When an admin is logged in a new nav item is added called Categories. Clicking on this page allows an admin to view exisiting catgories, as well as edit or delete them. Additionally there is an add category button allowing then to add a new category on the front end.

#### Functionality Test Cases
#### Navigation:
1. While logged out, make sure you can see all the nav links for logged out and unregistered users:
   - home
   - explore 
   - sign in
   - register

#### Home:
2. While se logged out make sure that you can see welcome page that are on the home page, and that it includes the following:
- nav-links
- 2 background parallax images
- 3 column information/how to get started
- 1 CTA get started button
- contact us btn
- footer with quick links info , logo and copyright.


#### Explore:  
3. While logged out make sure that you can see all recommendations that are on the home page, and that each recommendations included the follow:
- Category name_
- title
- content
- tags
- Created by
- published date
 
 #### login
4. While logged in, make sure  you can see all blogs and that any blogs that was created by you, now has the edit and delete button on them.
- while logged in , make sure you can see blogs written by you on your profile page.

5. While logged in as an admin, make sure you can view all blogs  and blog categories and that all categories blogs now have the edit and delete button. so the admin may delete inappropriate blogs created by users  but may not  edit blogs  created by other users.
- admin can delete and edit blogs created by him /her
- admin can also create edit and delete  blog categories

### Home: Search funtionality

Type a word into the search box that you know there isn't match for in the DB, ensure that the flash messaging saying that "Sorry ,No results were found ".
Click the reset button and ensure all blogs are visble again.
blogs that match that criteria are visible.
Home: Filter functionality

Click on the word filter above the blogs and ensure the filter option buttons are visible.
Click on each button in turn and ensure that only recommendations that match that filter are visble.
Ensure there is one filter option that has no corresponding entries in the DB and then click on the option, ensure the flash messagin saying "Sorry ,No results were found".

### Registration:

1. Firstly complete the fields, click submit and ensure that the data is saved to the DB.
2. Attempt to submit the form with empty fields and ensure that valitation errors are displayed.
3. Attempt to submit the form without a correctly formatted email address and ensure validation error is displayed.
4. Log in with valid data and ensure flash message is show to confirm that the data has been submitted.
5. Log in with valid data and enusre you are taken to the  profile page.
6. Attempt to register with a username that you know already exists and ensure the error message is shown and you are redirected back to the register form.
7. Attempt to register with an email that you know already exists and ensure the error message is shown and you are redirected back to the register form.
8. Click on the 'Log In' link at the bottom of the registration form and ensure you are taken to the Log In screen.
9. While logged out ensure that you can only see 'Home','Explore 'Log In', and 'Register' in the navigation bar.

### Log In:

1. Log in with valid credentials and ensure you are logged in and directed to your profile page and you can now see 'profile', 'write a blog' and 'Log Out' in the navigation.
2. Attempt to log in with invalid credentials and ensure that an error message is displayed on screen and you are redirected to the Log In screen.
3. Click on the 'Register here' link at the bottom of the form and ensure you are taken to the Registration Screen.

### Log Out:

1. While logged in, click on the 'Log Out' item in the navigation bar and ensure that you are logged out, that you see the success confirmation message and that you can now only see 'Home', 'Log In', and 'Register' in the navigation bar.
### Profile:

While logged in, navigate to the explore page and ensure you can see all the blogs that you have added.
While on the profile page ensure that a greeting and your username are visible in your profile.
While on the explore page click on the edit button and ensure that the Edit blog page opens.
While on the explore page click on the delete button and ensure that a pop up verification modal appears.

### write a blog:

1. While logged in, navigate to the write a blog page and ensure the form loads and all fields are visible
2. While on the write a blog page ensure that all the categories are visible in the category drop down.
3. While on the Write a blog page ensure that all the levels are visible in the category drop down.
4. While on the write a blog page try to submit the form with fields left blank, ensure that custom valitation message is shown. Do this with each field in turn.
5. While on the write a blog page  check the textarea/ content feield to see the data length - only upto 2000 words allowed.
6. While on the write a blog page try to submit the form with blank spaces entered into the fields and ensure validation messages are shown.
7. While on the write ablog page complete all fields and submit the form, ensure the new entry is saved in the DB and is visible in the recommendations page.

### Edit blog:

1. While logged in, navigate to the Explore,select blogs written by you and click on edit button, ensure the form loads and all fields are visible and pre populated with the data for that blog.
2. While on the Edit blog form ensure that all the categories are visible in the category drop down.
3. While on the Edit blog form try to submit the form with fields left blank, ensure that custom valitation message is shown. Do this with each field in turn.
4. While on the Edit blog form try to submit the form with blank spaces entered into the fields and ensure validation messages are shown.
5. While on the Edit blog form make an edit to the blog and click the edit button, ensure the new edited version is saved in the DB and the edited version is visible in the explore page.
6. While on the Edit blog form don't make any changes and click the cancel button, ensure you are taken back to the explore page.
7. Delete blog: Carry out the tests below from the explore page
- Click the delete button within a blog, ensure that a delete verification modal appears.
When the modal has appeared, click the cancel button and ensure the modal closes and theblog is still visible on the page.
- Click  this time click the delete button. Ensure the blog is deleted and the confrimation flash message is visible. Take care to ensure that the correct blog has been deleted i.e. the one in which you click the delete button.

### Category & Add Category Pages (Admin Only):

1. While logged in and admin navigate to the Categories page and ensure all existing categories are visible with the option to edit or delete.
2. While on the Categories page click on the Add Category button and ensure the form opens.
3. While on the Add Categories page try to submit the form with fields left blank, ensure that custom valitation message is shown. Do this with each field in turn.
4. While on the Add Categories page try to submit the form with fields left blank, ensure that custom valitation message is shown. Do this with each field in turn.
5. While on the Add Categories page try to submit the form with blank spaces entered into the fields and ensure validation messages are shown.
6. While on the Add Categories page complete all fields and submit the form, ensure the new entry is saved in the DB and is visible in the categories page.

### Edit Category (Admin Only):

1. While logged in and admin navigate to the Categories page and click the edit button on one of the categories and form loads and all fields are visible and pre populated with the data for that category.
2. While on the Edit Categories page try to submit the form with fields left blank, ensure that custom valitation message is shown. Do this with both fields.
3. While on the Edit Categories page try to submit the form with blank spaces entered into the fields and ensure validation messages are shown.
4. While on the Edit Categories page make an edit to the blog and click the edit button, ensure the new edited version is saved in the DB and the edited version is visible in the categories page.
5. While on the Edit Categories page don't make any changes and click the cancel button, ensure you are taken back to the categories page.

### Delete Category (Admin Only):

1. Click the delete button within a category, ensure that a delete verification modal appears.
When the modal has appeared, click the cancel button and ensure the modal closes and the category is still visible on the page.
2. Click the delete button again, this time click the delete button. Ensure the category is deleted and the confrimation flash message is visible. Take care to ensure that the correct category has been deleted i.e. the one in which you click the delete button.
***

# Lighthouse testing
## Accessibility
In addition to all the above testing I also checked my site with accessibility tools in the inspector.
- scored 91%

## SEO 
- scored 100%

## Best practices
 - scored 

## performances
 -  😢 

## Bugs
          

#### Technology Configuration

#### MongoDB 

[MongoDB](https://www.mongodb.com/) was used as the database to store the users details to set up MongoDB follow the steps below

* Sign up to MongoDB
* Create a new shared Cluster
* Select a Cloud provider and region
* For free use  m0 cluster tier
* Give your cluster a name
* Go to collections and add a database
* Go to database access and add a username and password

Connecting - via application
* Go back to the cluster overview
* Click the CONNECT button.
* Select 'connect your application'
* Select your language/ driver (I used Python 3.6 or later)
* Copy the connection string and change the details. 
* Set the cluster name, collection name, URI connection string and password as environmental - see [Configuration](#Configeration) to set up your application configurations
***


## Deployment 

### Configuration 
Beneath your imports you will need to configure your app.py file.  You will need to import your local env.py for local environments.  For [configuration for Heroku](#deploying). 

Configure as follows:

        if os.path.exists('env.py'):
            import env


        app = Flask(__name__)

        app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
        app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
        app.secret_key = os.environ.get('SECRET_KEY')
    

        mongo = PyMongo(app)
        mail = Mail(app)

To start your application, you will need to user the following at the bottom of your app.py file. You will need to ensure that debug=False prior to deployment.

        if __name__ == '__main__':
            app.run(host=os.environ.get('IP'),
                    port=int(os.environ.get('PORT')),
                    debug=False)

You will need to add a Procfile and ensure your requirements.txt are up to date. 
In your root folder in the terminal type - touch Procfile -  this will create a Procfile
Add the following with the following 
    echo web: python app.py

To install the requirements.txt use the following command in the terminal command line
    pip3 install -r requirements.txt



#### Local Environment
Create env.py file in the same file system.  In your route folder type - touch env.py - to create the file. 
Your virtual configurations should look similar to this. You will need to create a SECRET_KEY and input the IP and PORT settings. I used [Random Key Gen](https://randomkeygen.com/).

        import os

        # App config
        os.environ.setdefault("IP", "0.0.0.0")
        os.environ.setdefault("PORT", "5000")
        os.environ.setdefault("SECRET_KEY", "<Your secret key>")

        # MongoDB config
        os.environ.setdefault(
            "MONGO_URI", "mongodb+srv://<user>:<password>@<project>.af8bz.mongodb.net/<database>?retryWrites=true&w=majority")
        os.environ.setdefault("MONGO_DBNAME", "<database>")



### Adding and Committing files

To add files to the repository, take the following steps

In the command line type -
        git add .  
        git commit -m "This is being committed"
        git push

To add all new files or modified file use " ."  - To add a single file, use the pathway to the file eg .index.html  or assets/css/style.css
When committing make sure your comments are clear about what changes have been made. 
Pushing will send your work to the repository


### Deploying 
Requirements for deploying:
* MongoDB Account
* Heroku Account
* Email account

Deploying to [Heroku](https://dashboard.heroku.com/)

* You will need to sign up to [Heroku](https://dashboard.heroku.com/)
* Once logged in click the create new app button
* Select the region closest to you and give the APP a name
* Set your deployment method to 'GitHub'
* Connect to GitHub and login
* Search for the repository you wish to deploy from
* You will need to head to settings and click 'Config Vars'
    * You will now need to set up your Configuration Vars the same way as you did for your env.py
![Config Vars](docs/images/config.png)    
* Make sure you have set up your Procfile and you have updated the requirements.txt prior to deploying    
* Click the deploy tab and go to manual deploy
* Select the branch you wish to deploy and deploy the application
* Once it is deployed you will be able to view the app
* You can set it to automatically deploy every time you push to the repository by enabling the Automatic deploys


### Forking

Forking the GitHub Repository

By forking the GitHub Repository, you can make a copy of the original repository in your own GitHub account.  This means we can view or make changes without making the changes affecting the original.

* Log into GitHub and locate the GitHub Repository.
* At the top of the Repository there is a "Fork" button about the "Settings" button on the menu.
* You should now have a new copy of the original repository in your own GitHub account.
* You will need to install the requirements.txt using the following command the command line
        pip3 install -r requirements.txt
* You will need to set up your local environments and key value pairs for deployment

### Cloning 

Making a Local Clone

* Log into your GitHub then find the gitpod repository
* Under the repository name there is a button that says, "Clone or download". Click on this button.
* If cloning with HTTPS "Clone with HTTPS", copy this link.
* Open Gitbash
* Change the current working directory to the location where you want the cloned directory to be.
* Type git clone, and then paste the URL you copied earlier.

        $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
        Press - Enter- Your local clone will be created.
        $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
                > Cloning into `CI-Clone`...
                > remote: Counting objects: 10, done.
                > remote: Compressing objects: 100% (8/8), done.
                > remove: Total 10 (delta 1), reused 10 (delta 1)
                > Unpacking objects: 100% (10/10), done.
[Click Here](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository) for more info on cloning. 

You will need to install the requirements.txt using the following command the command line
        pip3 install -r requirements.txt
* You will need to set up your local environments and key value pairs for deployment and running the application in your local environment. 


## Deployment

This project is hosted on [Heroku](heroku.com). It's been deployed using the following steps:
1. Sign up (new user) or sign in to Heroku account. _I already had an account from previous projects, so only needed to sign in._
1. Click the button at the top right that says "New", select "Create new app" in the dropdown.
1. Choose an app name. __Caution! This must be unique!__
1. Select your region. _In my case, this is Europe._ 
1. You'll be redirected to the Deploy tab of the new app.
1. Go to Deployment method. Select your prefered deployment method. _As my code was already on Github, I chose the "Connect to Github" option. The following steps will be specific to this option._
1. Sign in to your Github account to allow Heroku access to repositories.
1. Search for your repo name. If you can't remember the specific spelling of the name, leave the input field blank and click "Search" to get a list of all your repos.
1. When you've found your repo in the list, click the "Connect" button.
1. You now have the choice to enable automatic deploys or deploy manually. 
1. Your project will need to contain the following in order for Heroku to deploy it:
    - a Procfile: this specifies the commands that are executed by the app on startup. You can use a Procfile to declare a variety of process types, including:
        - Your app’s web server
        - Multiple types of worker processes
        - A singleton process, such as a clock
        - Tasks to run before a new release is deployed.

        _In the case of this project, the Procfile contains only a single line:_
        ```
        echo web: python app.py
        ```
    - a requirements.txt file. This tells Heroku which dependencies need to be installed in order for the project to run. It's created by using the command `pip install` + the name of any dependencies you have (for example, Flask needs to be installed for this project) in the terminal of your prefered editor, followed by the command `pip freeze > requirements.txt` which will write the installed dependencies to a text file which Heroku then installs using `pip install requirements.txt`. 
1. Go to settings in the Heroku tab. Click "Reveal Config Vars". Add the relevant environment variables you've used in your project to the Config Vars so Heroku can access them. Specifically, for this particular project, that means the following Config Vars were added: 
    - DEBUG (set to False to turn off Debug mode in the deployed version. Locally, in development, this variable was set to True.)
    - IP
    - MONGO_DBNAME
    - MONGO_URI
    - PORT
    - SECRET_KEY
1. Check the activity tab. The two most recent items in the list should read "Deployed" and "Build Succeeded" in their status. 
1. Click "Open App" in the top right side if this is the case, this will take you to the live site of the [Blog It]().

### To run this project locally:
1. Clone the [Github repo]() using the green "Clone or download" button. Several options are available here.
1. Open the project in your prefered editor.
1. Create a virtual environment using the command `python -m venv envname`, replacing "envname" with the name you want to give this environment. (More information on virtual environments: https://docs.python.org/3/library/venv.html)
1. Open the virtual environment:
    - Windows Cmd Shell: `<envname>\Scripts\Activate`
    - Posix/Linux bash Shell:
    `$ source <envname>/bin/activate`
1. Install the dependencies using the command `pip install -r requirements.txt`
1. Set up environment variables. There are different ways to do this  depending on your system and/or editor. In my editor of choice, VS Code running on Windows, you can do this in the .vscode directory that's generated for every project. This will contain a settings.json file. Add the following to the json dictionary: 
    ``` 
    "terminal.integrated.env.windows": 
    {
        "MONGO_DBNAME": "theDatabaseName",
        "MONGO_URI": "theDatabaseURL",
        "SECRET_KEY": "YourSecretKeyHere"
    },
    ``` 
1. Run the project in your terminal using the command `python app.py` (like pip, for Unix-based systems you may need to use `python3`).

# Credits

### Content
#### The content of the site was written by the team and inspired by the idea of creating a  social blogging site that has room for improvement as i improve on our skills and make it fully functional with time

### Code
- We borrowed code for audio recording from [codepen](https://codepen.io/jeremyagottfried/pen/bMqyNZ)

### Media
- Image for the [favicon](https://stock.adobe.com/ca/images/hands-in-heart-shape-on-white-transparent-background-painted-rainbow-color-symbol-of-lgbt-glbt-lgbtq-pride-flag-or-lesbian-gay-bisexual-transgender-queer-questioning-vector-illustration/197908448).


### Acknowledgements


