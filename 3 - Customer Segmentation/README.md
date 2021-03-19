# Customer segmentation
A project of the Olist ecommerce business analysis

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
9. [K-Means Clustering](#kmeans)
10. [Conclusion](#conclusion)
11. [References and links](#references)

---
## Market Segmentation <a name="business_understanding"></a>
For the decision making process in business development in general, and potentially for the logistic strategy specifically,  an understanding of the customer behaviour and geographic conditions need to be analyzed. By extracting commonly shared demographic- and geodemographic characteristics methods are used to divide customers into groups (segments). This allows to apply tailor-made strategies that can target specific customer segments in a more effective way.

---
## Objectives <a name="objectives"></a>
The analysis in this repository is looking into the customer's buying behaviour as well as their locations. Three different approaches to segment customers is presented: Customer Segmentation, RFM Analysis and K-Means Clustering. By doing so a few quesions will be answered:

- **Demographic relationship between customers**

- **Geographic relationship in view of customer characteristics**

- **Strategy to target specific customer segments**

- **What are the conclusions for the logistic process?**

### libraries:
- python
- numpy
- pandas
- datetime
- re
- sklearn
- matplotlib
- seaborn
- plotly
- waffle

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

The bright red dots represent the `active-high` sub-segment. The color shifts to the cold- and inactive segments in the blue colors. With exception of a few pockets, there's a relatively evenly disctibution of the sub-segments accross the East of Brazil.

![Geo Subsegments](https://github.com/LarsTinnefeld/olist_ecom_analysis/blob/main/Images/Geo_subsegments_biggest_zip.PNG?raw=true)

As expected the highest concentration of customers is around major cities which can be explained by living density. The three biggest zip code prefix communities are around Rio de Janeiro.

**Distribution according total revenue**

![Geo Revenue](https://github.com/LarsTinnefeld/olist_ecom_analysis/blob/main/Images/Geo_totrev_200_1000.PNG?raw=true)

![Geo Renenue Zoom](https://github.com/LarsTinnefeld/olist_ecom_analysis/blob/main/Images/Geo_totrev_1000_3000_zoom.PNG?raw=true)

The chart shows that there is some clustering between higher revenue and lower revenue areas, especially if setting the lower bound threshold higher. In neighborhoods of "Campinas" mostly higher total values while in the suburbs "Vila Amelia", "Brasilandia" and "Limao District" mostly lower values dominate. Rio de Janeiro, especially around the waterfront is mostly red (high revenue), while the north-western suburbs are mainly blue (low revenue).

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

By adjusting the lower- and uppder band of the color scale it can be seen that there's a general tendency of lower purchase prices in the South of Brazil while higher purchase prices are more existing in the North. The effect is not very pronounced but still visible. A significance test to statistically prove that this difference has sufficient evindence would need to be done in case this will be considered important in the final business case.

The general disctribution of individual purchase values averaged accross zip codes:

![Avg Purch Dist](https://github.com/LarsTinnefeld/olist_ecom_analysis/blob/main/Images/Avg_purchvalue_dist_zipcode.png?raw=true)

Above chart shows the average purchase value distribution, averaged over zip codes. It shows a right-skewed distribution with the majority of the purchase values in the range of 100-120. This seems also to be in line with the general product cost distribution (reference EDA analysis in "Olist Business Trend Analysis").

**Conclusion: Geographic relationship in view of customer characteristics**
- There is not a clear correlation between location and customer sub-segment.
- Along the cost line of Rio de Janeiro are the biggest communities, which also falls in line with areas of high revenue. On the other hand, Sao Paulo has, by a big margin, the biggest overall customer count. This is an important conclusion for logistics and supply chain.
- Some level of clustering in view of higher- and lower total reveny can be seen. This might for a big part be the effect of the group sizes. Geographical clusters of high revenue are "Campinas" and the south east of Rio de Janeiro.
- There seem to be a slightly higher general purchase price in the north of Brazil when looking at the level of individual customers. A statistical test to validate this statement would need to be performed before basing any decisions on this.

---
## RFM Analysis <a name="rfm"></a>
**Strategy to target specific customer segments**

The RFM analysis is another way to segment customers in order to develop marketing strategies. The three used metrics `Recency`, `Frequency` amd `Monetary` lead to a combined individual classification. With this classification also an appropriate proposed marketing strategy will be developed. The number of the sub-segments which is created in this process is arbitrary and might not be in line with an underlying clustering as it appears in the data. To address this, also **K-Means Clustering** is applied to extract clusters from non-labeled data. The features used as inputs are the same as used for the RFM analysis.

**Recency**

Recency is the time duration from the last order to the reference date (last order date in data set in our case).

![Recency](https://github.com/LarsTinnefeld/olist_ecom_analysis/blob/main/Images/Recency.png?raw=true)

This chart makes sense because we see that there is the spike at round about 270 days before the reference day. That falls in the time period of the heavy Black Friday sales event where a lot of customers placed their latest order.

![Frequency](https://github.com/LarsTinnefeld/olist_ecom_analysis/blob/main/Images/Frequency.png?raw=true)

This is in line with what we have seen in the order profile analysis. There are many customers which only placed one order. As hinted in the initial "Business Trend Analysis", the error which many will likely get trapped is by simply applying `count of order_id` during grouping by customer_unique_id. Reason why this leads to a wrong result:
- Quantity in the original order table is created by number of rows (order quantity = 4 means 4 rows of data)
- Two SKUs (products) means two separate rows in the data table

=> If we group by user "X" whose order contains procuct "A" with quantity 2 and procuct "B" with quantity 1, we will get 3 as count for this customer while in reality only one single order was placed.

**Monetary**

Monetary is basically the cumulated purchase amount a customer as spent.

![Monetary](https://github.com/LarsTinnefeld/olist_ecom_analysis/blob/main/Images/Monetary.png?raw=true)

As also seen in the "Market Trend Analysis", most of the purchases are on the low side (under 100) of the distribution.

In step one of the RFM segment process each of the labels `Recency`, `Frequency` and `Monetary` is individually calculated per customer. In step two, two metrics are developed:
1. RFM score: A calculated value with is the product of the three scores (R-score * F-score * M-score)
2. RFM segment label: A number code with is created by combining the three scoces in a row (R-scoreF-scoreM-score)
In step three filter conditions based on the two metrics for customer types are defined. The segmentation process in this analysis is dealing with 7 customer types:
- Best Customer
- Big Spender
- Loyalist
- Potential Loyalist
- Hibernating
- Almost Lost
- Lost Customer

![Waffle RFM](https://github.com/LarsTinnefeld/olist_ecom_analysis/blob/main/Images/Waffle_RFM.png?raw=true)

Based on the observed customer behaviour the appropriate marketing strategy added to a summarized list.

| RFM Segment |  Count | Recency | Frequency | Monetary | Marketing Strategy |
| --- | --- | --- | --- | --- | --- | 
| Best customer | 6,552 | 66.6 | 1.2 | 356.4 | Personalized communication, offer loyalty program, no promotional offers needed |
| Big Spender | 5,715 | 172.9 | 1.1 | 346.3 | Make them feel valued and offer quality products, encourage to stick with brands |
| Loyalist | 1,132 | 290.9 | 2.1 | 173.4 | Offer loyalty program |
| Potential Loyalists | 51,001 | 184.2 | 1.0 | 136.7 | Recommend products and offer discounts |
| Hibernating | 5,803 | 446.5 | 1.0 | 64.8 | Make great offers with big discounts |
| Almost Lost | 11,581 | 360.9 | 1.0 | 88.8 | Try to win them with limited sales promotions |
| Lost Customer | 11,574 | 367.6 | 1.0 | 29.0 | Do not spent much effort and money to win them |

**Conclusion: Strategy to target specific customer segments**
- The order frequency and order amounts are concentrated on the lower end. This is what we have repeatedly have seen before.
- The biggest RFM segment is the group of `Potential Loyalists`. These are customers that need to be targeted with offers and discounts in order to make the business successful. If Olist manages to do a good job by winning the majority of this sub-segment it would make a big impact in growth.
- There is a good base of `Best Customers`, which is good news for the business.
- Some effort needs to be spent to target `hibernating` customers and customers which are `almost lost`

---
## K-Means Clustering <a name="kmeans"></a>
**Evaluation of the applied RFM segmentation by comparison with ML clustering method**

K-Means Clustering is a method that supports identifying clusters in unlabeled data. Sklearns K-means algorithm is applied to find underlying segments that are different from the aribrarily chosen RFM classes. This will provide a different angle of view and confidence level on the above performed segmentation.

Before the data is processed a scatter plot often helps to identify custering in a visual way already beforehand. The current analysis is dealing with three features which can still be visualized in a 3D scatter plot.

![RFM Scatter](https://github.com/LarsTinnefeld/olist_ecom_analysis/blob/main/Images/RFM_scatter_3d.png?raw=true)
<img src="https://github.com/LarsTinnefeld/olist_ecom_analysis/blob/main/Images/RFM_scatter_3d_2.png" width=400 height=257>

The above scatter plot shows a zoomed view in order to get a clearer picture without the outliers. Obviously, the major segmentation factor in this plot is generated by the purchase frequency. Apart from this and the small cluster of very early customers (in the range of 700 days Recency), there is not a clear segmentation to observe.

The SSE (Sum of Squared Errors) in K-Means Clustering is depending on the number of selected clusters. The goal is to select a number of clusters that is as small as possible, but one that still archives a significant improvemet if fitting the data. The process is known as "Elbow Method".

A range of 1 to 10 clusters is used to calculate the resulting SSE.

![Elbow method](https://github.com/LarsTinnefeld/olist_ecom_analysis/blob/main/Images/Elbow_method.png?raw=true)

The chart shows that a cluster number of 4 is a good choice. When K-Means is applied for 4 clusters we can see where the borders were defined. The summary table and the pie charts below visualize the new clustering.

| K-Means Cluster |  Recency | Frequency | Monetary | Count | Customer Description |
| --- | --- | --- | --- | --- | --- | 
| 0 | 127.8 | 1.0 | 113.4 | 50,832 | New Low-Spenders |
| 1 | 219.9 | 2.1 | 243.2 | 2,774 | Loyalists |
| 2 | 387.2 | 1.0 | 114.1 | 37,566 | Hibernating Low-Spenders |
| 3 | 237.1 | 1.0 | 1142.7 | 2,186 | Big Spenders |

<img src="https://github.com/LarsTinnefeld/olist_ecom_analysis/blob/main/Images/K_means_customers.png?raw=true" width=300 height=300><img src="https://github.com/LarsTinnefeld/olist_ecom_analysis/blob/main/Images/K_means_revenue.png?raw=true" width=300 height=300><img src="https://github.com/LarsTinnefeld/olist_ecom_analysis/blob/main/Images/K_means_recency.png?raw=true" width=300 height=300>

The Big Spenders are a small portion of the customers, but the revenue impact is very high. It is essential to make these customers feel valued. Encourage them to stick with their brands. New Low Spenders are the biggest group but show a relatively small revenue. For the growth of the business it is important to spend great effort in these customers in order to turn them into Loyalists or Big Spenders.

The relation of these clusters to each other can be visualized in the 3D scatter plot.

<img src="https://github.com/LarsTinnefeld/olist_ecom_analysis/blob/main/Images/KMeans_scatter_3d.png?raw=true" width=450 height=270>   <img src="https://github.com/LarsTinnefeld/olist_ecom_analysis/blob/main/Images/KMeans_scatter_3d_zoom.png?raw=true" width=450 height=270>

It now would be interesting to see if there is a geological relationship for these new classes.

<img src="https://github.com/LarsTinnefeld/olist_ecom_analysis/blob/main/Images/Geo_kmeans_customers.PNG?raw=true">

There is no general tendency to observe when looking at Brazil in total. Taking a closer look at the major cities reveals local clustering.

<img src="https://github.com/LarsTinnefeld/olist_ecom_analysis/blob/main/Images/Geo_kmeans_zoom.PNG?raw=true" width=300 height=154><img src="https://github.com/LarsTinnefeld/olist_ecom_analysis/blob/main/Images/Geo_kmeans_saopaulo.PNG?raw=true" width=300 height=154><img src="https://github.com/LarsTinnefeld/olist_ecom_analysis/blob/main/Images/Geo_kmeans_riodejaneira.PNG?raw=true" width=300 height=154>

The color coding shows that a big portion of Sao Paulo's neighbohoods are `Hibernating Low-Spenders`. Compared to this, it appears that Rio de Janeiro has more `New Low-Spenders`. There is no clearly visible concentration of the important segment `Big Spenders` to see when scanning over Brazil.

---
## Conclusion <a name="conclusion"></a>
### Demographic relationship between customers
The shared message between the different segmentation methods is that there is a small group of high spending customers that is essential to maintain as it is representing a significant portion of the revenue, and a relatively large group of customers which have the potential to impact Olist's future business. A very small segment can be called "Loyalists" based on multiple orders placed.

Order frequency in this order dataset is in general low with a high concentration in just above one order placed. Based on this, the definition of "inactive" is a very sensitive metric which can swing quickly based on where thresholds are set. The customer segmentation and the RMF in the initial part of the analysis did not work with normalized data and show a smaller portion of "inactive", "hibernating" and "lost" customers. K-Menas Clustering worked with normalized data and came up with only 4 customer clusters, in which "Hibernating Low-Spenders" are 40% of all customers.

### Geographic relationship in view of customer characteristics
There is a big imbalance in regards to where the customers live. Most of the customers live in Sau Paulo by a big margin. This must have an impact for statistical validations and also for decisions which target business development.

The geological distribution of the defined RFM segments across Brazil appears random. The K-Means segments on the other hand indicate some local clustering which could further be validated with statistical methods. In this view, big parts of Sao Paulo show "Hibernating Low-Spenders" while bigger portions of Rio de Janeiro show "New Low-Spenders". In terms of cumulated revenue there is also some local clustering to observe. The south-east of Rio de Janeiro and "Campinas" show a greater density of higher cumulated revenue. It is likely that this is impacetd by residential density which is confirmed when looking at individual total value. The colors which indicate average individual purchase value in the map show that there could be a tendency that northern parts of Brazil spend more on their purchase. Also this observation needs to be statistically validated.

### Strategy to target specific customer segments
Along with the segmentation of customers a table with marketing strategies is available. The recommendations in this table also need to be seen in the light of the segment's importance for the business. As mentionioned above, "High Spenders" and the big group of "Potential Loyalists" (or "New Low-Spenders") have a high importance. Their marketing strategy has therefore a higher priority.

### What are the conclusions for the logistic process?
As seen in the initial **Olist Business Trend Analysis**, shipping time is varying and has some correlation with product cost. While the correlation between shipping duration and customer satisfaction is still to be investigated, it can be concluded from the above geodemographis analysis that some areas have a higher relevance. When including `direct shipping` vs. `drop shippment` in the business development planning, we can think about **micro fullfillment facilities** close to dense areas. These facilities would be part of a hybrid concept in which the "hot" product groups `Health & Beauty`, `Gift Watches` and `Information Accessories` (compare to Business Trend Analysis) would be logistically incorporated to archive an effective supply chain for the very important `High Spenders` and `Loyalist` segment. The small product size of this product group allows to maintain a small facility footprint which helps to facilitate the warehouse process and to keep the investment cost low. A bigger portion of this hybrid business would still be executed via **drop ship** as it operates today. This helps to serve a the large group of `Potential Loyalists` (or `New Low-Spenders`) more effectively.

### Next steps
The analysis in this part of the project is a reflection of how consumers react to what and how Olist is offering. After seeing the customer behaviour, along with some demographic and geodemographic background, it is now important to also understand which improvements would enhance satisfaction and increase consumer attraction. This is one of the key objectives of the business case analysis and would be the logical next step. The objective can be archived by analyzing data from the customer satisfaction report, and also finding a way to recommend products in an effective way.

---
## References and links <a name="references"></a>

**[Data in Kaggle](https://www.kaggle.com/olistbr/brazilian-ecommerce)**

**[Blog post in Medium](https://larstinnefeld.medium.com/customer-segmentation-of-a-brazilian-e-commerce-business-c6dae31a7861)**
