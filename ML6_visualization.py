
# data visualization


"""
# scatter plot
plt.scatter(df['Age'], df['Overall'])
# histogram
plt.hist(df['Overall'], bins=20)
# pie
plt.pie(df_temp['Weak Foot'],labels = df_temp.index)
# boxplot
temp = [df[df['Position']==i]['Age'] for i in df_temp.index]
plt.boxplot(temp, labels = df_temp.index)
# violin
temp = [df[df['Position']==i]['Age'].to_numpy() for i in df_temp.index]
plt.violinplot(temp)
plt.legend(df_temp.index)
# same
seaborn.violinplot(x="Position", y="Age", data=df)
# stacked bar plot
# example
# first normalized to 1
fig, ax = plt.subplots()
ax.bar(group_name, proportion[0], label='1')
temp = proportion[0]
ax.bar(group_name, proportion[1], bottom = temp, label='2')
temp = temp+proportion[1]

# countplot
seaborn.countplot(x='property_magnitude', data=data)
"""


