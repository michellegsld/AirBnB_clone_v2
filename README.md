<h1 align="center">AirBnB Clone V2 - MySQL</h2>

<p align="center"><img src="/web_static/images/HBnb.png"/></p>

## Description

> ### HBnB is a clone of AirBnB's command interpreter. This project focuses on the backend.
>> First step, is to write a parent class to take care of the initialization, serialization and deserialization of future instances.
>> Second step, to create a flow of serialization/deserialization:
`Instance<->Dictionary<->JSON string,<->file`
>> Third step, to create all classes used for AirBnB that inherit from the parent class
>> Fourth step, to create the first abstracted storage engine of the project
>> Final step, to create all unittests to validate all classes and storage engine

### What is a command interpreter?

> A command interpreter is the part of the operating system that takes commands via the command line from the user and executes them. The Shell is an example of one.
>> To start the command interpreter, first clone the repo to your local machine, and run the console:
›   `./console`
>> Once running, the prompt will appear `(HBNB)`, and you can enter your command. With this command line interpreter, the user can create a new User, Place, State, or City, as well as retrieve an object from a file. The user may also update any of these attributes or destroy them.
## Project Scope

With HBnB, the user can create Users, Places, States, Cities, and Reviews, as well as update each class with attributes such as name, first_name, last_name, email, and password. Below is a table with all functionality of the console:

| Command | Description |
| ------------- | -------------------------------------------------- |
| create | creates a new instance of a class |
| show | shows instance of a specified class or all class instances |
| destroy | deletes an instance based on class name and id |
| all | prints all string representations of all instances |
| update | updates an instance of a class ie email attribute of a User |

## Available Classes and associated attributes

| Class | Attributes  |
| ------------- | -------------------------------------------------- |
| User | email, password, first_name, last_name  |
| State | name |
| City | state_id, name |
| Amenity | name |
| Place | city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, amenity_ids |
| Review | place_id, user_id, text |

## Examples of using the console in interactive mode:

```

$ ./console.py•
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) create
** class name missing **

(hbnb) create BaseModel
138486be-3e76-43c8-b4f0-59f8c4888e87

(hbnb) show
** class name missing **

(hbnb) create User
e16d4b4d-9320-408c-90f4-0752be7fa65d

(hbnb) all
{'BaseModel.e12c8168-bad8-4ac1-b685-f8bcc1a57bed': <models.base_model.BaseModel object at 0x7f6d0780c780>, 'BaseModel.14dd894f-da3b-4e40-84a0-03b558ff80f1': <models.base_model.BaseModel object at 0x7f6d0847e470>, 'User.e1839253-151c-4bdb-80ad-7781cfec0cac': <models.user.User object at 0x7f6d084a8208>, 'User.7f69c2a7-fd1c-40bf-a948-b30d186e26be': <models.user.User object at 0x7f6d0847e438>, 'User.e16d4b4d-9320-408c-90f4-0752be7fa65d': <models.user.User object at 0x7f6d0847e358>, 'BaseModel.138486be-3e76-43c8-b4f0-59f8c4888e87': <models.base_model.BaseModel object at 0x7f6d089976a0>}

(hbnb)

```

## Examples of using the console in non-interactive mode:

```

$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)

$ echo show | ./console.py
(hbnb) ** class name missing **
(hbnb)

$ echo all | ./console.py
(hbnb) {'BaseModel.14dd894f-da3b-4e40-84a0-03b558ff80f1': <models.base_model.BaseModel object at 0x7f49b4f29e80>, 'User.7f69c2a7-fd1c-40bf-a948-b30d186e26be': <models.user.User object at 0x7f49b42ba7b8>, 'User.e1839253-151c-4bdb-80ad-7781cfec0cac': <models.user.User object at 0x7f49b42efc18>, 'BaseModel.138486be-3e76-43c8-b4f0-59f8c4888e87': <models.base_model.BaseModel object at 0x7f49b42efb38>, 'User.e16d4b4d-9320-408c-90f4-0752be7fa65d': <models.user.User object at 0x7f49b42efb00>, 'BaseModel.e12c8168-bad8-4ac1-b685-f8bcc1a57bed': <models.base_model.BaseModel object at 0x7f49b42efd30>}
(hbnb)
$

```

#### Authors
| Name | Email | Project Component |
| -------------------------- | ------------------------- | ----------------------|
[Michelle Giraldo](https://github.com/michellegsld) | michelle.giraldo@holbertonschool.com | MySQL
[Kati Fredlund](https://github.com/KFredlund) | kati.fredlund@holbertonschool.com | MySQL
[Kevin Yook](https://github.com/yook00627) | kevin.yook@holbertonschool.com | [Console](https://github.com/yook00627/AirBnB_clone)
