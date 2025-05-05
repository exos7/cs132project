import pandas as pd

fish_produce = pd.read_csv('datasheet.csv')

for year in range(2002, 2025):
    fish_produce[f'{year}'] = fish_produce[f'{year}_Q1'] + fish_produce[f'{year}_Q2'] + fish_produce[f'{year}_Q3'] + fish_produce[f'{year}_Q4']
# Drop the quarterly columns
fish_produce = fish_produce.drop(columns=[f'{year}_Q1' for year in range(2002, 2025)] + [f'{year}_Q2' for year in range(2002, 2025)] + [f'{year}_Q3' for year in range(2002, 2025)] + [f'{year}_Q4' for year in range(2002, 2025)])

fish_produce.to_csv('datasheet_total.csv', index=False)
print(fish_produce)