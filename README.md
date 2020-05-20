# Time Gavel
### Final Full Stack Project for Code Institute using Django

### Travis CI
[![Build Status](https://travis-ci.org/Didgerydont/fullstack-milestone.svg?branch=master)](https://travis-ci.org/Didgerydont/fullstack-milestone)

#### Requirements
For my project I have decided to build Project Example Idea 2. Build an auction place to sell historical artifacts.
The goal of this project is to create an auction website for selling valuable historic items. The site owner should
be able to make money from this as well as providing potential customers with a UX friendly website thatallows them to easily
engage with the site, learn about the items and spend their money. 

##### External user’s goal:
Find, learn about and acquire artifacts they are interested in

##### Site owner's goal:
Earn money on selling the artifacts (the site owner is the seller)

#### User Stories
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




#### Overview of the features of the site. 
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

##### 


#####Potential features to include:
Create an online store focused on selling unique historical artifacts, such as The Holy Grail to the highest bidder.

Allow users to search for artifacts based on various fields.

Allow users to see the price, image and other basic details about an artifact.

Users would be able to learn about the historical details of each artifact, the culture it came from, the way it was created and its journey across different owners in the past.

For example, you might want to include information about "events" that took place in the past and that one or more artifacts took place in, or originated from.

Allow users to bid on items, or pay a higher price to purchase them immediately. Users have to be registered for this.

#####Advanced potential feature (nice-to-have)
Allow registered users to write reviews about the artifacts, only if they purchased them.

Expand the search functionality to allow users to sort results based on price, age and other parameters in both ascending and descending order.

Include pagination and/or other dynamic display actions using javascript.

Use javascript polling to update the page whenever there's a new bid



notes so far 


El Schema

The website is for auctioning. That will weigh heavy on design. 
Auto bid? 
Notifications of other bids is essential using javascript
Email notifications? 
A proper Schema will have to be devised. 



Antiques // History Object selling site


'''' delivery of items
Due to the nature of our products, standard delivery isnt available on any orders. The onus will be on the consumer to arrange
pick up and delivery. We will provide dimensions and whatever else is handy. 


'''
'''
As a consumer, I would like to be able to see the product I am buying with the price being immediately obvious.
I should be be able to click on the item to get more information about it. 
I should be able to create an account in order to have my details saved.
I should be notified if someone out bids me
Automatic bid raising up to a preset amount if someone bids on my item. (https://davidwalsh.name/javascript-polling)
Allow me to write reviews about the artifacts, only on products that I have purchased.

'''
'''
As the site owner, I should have a profile page where I can manage all of the items that I currently have for sale
I should be able to chop and change the starting price of items as well as upload multiple pictures of the item. 
I should be able to recieve messages from my buyers if they are looking for details. I should only be doing this with customers
after they have made a bid or purchased items in order to remove time wasters. 
I should be able to self manage my own account as well as manage users accounts via an admin panel. 
I should be GDPR compliant. 
I need to be able to take payments. 
Allow users to bid on items, or pay a higher price to purchase them immediately. Users have to be registered for this.
Include pagination and/or other dynamic display actions using javascript.
Expand the search functionality to allow users to sort results based on price, age and other parameters in both ascending and descending order.
'''

FUNCTIONS BASED ON USER STORIES
User Profile --> 
	Products --> Previously purchased, reviews
	Accounts --> Delivery address, personal information, password reset, user_id, the user should have to enter some card details before being allowed to bid in order to prevent time wasters
	Cart --> Remember cart on next login
	Bid system --> create bids, notification on bids, watch item function 
	

Owner Profile --> 
	Admin --> Password reset, user management, respond to queries, notification of purchases, pass information to warehouse?
	Products --> History, pictures, set buy immediately price, time left for bids, questions on items become available after bid. Inbox within admin page see bidder by user_id
	
	
	
==========
Test -- JShint passed, w3 html passed, css passed one error that I cant find
========== 

Requirements
==========================================================================================

Project Example Idea 2
Build an auction place to sell historical artifacts

External user’s goal:
Find, learn about and acquire artifacts they are interested in

Site owner's goal:
Earn money on selling the artifacts (the site owner is the seller)

Potential features to include:
Create an online store focused on selling unique historical artifacts, such as The Holy Grail to the highest bidder.

Allow users to search for artifacts based on various fields.

Allow users to see the price, image and other basic details about an artifact.

Users would be able to learn about the historical details of each artifact, the culture it came from, the way it was created and its journey across different owners in the past.

For example, you might want to include information about "events" that took place in the past and that one or more artifacts took place in, or originated from.

Allow users to bid on items, or pay a higher price to purchase them immediately. Users have to be registered for this.

Advanced potential feature (nice-to-have)
Allow registered users to write reviews about the artifacts, only if they purchased them.

Expand the search functionality to allow users to sort results based on price, age and other parameters in both ascending and descending order.

Include pagination and/or other dynamic display actions using javascript.

Use javascript polling to update the page whenever there's a new bid.

==========================================================================================