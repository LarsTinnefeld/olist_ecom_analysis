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

---
## Market Segmentation <a name="business_understanding"></a>
For the decision making process for the business development in general, and potentially for the logistic strategy specifically,  an understanding of the customer behaviour and geographic conditions need to be analyzed. By extracting commonly shared demographic- and geodemographic characteristics methods are used to divide customers into groups (segments). This allows to apply tailor-made strategies that can target specific customer segments in a more effective way.

---
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

---
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

---
## Data preparation <a name="preparation"></a>
The notebooks contain a complete procedure of data checks and cleaning. Applied verification methods:
- Data formats: Date columns were converted to datetime format
- Check for nan values and duplicates
- Zip code - coordinates (latitude and longitude) are not unique. An average coordinate was developed to have a defined lookup value when matching with customer (key label is zip code prefix).
- For the customer segmentation analysis only orders with status `delivered` were filtered

---
## Exploratory Data Analysis <a name="eda"></a>
Goal: The focus is on getting an understanding about the customer's buying habits and their locations.

**Where are the customers from?**

Customers live in 4,119 unique cities in 27 unique states.

![Top cities](https://github.com/LarsTinnefeld/olist_ecom_analysis/blob/main/Images/Top_50_cities.png?raw=true)

![Top states](https://github.com/LarsTinnefeld/olist_ecom_analysis/blob/main/Images/Top_states.png?raw=true)

The imbalanced distribution accross cities and states need to be kept in mind when drawing conclusions of statistical nature.

![Top zip codes](https://github.com/LarsTinnefeld/olist_ecom_analysis/blob/main/Images/Top_50_zip_codes.png?raw=true)

There are 14,994 unique zip code prefixes.

**When did customers join?**

The date of the first order is assumed to be the user sign-up date.

![Signup cum](https://github.com/LarsTinnefeld/olist_ecom_analysis/blob/main/Images/New_customers_cumulative.png?raw=true)

![Signup dly](https://github.com/LarsTinnefeld/olist_ecom_analysis/blob/main/Images/New_customers_daily.png?raw=true)

Many new cutomers appeared on Black Friday. It is interesting to see that the impact is not very pronounced when looking at the cumulative customer count for the total time span. Overall, the increase of customers has an upward trend. The trendline is slightly exponential, which means that the growth is accelerating slowly.

---
## Customer segmentation <a name="segmentation"></a>
**Demographic relationship between customers**

The segmentation will classify customers based on thre metrics:
- Date since last order was placed (`Recency`)
- Total money spent

The Recency segments are defined by dividing the total time period (oldest order to the newest order) in four periods. In that way we get the following classes:
- Inactive
- Cold
- Hot
- Active

In a second step the total purchase amount of a customer was sorted to either, higher than the median total purchase amount or lower. Doing so produces two classes:
- Low
- High

The two classes were combined for each customer to a sub-segment. The disctibution can be made visible in a tree map or waffle chart. The distribution can be reviewed accoring a range of different KPIs.

![Waffle revenue](https://github.com/LarsTinnefeld/olist_ecom_analysis/blob/main/Images/Waffle_revenue_subsegment.png?raw=true)

![Waffle orders](https://github.com/LarsTinnefeld/olist_ecom_analysis/blob/main/Images/Waffle_orders_subsegment.png?raw=true)

![Waffle customers](https://github.com/LarsTinnefeld/olist_ecom_analysis/blob/main/Images/Waffle_customers_subsegment.png?raw=true)

**Conclusion: Demographic relationship between customers**
- The strongest class of the 7 generated sub-segments is active customers with high spending, followed by "hot" customers which high spending, which is a good sign for the business.
- Active customers with high and low spending placed the most orders, followed by "hot" customers.
- Active customers are also the biggest groups in terms of head count.
- Inactive customers represent in each chart the smallest proportion.

---
## Geodemographic Segmentation <a name="geosegmentation"></a>
**Geographic relationship in view of customer characteristics**

As mentioned above, there is no direct link between the coordinates (logitude, latitude) and the customer, because the zip code prefix is not uniquely assigned to one specific coordinate, but a range which fall into the same neighborhood. In this way many customers fall onto the same coordinate. To deal with this, for each coordinate the majority class was calculated. In that way the unique zip code prefix is shown on the map with the color of the majority segment.

**Distribution of sub-sebments**

![Geo Subsegments](https://github.com/LarsTinnefeld/olist_ecom_analysis/blob/main/Images/Geo_subsegments.PNG?raw=true)

The bright red dots represent the `active-high` sub-segment. The color shifts to the cold- and inactive segments in the blue colors. With exception of a few pockets, there's a relatively evenly disctibution of the sub-segments accross the East of Brazil. As expected the highest concentration of customers is around major cities which can be explained by living density.

**Distribution according total revenue**

![Geo Revenue](https://github.com/LarsTinnefeld/olist_ecom_analysis/blob/main/Images/Geo_totrev_200_1000.PNG?raw=true)

![Geo Renenue Zoom](https://github.com/LarsTinnefeld/olist_ecom_analysis/blob/main/Images/Geo_totrev_1000_3000_zoom.PNG?raw=true)

The chart shows that there is some clustering between higher revenue and lower revenue areas, especially if setting the lower bound threshold higher. In neighborhoods of "Campinas" mostly higher total values while in the suburbs "Vila Amelia", "Brasilandia" and "Limao District" mostly lower values dominate. Rio de Janeiro, especially around the waterfront is mostly blue, while the north-western suburbs are mainly red.

Even so we can identify areas of higher interest for the business, we need to be careful with the interpretation on an individual level:

As seen in the EDA section, some zip codes have more customers assigned, so a high total value can be an effect of a big group size, and therefore a higher acumulated revenue.
As a refresher, a box chart to display the statistical distribution of the group sizes:

![Box chart zip code](https://github.com/LarsTinnefeld/olist_ecom_analysis/blob/main/Images/Zipcode_sizes_boxplot.png?raw=true)

To have the real distribution of the total revenue accross zip codes from another perspective:

![Dist revenue](https://github.com/LarsTinnefeld/olist_ecom_analysis/blob/main/Images/Tot_revenue_dist_zipcode.png?raw=true)

A big majority of neighborhoods is on the low end of the distribution when looking at the summarized revenue. This can have different reasons:
- Small group size
- Low purchase values
- a combination of the two

**Distribution according average purchase value**

The following visualization shows the distribution on an individual level, independent from the zize of a neighborhood.

![Geo Avg purch](https://github.com/LarsTinnefeld/olist_ecom_analysis/blob/main/Images/Geo_avgpurch_50_300.png?raw=true)

