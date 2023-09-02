#############################################################
# Calculating Return on Leads with Rule-Based Classification
#############################################################

#############################################
# PROJECT TASKS
#############################################

#############################################
# TASK 1: Answer the following questions.
#############################################

# Question 1: Read the persona.csv file and show general information about the dataset.
import pandas as pd
pd.set_option("display.max_rows", None)
df = pd.read_csv('Python 2/pythonProgramlama/python_for_data_science/data_analysis_with_python/datasets/persona.csv')
df.head()
df.shape
df.info()

# Question 2: How many unique SOURCEs are there? What is their frequency?
df["SOURCE"].nunique()
df["SOURCE"].value_counts()

# Question 3: How many unique PRICE are there?
df["PRICE"].nunique()

# Question 4: How many sales were realized from which PRICE?
df["PRICE"].value_counts()

# Question 5: How many sales were there from which country?
df["COUNTRY"].value_counts()
df.groupby("COUNTRY")["PRICE"].count()
df.pivot_table(values="PRICE",index="COUNTRY",aggfunc="count")

# Question 6: How much was earned from sales by country?
df.groupby("COUNTRY")["PRICE"].sum()
df.groupby("COUNTRY").agg({"PRICE": "sum"})
df.pivot_table(values="PRICE",index="COUNTRY",aggfunc="sum")

# Question 7: What is the number of sales by SOURCE types?
df["SOURCE"].value_counts()

# Question 8: What is the average PRICE by country?
df.groupby(by=['COUNTRY']).agg({"PRICE": "mean"})

# Question 9: What is the average PRICE by SOURCE?
df.groupby(by=['SOURCE']).agg({"PRICE": "mean"})

# Question 10: What are the PRICE averages in the COUNTRY-SOURCE breakdown?
df.groupby(by=["COUNTRY", 'SOURCE']).agg({"PRICE": "mean"})


#############################################
# TASK 2: What are the average earnings by COUNTRY, SOURCE, SEX, AGE?
#############################################

df.groupby(["COUNTRY", 'SOURCE', "SEX", "AGE"]).agg({"PRICE": "mean"}).head()


#############################################
# TASK 3: Sort the output by PRICE.
#############################################

agg_df = df.groupby(by=["COUNTRY", 'SOURCE', "SEX", "AGE"]).agg({"PRICE": "mean"}).sort_values("PRICE", ascending=False)
agg_df.head()


#############################################
# TASK 4: Convert the names in the index to variable names.
#############################################

agg_df = agg_df.reset_index()
agg_df.head()


#############################################
# TASK 5: Convert AGE into a categorical variable and add it to agg_df.
#############################################

bins = [0, 18, 23, 30, 40, agg_df["AGE"].max()]

mylabels = ['0_18', '19_23', '24_30', '31_40', '41_' + str(agg_df["AGE"].max())]

agg_df["age_cat"] = pd.cut(agg_df["AGE"], bins, labels=mylabels)
agg_df.head()

#############################################
# TASK 6: Define new level based customers and add them as variables to the data set.
#############################################

agg_df['customers_level_based'] = agg_df[['COUNTRY', 'SOURCE', 'SEX', 'age_cat']].agg(lambda x: '_'.join(x).upper(), axis=1)

agg_df["customers_level_based"] = ['_'.join(i).upper() for i in agg_df.drop(["AGE", "PRICE"], axis=1).values]

agg_df.columns

for row in agg_df.values:
    print(row)

[row[0].upper() + "_" + row[1].upper() + "_" + row[2].upper() + "_" + row[5].upper() for row in agg_df.values]

agg_df["customers_level_based"] = [row[0].upper() + "_" + row[1].upper() + "_" + row[2].upper() + "_" + row[5].upper() for row in agg_df.values]
agg_df.head()

agg_df = agg_df[["customers_level_based", "PRICE"]]
agg_df.head()

for i in agg_df["customers_level_based"].values:
    print(i.split("_"))

agg_df["customers_level_based"].value_counts()

agg_df = agg_df.groupby("customers_level_based").agg({"PRICE": "mean"})

agg_df = agg_df.reset_index()
agg_df.head()

agg_df["customers_level_based"].value_counts()
agg_df.head()


#############################################
# TASK 7: Segment new customers (USA_ANDROID_MALE_0_18).
#############################################

agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], 4, labels=["D", "C", "B", "A"])
agg_df.head(30)
agg_df.groupby("SEGMENT").agg({"PRICE": "mean"})


#############################################
# TASK 8: Categorize new customers and estimate how much revenue they can generate.
#############################################

# Which segment does a 33-year-old ANDROID-using Turkish woman belong to and how much income is she expected to earn on average?
new_user = "TUR_ANDROID_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user]

# Which segment and how much revenue would a 35-year-old French woman using IOS be expected to bring in on average?
new_user = "FRA_IOS_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user]

