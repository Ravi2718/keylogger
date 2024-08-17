
# Keylogger Script

## Overview

This script is a basic keylogger that records keystrokes and logs them to a file. It uses the `pynput` library to listen to keyboard events and logs each key press with a timestamp.

## Prerequisites

- Python 3.x
- `pynput` library

## Installation

1. **Install Python:** Ensure you have Python 3.x installed on your system.

2. **Install pynput:** You can install the `pynput` library using pip:

    ```bash
    pip install pynput
    ```

## Configuration

1. **Set Log Directory:** Modify the `log_dir` variable in the script to specify the directory where the log file will be saved. For example:

    ```python
    log_dir = "/path/to/log/directory/"
    ```

2. **Log File Name:** The log file will be named `key_log.txt` and will be created in the specified directory.

## Usage

1. **Run the Script:**

    Execute the script using Python:

    ```bash
    python script_name.py
    ```

    Replace `script_name.py` with the name of your Python file.

2. **Log File:** Keystrokes will be logged to `key_log.txt` in the specified directory. Each entry will include a timestamp.

## Important Note

This script is intended for educational purposes only. Unauthorized use of keylogging software is illegal and unethical. Ensure you have permission before running this script on any computer or device.

