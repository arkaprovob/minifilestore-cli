# ops.py
import os
from tabulate import tabulate
from helper import file_exists, compute_md5, upload_file, delete_file, list_files


def process_add_command(files):
    for filename in files:
        if not os.path.isfile(filename):
            print(f"Error: File '{filename}' not found.")
        else:
            exists, response = file_exists(filename)
            if exists:
                print("\n")
                print(
                    f"A file with the same name or content already exists on the server, "
                    f"details to which are given below. This "
                    f"might prevent you from uploading your file. To proceed, please try "
                    f"the `update` "
                    f"command")
                print(tabulate([response], headers="keys"))
            else:
                upload_file(filename)


def process_ls_command():
    success, data = list_files()
    if success:
        if data:
            print("Files in the store:")
            print(tabulate(data, headers="keys"))
        else:
            print("No records found.")
    else:
        print(data)


def process_rm_command(files):
    for filename in files:
        success, message = delete_file(filename)
        print(message)


def process_wc_command():
    success, data = list_files()
    if success:
        if data:
            # Create a new list of dictionaries with only the Filename and WordCount fields
            filtered_data = [{'Filename': item['Filename'], 'WordCount': item['WordCount']} for item in data]
            print("Total Word count for each file:")
            print(tabulate(filtered_data, headers="keys"))
        else:
            print("No records found.")
    else:
        print(data)
