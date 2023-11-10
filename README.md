# Django Project 
## Building a small website for a band

### Table of Contents
- [About the Project](#about-the-project)
- [Getting Started](getting-started)
  - [Using Dockerhub](using-dockerhub)
  - [Using Django](using-django)
- [Usage](usage)
- [Credits](credits)
<br  />
<br  />


### About the Project <br />
This program will assist you to build a small website (for example, a simple site for a fictional band, or political candidate) using Django.  The site has 3 pages and 1 database-driven component.
<br  />
<br  />

### Getting Started <br />
You may access the project either by using Dockerhub or Django.

#### Using Dockerhub
##### Prerequisites
- Docker, preferably desktop: 
https://www.docker.com/products/docker-desktop
- A free Docker Hub account:
https://hub.docker.com 

##### Installation
- Open your terminal and type the following command:

  ````docker pull hogwarts1/docker_django:django_docker ````
- Once the image is downloaded, run the following command:

  ```` docker run -t -p 8000:80/hogwarts1/docker_django:django_docker````
- Navigate to: http://localhost:8000 to start using the application.
<br  />


#### Using Django
##### Prerequisites
- Python, download the latest version of Python from the official website: https://www.python.org/downloads/
- pip, it is typically included with Python, but if not, you can install it by running the command: ````python -m ensurepip --default-pip ````

#### Installation
- The first thing to do is to clone the repository:

    ```git clone https://github.com/VanessaH85/capstone.git```

     ``` cd capstone```


- Install virtual environment: ```pip install virtualenv```
- Create a new virtual environment: 

  ```virtualenv <name_of_virtual_environment>```
- Activate the virtual environment: ```<name_of_virtual_environment>\Scripts\activate```

 

- Install Django: ```(env) pip install django```
- Verify that Django is installed correctly:
```(env) django-admin --version``` 

- Then install the dependencies:

  ```(env) pip install -r requirements.txt```

- Once pip has finished downloading the dependencies: 
  ```(env) cd project```
- Create datatables run commands: 

  ```python manage.py migrate```

  ```python manage.py makemigrations```

  ```python manage.py migrate```
- Run the server: 
  ```(env) python manage.py runserver```
   
- And navigate to http://127.0.0.1:8000
<br  />
<br  />

### Usage
- Home <br />
By clicking ````Home```` on the sample application website, you are taken to an introductory page of the website, set as the default or start-up page on a browser.

- About <br />
By clicking ```About``` on the sample application website, you are taken to a page on the website that tells your visitors who you are, what you do, and why they should care.

- Songs <br />
By clicking ```Songs``` on the sample application website, you are taken to a page that lists songs for the band.

- Login <br />
By clicking ```Login``` on the sample application website, you are taken to a page where the user will be prompted to login using username and password.
<br  />
<br  />

### Credit
- Vanessa Hlabahlaba @vanessah85

