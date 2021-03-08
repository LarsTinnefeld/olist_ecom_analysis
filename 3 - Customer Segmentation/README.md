# Olist customer segmentation
An order profile analysis of Olist's dataset

**Lars Tinnefeld**, 2021-03-27

![segments](https://images.unsplash.com/photo-1521104846606-f05901fc8aa7?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80)

*Image: [CHUTTERSNAP](https://unsplash.com/@chuttersnap) on Unsplash*

## Table of content
1. [Clustering data](#business_understanding)
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

## Clustering <a name="business_understanding"></a>
...

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

