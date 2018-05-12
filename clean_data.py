import pandas as pd
import re, math

df = pd.read_csv("properties.csv")

p = pd.Series(df.iloc[:, 2].values)
a = pd.Series(df.iloc[:, 0].values)
avg = []

for i in range(len(p)):
    p[i] = float(re.sub('[^0-9]', '', p[i]))

for i in range(len(p)):
    if p[i] < 5: p[i] = p[i]*100

for i in range(len(a)):
    a[i] = int(re.sub('[^0-9]', '', a[i]))

for i in range(len(a)):
    avg.append(math.ceil(100000*p[i]/a[i]))

avg = pd.Series(avg)
    
df['localilty'] = df['localilty'].apply(lambda x: x.replace("or Sale", ""))
df['localilty'] = df['localilty'].apply(lambda x: x.replace("ale", ""))
df['localilty'] = df['localilty'].apply(lambda x: x.replace("Sale", ""))
df['localilty'] = df['localilty'].apply(lambda x: x.replace("ale in", ""))
df['localilty'] = df['localilty'].apply(lambda x: x.replace(",in ", ", "))
df['localilty'] = df['localilty'].apply(lambda x: x.replace(" in", ""))
df['localilty'] = df['localilty'].apply(lambda x: x.replace("in ", ""))
df['localilty'] = df['localilty'].apply(lambda x: x.replace(",", ", "))

df = df.drop('area', axis=1)
df = df.drop('price', axis=1)

df['Area in sqft'] = a.values
df['Price in Lac'] = p.values
df['Price per sqft (in Rs.)'] = avg.values

df = df.sort_values(by=['Price per sqft (in Rs.)'], ascending=False)

# Now select top 5 localities:
x1 = pd.Series(df.iloc[0, :])
x2 = pd.Series(df.iloc[16, :])
x3 = pd.Series(df.iloc[24, :])
x4 = pd.Series(df.iloc[26, :])
x5 = pd.Series(df.iloc[27, :])

df_top_5 = pd.DataFrame([x1, x2, x3, x4, x5])

df.to_csv('Prop_cleaned.csv')
df_top_5.to_csv('top_five.csv')