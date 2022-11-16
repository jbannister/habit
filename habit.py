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

def list_habit(habit_df: pd.DataFrame) -> pd.DataFrame:
    print(habit_df.head())

df_habit = create_habit()

def habit():
    global df_habit
    parser = argparse.ArgumentParser(
                    prog = 'Habit',
                    description = 'What the program does',
                    epilog = 'Text at the bottom of help')

    parser.add_argument("-c", "--create")               # C - Create a new habit entry
    parser.add_argument("list")                         # R - List all habit entries
    parser.add_argument("-u", "--update")               # U - Update a habit entry
    parser.add_argument("-d", "--delete")               # D - Delete a habit entry

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


if __name__ == "__main__":
    habit()