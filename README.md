# using-formatted-filenames-to-generate-folders
Using Formatted Filenames to Generate Folders

* [Prerequisites](#prerequisites)
* [Setup](#setup)
* [Running the Script](#running-the-script)
* [Configuration](#configuration)

#### <a name="prerequisites"></a>Prerequisites
* A complete install of `Python 3.x`.
* Under `Downloads`, the properly formatted files.

Formatted Files:
```
report-working with ai.txt
sales-2007.txt
2008-requirements.txt
```
You'll notice that the files names start with a word or number, followed by a dash, and end with a word or number. The script isn't exclusive to just `.txt`. We can work with any file type, as long as the filename properly formatted. 

#### <a name="setup"></a>Setup
1. Under your `USERPROFILE`, extract `using-formatted-filenames-to-generate-folders-main.zip`.

**Example**:
```batch
C:\Users\nso89\using-formatted-filenames-to-generate-folders-main
```
#### <a name="running-the-script"></a>Running the Script
1. Open `cmd.exe` and change the directory to the `using-formatted-filenames-to-generate-folders-main` folder.

**Example**:
```batch
C:\Users\nso89>cd using-formatted-filenames-to-generate-folders-main
```
2. Start the `main.py` script.

**Example**:
```batch
C:\Users\nso89\using-formatted-filenames-to-generate-folders-main>python main.py
```

3. It takes the word before the hyphen, and generates a folder. It then renames and moves the file to that folder.

**Example**:
```batch
Renaming ..\Downloads\2008-requirements.txt --> ..\Downloads\2008\requirements.txt
Renaming ..\Downloads\report-working with ai.txt --> ..\Downloads\Report\working-with-ai.txt
Renaming ..\Downloads\sales-2007.txt --> ..\Downloads\Sales\2007.txt
```

#### <a name="configuration"></a>Configuration
If you need to change the `SOURCE` or the `DELIMITER`:

1. Open the `main.py` script in any text editor.
2. Locate the `SOURCE` and `DELIMITER` variable.

**Example**:
```python
SOURCE = Path.home().joinpath("Downloads")
DELIMITER = "-"
```
3. When you finish changing the variables, save and close the editor.
