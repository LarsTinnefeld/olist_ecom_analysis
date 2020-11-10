# Olist eCommerce Data Analysis

**Lars Tinnefeld**, 2020-11-16

![portrait](https://images.unsplash.com/photo-1522204523234-8729aa6e3d5f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80)

## Objectives
The ultimate goal of the work in this notebook is to extract meaningful information from a set of data- and lookup tables from Olist, a Brazilian e-commerce department store (SaaS). *Meaningful* in this context means adequate to serve as a base for beneficial data driven decision making. Beside identifying contributors to customer satisfaction and trends, a hypothetical extension of the business service will be reviewed. This new service consists of warehousing and logistics of the shopkeeper's products. The analysis will therefore be focussed on three points of attention:
- Trends in the business development and a prognosis where the business is headed
- Main contributors to user satisfaction and a model with allows to predict the impact of changes
- An initial analysis of the product characteristics and SKU profile to identify qualification for a logistic process

## About Olist
Olist is for everyone "who wants to sell more and better" and "who wants to attract new customers". As a SaaS business in the e-commerce sector, Olist is a online selling platform for small businesses. On Olist's sign-up page a range of shopkeeper profiles is listed which fits the business model. Clearly, a strong focus is on attracting more customers.

## The data
The provided data set consists of historical order data from 2016 to 2018 and contains 100,000 orders. There are 8 files available. The below data model displays high level the references between these data- and lookup tables. The data was generously provided by Olist under the license CC BY-NC-SA 4.0 and can be found *[here](https://www.kaggle.com/olistbr/brazilian-ecommerce)* in Kaggle.

![Data Structure](https://i.imgur.com/HRhd2Y0.png)
*Data model as provided in Kaggle*

