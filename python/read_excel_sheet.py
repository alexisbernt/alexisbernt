import pandas as pd
import os # Python OS module is for interaction with the operating system (can interact with the file system)

def read_excel_sheet(source_file): # Default set sheet_name to 'Sheet1'
    try:
        # Load data from the specified sheet in the Excel file
        data = pd.read_excel(source_file)
        print(f"Data from sheet in {source_file} read. ")
        print("Status: Success")
        return data
    except FileNotFoundError as e:
        print(f"Error: {e}. Ensure the source file exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__": # Python convention to only execute specific file / function when run directly
    # The Excel file is in the same directory as the script
    file_name = input("\nEnter '[name of file].[file type]' (for example 'Sheet1.xlsx'): ")
    source_file = os.path.join(os.path.dirname(__file__), file_name)

    # Read the specified sheet from the source Excel file
    data = read_excel_sheet(source_file)
    if data is not None:
        print(data)
