# E-commerce order profile analysis
A project of the Olist ecommerce business analysis

**Lars Tinnefeld**, 2021-03-27

![Hero_picture](https://cdn.pixabay.com/photo/2016/03/23/07/57/receipt-1274307_960_720.jpg)

## Table of content
1. [Order profile analysis](#business_understanding)
2. [Objectives](#objectives)
3. [Data](#data)
4. [Data preparation](#preparation)
5. [Exploratory data analysis](#eda)
6. [Order profile analysis](#order_analysis)
7. [Affinity Analysis](#affinity)
8. [Conclusion](#conclusion)
9. [References and links](#references)

## Order Profile Analysis <a name="business_understanding"></a>
Gaining an understanding about key metrtrics, correlations and patterns of the business is one of the most important steps in developing a successcul warehouse- and logistic concept. Ecommerce proves to be a very challenging business field in that aspect thanks to the dynamics and often unpredictable day-to-day developments. There is a range of "traditional" analysis outputs which provide an experienced logistics specialist with insights into the business: Pareto diagram, ABC classification, XYZ classification, Units-per-order distribution, Lines-per-order distribution, category breakdown. These are important metrics because they directly impact warehouse concept and sizing. Beside this, it is in many cases useful to understand the data in a bigger context, often including the characteristics of users and their shopping choices. "Market Baset Analysis" and "Product Correlation" help to disclose information in this aspect and support experts to make better decisions.

## Objectives <a name="objectives"></a>
The analysis in this repository will follow above mentioned pattern in order to answer a set of questions around order- and SKU profile:

**- What conclusions can we draw from order- and SKU-profile?**

**- Impacts of Olist's business model on inventory and fullfillment process**

**- Can we predict buying behaviour between articles (association)?**

### libraries:
- python
- numpy
- pandas
- datetime
- matplotlib
- seaborn
- apyori

## Data <a name="data"></a>
The provided data set consists of historical order data from 2016 to 2018 and contains 100,000 orders. There are 8 files available. The below data model displays high level the references between these data- and lookup tables. The data was generously provided by Olist under the license CC BY-NC-SA 4.0 and can be found *[here](https://www.kaggle.com/olistbr/brazilian-ecommerce)* in Kaggle.

![Data Structure](https://i.imgur.com/HRhd2Y0.png)
*Data model as provided in Kaggle*

There is also a prepared dataset (df_orders_consolidated.csv) available as an output of the initial Olist E-commerce Data Analysis:

![ERD1](https://github.com/LarsTinnefeld/olist_ecom_analysis/blob/main/Olist-Analysis_1_New_tables.PNG?raw=true)

For the current analysis following data files are used:
- df_orders_consolidated.csv
- olist_customers_dataset.csv
- olist_products_dataset.csv

`df_orders_consolidated.csv`: Data table with order which was generated in the previous analysis

| # |  Column | Non-Null Count | Dtype | Content |
| --- | --- | --- | --- | --- |
| 0 | Unnamed | 102425 | int64 | --- |
| 1 | order_id | 102425 | object | Unique order identifier |
| 2 | customer_id | 102425 | object | Order-specific customer identifier |
| 3 | order_status | 102425 | object | Latest status of the order |
| 4 | order_purchase_timestamp | 102425 | object | Date of purchase |
| 5 | order_approved_at | 102425 | object | Date of order approval |
| 6 | order_delivered_carrier_date | 102425 | object | Date when shipped to carrier |
| 7 | order_delivered_customer_date | 102425 | object | Date of delivery to customer |
| 8 | order_estimated_delivery_date | 102425 | object | Estimated delivery date |
| 9 | order_time | 102425 | object | Time of day of order entry |
| 10 | delivery_time | 102425 | object | Time of day of delivery |
| 11 | date_ordinal | 102425 | int64 | Ordinal format of order date |
| 12 | shipping_time_delta | 102425 | int64 | Difference between estimated- and true shipping duration |
| 13 | shipping_duration | 102425 | int64 | (True) Shipping duration |
| 14 | estimated_duration | 102425 | int64 | Estimated shipping duration |
| 15 | product_id | 102425 | object | Unique prodcut identifier (SKU) |
| 16 | qty | 102425 | int64 | Order quantity |
| 17 | seller_id | 102425 | object | Unique seller identification |
| 18 | shipping_limit_date | 102425 | object | Shipping limit date |
| 19 | price | 102425 | float64 | Product unit price |
| 20 | freight_value | 100965 | float64 | Cost of shipping |
| 21 | product_category_name | 100965 | object | Product category |
| 22 | product_name_lenght | 100965 | float64 | Length of product name |
| 23 | product_description_lenght | 100965 | float64 | Product name |
| 24 | product_photos_qty | 100965 | float64 | Number of product photos |
| 25 | product_weight_g | 102425 | float64 | Product weight in gramms |
| 26 | product_length_cm | 102425 | float64 | Product length in cm |
| 27 | product_height_cm | 102425 | float64 | Prodcut height in cm |
| 28 | product_width_cm | 102425 | float64 | Prodcut width in cm |
| 29 | order_line_cube_in_ltr | 102425 | float64 | Volume (cube) of order line in liters |
| 30 | price_round | 102425 | float64 | Rounded product price |
| 31 | customer_unique_id | 102425 | float64 | Unique customer identification |

`olist_customers_dataset.csv`: Lookup table which contains all customers

| # |  Column | Non-Null Count | Dtype | Content |
| --- | --- | --- | --- | --- |
| 0 | customer_id | 99441 | object | Customer key for referencing or order table |
| 1 | customer_unique_id | 99441 | object | Unique customer identifier |
| 2 | customer_zip_code_prefix | 99441 | int64 | Customer zip code  |
| 3 | customer_city | 99441 | object | Customer city |
| 4 | customer_state | 99441 | object | Customer state |


`olist_customers_dataset.csv`: Lookup table which contains all customers

| # |  Column | Non-Null Count | Dtype | Content |
| --- | --- | --- | --- | --- |
| 0 | product_id | 99441 | object | Customer key for referencing or order table |
| 1 | product_category_name | 100965 | object | Product category |
| 2 | product_name_lenght | 100965 | float64 | Length of product name |
| 3 | product_description_lenght | 100965 | float64 | Product name |
| 4 | product_photos_qty | 100965 | float64 | Number of product photos |
| 5 | product_weight_g | 102425 | float64 | Product weight in gramms |
| 6 | product_length_cm | 102425 | float64 | Product length in cm |
| 7 | product_height_cm | 102425 | float64 | Prodcut height in cm |
| 8 | product_width_cm | 102425 | float64 | Prodcut width in cm |

## Data preparation <a name="preparation"></a>
The notebook "olist_order_profile" contains a complete procedure of data checks and cleaning. Applied verification methods:
- Data formats: Date columns were converted to datetime format
- Added unique customer id to order table

## Exploratory Data Analysis <a name="eda"></a>
Goal: getting insights around order composition and customer buying habits.

**Top customers:**

![Top customers](https://github.com/LarsTinnefeld/olist_ecom_analysis/blob/main/Images/Top_customers2.png?raw=true)

There are a few customers which come back to place orders again but given the large range of customers overall and average user is only placing a small amount or orders.

**Top categories:**

![Top categories](https://github.com/LarsTinnefeld/olist_ecom_analysis/blob/main/Images/Top_categories.png?raw=true)

There are 73 product categories in which the first third represent the majority of the order volume.

**Matrix factorization to find category similarities**

Matrix factorization is used in a small function with the goal to calculate distance (similarity) between categories. The method is based on comparing all ordered product categories in an order to all other orders. The greater the overlap between the orders the greater the similarity. This method is also used in recommender functions to identify similar customers based on the shopping history.

![Similar categories](https://github.com/LarsTinnefeld/olist_ecom_analysis/blob/main/Images/Similar_categories.PNG?raw=true)

## Order profile analysis <a name="order_analysis"></a>
Question to answer:

**What conclusions can we draw from the order- and SKU-profile?**

**Impacts of Olist business model on inventory and fullfillment process**

**Order profile:**

![Order profile](https://github.com/LarsTinnefeld/olist_ecom_analysis/blob/main/Images/Order_profile.png?raw=true)

The orders are generally small, as expected for e-commerce. Very few orders have more than one SKU. This already tells that an Market Basket Analysis will not produce a lot of results, if any. 79% SIO (single-item-orders), 93% SLO (single-line-orders).

**Pareto chart:**

![Pareto](https://github.com/LarsTinnefeld/olist_ecom_analysis/blob/main/Images/Pareto_revenue.png?raw=true)

The pareto chart shows almost the typically expected 80/20 profile. That means, there is a good distinction between the product's velocities. Under under circumstances this would be a base for a clever product allocation to different pick methods and technilogies in a warehouse.

**SKU classification:**

![Pareto](https://github.com/LarsTinnefeld/olist_ecom_analysis/blob/main/Images/SKU_classes.png?raw=true)

The ABC classes explain how frequently an item was picked in the observed time period. It shows that that there is no SKU ranked as X-mover and only some very few as Y. This is an extreme instance and shows that the SKUs are in general very infrequently picked. Even the faster moving SKUs are very infrequently sold which can mean a range of things:
1) That product is highly seasonal
2) There was a promotion event for these products
3) These SKUs were a sold out batch without re-ordering

## Affinity analysis <a name="affinity"></a>
Question to answer:

**Can we predict buying behaviour between articles in one order (association)?**

![affinity](https://miro.medium.com/max/1067/1*--iUPe_DtzKdongjqZ2lOg.png)

*Source: A Gentle Introduction on Market Basket Analysis — Association Rules (Susan Li)*

Due to the very small order sizes the method is first applied to the product categoy. A filter was applied to only extract the orders which contained more than one product. These orders were then converted to an order-category matrix, which was in turn than converted into the list form the `apyori` model is using as input.

**Result:**

We only found 11 relationships. On top, we only worked with categories. Going one level more detailed (products) would be most likely result in no findings. The small order sizes and the low pick frequency which we could observe in the order profile is also show their impact in this Affinity Analysis.

There is no association between the products. Reasons:
- Very low pick frequency
- Large product range
- Small orders

This is not a lot and not a good base to deepen the efforts to extract information with this method.

## Conclusions <a name="conclusion"></a>

**- What conclusions can we draw from order- and SKU-profile?**
- Orders sizes are very small: SIO is 79%, MLO is 93%
- The parato curve is steep, in the range of 75/20 to 80/20, which means a pronounced defferentiation between fast- and slow movers
- SKUs are picked extremely infrequently, with almost 100% Z-movers

**- Impacts of Olist's business model on inventory and fullfillment process**
- With this XYZ-ABC profile any inventory would not make much sense
- Because of the infrequent picks, batching SIOs would not work

**- Can we predict buying behaviour between articles (association)?**
- We can calculate similarity between product classes based on appearance in historical order data
- Because of the small order sizes, a large product range and a very low pick frequency we can not draw good conclusions about product assiciation.

## Conclusions <a name="conclusion"></a>

**[Data in Kaggle](https://www.kaggle.com/olistbr/brazilian-ecommerce)**

Add link for blog post here
