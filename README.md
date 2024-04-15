# File Upload CLI

This is a command-line interface (CLI) for uploading, listing, removing, and updating files on a server.

## Requirements

- Python 3.11
- pip

To install the required Python packages, run the following command:

```shell
pip install -r requirements.txt
```

## Creating an Executable

To create an executable of this project, you can use PyInstaller:

```shell
pyinstaller --onefile store.py
```

The executable will be created in the dist directory.

**This project includes a pre-compiled executable named `store`, located in the `dist` directory.
This executable was built on a Linux operating system, allowing any Linux user to run it 
directly. Commands can be executed as follows:**
```shell
./store ls
```



## Usage

### Add Files

To upload files, use the add command followed by the names of the files you want to upload:

```shell
python store.py add file1.txt file2.txt
```

### List Files

To list all files, use the ls command:

```shell
python store.py ls
```

### Remove Files

To remove file, use the rm command followed by the name of the file you want to remove:

```shell
python store.py rm file1.txt
```

### Word Count

To get the word count of all files, use the wc command:

```shell
python store.py wc
```

### Frequency of Words

To get the frequency of words, use the freq-words command followed by the limit:

```shell
python store.py freq-words 10
```

You can also specify the order of frequency (ascending or descending) with the --order option:

```shell
python store.py freq-words 10 --order asc
```

### Update Files

To update a file, use the update command followed by the name of the file:

```shell
python store.py update file1.txt
```

You can also create a duplicate file during the update with the --duplicate option:

```shell
python store.py update file1.txt --duplicate
```


## Configuration

The base URL of the server can be configured with the `STORE_BASE_URL` environment variable. If this variable is not set, the default value is http://localhost:8080/api/v1.

