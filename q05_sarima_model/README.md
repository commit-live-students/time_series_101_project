# Fitting your sarima model

In the class we have seen that SARIMA model is out-performing all the other DataDriven models we have discussed in the class. Do u remember the reason why this is so?

It is a robust model when there is a clear seasonality in your data.

So lets write a fuction to build a sarimax model. 

## Let's write a function `sarima()` that
* Takes as input as train_data (index has time variable and has one column with Time-Series values)
* Fit a SARIMAX model from statsmodels.tsa.statespace module

### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| X | DataFrame | compulsory | | Dataframe containing time variable as index and one column with time-series values |
| order | tuple | compulsory | | A tuple contain the (p, d, q) values of Non-seasonal part of the model |
| seasonal_order | tuple | compulsory | | A tuple containing the (p, d, q) values of seasonal part of the model |

### Returns:

| Return | dtype | description |
| --- | --- | --- |
| lm | statsmodels.tsa.statespace.sarimax.SARIMAX | Fitted a SARIMAX Model |
