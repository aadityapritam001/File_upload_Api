# File_upload_Api
Simple API for file upload using Flask &amp; Mongodb

# database folder:
* In the database folder there is a python file having database configuration and operations of DB ( like - insert and retrieve)

# upload :
* It is a folder where all the files will store when uploaded 

# __init__.py:
* It is a simple python file where the app is getting initialized 

# models.py:
* This models.py act as a controller here, which is connected to main file and database. It helps in securing the data and make more secure and flow as model views controller (MVC) 

# main.py :
* It is the main file, which needs to be run using the command ( python main.py or python3 main.py )
Once it is executed , for testing we have to use the postman and on the postman, we need to select the file or multiple files and in place of key we have to write "files" as key and selecting files as value.
After execution, it will return the path or you can change it to files id as well.

e.g ![alt text](https://user-images.githubusercontent.com/37104890/116814085-a05df400-ab74-11eb-8939-914258f930af.png)

