# Cipher Text Converter - Python Edition

<img src="logo_python.png" width="128" height="128" alt="text-encryption" align="right" />

### Overview

For a complete understanding of this project, please refer to the [Main Documentation](https://github.com/ivin-titus/Text-Encryption/blob/master/README.md).

<b> [Download](https://www.mediafire.com/file/npikkymx3hleurt/Text_Encryption.apk/file)</b>

### Usage:

1. **Command Line Mode**:
    - Run the script `cipher_cli.py` directly from the command line.
    - Example command: `python cipher_cli.py <mode> <level> <key1> <key2>` (or `python3` on some devices).

2. **Graphical User Interface (GUI)**:
    - Run the script `cipher_app.py` to launch the graphical application.
    - Example command: `python cipher_app.py`.

3. **Import into Other Python Projects**:
    - You can import the functionality into other Python projects.
    - Example import statement: `from cipher_cli import convert`.
    - Example usage in code: `convert(mode, level, text, key1, key2)`.

### Requirements:

- **Python Interpreter**: Required to execute the scripts.

- **Command Line Interface (CLI)**: No additional packages are needed.

- **Graphical User Interface (GUI)**:
    - Required packages: `customtkinter`, `pyperclip`.
    - To install these packages: Simply run `cipher_app.py`, and the necessary packages will be automatically installed.
    - **Note**: An internet connection is required during the first run to download the required packages.

- **Imported Usage in Other Projects**:
   - Ensure that the `Files` folder and the `cipher_cli.py` script are located in the same directory as the project where they will be used.

### Command Line Interface (CLI):

To use the CLI:

1. Navigate to the directory containing `cipher_cli.py`.
2. Run the following command:

```bash
python cipher_cli.py <mode> <level> <key1> <key2>
```

- `mode`: Choose either `encrypt` or `decrypt`.
- `level`: Choose `simple`, `normal`, or `advanced`.
- `key1`: The first key, which is an integer (required for all levels).
- `key2`: The second key, which is a string (required for `normal` and `advanced` levels; optional for `simple` level).

Example:

```bash
python cipher_cli.py encrypt simple 4
```

### Graphical User Interface (GUI):

To use the GUI:

1. Navigate to the directory containing `cipher_app.py`.
2. Run the following command:

```bash
python cipher_app.py
```

This will launch the graphical application, where you can select the mode (encrypt/decrypt), the level (simple/normal/advanced), enter your keys, and perform the encryption or decryption.
Note : This script is only supported on Desktop OS like any Linux distros , MacOS, Windows etc. For smartphones, visit <b>[Flutter Edition](https://github.com/ivin-titus/Text-Encryption/tree/master/text_encryption_flutter)</b>
