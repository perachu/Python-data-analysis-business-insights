## import library and dataset
import pandas as pd
store = pd.read_csv("sample-store.csv")

# review shape of dataframe
store.shape

# see data information using .info()
store.info()

## Data cleansing

# 1st step: convert data from Date to Date&Time format and assign to new variable, to be ready to be updated to dataframe
# method: using .to_datetime()
cv_orderdate = pd.to_datetime(store['Order Date'], format='%m/%d/%Y')
cv_shipdate = pd.to_datetime(store['Ship Date'], format='%m/%d/%Y')

# 2nd step: update variable that we prepare in 1st step to the dataframe
store['Order Date'] = cv_orderdate
store['Ship Date'] = cv_shipdate
store.head()

# 3rd step : extract only year data from 'Order date' column and assign to new column which named 'Order_Year'
store['Order_Year'] = store['Order Date'].dt.year
store.head()

## Let's analyze
# 1) How much total sales, average sales, and standard deviation of sales your company make in 2017
store.query('Order_Year == 2017')['Sales'].agg(['sum', 'mean', 'std'])

# 2) Which segment has the highest profit in 2018
store.query('Order_Year == 2018').groupby('Segment')['Profit'].sum()\
                                 .sort_values(ascending=False)

# 3) Which top 5 States have the least total sales between 15 April 2019 and 31 December 2019
store[(store['Order Date'] >= "2019-04-15 00:00:00") & (store['Order         Date'] <= "2019-12-31 00:00:00")]\
     .groupby('State')['Sales'].sum()\
     .sort_values().head(5)

# 4) Your friend ask for all order data in ‘California’ and ‘Texas’ in 2017 (look at Order Date), send him .csv file
store_filtered = store.query('(State == "California" or State ==     "Texas") & Order_Year == 2017')
store_filtered.to_csv("store_filtered.csv")

# 5) Profit distribution by product in graphical using bar plot
import matplotlib.pyplot as plt
store.groupby('Product Name')['Profit']\
     .sum().plot(kind='hist',bins=100);

plt.xlim(-5000, 3000);
plt.xlabel('Total Profit by Product')
plt.ylabel('Frequency')
plt.title('Distribution of Product Profits')
plt.show()

# 6) Top 10 products that make lowest profit and display in graphical using bar plot
store.groupby('Product ID')['Profit'].sum()\
     .sort_values().head(10).plot(kind='bar');

plt.xlabel('Product ID')
plt.ylabel('Profit')
plt.title('Top 10 Lowest Profit by Product')
plt.show()

