# Python File & OS Automation Practice

This folder contains practice scripts and exercises from **Module 2** of the Google IT Automation with Python course. It covers:

- File handling with Python
- Working with CSV files
- OS module: working with directories, paths, and files
- Regular Expressions using `re` and `grep`
- Useful Bash commands for text search
- Writing modular and reusable Python scripts

---

## 🔧 Scripts

| File                | Description |
|---------------------|-------------|
| `areas.py`          | Calculates area of shapes (basic Python practice) |
| `hello.py`          | Simple Hello World script |
| `health_check.py`   | Checks disk and CPU usage using `shutil` and `psutil` |
| `check_content.py`  | Lists files and directories in current folder |
| `sort_poem.py`      | Sorts lines from a text file alphabetically |
| `parse_csv.py`      | Parses CSV file from command-line argument |
| `word.py`           | Used for regex practice with `grep` |


## 📂 cli_scripts

This folder contains command-line Python scripts from Module 2 practice, focusing on automation, environment variables, subprocess, and CLI tools.

| Script | Description |
|--------|-------------|
| `hello.py` | Simple Hello World CLI with input |
| `seconds.py` | Converts hours, minutes, seconds into total seconds |
| `streams.py` | Demonstrates STDIN, STDOUT, STDERR |
| `variables.py` | Prints environment variables (HOME, SHELL, etc.) |
| `parameters.py` | Demonstrates `sys.argv` for passing CLI arguments |
| `check_cron.py` | Basic cron job format validator |
| `my_app.py` | Demonstrates custom `PATH` via `subprocess` |

---

## 📁 Sample Data Files

- `csv_file.txt`: Sample CSV (manual format)
- `software.csv`: CSV with headers (used with `DictReader`)
- `host.csv`: CSV written using Python `csv.writer`
- `spider_poem.txt`: Sample poem text

---

## 🧪 Practice Notes

- `grep_regex_cheat_sheet.md`: Regex syntax and Bash usage examples
- `notes.txt`: Notes and learnings from file handling, OS, and regex modules

---

## 🧠 Key Skills Practiced

- Reading/writing files with `open()`, `with`
- OS module (`os.getcwd`, `os.listdir`, `os.path`)
- Handling file paths and metadata
- Bash: `cat`, `grep`, `nano`, `chmod`, `./filename.py`
- Regex: `re.search()`, `re.findall()`, character classes, quantifiers

---

## ✅ To Run

```bash
chmod +x script_name.py   # Make executable (optional)
./script_name.py          # Run directly
# or
python3 script_name.py    # Run with Python
