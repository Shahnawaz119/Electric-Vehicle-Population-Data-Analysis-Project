import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
file=pd.read_csv("C:\\Users\\Shahnawaz Saifi\\OneDrive\\Pictures\\Desktop\\Python_code\\Sem4\\Electrical_Vehical.csv")
print("\nDisplay 5 rows from Starting")
print(file.head())
print("Display 5 rows form ending")
print(file.tail())
print("\n Shape of Data")
print(file.shape)
print("\nShow All Columns in this Data")
print(file.columns)
print("\nDisplay All Basic Information")
print(file.info())
print("\nDescribe")
print(file.describe())
print("\nDisplay total null Values in this Data")
print(file.isnull().sum())
print("\nDrop Missing Values")
file=file.dropna()
print(file.head())
print("\total Missing values after Drop")
print(file.isnull().sum())
print("\nDrop Duplicate Values")
file.drop_duplicates
print(file)


#Univeriate Analysis
plt.figure(figsize=(10,6))
sns.set_style(style="whitegrid")
sns.countplot(data=file.head(1000),
              x='Make',
              saturation=20,
              color='r'
              
            )

plt.xticks(rotation=70)
plt.title("Count of Vehicle by Make",fontsize=12)
plt.xlabel("Vehicle Make")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(10,6))
sns.histplot(data=file.tail(10000),
             x='Model Year',
             kde=True,
             bins=15,
             color='m'
            )
plt.title("Distribution of Model Year",fontsize=12)
plt.show()

#Biveriate/Multivariate Analysis

plt.figure(figsize=(10,6))
sns.boxplot(data=file.head(1000),
            x="Make",
            y="Model Year",
            hue="Electric Vehicle Type",
            palette="bright",
            showmeans=True,
            meanprops={"marker":"*","markersize":8},
            linewidth=1,
            linecolor='m'
            )
plt.xticks(rotation=70)
plt.title("Model Year Distribution by Make",fontsize=12)
plt.show()

plt.figure(figsize=(10,6))
sns.lineplot(data=file.head(5000),
             x="County",
             y="Make",
             hue="Electric Vehicle Type",
             style="Electric Vehicle Type",
             palette="plasma",
             markers=["o","^"],
             dashes=False,
             legend=True
             )
plt.xticks(rotation=70)
plt.yticks(rotation=30)
plt.title("Distribution Make Vehicle by County")
plt.show()

plt.figure(figsize=(10,6))
corr=file.corr(numeric_only=True)
sns.heatmap(corr,
            annot=True,
            cmap="PuOr",
            annot_kws={"fontsize":"11","color":"r"},
            linewidth=4,
            linecolor='m'
            )
plt.xticks(rotation=70)
plt.yticks(rotation=30)
plt.show()

plt.figure(figsize=(10,6))
sns.scatterplot(data=file.head(200),
                x="Model Year",
                y="Electric Range",
                hue="Make",
                style="Make",
                size="Make",
                palette="Accent"
                )
plt.title("Electric Range Over Model Year")
plt.xticks(rotation=70)
plt.yticks(rotation=30)
plt.show()

plt.figure(figsize=(10,6))
subset = file[['Model Year', 'Electric Range', 'Base MSRP','Electric Vehicle Type']]
sns.pairplot(data=subset.head(2000),
             hue="Electric Vehicle Type",
             hue_order=['Battery Electric Vehicle (BEV)','Plug-in Hybrid Electric Vehicle (PHEV)'],
             palette="gist_heat_r",
             markers=["o","*"]
             )
plt.show()
