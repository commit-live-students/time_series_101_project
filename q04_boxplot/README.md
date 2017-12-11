# Box-Plot using Sea-born

Again Visualization, As this is foremost the most important thing to do in any Machine learning.

Do you know that Data Scientist Usually spend 80% of their time collecting data and Visualizing it?
Do you know the famous Quote which Every Data Scientist have in their mind ? **GARBAGE IN.. GARBAGE Out**


## Let's write a function `box_plot()` that
* Takes as input the path, x_column_name, y_column_name, order_of_the_axis, size as input
* Outputs a box_plot visualization map.


**Note :** Training and validation sets have been preloaded for you.


### Parameters:
| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| path | str | compulsory |  | file path of csv file |
| x | str | compulsory | "month" | x-column name |
| y | str | compulsory | "Sales" | y-column name |
| order_of_the_axis | str | compulsory | ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug','Sep', 'Oct', 'Nov', 'Dec'] | order of plotting |





In this problem use x_column_name as **"month"**, y_column_name as **Sales** , data as **X_train** and **order_of_the_axis** as list with **Jan to Dec**  


Hint:
- Use seaborn factorplot with kind="box"

### Returns:

This function plots a box_plot using seaborn factorplot. This function returns nothing.

* Note -
Return Image should look like this

https://github.com/commit-live-students/time_series_101_project/blob/master/images/q03_stacked_point_plot.png
