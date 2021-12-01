import pandas as pd 



my_file = open("data1.txt", "r")
content_list = my_file.readlines()

content_list = [float(x.replace("\n", "")) for x in content_list]


df = pd.DataFrame(content_list)
# print(df)
df = df.rolling(3).sum()
# print(df)
increased = 0
for i in range(3, len(df.index)):
    print(df.iloc[i][0])
    
    if (df.iloc[i][0] - df.iloc[i-1][0]) > 0:
        increased += 1

print(increased)
 