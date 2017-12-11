# Split Data into train and validation - Setting up the analysis

Now that you have imported the data, lets split the data into train and validation

Why do we need to split the data ?
Tip: In practice, before predicting for future, We need to backtest our model performance. So first we need to split our data into train and validation. Build our model on train data and verify it on validation data

Why do we need to test our model performance on validation data and not on train data ?
Tip: Learn what does Over-fitting means

## Write a function `data_splitter()` which splits the data into train and validation using the following parameters
- Convert the `'Month'` column to a *datetime* object using the **.to_datetime()** method.
- Train: < 1971-10-01
- Valid: >= 1971-10-01
- Use Month column to split the data.

## Tip:
- Convert the Month column to datetime64[ns] object using pandas **to_datetime** function.
- Use datetime package to create a datetime type object from string.

### Parameters:

Function should take data, split_time and column name as input and output two DataFrames.

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| path | str | compulsory |  | file path of csv file |


### Returns:

| Return | dtype | description |
| --- | --- | --- |
| X_train | DataFrame | Dataframe containing train data |
| X_valid | DataFrame | Dataframe containing train data |
