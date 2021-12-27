<p align="center">
  <a href="https://github.com/udz-codes/Pholio" target="_blank">
    <img src="pholio/static/pholio/src/Pholio.svg" alt="Pholio" width="200" >
  </a>

  <h3 align="center">Setup a personal portfolio webpage without writing any code</h3>

  <p align="center">
    <a href="https://pholio1.herokuapp.com" target="_blank"><strong>Visit website »</strong></a>&nbsp&nbsp
    <a href="https://youtu.be/Vz7sHj9eIv0"><strong>Youtube video »</strong></a>
  </p>
</p>

___

<h1 align="center">About The Project</h1>
<p align="center">A portfolio website but not like a usual portfolio that is created for a single user. Here, users can register for an account and set up a personal portfolio webpage by just entering their information, without writing any code.</p>
<p align="center">Users are provided with various sections on a single page webpage like About, Experience, Projects, Education, Skills and Certifications. They have complete control over what information they want to add in these sections, what sections of the webpage they want the world to see and all of the information is presented in a single webpage dedicated to that user.</p>
<br>
<p align="center">
  <img src="https://media.giphy.com/media/zIX5gcH1j5cSSmZIKZ/giphy.gif" width="70%"><br>
  <h4 align="center">Demo portfolio : <a href="https://pholio1.herokuapp.com/john-doe"><strong>pholio.tech/john-doe »</strong></a></h4><br>
</p>

### Built With
* [Python](https://www.python.org)
* [Django](https://www.djangoproject.com)
* [Bootstrap](https://getbootstrap.com)

___

<h1 align="center">Getting Started</h1>

<p>Please make sure you have following requirements satisfied to run this project. Install given version of python, and packages from <i>requirements.txt</i> file.</p>

### Prerequisites

* [Python 3.7.9](https://www.python.org/downloads/release/python-379/)

### Installation

#### 1. Clone the repo:
```sh
git clone https://github.com/udz-codes/Pholio.git
```
#### 2. Install packages from <i>requirements.txt</i>:
```sh
pip3 install -r requirements.txt
```
#### 3. Setup [database configuration](https://docs.djangoproject.com/en/3.1/ref/databases/) in <i>project_pholio/settings.py</i>, OR use default sqlite3 database by adding following code to <i>project_pholio/settings.py</i>.
```Python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
#### 4. Make migrations to database:
```sh
python manage.py makemigrations
```
```sh
python manage.py migrate
```
#### 5. Add secret key in <i>project_pholio/settings.py</i>.
Generate secret key with this python script:
```sh
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```
#### 6. Change email settings according to you in <i>project_pholio/settings.py</i>:
* Set smtp of email client you want to use as value of <b>EMAIL_HOST</b>.
* Set your desired email address as value of <b>EMAIL_HOST_USER</b>.
* Set password of that email address as value of <b>EMAIL_HOST_PASSWORD</b>.
#### 7. Run project:
```sh
python manage.py runserver
```

___

<h1 align="center">Contributing</h1>

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

For major changes or suggestions, open an issue first.

___

<h1 align="center">Contact</h1>

<p align="center">Contact me on following links to discuss about the project or send feedback and suggestions</p>

<p align="center">Ujjwaldeep Singh - <a href="https://www.linkedin.com/in/udz">Linkedin</a> - <a href="https://twitter.com/udz_codes">Twitter</a> - <a href="mailto:ujjwal2699singh@gmail.com">ujjwal2699singh@gmail.com</p>
