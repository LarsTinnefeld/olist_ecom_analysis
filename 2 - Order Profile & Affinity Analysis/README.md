# Olist e-commerce order profile analysis
An order profile analysis of Olist's dataset

![Hero_picture](https://cdn.pixabay.com/photo/2016/03/23/07/57/receipt-1274307_960_720.jpg)

## Table of content
1. [Order profile analysis](#business_understanding)
2. [Objectives](#objectives)
3. [Approach](#approach)
4. [Data](#data)
5. [Data preparation](#preparation)
6. [Data Modelling](#modelling)
7. [Evaluation](#evaluation)
8. [References and links](#references)

## Order Profile Analysis <a name="business_understanding"></a>
Gaining an understanding about key metrtrics, correlations and patterns of the business is one of the most important steps in developing a successcul warehouse- and logistic concept. Ecommerce proves to be a very challenging business field in that aspect thanks to the dynamics and often unpredictable day-to-day developments. There is a range of "traditional" analysis outputs which provide an experienced logistics specialist with insights into the business: Pareto diagram, ABC classification, XYZ classification, Units-per-order distribution, Lines-per-order distribution, category breakdown. These are important metrics because they directly impact warehouse concept and sizing. Beside this, it is in many cases useful to understand the data in a bigger context, often including the characteristics of users and their shopping choices. "Market Baset Analysis" and "Product Correlation" help to disclose information in this aspect and support experts to make better decisions.

## Objectives <a name="objectives"></a>
The analysis in this repository will follow above mentioned pattern in order to answer a set of questions around order- and SKU profile:

**- What conclusions can we draw from order- and SKU-profile?**

**- Impacts of Olist's business model on inventory and fullfillment process**

**- Can we predict buying behaviour between articles (association)?**


## Approach <a name="approach"></a>
Following steps will be followed:

- Data import and wranglig if required
- Exploratory data analyis, aimed at products and orders
- Order- and SKU profile analysis
- Affinity analysis


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
| 0 | customer_id | 99441 | object | Customer key for referencing or order table |
| 1 | customer_unique_id | 99441 | object | Unique customer identifier |
| 2 | customer_zip_code_prefix | 99441 | int64 | Customer zip code  |
| 3 | customer_city | 99441 | object | Customer city |
| 4 | customer_state | 99441 | object | Customer state |



## Data preparation <a name="preparation"></a>
The notebook "olist_analysis" contains a complete procedure of data checks and cleaning. Applied verification methods:
- Missing data check: 3% missing data were substituted with forward fill, 0.05% of missing SKU dimensions were substitured with mean
- Duplicate records: No duplicates found
- Data formats: Date columns were converted to datetime format

Following data tables were constructed to perform the analysis:
- df_order_items_consolidated (merging of the three original tables)
- df_orders_daily (grouping by date)






