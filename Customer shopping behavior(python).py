import pandas as pd
df = pd.read_csv(r"C:\Users\Akansha Singh\Downloads\DATA ANALYST - DOCS\Complete project\1st project\customer_shopping_behavior.csv")
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
df['Review Rating'] = df.groupby('Category') ['Review Rating']. transform(lambda x: x.fillna(x.median()))
print(df.isnull().sum())
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ', '_')
df = df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})
print(df.columns)
#Create a column age_group
labels = ['Young Adult', 'Adult', 'Middle-aged', 'Senior']
df['age_group'] = pd.qcut(df['age'], q=4, labels = labels)
print(df[['age', 'age_group']]. head(10))
#create a column purchase_frequency_days
Mapping_frequency = {
'Fortnightly' : 14,
'Weekly' : 7,
'Annually' : 365,
'Quarterly' : 90,
'Bi-Weekly' : 14,
'Monthly' : 30,
'Every 3 Months' : 90
}

df['purchase_frequency_days'] = df['frequency_of_purchases'].map(Mapping_frequency)
print(df[['frequency_of_purchases','purchase_frequency_days' ]].head(10))
print(df[['discount_applied','promo_code_used']].head(10))
print((df['discount_applied'] == df['promo_code_used']).all())
df = df.drop('promo_code_used', axis=1)
print(df.columns)
from sqlalchemy import create_engine
engine = create_engine(
    "postgresql+psycopg2://postgres:Akansha%40098@localhost:5432/customer_behavior"
)
table_name = "customer"
df.to_sql(
    table_name,
    engine,
    if_exists="replace", 
    index=False
)
print(f"Table '{table_name}' loaded successfully")