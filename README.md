# TextGame
A Simple Text-Based game played through your phone's SMS service. There is nothing to download and nothing to Sign-Up for. All you do is text the registered phone number!
## Basics

  This main directory represents the Django Apps set-up on top of a LAMP server (Linux, Apache, MySQL, Python). The TextGame directory contains the main configuration files for the Django installation. This project utilizes the Twilio API as part of the Django back end to handle the SMS messages sent to the server from Twilio as GET requests. 

  To run the server, SSH in and navigate to TextGame Directory (the folder with the manage.py file) from the root folder and run the following command:
  
>python manage.py runserver [::]:[DESIRED PORT NUMBER]
