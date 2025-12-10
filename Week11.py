import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('Data/vgsales.csv')

# Display basic information
print("First 5 rows:")
print(df.head())
print("\nInfo:")
print(df.info())
print("\nSummary Statistics:")
print(df.describe())
print("\nMissing Values:")
print(df.isnull().sum())
print("\nUnique Values per Column:")
print(df.nunique())

# ----------------- ANALYSIS -----------------

sales_by_year = df.groupby('Year')['Global_Sales'].sum().dropna()
print(sales_by_year)

plt.figure()
sales_by_year.plot(kind='line')
plt.title('Total Global Video Game Sales by Year')
plt.xlabel('Year')
plt.ylabel('Sales (Millions)')
plt.tight_layout()
plt.savefig('sales_by_year.png')
plt.show()

platform_sales = df.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False).head(10)

plt.figure()
platform_sales.plot(kind='bar')
plt.title('Top 10 Platforms by Global Sales')
plt.xlabel('Platform')
plt.ylabel('Sales (Millions)')
plt.tight_layout()
plt.savefig('platform_sales.png')
plt.show()

publisher_sales = df.groupby('Publisher')['Global_Sales'].sum().sort_values(ascending=False).head(10)

plt.figure()
publisher_sales.plot(kind='bar')
plt.title('Top Publishers by Global Sales')
plt.xlabel('Publisher')
plt.ylabel('Sales (Millions)')
plt.tight_layout()
plt.savefig('publisher_sales.png')
plt.show()

print("\nCONCLUSIONS:")
print("- Video game sales peaked around 2008–2010 and declined after that.")
print("- Nintendo platforms and PlayStation platforms generated the highest total sales.")
print("- Nintendo is one of the top publishers in global sales.")