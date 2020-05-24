# Time Gavel
### Final Full Stack Project for Code Institute using Django
---




## Requirements
---
For my project I have decided to build Project Example Idea 2. Build an auction place to sell historical artifacts.
The goal of this project is to create an auction website for selling valuable historic items. The site owner should
be able to make money from this as well as providing potential customers with a UX friendly website that allows them to easily
engage with the site, learn about the items and spend their money. 

## UX
---

The user interface for this project will remain as clear and simple as possible as the focus of the project is to 
make it easy for the website to sell objects and for the end user to be able to spend their money in as straightforward a way as possible.
The UX will utilise HTML, CSS, Django Templates and JQuery. The Bootstrap framework provided by the good people over at Twitter is also
used on the project for their excellent ability for responsiveness across different devices. The colour scheme for the website is probided by the talented people over at [Bootswatch](https://www.bootstrapcdn.com/bootswatch/).
This project colour scheme is primarily Bootswatch's [Darkly](https://bootswatch.com/darkly/) styling. The style has been
downloaded as a static file in this project in order to remove possible issues reading from the CDN that Bootswatch uses.



### User Stories
---

>As a Consumer  
I would like to be able to see the product I am buying with the price being immediately obvious.  
I should be be able to click on the item to get more information about it.  
I should be able to create an account in order to have my details saved.  
I should be notified if someone out bids me  
Automatic bid raising up to a preset amount if someone bids on my item.  
Allow me to write reviews about the artifacts, only on products that I have purchased.  

>As the Owner  
I should have a profile page where I can manage all of the items that I currently have for sale  
I should be able to chop and change the starting price of items as well as upload multiple pictures of the item.   
I should be able to recieve messages from my buyers if they are looking for details. I should only be doing this with customers  
after they have made a bid or purchased items in order to remove time wasters.  
I should be able to self manage my own account as well as manage users accounts via an admin panel.  
I need to be able to take payments.  
Allow users to bid on items, or pay a higher price to purchase them immediately. Users have to be registered for this.  
Include pagination and/or other dynamic display actions using javascript.  
Expand the search functionality to allow users to sort results based on price, age and other parameters in both ascending and descending order.  

### External user’s goal:
---
Find, learn about and acquire artifacts they are interested in


### Site owner's goal:
---
Earn money on selling the artifacts (the site owner is the seller)


## Brainstorm based on User Stories
---

Not all features from the original brainstorming session made it to the site in the end. Most of these will be implemented
in future verisons of the project.

### FUNCTIONS BASED ON USER STORIES


>User Profile -->  
	Products --> Previously purchased, reviews  
	Accounts --> Delivery address, personal information, password reset, user_id, the user should have to enter some card details before being allowed to bid in order to prevent time wasters  
	Cart --> Remember cart on next login  
	Bid system --> create bids, notification on bids, watch item function  
	

>Owner Profile -->  
	Admin --> Password reset, user management, respond to queries, notification of purchases, pass information to warehouse?  
	Products --> History, pictures, set buy immediately price, time left for bids, questions on items become available after bid. Inbox within admin page see bidder by user_id  


## Wireframes & Schema

### Wireframes

##### All Auctions view
![alt wireframe one](https://github.com/Didgerydont/fullstack-milestone/blob/master/screenshots_and_wireframes/wireframes/all-auctions-view.JPG "Wireframe 1")  

##### Auction Singular
![alt wireframe two](https://github.com/Didgerydont/fullstack-milestone/blob/master/screenshots_and_wireframes/wireframes/auction-singular.JPG?raw=true "Wireframe 2")  


##### All Auctions view
![alt wireframe three](https://github.com/Didgerydont/fullstack-milestone/blob/master/screenshots_and_wireframes/wireframes/base-html.JPG?raw=true "Wireframe 3")  

##### Auction Singular
![alt wireframe four](https://github.com/Didgerydont/fullstack-milestone/blob/master/screenshots_and_wireframes/wireframes/index-html.JPG?raw=true "Wireframe 4")  

##### All Auctions view
![alt wireframe five](https://github.com/Didgerydont/fullstack-milestone/blob/master/screenshots_and_wireframes/wireframes/mobile-view.JPG?raw=true "Wireframe 5")  

##### Auction Singular
![alt wireframe six](https://github.com/Didgerydont/fullstack-milestone/blob/master/screenshots_and_wireframes/wireframes/all-auctions-view.JPG "Wireframe 6")  


### Schema and models

##### Models
![alt model one](https://github.com/Didgerydont/fullstack-milestone/blob/master/screenshots_and_wireframes/wireframes/models.JPG?raw=true "Model One")  


![alt model two](https://github.com/Didgerydont/fullstack-milestone/blob/master/screenshots_and_wireframes/wireframes/models2.JPG?raw=true "Model two")  

##### Schema
![alt schema](https://github.com/Didgerydont/fullstack-milestone/blob/master/screenshots_and_wireframes/wireframes/el-schema.jpeg?raw=true "Schema")  





## Overview of the features that made it onto the site. 
---
Here I will fo trough the main features of the site that been implement to best fit the needs of the owner and the end-user


### The user profile

The user profile attaches itself to Django's built in User object and allows extra fields to be added to the object. Here I have allowed the user to keep an address stored on file 
that they are able to keep updated themselves. The user here can enter their address to be kept on record and update it themselves as necessary  
![alt profile](https://github.com/Didgerydont/fullstack-milestone/blob/master/screenshots_and_wireframes/screenshots/profile-page.png?raw=true "Profile") 

### Requests for Specific Items

The Enquiries section of the site allows existing or new customers to request the auctioneers keep an eye out for specific items for a user
which can be expanded into a business for the contracted locating of items.  
![alt form](https://github.com/Didgerydont/fullstack-milestone/blob/master/screenshots_and_wireframes/screenshots/Item-request-form.png "Form") 

### Search Bars

The search bar is a central feature of the site and exists on all pages where more than one item is shown at a time. 
The search bar utilises Django's built in Q query function to check if the users quieried term exists within the desription or title
fields of the relevant model. 

![alt form](https://github.com/Didgerydont/fullstack-milestone/blob/master/screenshots_and_wireframes/screenshots/Annotation%20Search%202020-05-23%20155833.png?raw=true "Search") 


### Previuosly Sold Items

As the name suggests, the index page currently contains information of items previously sold on the website. At present
this has its own dedicated part of the database that the site owner can items too as he pleases. I did want to set this
model up where the item would automaticly be moved to the past sold items model but couldnt quite wrap around my head around
it. I will be returning to add this in a future version of the project. 


### Current auctions

The current auctions page (showallauctions.html) shows all currently running auctions. This utilizes a for loop
for iterating through the Auction model. There is an if statement wrapped around instance of the object that prevents expired
auctions from being shown on the page. This page also utilises pagination which I have will explain further down the features.


### All items & Enquiry

The all items page shows all items currently on file within model. This includes items that are in stock but not
up for auction yet. On each item there is a link to the current auctions page where the user can have a look to see
if an when the item will be up for grabs or alternatively if this hasnt been decided by the site owner they can make an enquiry
about the item. This does require login as it will take the users email address from their profile for correspondance

![alt form](https://github.com/Didgerydont/fullstack-milestone/blob/master/screenshots_and_wireframes/screenshots/Annotation%20Enquire%202020-05-24%20001036.png?raw=true "Search") 

### Pagination

The pagination on this project was inspired by [Master Code Online](https://www.youtube.com/channel/UCbhm6TbMBTWn_GxrIbPFapA)
They offer a really good tutorial on pagination// search bars which was easily altered to fit my needs. The pagination also uses its own
config.py file which makes creates an infinitely reusable function that can be called into the views that they are being used in

![alt form](https://github.com/Didgerydont/fullstack-milestone/blob/master/screenshots_and_wireframes/screenshots/Annotation%20Enquire%202020-05-24%20000942.png?raw=true "Search") 

## Checkout & Stripe

The checkout app and stripe set up are an adaptation of [Code Institute's](https://www.code-institute.net) checkout and stripe lesson taught in
the final module of their fullstack web development course. To make this work I had to remove a cart from the code and also had to change the views
in order to interact with models correctly. 


## Future Features
---

This has been my most challenging undertaking to date. The hours that have been poured into this project were tough 
at times and there was often times where I had taught I was completely defeated but perseverence and a little help
from the course tutors always kept me on track. This project has taught me so much about Python and Django but 
had left me defeated on a couple features that will need to added to the project in future in order to bring it
to a point where I can put it to bed and call it 100% completed.  


### Automaticly Expiring Models

I would have really liked to be able to figure out how to get my auctions to expire automaticly once the 
time had been reached but I was unable to figure this out before having to hand the project in


### Antiques Automaticly move to PastSold

Similar to above, I would have liked to have the item to move from the Antiques model to the more appropriate one after
it had been sold.


### Javascript Polling

One of the suggestions the advanced features section of the website was to create a javascript polling tool
that would automaticly refresh the bid information every ten seconds or so and reveal if their had been a new bid within that time.
This is a feature that I really would have liked to implemented but with the time given I will need to revert to it. 

	
## Testing the Project	

### UX
The code has been used on the following devices with no issue due to Bootstraps responsiveness

#### Large Viewports
* Lenovo Think Pad T490
* Macbook Pro
* IMac
* HP 250

#### Small Viewports
* Huawei Y30
* Samsung a70
* Samsung s7
* Iphone SE
* Samsung s9
* Samsung s5
* Pixel 2 / XL
* Iphone 6/7/8
* Iphone 6/7/8 Plus
* Iphone X
* Ipad Pro

## Code Validators
The code is currently been tested by Travis CI and is passing all tests. The jquery has passed [JSHINT](https://www.code-institute.net). 
The base.html has passed [HTML W3](https://validator.w3.org/) validation except
for the django template lines. CSS is also passing on [CSS Jigsaw](https://jigsaw.w3.org/css-validator/) validator as well. 


### Travis CI
---
[![Build Status](https://travis-ci.org/Didgerydont/fullstack-milestone.svg?branch=master)](https://travis-ci.org/Didgerydont/fullstack-milestone)


## Tech Used
In order to get this project to where it is at currently. I used the following technologies
* HTML
* CSS
* Bootstrap
* Django
* Python
* JQuery
* Stripe



## Deployment
Github, Heroku and AWS S3 were used for the deployment of this project.

You can view the production version of this project below: 
https://time-gavel.herokuapp.com/


If you would like to download the project and deploy it yourself. Then you will need to follow the following steps...  

* Create a Heroku account if you don’t already have one: 
https://www.heroku.com
* Install Heroku CLI on your local machine: 
https://devcenter.heroku.com/articles/heroku-cli
* Check that Heroku has successfully been installed by typing this in your terminal:


```sh
heroku --version 
```

* Now login to your Heroku account from your terminal. This will prompt a browser login via the CLI and all you will have to do is
 click 'login'

```sh
heroku login 
```

### Loading my Heroku App within the Project 

* Download this project as either a zip file or you can clone the project 

* Install all project requirements via requirments.txt
    ```sh
        pip3 install -r requirements.txt 
    ```
* Set the config variables:
    * I recommend setting these up in an env.py file that has been gitignored in order to keep these secret.  
    * This file will contain all relevent variables for all sites that we will be deloying on.   
    This project will need variables for Stripe, AWS S3 and Heroku. These will all also need to be entered
    on the corresponding websites.  
    I have set my env.py file like so...  
    ```python
        import os

        os.environ.setdefault("DATABASE_URL", "keepThisASecret")
        os.environ.setdefault("SECRET_KEY", "keepThisASecret")
        os.environ.setdefault("STRIPE_PUBLISHABLE_KEY", "keepThisASecret")
        os.environ.setdefault("STRIPE_SECRET_KEY", "keepThisASecret")
        os.environ.setdefault("AWS_ACCESS_KEY_ID","keepThisASecret")
        os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "keepThisASecret")
    ```

* Once this has been done. You should do ahead an download dj_database_url and activiate a free tiered Postgress database to use on your site.  
You can then use a simple if statment in the project to have the code determine whether you are on a development or production server.  

I have done mine like so...

```python

    if os.environ.get('DEVELOPMENT'):
    development = True

    else:
        development = False


    DEBUG = development

    if development:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }
        MEDIA_URL = '/media/'

    else:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }


```

* It is worth nothing that once we have successfully moved the project onto Heroku and S3 that we will have two instances of the same site.
The local site will use its own sqlite3 DB and the production one hosted by Heroku will have its own separate one as well which makes life easier on version control
 whiles working on a live

* DONT FORGET TO USE COLLECTSTATIC IN ORDER TO PUSH CHANGES TO S3.  
Like so....
```sh
    python3 manage.py collectstatic
```


* You will also need to set up an account with [S3](https://console.aws.amazon.com/s3/) for handling our static files. 

* We will then need to set up our media and static routes within settings.py to match our S3 account. My example using secret files has been 
included below  


```python
    AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000'
}

AWS_STORAGE_BUCKET_NAME = 'fullstack-django'
AWS_S3_REGION_NAME = 'eu-west-1'
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS")

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


```

* Once this has been completed. We can the run the project two ways:
    ```
        python3 manage.py runserver 
    ```

### Linking Github and Heroku pushes 
1. Log on to Heroku and locate the project. 
2. When you are on the main dashboard of the project, locate the deploy tab.
3. Once you have clicked this and have been redirected, scroll down to the option that allows you to connect your Github repo to Heroku. 
4. Once connected you will then be able to enable automatic deploys. 

* Now pushing to Github will also push changes to Heroku. 


