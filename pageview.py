import pandas as pd
import uuid
import random
from faker import Faker
from datetime import datetime
from datetime import timedelta

df = pd.read_csv('Page_view.csv')
df = pd.to_numeric(df)
df['scroll_depth'] = (df['scroll_depth']/100)

print(df)