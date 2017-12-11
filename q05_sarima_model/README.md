# Fitting your sarima model

In the class we have seen that SARIMA model is out-performing all the other DataDriven models we have discussed in the class. Do u remember the reason why this is so?

It is a robust model when there is a clear seasonality in your data.

Train and validation models have been pre-loaded for you.

So lets write a fuction to build a sarimax model properly in the next function. 

## Let's write a function `sarima()` that
* Takes input as path of the csv file.
* Creates new dataframes for both training and validation sets with a single column whose values are the values of the `Sales`   column and the index values are the `Month` values.

## Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| path | str | compulsory | | file path of the csv file |

### Returns:

| Return | dtype | description |
| --- | --- | --- |
| tss | pandas Dataframe | training dataframe |
| tss_valid | pandas Dataframe | training dataframe |
