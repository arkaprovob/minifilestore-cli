# helper.py
import hashlib
import os

import requests
import time

BASE_URL = os.getenv('STORE_BASE_URL', 'http://localhost:8080/api/v1')


def compute_md5(filename):
    # Compute the MD5 hash of a file
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def file_exists(filename):
    # Check if a file exists on the server
    file_hash = compute_md5(filename)
    filename = os.path.basename(filename)
    response = requests.get(BASE_URL + '/exists', params={'hash': file_hash, 'name': filename})
    return response.status_code == 200, response.json() if response.status_code == 200 else None


def upload_file(filename):
    # Upload a file to the server
    max_retries = 3
    retry_delay = 5  # delay between retries in seconds

    for attempt in range(max_retries):
        try:
            with open(filename, 'rb') as f:
                files = {'file': f}
                base_filename = os.path.basename(filename)
                response = requests.post(BASE_URL + '/store', files=files,
                                         data={'filename': base_filename})
                if response.status_code == 200:  # 200 means 'OK' - file uploaded successfully
                    print(f"File '{filename}' uploaded successfully.")
                    return
                else:
                    print(f"Upload failed for '{filename}'. Error: {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"Network error occurred while uploading '{filename}': {str(e)}")

        # If we haven't returned from the function yet, we've hit an error
        if attempt < max_retries - 1:  # no delay on the last attempt
            print(f"Retrying in {retry_delay} seconds...")
            time.sleep(retry_delay)

    print(f"Failed to upload '{filename}' after {max_retries} attempts.")


def list_files():
    try:
        response = requests.get(BASE_URL + '/list')
        if response.status_code == 200:
            return True, response.json()
        else:
            return False, (f"Failed to retrieve file list. "
                           f"Server responded with status code {response.status_code}.")
    except requests.exceptions.RequestException as e:
        return False, f"Network error occurred while trying to retrieve file list: {str(e)}"


def delete_file(filename):
    try:
        response = requests.post(BASE_URL + '/delete', data={'filename': filename})
        if response.status_code == 200:
            return True, f"File '{filename}' deleted successfully."
        else:
            return False, (f"Failed to delete '{filename}'. "
                           f"Server responded with status code {response.status_code}.")
    except requests.exceptions.RequestException as e:
        return False, f"Network error occurred while trying to delete '{filename}': {str(e)}"


def get_word_frequency(no_of_words, most_frequent):
    try:
        response = requests.post(BASE_URL + '/frequency',
                                 params={'noOfWords': no_of_words, 'mostFrequent': most_frequent})
        if response.status_code == 200:
            return True, response.json()
        else:
            return False, (f"Failed to retrieve word frequency. "
                           f"Server responded with status code {response.status_code}.")
    except requests.exceptions.RequestException as e:
        return False, f"Network error occurred while trying to retrieve word frequency: {str(e)}"


def update_file(prev_filename, filename, duplicate, file_path):
    data = {'prevFilename': prev_filename, 'filename': filename, 'duplicate': duplicate}
    print(data)
    try:
        if file_path is not None:
            with open(file_path, 'rb') as f:
                file_content = f.read()
                file_data = {'file': (filename, file_content)}
                response = requests.post(BASE_URL + '/update', files=file_data, data=data)
        else:
            response = requests.post(BASE_URL + '/update', files={'file': None}, data=data)
        if response.status_code == 200:
            print(f"File '{filename}' updated successfully.")
            return True
        else:
            print(f"Update failed for '{filename}'. Error: {response.text}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"Network error occurred while updating '{filename}': {str(e)}")
        return False