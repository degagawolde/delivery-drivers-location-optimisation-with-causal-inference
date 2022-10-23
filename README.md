# delivery-drivers-location-optimisation-with-causal-inference

## Objective
Gokada wants to work on its data to help it understand the primary causes of unfulfilled requests as well as come up with solutions that recommend drivers locations that increase the fraction of complete orders. Since drivers are paid based on the number of requests they accept, your solution will help Gokada business grow both in terms of client satisfaction and increased business.

## The Data
There are two datasets available for this project.


The first one is the table that contains information about the completed orders
|   |  Column      |       Non-Null Count  |  Dtype | 
| --- |  ------          |   -------------- |   ----- | 
|  0|    Trip ID          |  536020 non-null|   int64 | 
|  1|    Trip Origin      |  536020 non-null  | address| 
|  2|    Trip Destination |  536020 non-null  | address| 
|  3|    Trip Start Time  |  534369 non-null  | timestamp| 
|  4|    Trip End Time    |  536019 non-null  | timestamp| 

The second one is the table that contains delivery requests by clients (completed and unfulfilled) 
| | Column   |       Non-Null Count |    Dtype|   
| --- |  ------      |    -------------- |    -----  | 
|  0  |  id         |     1557740 non-null |  int64  | 
|  1  |  order_id      |  1557740 non-null |  int64  | 
|  2   | driver_id     |  1557740 non-null |  int64  | 
|  3   | driver_action |  1557740 non-null |  object | 
|  4   | lat           |  1557740 non-null |  float64| 
|  5   | lng           |  1557740 non-null |  float64| 
|  6   | created_at    |  0 non-null       |  float64| 
|  7   | updated_at    |  0 non-null       |  float64| 


## Data Cleaning
- [x] Drop columns with empty entries
- [x] Drop rows with NaN entries
- [x] Merge the Two tables

## Feature Engineering
- [x] Generate month, day, week day, and an hour from the trip start time column.
- [x] Calculate the driver proximity to the order using trip origin and driver location when the
driver got the order which is given in lat and lng in the second table. 
- [x] Calculate trip distance and trip duration and then trip speed.
- [x]I also used the API from https://api.weatherbit.io/v2.0/history/daily? to get the weather
at a given location and time-stamp.
- [x] Public, school, regional and national holidays are calculated
from the trip start time.

## Visualization

- [x] plot driver distance vs acceptance rate
- [x] plot latitude vs longitude of dirver location 


## Future Works
- Create a causal graph using all training data and get the insights 
- Create new causal graphs using increasing fractions of the data and compare them with the ground truth graph.
- Train ML models (at least consider XGboost and Random Forest
- Measure how much each of the models overfits the hold-out set created.
- Formalise the problem of driver placement recommendation based on integer optimization.
