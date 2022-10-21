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

## Feature Engineering

## Visualization

## Causal Inference

## Conclusion

## Future Works