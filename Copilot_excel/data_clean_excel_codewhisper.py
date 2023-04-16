# Write a function to return all excel files path in a directory
import os


def get_excel_files(directory):
    files = []
    for file in os.listdir(directory):
        if file.endswith(".xlsx"):
            files.append(os.path.join(directory, file))
    return files

path = "/Users/shuaiwang/Documents/video_project/ben_tech_python/Copilot_excel/data"

# Get all excel files in the directory
excel_files = get_excel_files(path)
print(excel_files)

# return dataframe from excel path
import pandas as pd


def get_excel_df(excel_path):
    return pd.read_excel(excel_path)
# return dataframe from excel path

# new a folder "data_new2" to store the new excel files
import os


def create_new_folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


path_new = "/Users/shuaiwang/Documents/video_project/ben_tech_python/Copilot_excel/data_new2"

create_new_folder(path_new)

# get each dataframe from excel files
for excel_path in excel_files:

    df = get_excel_df(excel_path)
    # Replace each cell to 0 if the value is not a number
    df = df.replace("[^0-9]", "0", regex=True)
    # convert each cell to integer
    df = df.astype(int)
    # Sum each row
    # print(df)
    # Sum each row to the last column
    df["Total"] = df.sum(axis=1)
    # print(df)
    # save the new dataframe to a new excel file by the same name add "_new" at the end before ".xlsx"
    df.to_excel(path_new + "/" + os.path.basename(excel_path)[:-5] + "_new.xlsx", index=False)
    # print(df)

