# Xmeme 
An meme stream application made for CRIO winter of doing program. This application helps user posts memes by giving their name, caption for the meme with tags and publically hosted url of any image. 

# Technology Stack

Frontend : HTML, CSS, Vanilla Javascript, Bootstrap.

Backend : Python(Django)

Database : SQLite( in development ), Postgresql( in production )

Deployment : Heroku ( Both for Frontend and Backend )

# Frontend Design

The Frontend was designed using figma and the application can be found out at the link : https://www.figma.com/file/iWwJIr5e7HNU1iusQa8ls1/xmeme

Figma helps in fast designing and prototyping.


# How to run the application

1. Make sure you have python version 3 and above installed in your system. Because it is required to run the backend server. 
2. After cloning the repository, go to terminal and type `cd xmeme-backend`
3. Create a virtual environment to avoid any package colliosions. 
```
pip3 install virtualenv
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
4. After this the backend will start running on default address http://localhost:8000 
5. To run the frontend simply open the `index.html` from `xmeme-frontend` inside the browser and the application will start working.

# Additional Features

1. Added the feature to let user enter tags with caption and the frontend will understand and highlight the tags for the user. Thus, the caption can be entered with tags.
2. All the posts having the same tags can also be seen and thus they are kind of categorized together having same tag names. for example all memes having tag `#crio` can be seen on a single page to get more enjoyment and user interactivity.
3. Added the feature to notify user in realtime that new posts are being posted by user and are available to view. The user have to simply click on the notification and the application will reload with new memes showing on the top.