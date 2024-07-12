# socialNetworkWebApp 


This social networking website project (end term coursework) is created for my Advanced Web Development module. 

This app allowed users to create, update profile, add or remove friends, create posts, chat in real time with friends.

<br/>


This project mainly uses:<br/>

Django 


<br/>

## Initialising project

Initialise with <i><ins>pip install -r requirements.txt</ins></i><br/>

Run <i><ins>python manage.py runserver</ins></i> to run the website

<br/>
<br/>

### The application contains the functionality requires
<br/>
a) Users can create accounts <br/>
b) Users can log in and log out <br/>
c) Users can search for other users <br/>
d) Users can add other users as friends <br/>
e) Users can chat in real time with friends <br/>
f) Users can add status updates to their home page <br/>
g) Users can add media (such as images to their account and these are
accessible via their home page <br/>
h) correct use of models and migrations <br/>
i) correct use of form, validators and serialization <br/>
j) correct use of django-rest-framework <br/>
k) correct use of URL routing <br/>
m) An appropriate method for storing and displaying media files is given <br/>
Implements and appropriate database model to model accounts, the stored data
and the relationships between accounts

<br/>

<br/>

## Functionality: User Registration

<br/>

Implemented a user registration form using Django's UserCreationForm, allowing users to create accounts with usernames, passwords, and email addresses. Leverage Django's built-in authentication system for handling user account creation and management.

<br/>

#### Define user registration form:

<br/>

