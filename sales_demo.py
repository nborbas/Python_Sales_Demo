#Importing relevant libraries
import pandas as pd
from matplotlib import pyplot as plt

#Creating dummy data for line chart as vocabulary
daily_sales = { 'Days' : ['1 Feb', '2 Feb', '3 Feb', '4 Feb'],
                'Sales - Running' : [23, 33, 77, 110] }

#Creating dummy data for column chart as vocabulary
product_sales = { 'Product' : ['Chair', 'Table', 'Wardrobe', 'Bed'],
                  'Sales' : [48, 12 , 23, 27] }

#Defining DataFrames with pandas' DataFrame function
df_daily = pd.DataFrame(daily_sales)
df_product = pd.DataFrame(product_sales)

#Setting plotting style
plt.style.use('fivethirtyeight')

#Adding line chart plotting attributes
plt.plot(df_daily['Days'], df_daily['Sales - Running'], color = 'teal')

#Adding formatting attributes
plt.xlabel('Day')
plt.ylabel('Running Sum of Units Sold')
plt.title('Daily Sales')

#Show line chart
plt.show()

#Adding column chart plotting attributes
plt.bar(df_product['Product'], df_product['Sales'], color = 'maroon')

#Adding formatting attributes
plt.xlabel('Product')
plt.ylabel('Units Sold')
plt.title('Product Sales')

#Show column chart
plt.show()
