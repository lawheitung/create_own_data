import pandas as pd
import uuid
import random
from faker import Faker
from datetime import datetime
from datetime import timedelta


df=pd.read_csv("Product_Purchase.csv")
num_of_users = len(df.index)
columns = ["user_id","timestamp","Duration","IP","ProductID","ProductQuantity"]
new_table = pd.DataFrame(columns=columns)

## Visitors who made a purchase 
new_table['timestamp'] = randomtimes(start, end, num_of_users)
new_table['ip'] = random.choices(dict['IP'], weights=(40,15,10,15,13,7), k=num_of_users )
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

# pd.set_option('display.max_columns', None)
# print(df['action_5'])
print(new_table)
# print(new_table['user_id'].nunique()==df.iloc[0,8])

new_table.to_csv('Product_Purchase.csv', encoding='utf-8')
print('done')