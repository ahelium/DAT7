### Problem statement:

SmartBrief produces 231 different digital newsletters(briefs) in a number of industries. I am working with the Director of Audience Development to send batch outreach to our subscribers to suggest additional briefs they would like to receive. We will be testing two different modeling approaches against a controll group, evaluating the response, and using it to determine which model to put into production (if any), so that a subscriber sees recommendations at time of subscription. 

1. When someone subscribes to one brief, can I successfully recommend other briefs he/she would like to read? Specifically, can I create a model that will increase outreach conversion rates? 
2. Will position function or company type information more heavily influence a subscribers product decision making? Specifically, will position function informaiton or company type information affect conversion rates?

### Hypothesis:
Using historical subcriber behavior to understand future subscriber behavior will increase conversion rates. Company type informaiton will hold more predictive power than Position Function informaiton. 

### Dataset(s):

Training Dataset:
Pulled from our proprietary database using SQL. 1.2 mm subscribers with at least two newsletter subscriptions in a pre-defined number of briefs. 

Prediction Dataset:
Pulled from our proprietary database using SQL. 120 thousand subscribers, director level or above, with only one newsletter subscription, in a defined number of briefs. Cut into 3 groups, controll, prediction 1, and prediction 2.

Data must haves:
Subscriberid, Email, Normalized Subscriber Information (company type and position function), Product Information (brief name, briefid)

### Data Pre-processing:

Data mapping:
Use dictionaries with map to clean up the position function and company type data. 

Data segment:
Use list to segment the data to remove products we dont want to recommend. 


### Data Exploration:
Grouped data by the different subscriber attributes to determine if there was enough to use both normalized position funciton and company type information. 
TODO: Run regression to explore if company_type or position_function could determine what brief a subscriber is subscribed to. 

###Modeling Process:

For each of normalized values (company type, position function):

-Segmented training data by normalized subscriber informaiton. Used dictionaries with key=normalized value, value=data.
-Pivoted data to get a sparse matrix of product informaition for each subscriber. 
-Created co-occurence matrices for each subset of data. 
-Filled co-occurence matrices where product combinations did not previously exist. 

-Segmented prediction data by normalized subscriber information. Used dictionaries with key=normalized value, value=data.
-Pivoted data to get a sparse matrix of product informaition for each subscriber. 
-Filled subscriber matrices where product combinations did not previously exist. 
-For each subset of subscribers, multiplied each row of prediction data by the corresponding co-occurence matrix to get a row of predictions. 
*Removed subscription that each subscriber already has.
*Sort by highest value to order the briefs
-Join back with original data to give to colleagues and clean it up.  

###Challenges
-NOT ENOUGH DATA!
* I was unable to use BOTH position function AND company type information becuase there was not enough data to build co-occurence matrices for every combination of the two. Further tests should update mapping proceedures and train on a larger subset of our database. 
-Processing Time! 
* I need to separate out parts of this script so that the objects are stored for future use. For example, say I train on 4 million subscribers, and use that at different times to predict subscriber preferences. Can I use a pickle (or something else) to store the training information and use it at different points of time for prediction?
-Product Size:
* I need to find a way to normalize for the size of each brief. For example, if one brief has 100 thousand subscribers, and another has 2000 subscribers, this model will recommend the larger brief much more (assuming people are still flowing into it). How can I account for this? I tried with a log likelihood approach, but the output was not what I wanted. 
-Bias of training data:
* Our subscribers come in to our publications through a number of different channels, and for each channel we do already suggest other products for them to receive. BUT, in the past, these suggestions have been made based on employee choice. How can I adapt my model to best mitigate these past decisions?

###Applications:
Depending on how the test goes, I need to find a way to make this fast enough to put in production. At first, we will batch the update of the training sets, and continuously predict against them, but at one point I would like to have this work in real time when a subscriber enters our system.

###Conclusions:
TBD. Test running this week, will need to run A/B stats on results to determine the best approach.











 NVM_DIR="/Users/annaglander/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"  # This loads nvm

