# Dataset attribution and scope

**Provider:** Den_Kuznetz (Kaggle handle `denkuznetz`).

**Title:** Food Delivery Time Prediction. **Version:** 1.

Source: https://www.kaggle.com/datasets/denkuznetz/food-delivery-time-prediction

Download endpoint: https://www.kaggle.com/api/v1/datasets/download/denkuznetz/food-delivery-time-prediction

Retrieved 11 October 2026. `Food_Delivery_Times.csv` is an unchanged copy from the provider's archive. The input SHA-256 is recorded in `results/summary.json`.

Kaggle's API identifies the dataset license as **Apache 2.0**. The license text is included in `DATA_LICENSE.txt`; the provider metadata snapshot is `source_metadata.json`. Attribution is retained here. The license statement applies to the dataset, not automatically to all project code.

The source describes fields but does not identify a collection period, city, delivery company or collection protocol. This project does not assert that the data are verified operational records, nor that they are definitively synthetic. They are used as a public educational benchmark.

## Data dictionary

| Column | Meaning | Role |
|---|---|---|
| Order_ID | Unique order identifier | Audit only; excluded |
| Distance_km | Delivery distance in km | Numeric predictor |
| Weather | Clear, Rainy, Snowy, Foggy, Windy | Categorical predictor |
| Traffic_Level | Low, Medium, High | Categorical predictor |
| Time_of_Day | Morning, Afternoon, Evening, Night | Categorical predictor |
| Vehicle_Type | Bike, Scooter, Car | Categorical predictor |
| Preparation_Time_min | Recorded preparation duration | Excluded: availability at order time is unverified |
| Courier_Experience_yrs | Courier experience in years | Numeric predictor |
| Delivery_Time_min | Total delivery duration in minutes | Target |

`example_input.csv` is a derived subset containing only predictor columns of the first held-out order. No target or preparation duration is supplied to inference. Blank predictor entries are imputed by the saved training pipeline.
