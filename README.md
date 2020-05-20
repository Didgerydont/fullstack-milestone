# Time Gavel
### Final Full Stack Project for Code Institute using Django
---


### Travis CI
---
[![Build Status](https://travis-ci.org/Didgerydont/fullstack-milestone.svg?branch=master)](https://travis-ci.org/Didgerydont/fullstack-milestone)



#### Requirements
---
For my project I have decided to build Project Example Idea 2. Build an auction place to sell historical artifacts.
The goal of this project is to create an auction website for selling valuable historic items. The site owner should
be able to make money from this as well as providing potential customers with a UX friendly website that allows them to easily
engage with the site, learn about the items and spend their money. 

#### UX
---

The user interface for this project will remain as clear and simple as possible as the focus of the project is to 
make it easy for the website to sell objects and for the end user to be able to spend their money in as straightforward a way as possible.
The UX will utilise HTML, CSS, Django Templates and JQuery. The Bootstrap framework provided by the good people over at Twitter is also
used on the project for their excellent ability for responsiveness across different devices. The colour scheme for the website is probided by the talented people over at [Bootswatch](https://www.bootstrapcdn.com/bootswatch/).
This project colour scheme is primarily Bootswatch's [Darkly](https://bootswatch.com/darkly/) styling. The style has been
downloaded as a static file in this project in order to remove possible issues reading from the CDN that Bootswatch uses.


##### External user’s goal:
---
Find, learn about and acquire artifacts they are interested in


##### Site owner's goal:
---
Earn money on selling the artifacts (the site owner is the seller)



#### User Stories
---

##### As a Consumer
>I would like to be able to see the product I am buying with the price being immediately obvious.
>I should be be able to click on the item to get more information about it. 
>I should be able to create an account in order to have my details saved.
>I should be notified if someone out bids me
>Automatic bid raising up to a preset amount if someone bids on my item.
>Allow me to write reviews about the artifacts, only on products that I have purchased.

##### As the Owner
>I should have a profile page where I can manage all of the items that I currently have for sale
>I should be able to chop and change the starting price of items as well as upload multiple pictures of the item. 
>I should be able to recieve messages from my buyers if they are looking for details. I should only be doing this with customers
>after they have made a bid or purchased items in order to remove time wasters. 
>I should be able to self manage my own account as well as manage users accounts via an admin panel. 
>I need to be able to take payments. 
>Allow users to bid on items, or pay a higher price to purchase them immediately. Users have to be registered for this.
>Include pagination and/or other dynamic display actions using javascript.
>Expand the search functionality to allow users to sort results based on price, age and other parameters in both ascending and descending order.

#### Brainstorm based on User Stories
---

Not all features from the original brainstorming session made it to the site in the end. Most of these will be implemented
in future verisons of the project.

>FUNCTIONS BASED ON USER STORIES


>User Profile --> 
	>Products --> Previously purchased, reviews
	>Accounts --> Delivery address, personal information, password reset, user_id, the user should have to enter some card details before being allowed to bid in order to prevent time wasters
	>Cart --> Remember cart on next login
	>Bid system --> create bids, notification on bids, watch item function 
	

>Owner Profile --> 
	>Admin --> Password reset, user management, respond to queries, notification of purchases, pass information to warehouse?
	>Products --> History, pictures, set buy immediately price, time left for bids, questions on items become available after bid. Inbox within admin page see bidder by user_id


#### Wireframes

![alt wireframe one][logo]


#### Overview of the features that made it onto the site. 
---
Here I will fo trough the main features of the site that been implement to best fit the needs of the owner and the end-user


##### The user profile

The user profile attaches itself to Django's built in User object and allows extra fields to be added to the object. Here I have allowed the user to keep an address stored on file 
that they are able to keep updated themselves. The user here can enter their address to be kept on record and update it themselves as necessary


##### Requests for Specific Items (Enquiries)

The Enquiries section of the site allows existing or new customers to request the auctioneers keep an eye out for specific items for a user
which can be expanded into a business for the contracted locating of items. 


##### Search Bars

The search bar is a central feature of the site and exists on all pages where more than one item is shown at a time. 
The search bar utilises Django's built in Q query function to check if the users quieried term exists within the desription or title
fields of the relevant model. 


##### Previuosly Sold Items

As the name suggests, the index page currently contains information of items previously sold on the website. At present
this has its own dedicated part of the database that the site owner can items too as he pleases. I did want to set this
model up where the item would automaticly be moved to the past sold items model but couldnt quite wrap around my head around
it. I will be returning to add this in a future version of the project. 


##### Current auctions

The current auctions page (showallauctions.html) shows all currently running auctions. This utilizes a for loop
for iterating through the Auction model. There is an if statement wrapped around instance of the object that prevents expired
auctions from being shown on the page. This page also utilises pagination which I have will explain further down the features.


##### All items

The all items page shows all items currently on file within model. This includes items that are in stock but not
up for auction yet. On each item there is a link to the current auctions page where the user can have a look to see
if an when the item will be up for grabs.


##### Pagination

The pagination on this project was inspired by [Master Code Online](https://www.youtube.com/channel/UCbhm6TbMBTWn_GxrIbPFapA)
They offer a really good tutorial on pagination// search bars which was easily altered to fit my needs. The pagination also uses its owne
config.py file which makes creates an infinitely reusable function that can be called into the views that they are being used in


##### Checkout && Stripe




#### Future Features
---

This has been my most challenging undertaking to date. The hours that have been poured into this project were tough 
at times and there was often times where I had taught I was completely defeated but perseverence and a little help
from the course tutors always kept me on track. This project has taught me so much about Python and Django but 
had left me defeated on a couple features that will need to added to the project in future in order to bring it
to a point where I can put it to bed and call it 100% completed.  


##### Automaticly Expiring Models

I would have really liked to be able to figure out how to get my auctions to expire automaticly once the 
time had been reached but I was unable to figure this out before having to hand the project in


##### Antiques Automaticly move to PastSold

Similar to above, I would have liked to have the item to move from the Antiques model to the more appropriate one after
it had been sold.


##### Javascript Polling

One of the suggestions the advanced features section of the website was to create a javascript polling tool
that would automaticly refresh the bid information every ten seconds or so and reveal if their had been a new bid within that time.
This is a feature that I really would have liked to implemented but with the time given I will need to revert to it. 


####
	
#### Testing the Project	



==========
Test -- JShint passed, w3 html passed, css passed one error that I cant find
========== 

Requirements
==========================================================================================

