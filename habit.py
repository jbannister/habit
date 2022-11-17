import argparse
import pandas as pd
from os.path import exists

def create_habit() -> pd.DataFrame:
    if not exists('habit.csv'):
        with open('habit.csv', 'w') as f:
            habit_dist = {"date":[], "habit":[], "yes_no":[]}
            # ToDo: Add columns for habit, date, and yes/no
            return pd.DataFrame.from_dict(habit_dist) 
    else:
        return pd.read_csv('habit.csv')

def list_habit(habit_df: pd.DataFrame):
    print(habit_df.head())

def update_habit(update_habit: pd.DataFrame, habit: str):
    update_habit = update_habit.append({'date': pd.Timestamp.now(), 
                                        'habit': habit, 
                                        'yes_no': 'no'}, ignore_index=True)
    update_habit.to_csv('habit.csv', index=False)

def delete_habit(habit_df: pd.DataFrame, habit: str):
    habit_df = habit_df[habit_df.habit != habit]
    habit_df.to_csv('habit.csv', index=False)

df_habit = create_habit()

def habit():
    global df_habit
    parser = argparse.ArgumentParser(
                    prog = 'Habit',
                    description = 'What the program does',
                    epilog = 'Text at the bottom of help')

    parser.add_argument("-c", "--create", help="Create a new habit entry", required=False)  # C
    parser.add_argument("list", help="List all habit entries")                              # R
    parser.add_argument("-u", "--update", help="Update a habit entry", required=False)      # U
    parser.add_argument("-d", "--delete", help="Delete a habit entry", required=False)      # D

    #parser.add_argument('filename')           # positional argument
    #parser.add_argument('-c', '--count')      # option that takes a value
    #parser.add_argument('-v', '--verbose', action='store_true')  # on/off flag
    # https://pandas.pydata.org/
    # DataFrames -> Tables
    #  (bool)

    args = parser.parse_args()
    # print(args)

    if args.create:
        df_habit = create_habit()

    if args.list:
        list_habit(df_habit)

    if args.update:
        update_habit(df_habit, args.update)

    if args.delete:
        delete_habit(df_habit, args.delete)

    # python habit.py -u "test 4" - crash!
    # delete_habit.py -d "test 4"


if __name__ == "__main__":
    habit()