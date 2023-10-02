import pandas as pd
import uuid
import random
from faker import Faker
from datetime import datetime
from datetime import timedelta


df=pd.read_csv("user.csv")
num_of_users = 100
columns = ["user_id","timestamp","Duration","IP","ProductID"]
new_table = pd.DataFrame(columns=columns)

dfip = pd.read_csv('ip.csv')
dict = dfip.to_dict('list')

dfprod = pd.read_csv("ProductCatelog.csv")
# dict = dfprod.to_dict('list')
# print(dict)

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
start = "2023-01-01 00:00:00"
end = "2023-02-28 00:00:00"

## Visitors who made a purchase 
new_table['timestamp'] = randomtimes(start, end, num_of_users)
new_table['IP'] = random.choices(dict['IP'], weights=(40,15,10,15,13,7), k=num_of_users )
new_table['Duration'] = [random.randint(3,70) for i in range(num_of_users)]
new_table['user_id']= df['id']
new_table['ProductID'] = [random.randint(dfprod['ProductID'][0],dfprod['ProductID'][len(dfprod.index)-1]) for i in range(num_of_users)]
new_table = pd.merge(new_table, 
                      dfprod, 
                      on ='ProductID', 
                      how ='inner')
new_table['ProductQuantity'] = random.choices([1,2,3], weights=(60,30,10), k=num_of_users)

print(new_table.loc[new_table.ProductID == 1238, 'ProductID'].count())
print(new_table.loc[new_table.ProductID == 1239, 'ProductID'].count())

pd.set_option('display.max_columns', None)
print(new_table)

new_table.to_csv('Product_Purchase.csv', encoding='utf-8')
print('done')

## Visitors who made a purchase (add to cart)
new_table['timestamp'] = new_table['timestamp']-random.randint(5,60)
new_table.to_csv('Add_to_cart.csv', encoding='utf-8')

print(new_table)

## Visitors who made a purchase (product view)
new_table.drop('ProductQuantity', inplace=True, axis=1)
new_table['timestamp'] = new_table['timestamp']-random.randint(5,60)
print(new_table)
new_table.to_csv('Product_view.csv', encoding= 'utf-8')

## Visitors who made a purchase (page view)
new_table['timestamp'] = new_table['timestamp']-random.randint(5,60)
new_table.drop('ProductName', inplace=True, axis=1)
new_table.drop('Price', inplace=True, axis=1)
new_table.drop('ProductID', inplace=True, axis=1)

new_table.rename(columns={"ProductCategory":"Title"}, inplace=True)
new_table['scroll_depth'] = random.choices([0.6,0.7,0.8,0.9,1], weights=(25,20,30,12,13), k=num_of_users )

RefType = ['Direct', 'Search Engine', 'Social Networks', 'Email', 'Back Links', 'Internal']
new_table['referrertype'] = random.choices(RefType, weights=(27,43,25,3,2,1), k=num_of_users)
print(new_table)

for i in range(num_of_users):
    new_table.loc[i,'url'] = new_table['Title'][i].replace("n's","ns")
    new_table.loc[i,'url'] = 'www.demo.com/' + new_table['url'][i].replace(" ","")

# new_table['url'] = [new_table['Title'].strip(" ","") for i in range(num_of_users)]

print(new_table)
new_table.to_csv('Page_view.csv', encoding='utf-8')

# print(df.iloc[0:100])



## Visitors who only add to cart but did not purchase
df.drop(index=df.index[0:100], 
        axis=0, 
        inplace=True)
df = df.reset_index()
print(df)

num_of_users = 270
columns = ["user_id","timestamp","Duration","IP","ProductID"]
addcart_table = pd.DataFrame(columns=columns)

addcart_table['timestamp'] = randomtimes(start, end, num_of_users)
addcart_table['IP'] = random.choices(dict['IP'], weights=(40,15,10,15,13,7), k=num_of_users )
addcart_table['Duration'] = [random.randint(3,70) for i in range(num_of_users)]
addcart_table['user_id']= df['id']
addcart_table['ProductID'] = [random.randint(dfprod['ProductID'][0],dfprod['ProductID'][len(dfprod.index)-1]) for i in range(num_of_users)]
addcart_table = pd.merge(addcart_table, 
                      dfprod, 
                      on ='ProductID', 
                      how ='inner')
addcart_table['ProductQuantity'] = random.choices([1,2,3], weights=(60,30,10), k=num_of_users)

pd.set_option('display.max_columns', None)
print(addcart_table)
addcart_table.to_csv('Add_to_cart.csv', mode='a', index=True, header=False)

print('done')

## Visitors who add to cart (product view)
addcart_table['timestamp'] = addcart_table['timestamp']-random.randint(5,60)
addcart_table.drop('ProductQuantity', inplace=True, axis=1)
print(addcart_table)
addcart_table.to_csv('Product_view.csv',  mode='a', index=True, header=False)

## Visitors who add to cart (page view)
addcart_table['timestamp'] = addcart_table['timestamp']-random.randint(5,60)
addcart_table.drop('ProductName', inplace=True, axis=1)
addcart_table.drop('Price', inplace=True, axis=1)
addcart_table.drop('ProductID', inplace=True, axis=1)

