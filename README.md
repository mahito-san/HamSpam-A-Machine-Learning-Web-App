# HamSpam: A Machine Learning Web Application

#Summary
This is a Machine Learning based web app. This app detects a spam comment. For dataset we used `YouTube Spam Collection Dataset`, which consists of spam comments of five different music videos of different singer. We used `Bi-directional Long-Short-Term-Memory (LSTM)` model for the backend of this project and `Django` to built the html, the frontend of this project. 

To run this project: 
* Open the folder containing this project in VSCode. 
* Open a new terminal.
* Run these 3 commands:
* * `py manage.py makemigrations comment_app`
* * `py manage.py migrate`
* * `py manage.py runserver`
* Then you will see a link given in the terminal, `127.0.0.1:~~`. Click this link and it will open a tab in your browser, where you can input a sentence and it will show you the result whether it is a spam comment or a ham (Not Spam) comment.
