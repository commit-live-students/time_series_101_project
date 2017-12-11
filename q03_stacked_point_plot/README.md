# Stacked point-plot chart using Seaborn

Visualizing is the key to extract insights from the data. We will use seaborn pointplot to visualize the data (We have discussed this in class).

## Let's write a function `Stacked_point_plot()` that
* Takes as input the path, x_column_name, y_column_name, hue, order_of_the_axis.


**Note :**
* Create two new columns `year` and `month` from the `Month` column by extracting the year and months. 
* This assignment is needed to be carried out on the training dataframe only.


### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| path | str | compulsory |  | file path of csv file |
| x_column_name | str | compulsory | "month" | month column |
| y_column_name | str | compulsory | "Sales" | Sales column |
| hue | str | compulsory | "year" | display colored plots by hue |
| order_of_the_axis | list | compulsory | ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug','Sep', 'Oct', 'Nov', 'Dec'] | order of plotting |

All the required data has already been loaded.

In this problem use x_column_name as **"month"**, y_column_name as **Sales** , hue as **"year"**, data as **X_train** and **order_of_the_axis** as list with **Jan to Dec**  



### Returns:

This function plots a stacked point plot using seaborn pointplot. This function returns nothing.
