# Olist customer segmentation
An order profile analysis of Olist's dataset

**Lars Tinnefeld**, 2021-03-27

![segments](https://images.unsplash.com/photo-1521104846606-f05901fc8aa7?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80)

*Image: [CHUTTERSNAP](https://unsplash.com/@chuttersnap) on Unsplash*

## Table of content
1. [Market Segmentation](#business_understanding)
2. [Objectives](#objectives)
3. [Approach](#approach)
4. [Data](#data)
5. [Data preparation](#preparation)
6. [Exploratory data analysis](#eda)
7. [Customer Segmentation](#segmentation)
8. [Geodemographic Segmentation](#geosegmentation)
9. [RFM Analysis](#rfm)
10. [K Means Clustering](#kmeans)
11. [Conclusion](#conclusion)
12. [References and links](#references)

## Market Segmentation <a name="business_understanding"></a>
For the decision making process for the business development in general, and potentially for the logistic strategy specifically,  an understanding of the customer behaviour and geographic conditions need to be analyzed. By extracting commonly shared demographic- and geodemographic characteristics methods are used to divide customers into groups (segments). This allows to apply tailor-made strategies that can target specific customer segments in a more effective way.

## Objectives <a name="objectives"></a>
The analysis in this repository is looking into the customer's buying behaviour as well as their locations. By doing so a few quesions will be answered:

- **Demographic relationship between customers**

- **Geographic relationship in view of customer characteristics**

- **Strategy to target specific customer segments**

- **What are the conclusions for the logistic process?**

## Approach <a name="approach"></a>
Following steps will be followed:

- Data import and wranglig if required
- Exploratory data analyis, aimed at products and orders
- Order- and SKU profile analysis
- Affinity analysis

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
...

## Data preparation <a name="preparation"></a>
The notebook "olist_order_profile" contains a complete procedure of data checks and cleaning. Applied verification methods:
- Data formats: Date columns were converted to datetime format
...


## Exploratory Data Analysis <a name="eda"></a>
Goal: The focus is on getting an understanding about the customer's buying habits and their locations.

**Where are the customers from?**

![Top cities](https://github.com/LarsTinnefeld/olist_ecom_analysis/blob/main/Images/Top_50_cities.png?raw=true)

![Top states](https://github.com/LarsTinnefeld/olist_ecom_analysis/blob/main/Images/Top_50_states.png?raw=true)

