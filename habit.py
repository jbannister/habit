import argparse
import pandas as pd

def habit():
    df = pd.read_csv('habit.csv')
    parser = argparse.ArgumentParser(
                    prog = 'Habit',
                    description = 'What the program does',
                    epilog = 'Text at the bottom of help')

    parser.add_argument("-c", "--create") # C - Create a new habit entry
    parser.add_argument("-l", "--list")   # R - List all habit entries
    parser.add_argument("-u", "--update") # U - Update a habit entry
    parser.add_argument("-d", "--delete") # D - Delete a habit entry


    #parser.add_argument('filename')           # positional argument
    #parser.add_argument('-c', '--count')      # option that takes a value
    #parser.add_argument('-v', '--verbose', action='store_true')  # on/off flag
    # https://pandas.pydata.org/
    # DataFrames -> Tables
    #  (bool)


    args = parser.parse_args()
    print(args, df)

if __name__ == "__main__":
    habit()