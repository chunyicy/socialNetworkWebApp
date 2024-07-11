# socialNetworkWebApp 


This social networking website project (end term coursework) is created for my Advanced Web Development module. 

This app allowed users to create a profile, add friends, create posts, chat with friends etc 

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





![friendList](https://user-images.githubusercontent.com/116086176/197456002-4adbc2f9-7aa6-4a82-84de-9dbcca148bbf.jpg)



![search](https://user-images.githubusercontent.com/116086176/197456050-823098b0-a0b5-499f-ae66-7c03857f37bc.jpg)



![chatRoom](https://user-images.githubusercontent.com/116086176/197456080-ca7e1c2c-76dc-49b3-9d0c-4d7647ce7d80.jpg)




![chat](https://user-images.githubusercontent.com/116086176/197456098-9046af49-9af8-4c35-838f-4d141b7e8b9f.jpg)
