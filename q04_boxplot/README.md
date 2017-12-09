# Box-Plot using Sea-born

Again Visualization, As this is foremost the most important thing to do in any Machine learning.

Do you know that Data Scientist Usually spend 80% of their time collecting data and Visualizing it?
Do you know the famous Quote which Every Data Scientist have in their mind ? **GARBAGE IN.. GARBAGE Out**


## Let's write a function `box_plot()` that
* Takes as input the x_column_name, y_column_name, order_of_the_axis, data as input
* Outputs a box_plot visualization map.


**Note :**


### Parameters:
x_column_name: string
y_column_name: String
data: pandas dataframe
order_of_the_axis: A list, The order in which you want the x-axis to be plotted


All the required data has already been loaded.

In this problem use x_column_name as **"month"**, y_column_name as **Sales** , data as **X_train** and **order_of_the_axis** as list with **Jan to Dec**  


Hint:
- month and year columns were already created in the file.
- Use seaborn factorplot with kind="box"

### Returns:

This function plots a box_plot using seaborn factorplot. This function returns nothing.
