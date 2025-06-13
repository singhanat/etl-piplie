import pandas as pd
import math

df = pd.read_csv('sample_products.csv')
df['unit_price'] = df['unit_price'].apply(math.ceil)
df.to_csv('output/cleaned_products.csv', index=False)
