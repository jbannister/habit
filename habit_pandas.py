import pandas as pd
import datetime
from os.path import exists

# C - Create 
def create_habit() -> pd.DataFrame:
    if not exists('habit.csv'):
        with open('habit.csv', 'w') as f:
            habit_dist = {"date":[], "habit":[], "yes_no":[]}
            # ToDo: Add columns for habit, date, and yes/no
            return pd.DataFrame.from_dict(habit_dist) 
    else:
        return pd.read_csv('habit.csv')

# R - List
def list_habit(habit_df: pd.DataFrame):
    print(habit_df.head())

def update_now(habit_df: pd.DataFrame):
    x = habit_df.where(habit_df['date'] < '2022-11-16')
    print(x)

    #out = pd.DataFrame([[datetime.datetime.now(),'habit 1','no']], 
    #                    columns=['date', 'habit', 'yes_no'])


    #habit_df.to_csv("habit.csv")  

# U - Update
def update_habit(update_habit: pd.DataFrame, habit: str):
    update_habit = update_habit.append({'date': pd.Timestamp.now(), 
                                        'habit': habit, 
                                        'yes_no': 'no'}, ignore_index=True)
    update_habit.to_csv('habit.csv', index=False)

# D - Delete
def delete_habit(habit_df: pd.DataFrame, habit: str):
    habit_df = habit_df[habit_df.habit != habit]
    habit_df.to_csv('habit.csv', index=False)


