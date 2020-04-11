# News Web App Project
This is a web application which allows logged in users to post and view articles. It currently houses a few test articles and text comments. It runs on a Django web framework, and has a user authentication and authorisation system set up.

## Testing
Tests have been implemented in the pages app, and they can be found in the respective pages/test.py file. This tests the Home page and SignUp page

## Authors
Based on a project from 'Django for Beginners' by William S. Vincent

##  Deployment
This web app is nearly ready to be deployed on a live website, however I am yet to setup the password reset email functionality with a service such as SendGrid. Currently, a password reset system is implemented, but it sends the automated email to the user's command line, rather than to the user's email inbox.

## Built with
* [Python 3.8](https://www.python.org/)
* [Django 3.0](https://www.djangoproject.com/)
* [Bootstrap 4.0](https://getbootstrap.com/) via [MaxCDN](https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css)
