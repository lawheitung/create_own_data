import pandas as pd
import uuid
import random
from faker import Faker
from datetime import datetime
from datetime import timedelta


df=pd.read_csv("user.csv")
df = df.astype({"num_of_user":'int'})
total_num_of_users = df['num_of_user'].sum()
columns = ["timestamp","URL","time_spent","user_id"]
new_table = pd.DataFrame(columns=columns)


def randomtimes(start, end, n):
    # """
    # Generates random time stamps based on a given amount between two time periods.
    # """   

    # The timestamp format
    frmt = "%Y-%m-%d %H:%M:%S"
    epoch = datetime(1970,1,1)  
    
    # Formatting the two time periods
    stime = (datetime.strptime(start, frmt)-epoch).total_seconds()
    etime = (datetime.strptime(end, frmt)-epoch).total_seconds()

    # Creating the pool for random times
    td = etime - stime

    # Generating a list with the random times
    times = [(round(random.random() * td + stime)) for _ in range(n)]


    return times

# Setting the start and end times
start = "2022-12-01 00:00:00"
end = "2023-02-15 00:00:00"

## Visitors who dropped out at homepage 
num_of_users=df['num_of_user'][0]
URL=df['action_1'][0]
new_table['timestamp'] = randomtimes(start, end, num_of_users)
new_table['URL'] = [URL for i in range(num_of_users)]
new_table['time_spent'] = [random.randint(3,15) for i in range(num_of_users)]
new_table['user_id']= [uuid.uuid4().hex for i in range(num_of_users)]

## Visitors who dropped out at course summary URL
num_of_users=df.iloc[1,8]
URL = df['action_2'][1]
new_table1 = pd.DataFrame(columns = columns)
new_table1['timestamp'] = randomtimes(start, end, num_of_users)
pd.to_datetime(new_table1['timestamp'])
new_table1['URL'] = [URL for i in range(num_of_users)]
new_table1['time_spent'] = [random.randint(8,75) for i in range(num_of_users)]
new_table1['user_id']= [uuid.uuid4().hex for i in range(num_of_users)]


## Visitors who dropped out at course detail URL
num_of_users=df.loc[2:6,'num_of_user'].sum()
new_table2 = pd.DataFrame(columns = columns)
new_table2['timestamp'] = randomtimes(start, end, num_of_users)
new_table2['time_spent'] = [random.randint(8,90) for i in range(num_of_users)]
new_table2['user_id']= [uuid.uuid4().hex for i in range(num_of_users)]
for i in range(2,7):
    if i==2:
        new_table2.loc[0:df.iloc[i,8],'URL'] = df['action_3'][i]
    elif i==3:
        new_table2.loc[df.iloc[2,8]+1:df.iloc[2:(i+1),8].sum(),'URL'] = df['action_3'][i]
    else:
        new_table2.loc[df.iloc[2:i,8].sum()+1:df.iloc[2:(i+1),8].sum(),'URL'] = df['action_3'][i]

## Visitors who dropped out at individual course detail URL
num_of_users=df.loc[7:18,'num_of_user'].sum()
new_table3 = pd.DataFrame(columns = columns)
new_table3['timestamp'] = randomtimes(start, end, num_of_users)
new_table3['time_spent'] = [random.randint(120,600) for i in range(num_of_users)]
new_table3['user_id']= [uuid.uuid4().hex for i in range(num_of_users)]
for i in range(7,19):
    if i==7:
        new_table3.loc[0:df.iloc[i,8],'URL'] = df['action_4'][i]
    elif i==8:
        new_table3.loc[df.iloc[7,8]+1:df.iloc[7:(i+1),8].sum(),'URL'] = df['action_4'][i]
    else:
        new_table3.loc[df.iloc[7:i,8].sum()+1:df.iloc[7:(i+1),8].sum(),'URL'] = df['action_4'][i]

## Visitors who dropped out at individual course detail and then sign up
a=19
b=30
num_of_users=df.loc[a:b,'num_of_user'].sum()
new_table4 = pd.DataFrame(columns = columns)
new_table4['timestamp'] = randomtimes(start, end, num_of_users)
new_table4['time_spent'] = [random.randint(40,570) for i in range(num_of_users)]
new_table4['user_id']= [uuid.uuid4().hex for i in range(num_of_users)]
for i in range(a,b+1):
    if i==a:
        new_table4.loc[0:df.iloc[i,8],'URL'] = df['action_5'][i]
    elif i==a+1:
        new_table4.loc[df.iloc[a,8]+1:df.iloc[a:(i+1),8].sum(),'URL'] = df['action_5'][i]
    else:
        new_table4.loc[df.iloc[a:i,8].sum()+1:df.iloc[a:(i+1),8].sum(),'URL'] = df['action_5'][i]


## Visitors who dropped out at individual course finance URL 
a=31
b=42
num_of_users=df.loc[a:b,'num_of_user'].sum()
new_table5 = pd.DataFrame(columns = columns)
new_table5['timestamp'] = randomtimes(start, end, num_of_users)
new_table5['time_spent'] = [random.randint(90,270) for i in range(num_of_users)]
new_table5['user_id']= [uuid.uuid4().hex for i in range(num_of_users)]
for i in range(a,b+1):
    if i==a:
        new_table5.loc[0:df.iloc[i,8],'URL'] = df['action_5'][i]
    elif i==a+1:
        new_table5.loc[df.iloc[a,8]+1:df.iloc[a:(i+1),8].sum(),'URL'] = df['action_5'][i]
    else:
        new_table5.loc[df.iloc[a:i,8].sum()+1:df.iloc[a:(i+1),8].sum(),'URL'] = df['action_5'][i]

## Visitors who dropped out at individual course finance URL 
a=43
b=54
num_of_users=df.loc[a:b,'num_of_user'].sum()
new_table6 = pd.DataFrame(columns = columns)
new_table6['timestamp'] = randomtimes(start, end, num_of_users)
new_table6['time_spent'] = [random.randint(3,15) for i in range(num_of_users)]
new_table6['user_id']= [uuid.uuid4().hex for i in range(num_of_users)]
for i in range(a,b+1):
    if i==a:
        new_table6.loc[0:df.iloc[i,8],'URL'] = df['action_6'][i]
    elif i==a+1:
        new_table6.loc[df.iloc[a,8]+1:df.iloc[a:(i+1),8].sum(),'URL'] = df['action_6'][i]
    else:
        new_table6.loc[df.iloc[a:i,8].sum()+1:df.iloc[a:(i+1),8].sum(),'URL'] = df['action_6'][i]



new_table = new_table.append([new_table1, new_table2, new_table3, new_table4, new_table5, new_table6])
# pd.set_option('display.max_rows', None)
# print(df['action_5'])
print(new_table)
# print(new_table['user_id'].nunique()==df.iloc[0,8])

# new_table.to_csv('activity.csv', encoding='utf-8')
print('done')