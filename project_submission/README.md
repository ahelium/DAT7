### Question
Can I predict, for a given SmartBrief subscriber, the likelihood of churn?

### Dataset
Pull subscribers directly from SB DB. For each subscriber:

Response
	* Churn (binary)

Features (Round 1):

	* Normalized values describing sub's preferences (position type, company type, position function, company size
	* Date of subscription (to turn into subscriber duration)
	* Brief (which product in our product suite are they subscribed to)

Features (Round 2?):
	* Engagement metrics: last open date (time since last open),  last click date (time since last click)

Features (Round 2 or 3?)
	* Acquisition Campaign Information: campaign_name or campaign_type

Questions:
	* I will need to make sure that I have an adequate number of people who churned and people who are still active, but I am not sure what time period I need to look at. Would it be best to pull information about a subscriber's first 30, 60, 90 days, and run a bunch of different things? 



### Process
I'd like to try a couple of different things here, starting with logistic regression. If I have time, I'd really like to explore survival analysis.


