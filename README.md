# todo_app-trello-
a trello backend clone. trello is a todo app : https://trello.com This simple backend API allows the client-side of the todo app to manage tasks.
The backend of the todo app provides a REST API for creating, updating, and deleting tasks. The following endpoints are available:
# POST api/user_API 
create a new user and save it in the database
Example request : 
POST api/user_API
{
    "username":"saidi abdelkader",
    "email":"abdo7dadygmail.com",
    "password":"abdelkader1234"
}

Example response : 

{
    "id": "63f8c32979a04e0da1b66707",
    "username": "saidi abdelkader",
    "email": "abdo7dady@gmail.com",
    "password": "abdelkader1234"
}

# GET api/empty_table/id_user
get all the tables created by a the user identified by the id in the path 

Example request :
GET api/empty_table/63f8c32979a04e0da1b66707

Example response : 
{
    "id": "63f89f194fd307052867a0c9",
    "todo": [
         "element1",
         "element2",
         "element3"
        ],
        "in_progress": [
            "in progress1",
            "in progress2"
        ],
        "done": [
            "done1",
            "done2"
        ],
        "table_name": "table name",
        "date": "2023-02-24T11:27:21.775000Z",
        "user": "63f8c32979a04e0da1b66707"
    }

# POST api/empty_table/id_user
create a empty table wit the name passed in json file 

Example request :  
POST api/empty_table/63f8c32979a04e0da1b66707
{"table_name" : "table name "}

Example response : 
empty table created succefully

# DELETE api/empty_table/id_table
delete the table indetified by the precedent id

Example request : 
DELETE api/empty_table/63f8c32979a04e0da1b66707

Example response :
{
    "id": "63f89f194fd307052867a0c9",
    "todo": [
         "element1",
         "element2",
         "element3"
        ],
        "in_progress": [
            "in progress1",
            "in progress2"
        ],
        "done": [
            "done1",
            "done2"
        ],
        "table_name": "table name",
        "date": "2023-02-24T11:27:21.775000Z",
        "user": "63f8c32979a04e0da1b66707"
    }
# POST api/todo_list/id_table.........api/InProgressList/id_table.........api/DoneList/id_table 
each endpoint create a new Element in each list in the table identified by her id in the path   1-todo list(list of tasks need to be finish)     2-in progres list(list of tasks in prgress)      3-done list(list of termintated tasks) 

Example request : 
api/todo_list/63f89f194fd307052867a0c9
{
"Elemen" : "a task"
}

Example response :
todo list added succefully
# GET api/todo_list/id_table.........api/InProgressList/id_table.........api/DoneList/id_table 
return the ( todo , in progress , done) lists in the specified table in the id 

Example request : 
api/todo_list/63f89f1e4fd307052867a0ca

Example response : 
["task1","task2","task3"]

# PUT api/todo_list/id_table.........api/InProgressList/id_table.........api/DoneList/id_table 
modify a list in the table specified in the path 

Example request : 
api/todo_list/63f89f1e4fd307052867a0ca 
{"todo": "element1","elements2"...}

api/DoneList/63f89f1e4fd307052867a0ca 
{"done": "element1","elements2"...}

api/InProgressList/63f89f1e4fd307052867a0ca 
{"in_progress": "element1","elements2"...}

Example response : 

{
    "id": "63f89f1e4fd307052867a0ca",
    "todo": [
        "element1",
        "element2"
    ],
    "in_progress": [],
    "done": [],
    "table_name": "new table",
    "date": "2023-02-24T11:27:26.217000Z",
    "user": "63f89e5c4fd307052867a0c8"
}

# GET STARTED 
to start using this APIs 
- in the folder of the project create a virtualenv
- download the packages in the requirements file (with the specified version)
- open mongodbcompass and connect to a localhost server ( or change the the server in the settings file in todo_mongo/settings.py)
- py manage.py runsrerver (in winodws)
- use the link : localhost:8000/endpoints in your project 
