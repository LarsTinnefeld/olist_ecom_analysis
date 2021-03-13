# Customer segmentation
An order profile analysis of Olist's dataset

**Lars Tinnefeld**, 2021-03-27

![segments](https://images.unsplash.com/photo-1521104846606-f05901fc8aa7?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80)

*Image: [CHUTTERSNAP](https://unsplash.com/@chuttersnap) on Unsplash*

## Table of content
1. [Market Segmentation](#business_understanding)
2. [Objectives](#objectives)
3. [Data](#data)
4. [Data preparation](#preparation)
5. [Exploratory data analysis](#eda)
6. [Customer Segmentation](#segmentation)
7. [Geodemographic Segmentation](#geosegmentation)
8. [RFM Analysis](#rfm)
9. [K Means Clustering](#kmeans)
10. [Conclusion](#conclusion)
11. [References and links](#references)

## Market Segmentation <a name="business_understanding"></a>
For the decision making process for the business development in general, and potentially for the logistic strategy specifically,  an understanding of the customer behaviour and geographic conditions need to be analyzed. By extracting commonly shared demographic- and geodemographic characteristics methods are used to divide customers into groups (segments). This allows to apply tailor-made strategies that can target specific customer segments in a more effective way.

## Objectives <a name="objectives"></a>
The analysis in this repository is looking into the customer's buying behaviour as well as their locations. By doing so a few quesions will be answered:

- **Demographic relationship between customers**

- **Geographic relationship in view of customer characteristics**

- **Strategy to target specific customer segments**

- **What are the conclusions for the logistic process?**

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
- olist_geolocation_dataset.csv

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
| 0 | product_id | 99441 | object | Customer key for referencing or order table |
| 1 | product_category_name | 100965 | object | Product category |
| 2 | product_name_lenght | 100965 | float64 | Length of product name |
| 3 | product_description_lenght | 100965 | float64 | Product name |
| 4 | product_photos_qty | 100965 | float64 | Number of product photos |
| 5 | product_weight_g | 102425 | float64 | Product weight in gramms |
| 6 | product_length_cm | 102425 | float64 | Product length in cm |
| 7 | product_height_cm | 102425 | float64 | Prodcut height in cm |
| 8 | product_width_cm | 102425 | float64 | Prodcut width in cm |

`olist_customers_dataset.csv`: Data table that lists zip code prefix along with longitude and latitude, city and state

| # |  Column | Non-Null Count | Dtype | Content |
| --- | --- | --- | --- | --- |
| 0 | geolocation_zip_code_prefix | 1000163 | int64 | Zip code prefix for a neighborhood |
| 1 | geolocation_lat | 1000163 | float64 | Latitude |
| 2 | geolocation_lng | 1000163 | float64 | Longitude |
| 3 | geolocation_city | 1000163 | object | City name |
| 4 | geolocation_state | 1000163 | object | State name |

## Data preparation <a name="preparation"></a>
The notebooks contain a complete procedure of data checks and cleaning. Applied verification methods:
- Data formats: Date columns were converted to datetime format
- Check for nan values and duplicates
- Zip code - coordinates (latitude and longitude) are not unique. An average coordinate was developed to have a defined lookup value when matching with customer (key label is zip code prefix).

## Exploratory Data Analysis <a name="eda"></a>
Goal: The focus is on getting an understanding about the customer's buying habits and their locations.

**Where are the customers from?**

Customers live in 4,119 unique cities in 27 unique states.

![Top cities](https://github.com/LarsTinnefeld/olist_ecom_analysis/blob/main/Images/Top_50_cities.png?raw=true)

![Top states](https://github.com/LarsTinnefeld/olist_ecom_analysis/blob/main/Images/Top_50_states.png?raw=true)

The imbalanced distribution accross cities and states need to be kept in mind when drawing conclusions of statistical nature.

![Top states](https://github.com/LarsTinnefeld/olist_ecom_analysis/blob/main/Images/Top_50_states.png?raw=true)