![registrationform](https://github.com/chunyicy/socialNetworkWebApp/assets/116086176/bf8b5861-1a2e-4e64-b9ba-e70f6b1477b0)

<br/>

#### Define a view file to handle user registration logic and render the registration form:

<br/>

![registerview](https://github.com/chunyicy/socialNetworkWebApp/assets/116086176/43940315-e9d0-4cbd-a75f-9b475251f21b)

<br/>

#### Create template files to display the registration form:

<br/>

![registertemplate](https://github.com/chunyicy/socialNetworkWebApp/assets/116086176/cb8bb471-4c9a-4cb9-b01e-b2cba57d287e)

![registertemplate2](https://github.com/chunyicy/socialNetworkWebApp/assets/116086176/23d99732-40d8-4839-a6db-0559ec64c28b)

<br/>

#### Add a URL pattern to map the registration view:

![registerurl](https://github.com/chunyicy/socialNetworkWebApp/assets/116086176/30f2194d-a052-4c9f-b4ee-bce17927d4f5)

<br/>

#### Registration page:

<br/>

![registerpage](https://github.com/chunyicy/socialNetworkWebApp/assets/116086176/ef05c393-7760-47bc-ba1a-6d619bcee541)

<br/>

A success message is displayed upon successful account creation and then redirects the user to the login page.

<br/>

![registermessage](https://github.com/chunyicy/socialNetworkWebApp/assets/116086176/29c8d583-3854-44ae-bd3f-5ff335ac2513)

<br/>
<br/>

## Functionality: User Log in and Log out

<br/>

#### Update URLs, include Django's authentication views:

<br/>

LoginView: Uses Django's built-in login view.

LogoutView: uses Django's built-in logout view.

![loginlogouturl](https://github.com/chunyicy/socialNetworkWebApp/assets/116086176/a1f4ff85-a176-4d78-8d7a-19e589724dd1)


<br/>

#### Create a Login Template:

<br/>

![logintemplate](https://github.com/chunyicy/socialNetworkWebApp/assets/116086176/58fb1976-9d1d-4d16-978e-5bddfc94e59a)

<br/>

#### Protect Views with 'login_required':

<br/>

'@login_required' : To restrict access to views only to authenticated users, ensures that only logged-in users can access the profile view.


<br/>

![protecturl_loginrequired](https://github.com/chunyicy/socialNetworkWebApp/assets/116086176/4b45ab8e-d22e-440e-a174-cc5ec7d7e639)

<br/>

#### Login page:

<br/>

![loginpage](https://github.com/chunyicy/socialNetworkWebApp/assets/116086176/1d01319a-d4c8-401b-b3ad-54b1b56b41a2)

<br/>

![loginhome](https://github.com/chunyicy/socialNetworkWebApp/assets/116086176/6cf482d5-67d4-45b6-8f09-d374d8dd1d9e)


<br/>
<br/>

#### Create logout link and logout template file :

<br/>

Checks if the user is authenticated (user.is_authenticated) and displays a logout link ({% url 'logout' %}) if they are logged in.

<br/>

![checkifauthenticated](https://github.com/chunyicy/socialNetworkWebApp/assets/116086176/5efd4412-f347-4d8a-af31-cc4c3a2a3cb9)

<br/>

Displays a short message to confirm the user that they have been logged out and a login link ({% url 'login' %} if user successfully logout.

<br/>

![logouttemplate](https://github.com/chunyicy/socialNetworkWebApp/assets/116086176/39e76832-d94c-43de-a2a9-b3db1a7793f0)

<br/>

#### Logout page:

<br/>

![logoutpage](https://github.com/chunyicy/socialNetworkWebApp/assets/116086176/d82abfd1-65d5-4972-ad03-ba7a2d3aacf1)

<br/>
<br/>

## Functionality: Update Profile

<br/>

#### Define Profile Model:

Create Profile model to store the user details and the profile picture.

<br/>

![updateprofilemodel](https://github.com/user-attachments/assets/ef213da5-d709-4339-8c02-78c9c2b98b4a)

<br/>

#### Create UserUpdateForm and ProfileUpdateForm:

To collect and update profile information.

<br/>

![profileupdateform](https://github.com/user-attachments/assets/9cb8876f-72ba-478e-9895-fa2d31a9709c)

<br/>

#### Create a View for Profile Update:

Handles updating the user profile. This view will render the form, process form submission, and update the profile.

<br/>

![updateprofileview](https://github.com/user-attachments/assets/c8773b47-fe9a-4c3a-b5cb-b895a930beec)

<br/>

#### Create a Template for Updating Profile

Create an HTML template to display the form:

![updateprofiletemplate](https://github.com/user-attachments/assets/78d7c385-beae-4cd3-9ddd-6d6cb91a2d6f)

<br/>

#### Update URLs:

Create a url path for the update profile page so that the user can update their profile.

<br/>

![image](https://github.com/user-attachments/assets/f71b09a2-28c1-4518-950a-ea4d59459116)

<br/>


#### Define a Signal Receiver:

Define a signal receiver function that listens for the post_save signal sent by the User model. This function will create a Profile instance whenever a new User instance is created.

<br/>

#### Update Profile Page:

<br/>
![updateprofilepage3](https://github.com/user-attachments/assets/7d87c1e9-5db9-469f-8eca-ca6236e0aa03)

<br/>

![updateprofilepage2](https://github.com/user-attachments/assets/8fedd461-5849-4cf6-895a-b354b50e7fb9)

<br/>

![updateprofilepage](https://github.com/user-attachments/assets/2bff4ba9-6c9c-459f-bd7b-e7e8a42acc56)

<br/>

![updateprofilesignalreceiver](https://github.com/user-attachments/assets/ef15933f-5c9e-41c3-b57c-d12afe426e95)

<br/>

<br/>

## Functionality: Create Post:

<br/>

- Define Post Model: This model will include fields such as content, image, date published, author (linked to the User model).
- Create a Form for Post Creation:  Allows users to input data for creating a post.
- Create Views to Handle Post Creation: Define views to render the form and process form submissions.
- Create a Template for Post Creation: Create a template to display the form for creating a post.
- Set Up URLs: Configure URL patterns (urls.py) to map the view for creating a post.

<br/>

![createpost2](https://github.com/user-attachments/assets/2ac2c00a-55b8-4795-8c77-a39ad8541cc3)

<br/>

![createpost1](https://github.com/user-attachments/assets/477cec8f-aa47-4edf-bd8d-bf452e5800c1)

<br/>

![createpost](https://github.com/user-attachments/assets/b0374bd5-4fc3-43d5-bbdf-b2683eaff811)

<br/>
<br/>

## Functionality: Search for a User

<br/>

#### Define Views to Handle User Search

Create views (views.py) to render the search form and process search queries.

<br/>

![searchview](https://github.com/user-attachments/assets/61d2ed4c-9917-4c9b-8b9e-2855d233ff16)

<br/>

#### Create Templates for User Search

Design templates for displaying search results.

<br/>

![searchtemplate](https://github.com/user-attachments/assets/2fee7a21-cdab-4b8c-82ff-3460d91fb691)

<br/>

#### Configure URLs

Set up URL patterns (urls.py) to map the views for user search.

<br/>

![searchurl](https://github.com/user-attachments/assets/159824b7-9313-4955-83e6-525c72e64064)

<br/>

![searchpage1](https://github.com/user-attachments/assets/b457e686-a7c5-4716-a72f-1a36aab89e75)

<br/>

![searchpage](https://github.com/user-attachments/assets/0bdf6bf3-0609-4711-babf-84ce8a0b1315)

<br/>
<br/>

## Functionality: Add a Friend or Remove a Friend

#### Create a Friendship Model:

Define a model to represent the friendship relationship between users. This model will use a many-to-many relationship with the User model.

![friendmodel](https://github.com/user-attachments/assets/4619cce3-b6f6-4728-884f-3ecbddf223d2)

<br/>

#### Define Views for Adding and Removing Friends

Create views (views.py) to handle adding and removing friends from the user's friend list.

<br/>

![addorremove](https://github.com/user-attachments/assets/b0e7d1db-79b6-49a2-bca4-c94287d44f68)

<br/>

#### Add/ Remove friend page:

<br/>
![friendlist](https://github.com/user-attachments/assets/edd10c26-b0c6-41e7-91ad-1fdf8ba16fc4)

<br/>

![addfriend](https://github.com/user-attachments/assets/c497bcfe-eeab-48a5-9dd8-4ed8af483d71)



<br/>

![removefriend](https://github.com/user-attachments/assets/ebabb8e0-0587-4acb-8b26-2a2320920ee4)


<br/>

<br/>

<br/>

## Functionality: Users can chat in Realtime with friends

<br/>

![chatRoom](https://user-images.githubusercontent.com/116086176/197456080-ca7e1c2c-76dc-49b3-9d0c-4d7647ce7d80.jpg)




![chat](https://user-images.githubusercontent.com/116086176/197456098-9046af49-9af8-4c35-838f-4d141b7e8b9f.jpg)
