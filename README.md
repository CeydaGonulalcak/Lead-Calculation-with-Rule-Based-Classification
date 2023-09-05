# Lead-Calculation-with-Rule-Based-Classification
This project aims to analyze the Persona.csv dataset, which contains the prices of the products sold by an international game company and some demographic information of the users who buy these products.

# Business Problem

A game company uses some of the characteristics of its customers
level based new customer definitions (persona)
and create segments according to these new customer definitions
and according to these segments, we create new customers
estimate how much the company can earn on average
wants.

For example:
A 25-year-old male IOS user from Turkey
determine how much the user can earn on average
is requested.


# Dataset Story

The Persona.csv dataset contains the prices of products sold by an international gaming company and the prices of these products.
Contains some demographic information of the users who purchased the products. Data
set consists of the records generated in each sales transaction. This means
The table is unduplicated. In other words, a person with certain demographic characteristics
the user may have made more than one purchase.

# Variables
* Price: Customer's spending amount
* Source: The type of device the customer is connecting to
* Sex: Gender of the client
*  Country: Country of the customer
* Age: Customer's age


# Pre-implementation Data Set:
  
|PRICE    |SOURCE    |SEX    |COUNTRY    |AGE    |
|:--------|:---------|:------|:----------|:------|
|39| android| male| bra| 17|
|39| android| male| bra| 17|
|49| android| male| bra| 17|
|29| android| male| tur| 17|
|49| android| male| tur| 17|


# Targeted output :

|customers_level_based    |PRICE    |SEGMENT   |
|:-----------------------|:----------|:------|
|BRA_ANDROID_FEMALE_0_18| 35.6453| B|
|BRA_ANDROID_FEMALE_19_23| 34.0773| C|
|BRA_ANDROID_FEMALE_24_30| 33.8639| C|
|BRA_ANDROID_FEMALE_31_40| 34.8983| B|
|BRA_ANDROID_FEMALE_41_66| 36.7371| A|


