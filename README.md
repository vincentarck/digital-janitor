# Digital Janitor: Automating File and Folder Organization with Python

## Overview

This project involves creating a Python script that automates the organization of files and folders in a user-specified directory. Think of it as a "digital janitor" that helps keep your directories tidy by moving files into appropriate subdirectories and cleaning up temporary files.

## The script follows these steps:

1. Import necessary libraries.
2. Ask the user to specify a directory.
3. Create a new directory called "closet" within the specified directory.
4. Create three subdirectories within "closet": `text_files`, `csv_files`, and `folders`.
5. Iterate over all items in the specified directory.
6. Move `.txt` files to the `text_files` subdirectory.
7. Move `.csv` files to the `csv_files` subdirectory.
8. Delete directories containing "temp" in their names.
9. Move remaining directories to the `folders` subdirectory.
10. Move remaining files to the `closet` directory.
11. Print a completion message.

## How to Use It
1. Make sure you have [python install](https://www.python.org/downloads/)
2. Clone this project and move into
```bash
git clone https://github.com/your-username/digital-janitor.git
cd digital-janitor
```
3. Run script
```python
python .\clean_sweep_starter.py 
```
4. Specify full path of your messy folder `C:\Users\<username>\<parent_folder>\<folder_name>`

## Find a Bug
If you encounter a bug, please check:

1. Check Permissions:
Ensure you have the necessary read/write permissions for the directory you're trying to organize.

2. Verify Paths:
Double-check the specified directory path and ensure it exists.

3. File Locking Issues:
Some files might be locked by other processes, causing permission errors. Ensure no other programs are using the files.

4. Report Bugs:
Open an issue on the GitHub repository with detailed information about the bug, including the error message and steps to reproduce it.
