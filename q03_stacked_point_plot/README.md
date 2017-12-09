# Stacked point-plot chart using Seaborn

Visualizing is the key to extract insights from the data. We will use seaborn pointplot to visualize the data (We have discussed this in class).

## Let's write a function `Stacked_point_plot()` that
* Takes as input the x_column_name, y_column_name, hue, order_of_the_axis, data as input


**Note :**


### Parameters:
x_column_name: string
y_column_name: String
hue: string
data: pandas dataframe
order_of_the_axis: A list, The order in which you want the x-axis to be plotted

All the required data has already been loaded.

In this problem use x_column_name as **"month"**, y_column_name as **Sales** , hue as **"year"**, data as **X_train** and **order_of_the_axis** as list with **Jan to Dec**  


Hint: month and year columns were already created in the file.

### Returns:

This function plots a stacked point plot using seaborn pointplot. This function returns nothing.
