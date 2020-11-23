# Olist e-commerce Data Analysis

**Lars Tinnefeld**, 2020-11-23

![portrait](https://images.unsplash.com/photo-1522204523234-8729aa6e3d5f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80)

## Objectives and Motivation
The goal of the work in this notebook is to extract information which can serve as a base for data driven decisions that could lead to improvement of the business. The data stems from Olist, a Brazilian e-commerce department store (Software as Service). In detail, the analysis is applying time series, modeling and regression analysis to reveal and validate trends and patterns in the development of the business. This output may allow projections for a future business model. In addition, a hypothetical extension of the business service will be reviewed. This new business model would include warehousing and logistic services for the shopkeepers. The analysis will therefore be focussed on these questions:
- Are there correlations and patterns in the data which lead to important conclusions?
- What is the general business trend?
- How dynamic is the operation and are there extreme events which impact logistic processes?
- What does the prediction say about the business in two years?

## About Olist
Olist is for everyone "who wants to sell more and better" and "who wants to attract new customers". As an business in the e-commerce sector, Olist is an online selling platform for small businesses. On Olist's sign-up page a range of shopkeeper profiles is listed which fits the business model. Clearly, a strong focus is on attracting more customers.

## The data
The provided data set consists of historical order data from 2016 to 2018 and contains 100,000 orders. There are 8 files available. The below data model displays high level the references between these data- and lookup tables. For the project not all data tables will be used. The data was generously provided by Olist under the license CC BY-NC-SA 4.0 and can be found *[here](https://www.kaggle.com/olistbr/brazilian-ecommerce)* in Kaggle.
For the current analysis following data files were used:
- olist_orders_dataset.csv: Contains the orders with order-id, delivery time stamps, the order status and customer-id
- olist_order_items_dataset.csv: Contains the details of the orders with order-id, product-id, seller-id, price, freight cost and shipping limit date
- olist_products_dataset.csv: Contains the details of the products with product-id, category, product name, name length, available photos, dimensions and weight

![Data Structure](https://i.imgur.com/HRhd2Y0.png)
*Data model as provided in Kaggle*

## Approach and used libraries
- Data import and wrangling (Python, Pandas, Numpy)
- Exploratory Data Analysis (Python, Pandas, Seaborn, Matplotlib)
- Time Series visualizations (Python, Pandas, Seaborn, Matplotlib)
- Logistic Regression (Python, Pandas, Seaborn, Matplotlib, Sklearn)

## Brief conclusion
The business is growing and the day-to-day volume is fluctuating very dynamically. Black Friday is a major event for the business. The prognosis is predicting with some error margin that in beginning 2020 in average 500 units per day will be sold. "Health and Beauty" and "Gift Watches" are key categories in the product mix. Delivery times for expensive products seem to be somewhat important for shopkeepers and customers. A final conclusion about the extension of the business model is outstanding due to more required concept selection steps, but initial results already show that a highly automated system would not be a good fit.