addcart_table.rename(columns={"ProductCategory":"Title"}, inplace=True)
addcart_table['scroll_depth'] = random.choices([0.6,0.7,0.8,0.9,1], weights=(25,20,30,12,13), k=num_of_users )

RefType = ['Direct', 'Search Engine', 'Social Networks', 'Email', 'Back Links', 'Internal']
addcart_table['referrertype'] = random.choices(RefType, weights=(27,43,25,3,2,1), k=num_of_users)
print(addcart_table)

for i in range(num_of_users):
    addcart_table.loc[i,'url'] = addcart_table['Title'][i].replace("n's","ns")
    addcart_table.loc[i,'url'] = 'www.demo.com/' + addcart_table['url'][i].replace(" ","")

addcart_table.to_csv('Page_view.csv',  mode='a', index=True, header=False)

## Visitors who only view products but did not add to cart
df.drop(index=df.index[0:270], 
        axis=0, 
        inplace=True)
df = df.reset_index()
print(df)

num_of_users = 250
columns = ["user_id","timestamp","Duration","IP","ProductID"]
viewprod_table = pd.DataFrame(columns=columns)

viewprod_table['timestamp'] = randomtimes(start, end, num_of_users)
viewprod_table['IP'] = random.choices(dict['IP'], weights=(40,15,10,15,13,7), k=num_of_users )
viewprod_table['Duration'] = [random.randint(3,70) for i in range(num_of_users)]
viewprod_table['user_id']= df['id']
viewprod_table['ProductID'] = [random.randint(dfprod['ProductID'][0],dfprod['ProductID'][len(dfprod.index)-1]) for i in range(num_of_users)]
viewprod_table = pd.merge(viewprod_table, 
                      dfprod, 
                      on ='ProductID', 
                      how ='inner')

# pd.set_option('display.max_columns', None)
print(viewprod_table)
viewprod_table.to_csv('Product_view.csv',  mode='a', index=True, header=False)

print('done')


## Visitors who view products (page view)
viewprod_table['timestamp'] = viewprod_table['timestamp']-random.randint(5,60)
viewprod_table.drop('ProductName', inplace=True, axis=1)
viewprod_table.drop('Price', inplace=True, axis=1)
viewprod_table.drop('ProductID', inplace=True, axis=1)

viewprod_table.rename(columns={"ProductCategory":"Title"}, inplace=True)
viewprod_table['scroll_depth'] = random.choices([0.6,0.7,0.8,0.9,1], weights=(25,20,30,12,13), k=num_of_users )

RefType = ['Direct', 'Search Engine', 'Social Networks', 'Email', 'Back Links', 'Internal']
viewprod_table['referrertype'] = random.choices(RefType, weights=(27,43,25,3,2,1), k=num_of_users)
print(viewprod_table)

for i in range(num_of_users):
    viewprod_table.loc[i,'url'] = viewprod_table['Title'][i].replace("n's","ns")
    viewprod_table.loc[i,'url'] = 'www.demo.com/' + viewprod_table['url'][i].replace(" ","")

viewprod_table.to_csv('Page_view.csv',  mode='a', index=True, header=False)



## Visitors who only view page
df.drop(index=df.index[0:250], 
        axis=0, 
        inplace=True)
df.drop('level_0', inplace=True, axis=1)
df = df.reset_index()
print(df)

num_of_users = 200
columns = ["user_id","timestamp","Duration","IP"]
viewprod_table = pd.DataFrame(columns=columns)
viewprod_table['timestamp'] = randomtimes(start, end, num_of_users)
viewprod_table['IP'] = random.choices(dict['IP'], weights=(40,15,10,15,13,7), k=num_of_users )
viewprod_table['Duration'] = [random.randint(3,70) for i in range(num_of_users)]
viewprod_table['user_id']= df['id']
viewprod_table['ProductID'] = [random.randint(dfprod['ProductID'][0],dfprod['ProductID'][len(dfprod.index)-1]) for i in range(num_of_users)]
viewprod_table = pd.merge(viewprod_table, 
                      dfprod, 
                      on ='ProductID', 
                      how ='inner')
viewprod_table.drop('ProductName', inplace=True, axis=1)
viewprod_table.drop('Price', inplace=True, axis=1)
viewprod_table.drop('ProductID', inplace=True, axis=1)

# pd.set_option('display.max_columns', None)

viewprod_table.rename(columns={"ProductCategory":"Title"}, inplace=True)
viewprod_table['scroll_depth'] = random.choices([0.6,0.7,0.8,0.9,1], weights=(25,20,30,12,13), k=num_of_users )

RefType = ['Direct', 'Search Engine', 'Social Networks', 'Email', 'Back Links', 'Internal']
viewprod_table['referrertype'] = random.choices(RefType, weights=(27,43,25,3,2,1), k=num_of_users)
print(viewprod_table)

for i in range(num_of_users):
    viewprod_table.loc[i,'url'] = viewprod_table['Title'][i].replace("n's","ns")
    viewprod_table.loc[i,'url'] = 'www.demo.com/' + viewprod_table['url'][i].replace(" ","")

print(viewprod_table)

viewprod_table.to_csv('Page_view.csv',  mode='a', index=True, header=False)