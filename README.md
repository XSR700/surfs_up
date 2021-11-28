# surfs_up

## Overview of the analysis: Explain the purpose of this analysis.

This analysis provides SQLlite weather data from Hawaii. W. Avy would like to join on a business venture to start a surf shop in Hawaii. He is concerned about the wether impact on the longevity of the business. This analysis will look into the typical weather conditions in June and December and make a conclusion if these findings will pose a risk for the start up surf shop. 


## Results: Provide a bulleted list with three major points from the two analysis deliverables. Use images as support where needed.

* The image below represents summary of the data collected from the month of June. Oahu of Hawaii has reached a maximum temperature of 85 degree F with an average temperatures of 74 degree F. 

!['June'](https://github.com/XSR700/surfs_up/blob/main/Resources/June.PNG)

* The image below represents summary of the data collected from the month of Decembere. Oahu of Hawaii has reached a maximum temperature of 83 degree F with an average temperatures of 71 degree F.  

!['December'](https://github.com/XSR700/surfs_up/blob/main/Resources/December.PNG)

* The summaries for June and Decmber do not show dramatic difference in terms of maximum temperature and mean values. The biggest difference is between the minumum temperature values. December reached a 56F minimum and June reached a 64F minimum. 


## Summary: Provide a high-level summary of the results and two additional queries that you would perform to gather more weather data for June and December

There are ways we can improve our analysis to help understand if our surfshop will suffer due to weather related events in Oahu, Hawaii. The SQLlite flat file that we have been working with to aquire our data has additional information to disect and retrieve. For example another query we can test is to look into elevation. The Measurement table also holds elevation points. If we create a list of elevations to each station, we can narrow down which stations are more useful. A station that is high up in the mountain will have much different temperatures and our surf shop will pressumubly be located closer to the beach near sea level. Another improvement we can add to our analysis is to split the data by the hour. We can edit our session.query code to extract not by mmm/dd/yyyy but also to include hours of each date. Then extract the data by looking at only the weather during the business hours (i.e. 8am-6pm). This will give us the conditions to expect during the time when the sur shop is open for business. 
