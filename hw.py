import pandas as pd
import random
import matplotlib.pyplot as plt

plt.rc('font', family='Microsoft JhengHei') 

# df = pd.read_csv('C:\\Users\\ruby1\\OneDrive\\桌面\\python\\分析資料作業\\奧林匹亞競賽歷年參賽成績.csv', encoding='utf-8') 
df = pd.read_csv('奧林匹亞競賽歷年參賽成績.csv', encoding='utf-8') 
print(df)
# 第一題
# 本資料共紀錄幾場奧林匹亞賽事
type_list1=[]
for i in df['類別']:
    if('奧林匹亞'in i):
        type_list1.append('奧林匹亞')
print(f"本資料共紀錄{type_list1.count('奧林匹亞')}場賽事。")

#第二題
# 國際 亞洲 亞太賽事各有幾場？
type_list = []

for i in df['類別']:
    if ('國際' in i):
        type_list.append('國際')
    elif ('亞洲' in i):
        type_list.append('亞洲')
    else:
        type_list.append('亞太')
    
print(f"本資料共紀錄{type_list.count('國際')}場國際賽事，{type_list.count('亞洲')}場亞洲賽事和{type_list.count('亞太')}場亞太賽事。")

# 第三題
# 中華民國主辦過幾場賽事
type_list2=[]

for i in df['主辦國']:
    if('中華民國' in str(i)):#改字串str()
        type_list2.append('中華民國')
print(f"中華民國共主辦了{type_list2.count('中華民國')}場奧林匹亞賽事。")

# 第四題
# 因疫情取消了幾屆比賽？

type_list3=[]
for i in df['主辦國']:
    if('疫情' in str(i)):
        type_list3.append('疫情')

print(f"因疫情取消了{type_list3.count('疫情')}屆賽事。")

# 第五題
# 主辦過最多次的國家
import collections
type_list4= df['主辦國']
counter = collections.Counter(type_list4)
most_common = counter.most_common(1)
print(f"主辦過最多次的國家是{most_common[0][0]}。")

# 第六題
# 中華民國拿過幾次團體冠軍

type_list5=[]
for i in df['排名']:
    if('第1名' in str(i)):
        type_list5.append('第1名')
print(f"中華民國共拿過{type_list5.count('第1名')}次團體冠軍。")

# 第七題
# 資料賽事中，參加國最多有幾個國家？最少有幾個國家？

type_list6=df['參加國']
number_list = []
for item in type_list6:

    if item.isdigit():
        number_list.append(int(item))
max_count = max(number_list)
min_count = min(number_list)
print(f"資料賽事中，最多的一次有{max_count}國參加；參加國最少的一次有{min_count}國參加。")

# 第八題
# 國際數學奧林匹亞競賽目前已辦到第幾屆？亞太數學奧林匹亞競賽目前已辦到第幾屆？
international_math_olympiad_df = df.query('類別 == "國際數學奧林匹亞"')
the_latest_session=max(international_math_olympiad_df['屆別'])
print(f"國際數學奧林匹亞競賽目前已辦到第'{int(the_latest_session)}'屆。")
asia_math_olympiad_df = df.query('類別 == "亞太數學奧林匹亞"')
the_latest_session = max(asia_math_olympiad_df['屆別'])
print(f"亞太數學奧林匹亞競賽目前已辦到第'{int(the_latest_session)}'屆。")

# 第九題
# 國際物理奧林匹亞競賽目前辦到第幾屆?亞洲物理奧林匹亞競賽目前已辦到第幾屆?
international_physic_olympiad_df= df.query('類別 == "國際物理奧林匹亞"')
the_latest_session = max(international_physic_olympiad_df['屆別'])
print(f"國際物理奧林匹亞競賽目前已辦到第'{int(the_latest_session)}'屆。")
asia_physic_olympiad_df = df.query('類別 == "亞洲物理奧林匹亞"')
the_latest_session = max(asia_physic_olympiad_df['屆別'])
print(f"亞洲物理奧林匹亞競賽目前已辦到第'{int(the_latest_session)}'屆。")

# 第十題
# 1991年至2022年各領域奧林匹亞競賽次數比較
# 1.數個領域次數
type_list7=[]
for i in df['類別']:
    if('數學'in i):
        type_list7.append('數學')
    elif('物理'in i):
        type_list7.append('物理')
    elif('化學'in i):
        type_list7.append('化學')
    elif('生物'in i):
        type_list7.append('生物')
    elif('地科'in i):
        type_list7.append('地科')
    elif('資訊'in i):
        type_list7.append('資訊')
    elif('國中科學'in i):
        type_list7.append('國中科學')
math=type_list7.count('數學')
physic=type_list7.count('物理')
chemistry=type_list7.count('化學')
biology=type_list7.count('生物')
earth_science=type_list7.count('地科')
computer_science=type_list7.count('資訊')
junior_science=type_list7.count('國中科學')

# 2.繪製長條圖
plt.bar(['數學','物理','化學','生物','地科','資訊','國中科學'],[math,physic,chemistry,biology,earth_science,computer_science,junior_science])
plt.title('1991年至2022年各領域舉辦奧林匹亞競賽次數')
plt.xlabel('領域')
plt.ylabel('舉辦奧林匹亞競賽次數')
plt.show()


