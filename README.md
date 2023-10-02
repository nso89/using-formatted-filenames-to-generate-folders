# project-name
Project Description

* [Prerequisites](#prerequisites)
* [Setup](#setup)
* [Running the Script](#running-the-script)
* [Configuration](#configuration)

#### <a name="prerequisites"></a>Prerequisites
* A complete install of `Python 3.x`.
* Under `Downloads`, the properly formatted files.
Formatted Files:
```
report-working with ai
sales-2007
2008-requirements
```
You'll notice that the files names start with a word or number, followed by a dash, and end with a word or number.

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
**Example**
```batch
Renaming C:\Users\nso89\Downloads\2008-requirements.txt --> C:\Users\nso89\Downloads\2008\requirements.txt
Renaming C:\Users\nso89\Downloads\report-working with ai.txt --> C:\Users\nso89\Downloads\Report\working-with-ai.txt
Renaming C:\Users\nso89\Downloads\sales-2007.txt --> C:\Users\nso89\Downloads\Sales\2007.txt
```

#### <a name="configuration"></a>Configuration
If you need to change the `SOURCE` or the `DELIMITER`:

1. Open the `main.py` script in any text editor.
2. Locate the `SOURCE` and `DELIMITER` variable.

**Example**:
```
SOURCE = Path.home().joinpath("Downloads")
DELIMITER = "-"
```
3. When you finish changing the variables, save and close the editor.
