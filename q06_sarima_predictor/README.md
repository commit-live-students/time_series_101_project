# Your very first prediction - Using fitted Sarima model

# Note:
The `tss` and `tss_valid` dataframes have been pre-loaded for you.

## Let's write a function `sarima_predictor()` that
* Takes in a fitted SARIMAX linear model and makes a prediction.
* It also calculates Root Mean square error.
* Fit on the tss and predict on the tss_valid
* Returns the prediction(a dataframe with index same as that of `tss_valid`) and measure(RMSE).


### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| path | str | compulsory | | file path of the csv file |


 

### Returns:

| Return | dtype | description |
| --- | --- | --- |
| pred | pandas Dataframe | Predicted values |
| measure | float | Root Mean square error |
