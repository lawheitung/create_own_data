import pandas as pd
import uuid
import random
from faker import Faker
import datetime
from datetime import timedelta

df=pd.read_csv("activity.csv")
columns = ["id","name","gender","email","country","stickiness","occupation","goal","financial_help"]
new_table = pd.DataFrame(columns=columns)
new_table['id'] = df['user_id']

num_users=df['user_id'].count()
print(num_users,type(num_users))

genders = ["male", "female", "na"]
new_table['gender'] = random.choices(
    genders, 
    weights=(47,47,6), 
    k=num_users
)

faker= Faker()

def name_gen(gender):
    #     """
    # Quickly generates a name based on gender
    # """
    if gender=='male':
        return faker.name_male()
    elif gender=='female':
        return faker.name_female()
    
    return faker.name()
# Generating names for each user
new_table['name'] = [name_gen(i) for i in new_table['gender']]

def emailGen(name, duplicateFound=False):
    # """
    # Generates a random email address based on the given name. 
    # Adds a number at the end if a duplicate address was found.
    # """
    # Fake domain name to use
    dom = "@fakemail.com"
    
    # Lowercasing and splitting
    name = name.lower().split(" ")
    
    # Random character to insert in the name
    chars = [".", "_"]
    
    new_name = name[0] + random.choice(chars) + name[1] 
    
    # Further distinguishing the email if a duplicate was found
    if duplicateFound:
        
        # Random number to insert at the end
        num = random.randint(0,100)
        
        # Inserting at the end
        new_name = new_name + str(num)
        
    # Returning the email address with the domain name attached
    return new_name + dom

emails = []
for name in new_table['name']:
    
    # Generating the email
    email = emailGen(name)
    
    # Looping until a unique email is generated
    while email in emails:
        
        # Creating an email with a random number
        email = emailGen(name, duplicateFound=True)
    
    # Attaching the new email to the list
    emails.append(email)
    
new_table['email'] = emails

countries = ['Vietnam', 'Philippines', 'Malaysia', 'Cambodia', 'Thailand', 'Laos', 'Bhutan']
new_table['country']=random.choices(
    countries,
    weights=(76,6,3,4,5,2,4),
    k=num_users
)

new_table['stickiness']=[random.randint(0,80) for i in range(num_users)]

boolean = ['yes','no']
new_table['financial_help']=random.choices(
    boolean,
    weights=(60,45),
    k=num_users
)

occupation = ['unemployed','student','IT professionals','marketing professionals','software engineer', 'Salesforce admin', 'manager', 'human resources professionals', 'sales professionals']
new_table['occupation'] = random.choices(
    occupation,
    weights=(10,25,11,13,8,11,3,13,6),
    k=num_users
)

goal = ['career advancement', 'learn new skills', 'interest', 'change career path']
new_table['goal'] = random.choices(
    goal,
    weights=(30,20,15,35),
    k=num_users
)

new_table.to_csv('user.csv', encoding='utf-8')

print(new_table)


## SDK – online data 

