# Your very first prediction - Using fitted Sarima model

## Let's write a function `sarima_predictor()` that
* Takes in a fitted linear model and makes a prediction.
* It also calculates Root Mean square error

### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| model | sarima model | compulsory | | Fitted sarima model |
| X | DataFrame | compulsory | | Dataframe containing time variable as index and one column with time-series values to measure rmse|


Note: Every element in X should have a predicted value 

### Returns:

| Return | dtype | description |
| --- | --- | --- |
| y_pred | numpy.ndarray | Predicted values |
| rmse | float | Root Mean square error |
