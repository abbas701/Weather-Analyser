from datetime import datetime
import calendar 
from collections import OrderedDict
import matplotlib.pyplot as plt
data1={}

fp=open("seattle-weather.csv","r")

lines=[]
for line in fp.readlines()[1:]:
    lines.append(line.strip())
for line in lines:
    line = line.split(",")
    data1[datetime.fromisoformat(line[0])] = (float((line[2])))

def Monthlyavg(dyear,month1,month2,data1):
    Monthlydata={}
    for dto,temperature in data1.items():
        month=dto.month
        if dto.year==dyear:
            if month>=month1 and month<=month2:
                if month in Monthlydata:
                    Monthlydata[month].append(temperature)
                else:
                    Monthlydata[month]= [temperature]

    Monthlydata = OrderedDict(sorted(Monthlydata.items()))
    Monthlyavg={}
    for month,temperature in Monthlydata.items():
        month_name= calendar.month_name[month]
        avgtemp= sum(temperature) / len(temperature)
        Monthlyavg[month_name] = avgtemp

    months=list(Monthlyavg.keys())
    avgtemp=list(Monthlyavg.values())
    plt.figure(figsize=(15,5))
    plt.plot(months,avgtemp,marker='o')
    plt.title("Average temperature of every month")
    plt.xlabel("Months")
    plt.ylabel("Avg Temperature")
    plt.grid(True)
    plt.show()


def Dailyavgpermonth(dyear,month1,month2,data1):
    Monthlydayavg={}
    for dto,temperature in data1.items():
        if dto.year==dyear:
            if dto.month>=month1 and dto.month<=month2:
                if dto.day in Monthlydayavg:
                    Monthlydayavg[dto.day].append(temperature)
                else:
                    Monthlydayavg[dto.day] =[temperature]
    Monthlydayavg = OrderedDict(sorted(Monthlydayavg.items()))
    Dayavgs={}
    for day,temperature in Monthlydayavg.items():
        avgtemp= sum(temperature) / len(temperature)
        Dayavgs[day] = avgtemp
    days=list(Dayavgs.keys())
    avgtemp=list(Dayavgs.values())
    plt.figure(figsize=(10,5))
    plt.plot(days,avgtemp,marker='o')
    plt.title("Average temperature of every Day per required month")
    plt.xlabel("Days")
    plt.ylabel("Avg Temperature")
    plt.grid(True)
    plt.show()
    

def hotcold(year,month,data1):
    Monthlydayavg={}
    for dto,temperature in data1.items():
        if dto.year==year:
            if dto.month==month:
                if dto.day in Monthlydayavg:
                    Monthlydayavg[dto.day].append(temperature)
                else:
                    Monthlydayavg[dto.day] =[temperature]
    Monthlydayavg = OrderedDict(sorted(Monthlydayavg.items()))
    Dayavgs={}
    for day,temperature in Monthlydayavg.items():
        avgtemp= sum(temperature) / len(temperature)
        Dayavgs[day] = avgtemp
    days=list(Dayavgs.keys())
    avgtemp=list(Dayavgs.values())
    maxtemp=0
    maxtempdate=0
    for i in range(0,len(avgtemp)):
        if avgtemp[i]>maxtemp:
            maxtemp=avgtemp[i]
            maxtempdate=days[i]
    lowtemp=9999
    lowtempdate=0
    for i in range(0,len(avgtemp)):
        if avgtemp[i]<lowtemp:
            lowtemp=avgtemp[i]
            lowtempdate=days[i]
    print("The max temperature for the month" ,calendar.month_name[month], "was",maxtemp ,"at the day of" ,maxtempdate)
    print("The lowest temperature for the month ",calendar.month_name[month],"was" , lowtemp,"at the day of ", lowtempdate)


def main(data1):
    choice=0
    while choice!=4:
        print("What do u want to do ")
        print("input 1 for monthly avgs")
        print("input 2 for daily avgs")
        print("input 3 for maxtemperature and lowest temperature obeserved for the month")
        print("print 4 to exit")
        choice=int(input("what is your choice"))
        if choice ==1:
            dyear=int(input("for what year do you want it for ? (2012-2015)"))
            months=input("what are your months, enter in X-X format, where X is the number of the month , 1 being january and 12 being december")
            month1=int(months.split("-")[0])
            month2=int(months.split("-")[1])
            Monthlyavg(dyear,month1,month2,data1)
        elif choice ==2:
            dyear=int(input("for what year do you want it for ? (2012-2015)"))
            months=input("what are your months, enter in X-X format, where X is the number of the month , 1 being january and 12 being december")
            month1=int(months.split("-")[0])
            month2=int(months.split("-")[1])
            Dailyavgpermonth(dyear,month1,month2,data1)
        elif choice == 3:
            dyear=int(input("for what year do you want it for ? (2012-2015)"))
            month=int(input("what is the number of the month, 1 being january and 12 being december"))
            hotcold(dyear,month,data1)
        else:
            if choice==4:
                print("Exited")
            else:
                print("invalid choice")


main(data1)
