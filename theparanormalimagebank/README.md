# The paranormal image bank
#### Video Demo:  <URL https://www.youtube.com/watch?v=acxp24BRZ0Y>
#### Description:
This idea of a project came from a little challenge me and some friends were facing while trying to solve a series of puzzles from a game franchise we love.
The game contains some simple puzzles, and many quite challenging ones, involving spectrograms and other cryptography methods.
But while solving the encryptions we ran into a logistic problem of separating and organizing the many prints of cyphers.
So, since i was on the cs50 program I proposed to make a Image Bank to keep our findings and translations.

originally I planned on having a automation for the translation of simbols, but I quicly realized that it was way out of my scope, to the point where some of the most advanced Ais from today are having trouble with (using an Api to an AI was also on my ideas but aparently when we give these instructions to chat GPT or gemini they just spit out gibrish)

Also, I had problems to start a flask, and sience I have allready a functioning flask file on my github I copied and edited a version of the "finance" project. it saved a lot of work and gave me a good base to develop the final project

# The static directory
is dedicated to keeping the "static" files as fotos and css.
## The styles.css
file houses all the Css for the site and it is a mixture of personal touches of mine and also some libraries ( for the lack of a better term) found on the internet all that on top the original Css of the finance project.
## cifra.png I_heart_validator.png and simbolo.png
are images. cifra is a cypher key used on the "edit" pop up pages and simbolo is the icon for the layout template. I_heart_validator.png is part of the original code of the "finance" project that I thought interesting to keep

# the flask_session
is a directory to run the flask. I honestly dont understand much of its purpose but removing it brings the site down so i kept it for the sake of not re-writing the entire project.

# App.py
file is my pyton main file. it contains all my routes and logic for the site to work. it contains routes for: index,update translation (edit), add image, login, and logout.

## Index
is a page that searches my database and displays all the images that correlate with the searchbar
## Login
checks if my password is correct ("MapleMaypole" is the sole password for the site simply because it is designed to be acessed just by me and a couple other friends who will be sharing images with, making the "users" logic obsolete )
## Logout
brings me to login screen again and locks the rest of the pages untill the password is apllyed.
## Update
translation does as the name says and update the translation/description of a selected photo
## Add image
brings me to another page where I can select a file to upload with a name and a translation/description

# Helpers
 is a litle bit of code I borrowed from the "finance" project, I edited it to have only the login logout and the apology functions(witch by the way is hilarious)

# Requirements.txt
 is another file I decided not to edit in fear of unknowinly removing something that (ironically) is actually required. But i comprehend that this file sets the required libraries

# images.db
is my database with some images allready in it ( for reference). the schema of the database is

__CREATE TABLE images(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,name, images BLOB, translation);__

image is Blob in order to keep on the database the binary sequence of images. this took me a long time to find and decide, i passed trough other 3 methods of keeping the images before that, for example until almost the end of the project i was downloading the images direcly on the github and simply referencing them on the code, but i figured it would get messy quicly and chose this aproach instead.


# templates
directory contains: add_image.html apology.html index.html layout.html And login.html
## layout.html
 contains the base for all my other templates, most of my choices of aperence most of it was borrowed from the "finance" and edited to be the way I intended, mostly removing unimportant parts of the original code and adding litle creative choices of my own.

## login.html
 is my login page, with only the password input (sience im not using multiple sessions) whose passowrd is " MapleMaypole".

## Apolog.html
is also somethin i borowed from the "finance" mostly because the angry cat is hilarious. but objectevly its simply a adition to the base layout with a image of a cat that has editable text that is imputed from the apology function at heplers.

## Add_image.html
 is similar to login but with a field to the translation/description, a field for name, and a button to select a image to upload.

## Index.html
contains the most variation from the base layout, it contains a searchbar with the option of searching by name or translation/description and a iterated table with all the images on the database and the acording names and translations. On index you can click at edit on the side of any of those photos to edit the translations/description of that specific row (and it atualizate the database too)

# final words
As said before i had plans way too big for this project (I Literally wanted to solve the problem of an entire industry haha), In the end I scoped it down to a manageble level. I will post the project as it is now because my freetime is starting to run low on the start of the year and i wont have as much time to work on this project. I am happy with it`s state, but i will keep working on it trougout this year as me and my friends find bugs and interesting features to add.

again, thanks for the learning oportunity.


