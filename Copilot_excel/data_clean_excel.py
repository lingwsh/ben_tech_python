# Write a function to return all excel files path in a directory
import os

def get_excel_files(directory):
    """
    Return a list of excel files in a directory
    """
    excel_files = []
    for file in os.listdir(directory):
        if file.endswith(".xlsx"):
            excel_files.append(os.path.join(directory, file))
    return excel_files

path = "/Users/shuaiwang/Documents/video_project/ben_tech_python/Copilot_excel/data"

# Get all excel files in the directory
excel_files = get_excel_files(path)

# Print the excel files
print(excel_files)

# return dataframe from excel path
import pandas as pd

def get_df_from_excel(excel_path):
    """
    Return a dataframe from excel path
    """
    df = pd.read_excel(excel_path, engine='openpyxl')
    return df

# new a folder "data_new" to store the new excel files
new_path = "/Users/shuaiwang/Documents/video_project/ben_tech_python/Copilot_excel/data_new"
if not os.path.exists(new_path):
    os.mkdir(new_path)

# get each dataframe from excel files
for excel_file in excel_files:
    df = get_df_from_excel(excel_file)
    # Replace each cell to 0 if the value is not a number
    df = df.applymap(lambda x: 0 if not isinstance(x, (int, float)) else x)
    # Sum each raw
    df['sum'] = df.sum(axis=1)
    # save the new dataframe to a new excel file by the same name add "_new" at the end
    df.to_excel(os.path.join(new_path, os.path.basename(excel_file).split(".")[0] + "_new.xlsx"), index=False)

    print(df)


