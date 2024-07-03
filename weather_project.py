import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import calendar

# print(dataset.shape)
# print(dataset.describe())
cities=["Karachi","Tokyo","Seattle","Tehran","Beijing"]
for i in range(len(cities)):
    print(i,cities[i])
city_index=int(input("Please enter a number from the above list for the city you want: "))
dataset = pd.read_csv("e:/Summer Ai Course Daniyal Ahmed/Linear Regression/"+cities[city_index]+".csv")
year = input("Data available for 4 years. Please enter the year 2012-2015: ")
month = (input("Considering Jan as 1 and Dec as 12. Please enter a number from 1 to 12: "))
start_month="0"
end_month="0"
if "-" in month:
    start_month=month.split("-")[0]
    end_month=month.split("-")[1]
else:
    start_month=month
    end_month=start_month

if int(start_month)<10:
    start_month="0"+start_month
if int(end_month)<10:
    end_month="0"+end_month

data1=dataset[dataset.date>=year+"-"+start_month+"-01"]
data2=dataset[dataset.date<=year+"-"+end_month+"-30"]
final_data = pd.merge(data1, data2, how='inner')
#print(final_data)

temperatures= final_data["temp_max"].tolist()
dates = final_data["date"].tolist()
dates_dict={}
temp_dict={}
for i in range(0,len(temperatures)):
    if (datetime.fromisoformat(dates[i]).month) in temp_dict:
        temp_dict[(datetime.fromisoformat(dates[i]).month)].append(temperatures[i])
        dates_dict[(datetime.fromisoformat(dates[i]).month)].append(dates[i])
    else:
        temp_dict[(datetime.fromisoformat(dates[i]).month)]=[temperatures[i]]
        dates_dict[(datetime.fromisoformat(dates[i]).month)] =[dates[i]]

loop_1st_month = int(start_month)
loop_2nd_month = int(end_month)
avg_temp=[]
months=[]
max_temp_array=[]
max_days=[]
min_temp_array=[]
min_days=[]
for i in range(loop_1st_month,loop_2nd_month+1):
    avg_temp.append(round(sum(temp_dict[i])/len(temp_dict[i]),2))
    months.append(calendar.month_name[i])
    
    max_temp = max(temp_dict[i])
    max_temp_array.append(max_temp)
    max_days.append(dates_dict[i][temp_dict[i].index(max_temp)])
    #print(dates)
    #print(max_days)

    min_temp = min(temp_dict[i])
    min_temp_array.append(min_temp)
    min_days.append(dates_dict[i][temp_dict[i].index(min_temp)])

print("The Average of the whole range is: "+str(round(sum(temperatures)/len(temperatures)),2)+" °C")
#print(max_temp_array,max_days)
#print(min_temp_array,min_days)
#print(temp_dict)
#print(max_temp_array)
sns.relplot(data=final_data, x='date', y='temp_max', kind='line')
plt.show()

if "-" in month:
    plt.figure(figsize=(12,5))
    plt.plot(months,avg_temp)
    plt.title("Monthly average temperatures")
    plt.show()

    plt.figure(figsize=(8,5))
    plt.title("Monthly Maximum Temperature")
    plt.plot(max_days,max_temp_array)
    plt.show()

    plt.figure(figsize=(8,5))
    plt.title("Monthly Minimum Temperature")
    plt.plot(min_days,min_temp_array)
    plt.show()