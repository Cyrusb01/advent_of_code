import pandas as pd 



my_file = open("data1.txt", "r")
content_list = my_file.readlines()

content_list = [float(x.replace("\n", "")) for x in content_list]
print(content_list)

increased = 0
for i in range(1, len(content_list)):
    # print(content_list[i])
    if (content_list[i] - content_list[i-1]) > 0:
        increased += 1

print(increased)