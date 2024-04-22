# ops.py
import os
from tabulate import tabulate
from helper import file_exists, compute_md5, upload_file, delete_file, list_files, \
    get_word_frequency, update_file


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
        base_filename = os.path.basename(filename)
        success, message = delete_file(base_filename)
        print(message)


def process_wc_command():
    success, data = list_files()
    if success:
        if data:
            # Create a new list of dictionaries with only the Filename and WordCount fields
            filtered_data = [{'Filename': item['Filename'], 'WordCount': item['WordCount']} for item
                             in data]
            print("Total Word count for each file:")
            print(tabulate(filtered_data, headers="keys"))
        else:
            print("No records found.")
    else:
        print(data)


def process_fw_command(limit, order):
    most_frequent = order == 'desc'
    success, data = get_word_frequency(limit, most_frequent)
    if success:
        if data:
            print("Word frequency:")
            print(tabulate(data, headers="keys"))
        else:
            print("No records found.")
    else:
        print(data)


def process_update_command(file, duplicate):
    filename = os.path.basename(file)
    file_hash = compute_md5(file)
    exists, response = file_exists(file)
    if exists:
        print(f"Ufile: {file}, already exists in server")
        server_record_hash = response.get('FileHash')
        server_record_name = response.get('Filename')
        if server_record_hash != file_hash and server_record_name == filename:
            update_file(server_record_name, filename, False, file)
        elif server_record_hash == file_hash:
            update_file(server_record_name, filename, duplicate, None)
    else:
        upload_file(file)