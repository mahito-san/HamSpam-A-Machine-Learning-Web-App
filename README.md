# HamSpam: A Machine Learning Web Application

# Summary
This is a machine learning-based web app that detects spam comments. We used the `YouTube Spam Collection Dataset for the dataset, which consists of spam comments on five music videos by various singers. We used the `Bi-directional Long-Short-Term-Memory (LSTM)` model for the backend of this project and `Django` to build the HTML, the frontend of this project. The paper related to this project can be found here: 

To run this project: 
* Open the folder containing this project in VSCode. 
* Open a new terminal.
* Run these 3 commands:
* * `py manage.py makemigrations comment_app`
* * `py manage.py migrate`
* * `py manage.py runserver`
* Then you will see a link given in the terminal, `127.0.0.1:~~`. Click this link and it will open a tab in your browser, where you can input a sentence and it will show you the result whether it is a spam comment or a ham (Not Spam) comment.
