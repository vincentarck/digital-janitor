from pathlib import Path
import shutil

# Ask the user to specify a directory
folder_path = Path(input("Enter the specified folder path relative to home directory: ").strip()).expanduser()

# Ensure the specified directory exists
if not folder_path.is_dir():
    print(f"Error: {folder_path} is not a directory.")
    exit()

# Create a new directory within that directory, called "closet"
closet_path = folder_path / "closet"
closet_path.mkdir(exist_ok=True)

# Create three sub-directories within closet: text_files, csv_files, and folders
text_files_path = closet_path / "text_files"
csv_files_path = closet_path / "csv_files"
folders_path = closet_path / "folders"

text_files_path.mkdir(exist_ok=True)
csv_files_path.mkdir(exist_ok=True)
folders_path.mkdir(exist_ok=True)

# Iterate over all the files and folders in the user-specified directory
for item in folder_path.iterdir():
    # Skip the closet directory
    if item == closet_path:
        continue

    # Move plaintext files (.txt) to the text_files sub-directory
    if item.is_file() and item.suffix == ".txt":
        shutil.move(str(item), text_files_path / item.name)
    
    # Move CSV files to the csv_files sub-directory
    elif item.is_file() and item.suffix == ".csv":
        shutil.move(str(item), csv_files_path / item.name)
    
    # Delete directories with "temp" in the name
    elif item.is_dir() and "temp" in item.name.lower():
        shutil.rmtree(item)
    
    # Move remaining directories to the folders sub-directory
    elif item.is_dir():
        shutil.move(str(item), folders_path / item.name)
    
    # Move remaining files to the closet directory
    elif item.is_file():
        shutil.move(str(item), closet_path / item.name)

# Print feedback to the user
print("Organizing files and folders is complete.")
