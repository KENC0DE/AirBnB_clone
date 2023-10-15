# AirBnB Clone

## Description

clone of AirBnB Website.

## Usage

### How Start it

    ./console.py

### display help

    (hbnb) help

    Documented commands (type help <topic>):
    ========================================
    EOF  all  count  create  destroy  help  quit  show  update

    (hbnb)

### exit the console

    (hbnb) quit
    $

### create a (User, State, Place, Amenity, Review)
    `$ create <name>`

    (hbnb) create User
    320098c5-ab99-4134-b205-5911dec9c9fa
    (hbnb)


### display a (User, State, Place, Amenity, Review)
>>> $ show <name> <id>

    (hbnb) show User 320098c5-ab99-4134-b205-5911dec9c9fa
    [User] (320098c5-ab99-4134-b205-5911dec9c9fa) {'id': '320098c5-ab99-4134-b205-5911dec9c9fa', 'created_at': datetime.datetime(2022, 10, 30, 14, 22, 59, 416038), 'updated_at': datetime.datetime(2022, 10, 30, 14, 22, 59, 416059)}
    (hbnb)

### delete a (User, State, Place, Amenity, Review)
>>> $ destroy <name> <id>

    (hbnb) destroy User 320098c5-ab99-4134-b205-5911dec9c9fa
    (hbnb)

### Display all the data
>>> $ all

    (hbnb) all
    ["[User] (320098c5-ab99-4134-b205-5911dec9c9fa) {'id': '320098c5-ab99-4134-b205-5911dec9c9fa', 'created_at': datetime.datetime(2022, 10, 30, 14, 22, 59, 416038), 'updated_at': datetime.datetime(2022, 10, 30, 14, 22, 59, 416059)}", "[State] (d7fb1ba3-5c46-4197-aca1-36094cf22ee9) {'id': 'd7fb1ba3-5c46-4197-aca1-36094cf22ee9', 'created_at': datetime.datetime(2022, 10, 30, 14, 23, 34, 516438), 'updated_at': datetime.datetime(2022, 10, 30, 14, 23, 34, 516491)}", "[City] (3e647f03-7954-48da-89fd-6504c68dfb09) {'id': '3e647f03-7954-48da-89fd-6504c68dfb09', 'created_at': datetime.datetime(2022, 10, 30, 14, 23, 54, 140492), 'updated_at': datetime.datetime(2022, 10, 30, 14, 23, 54, 140522)}", "[Amenity] (f81e070f-52b6-4a5d-b13b-6c6c33838b4b) {'id': 'f81e070f-52b6-4a5d-b13b-6c6c33838b4b', 'created_at': datetime.datetime(2022, 10, 30, 14, 24, 11, 584531), 'updated_at': datetime.datetime(2022, 10, 30, 14, 24, 11, 584564)}", "[Place] (25690873-52e4-4be3-8bcb-029249c91a32) {'id': '25690873-52e4-4be3-8bcb-029249c91a32', 'created_at': datetime.datetime(2022, 10, 30, 14, 24, 40, 116241), 'updated_at': datetime.datetime(2022, 10, 30, 14, 24, 40, 116287)}", "[Review] (e76e9aaa-9871-4db2-85dc-f5765cc85a71) {'id': 'e76e9aaa-9871-4db2-85dc-f5765cc85a71', 'created_at': datetime.datetime(2022, 10, 30, 14, 24, 49, 88134), 'updated_at': datetime.datetime(2022, 10, 30, 14, 24, 49, 88189)}"]
    (hbnb)

### update a (User, State, Place, Amenity, Review)
>>> $ update <name> <id> <variable> <value>

    (hbnb) update User 320098c5-ab99-4134-b205-5911dec9c9fa name School
    (hbnb)

### count number (User, State, Place, Amenity, Review)
>>> $ User.count()

    (hbnb) User.count()
    1
    (hbnb)
