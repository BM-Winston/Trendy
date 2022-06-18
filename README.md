## Trendy

### 18/06/2022

## Author

[Winston Musasia]

# Description

This as a web application where a user gets information about things happenning around the neighbourhood.





## Live link


## User Story
The user should be able to:

* Sign in with the application to start using.
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.



* 
## Setup and Installation

##### Clone the repository
```bash
git@github.com/BM-Winston/Trendy.git
```
##### Install requirements 
```bash
cd Trendy pip install -r requirements.txt
```
### Install and activate virtual environment
```bash
python3 -m venv virtual - source virtual/bin/activate
```
 ##### Database  
  SetUp your database. Add user and password, host then make migrations. 
 ```bash 
python manage.py makemigrations trends
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```

##### Run the application  
 ```bash 
 python manage.py runserver 
``` 

##### Tests 
 ```bash 
 python manage.py test 
```

Open application at '127.0.0.1.8000' at your web browser



## Technologies Used

* Python
* Django
* Heroku
* HTML
* CSS

# Known Bugs

* No known bugs


## License


Authors Information

[musasiawinston@gmail.com]

Winston Musasia (c) 2022


[Go Back to the top](#Trendy)


