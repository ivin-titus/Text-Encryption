import customtkinter as ctk
from tkinter import messagebox
import pyperclip  
import os


# check
import subprocess
import sys

def install_package(package_name):
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package_name])
        print(f"Package '{package_name}' installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while installing package '{package_name}': {e}")

def check_and_install_package(package_name):
    try:
        __import__(package_name.split('==')[0])
        print(f"Package '{package_name}' is already installed.")
    except ImportError:
        print(f"Package '{package_name}' is not installed.")
        install_package(package_name)

def checkninstall():
    # List of packages to check and install
    packages = ['customtkinter', 'pyperclip']
    
    for package in packages:
        check_and_install_package(package)


# simple

def simpledecrypt(word, key):
    cypher = []

    for char in word:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            decrypted_char = chr((ord(char) - base + 26 - key) % 26 + base)
            cypher.append(decrypted_char)
        else:
            cypher.append(char)

    return ''.join(cypher)

def simpleencrypt(word, key):
    cypher = []

    for char in word:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - base + key) % 26 + base)
            cypher.append(encrypted_char)
        else:
            cypher.append(char)

    return ''.join(cypher)


# normal
def normalencrypt(text, int_key, str_key):
    encrypted_text = ""
    str_key_index = 0
    for char in text:
        if char.isalpha():
            shift = (ord(str_key[str_key_index]) - ord('a') + int_key) % 26
            if char.isupper():
                encrypted_text += chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
            else:
                encrypted_text += chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
            str_key_index = (str_key_index + 1) % len(str_key)
        else:
            encrypted_text += char
    return encrypted_text

def normaldecrypt(encrypted_text, int_key, str_key):
    decrypted_text = ""
    str_key_index = 0
    for char in encrypted_text:
        if char.isalpha():
            shift = (ord(str_key[str_key_index]) - ord('a') + int_key) % 26
            if char.isupper():
                decrypted_text += chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
            else:
                decrypted_text += chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
            str_key_index = (str_key_index + 1) % len(str_key)
        else:
            decrypted_text += char
    return decrypted_text

# advanced

def derive_key(str_key):
    return sum(ord(char) for char in str_key)

def advancedencrypt(text, int_key, str_key):
    encrypted_text = ""
    derived_key = derive_key(str_key)

    for char in text:
        encrypted_char = chr(ord(char) + derived_key + int_key)

        encrypted_text += encrypted_char

    return encrypted_text

def advanceddecrypt(encrypted_text, int_key, str_key):
    decrypted_text = ""
    derived_key = derive_key(str_key)

    for char in encrypted_text:
        decrypted_char = chr(ord(char) - derived_key - int_key)

        decrypted_text += decrypted_char

    return decrypted_text


#cli

import sys

def usage():
    print('''Usage : python filename.py mode level key1 key2[optional] ( if its command line operation )\n
    Allowed modes : encrypt , decrypt\n
    Allowed Levels : simple, normal, advanced\n
    Key1 : Required - only integer value allowed\n
    Key2: Required if level is normal or advanced, only string value allowed(no special characters or whitespace allowed) ''')


def encrypt(level, text, key1, key2 = None):
    if level == 'simple':
        return simpleencrypt(text, key1)

    elif level == 'normal':
        if key2 == None:
            print('\nError on Encrypt : Key2 Missing ')
            raise TypeError
        return normalencrypt(text, key1, key2)

    elif level == 'advanced':
        if key2 == None:
            print('\nError on Encrypt : Key2 Missing ')
            raise TypeError
        return advancedencrypt(text, key1, key2)

    else:
        print('\nError on Encrypt : Invalid Level ')
        raise TypeError


def decrypt(level, text, key1, key2 = None):
    if level == 'simple':
        return simpledecrypt(text, key1)

    elif level == 'normal':
        if key2 == None:
            print('\nError on Decrypt : Key2 Missing')
            raise TypeError
        return normaldecrypt(text, key1, key2)

    elif level == 'advanced':
        #try:
            if key2 == None:
                print('\nError on Decrypt : Key2 Missing')
                raise TypeError
            return advanceddecrypt(text, key1, key2)
        #except ValueError:
            #sys.exit('Something went Wrong , Please Try Below Options\n1) Try again with another level\n2) Try another text that encrypted by advanced level\n3) Change values of key1 to a 2 digit one')

    else:
        print('\nError on Decrypt : Invalid Level')
        raise TypeError


def convert(mode, level, text, key1, key2):
    if mode == 'encrypt':
        return encrypt(level, text, key1, key2)

    elif mode == 'decrypt':
        return decrypt(level, text, key1, key2)

    else:
        print('\nError on Convert : Invalid Mode')
        raise TypeError



# app 
class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        
        self.title("")
        self.geometry("420x820")
        
        font_subhead = "Helvetica"
        size_subhead = 15
        weigh_head = "bold"
        size_button = 11

        ctk.CTkLabel(self, text="Text Encryption", font=("Poppins", 25, weigh_head), anchor="center").pack(pady=20)

        self.mode_var = ctk.StringVar(value="encrypt")
        self.level_var = ctk.StringVar(value="simple")
        
        ctk.CTkLabel(self, text="Mode", font=(font_subhead, size_subhead, weigh_head), anchor="center").pack(pady=8)
        ctk.CTkRadioButton(self, text="Encrypt", variable=self.mode_var, value="encrypt").pack(pady=6)
        ctk.CTkRadioButton(self, text="Decrypt", variable=self.mode_var, value="decrypt").pack(pady=6)

        ctk.CTkLabel(self, text="", font=("Poppins", 2), anchor="center").pack(pady=0.25)
        
        ctk.CTkLabel(self, text="Level", font=(font_subhead, size_subhead, weigh_head)).pack(pady=2)
        ctk.CTkRadioButton(self, text="Simple", variable=self.level_var, value="simple", command=self.update_key2_state).pack(pady=6)
        ctk.CTkRadioButton(self, text="Normal", variable=self.level_var, value="normal", command=self.update_key2_state).pack(pady=6)
        ctk.CTkRadioButton(self, text="Advanced", variable=self.level_var, value="advanced", command=self.update_key2_state).pack(pady=6)
        
        ctk.CTkLabel(self, text="", font=("Poppins", 2), anchor="center").pack(pady=0.25)

        ctk.CTkLabel(self, text="Text", font=(font_subhead, size_subhead, weigh_head)).pack(pady=1)
        self.text_entry = ctk.CTkEntry(self)
        self.text_entry.pack(pady=5)
        
        ctk.CTkLabel(self, text="Key 1", font=(font_subhead, size_subhead, weigh_head)).pack(pady=1)
        self.key1_entry = ctk.CTkEntry(self)
        self.key1_entry.pack(pady=5)
        
        ctk.CTkLabel(self, text="Key 2", font=(font_subhead, size_subhead, weigh_head)).pack(pady=1)
        self.key2_entry = ctk.CTkEntry(self, state="disabled")
        self.key2_entry.pack(pady=5)
        
        self.convert_button = ctk.CTkButton(self, text="Convert", font=(font_subhead, size_button, weigh_head), command=self.submit)
        self.convert_button.pack(pady=10)
        
        self.output_label = ctk.CTkLabel(self, text="   Result  ", font=(font_subhead, size_subhead, weigh_head), wraplength=300, anchor="center", justify="center")
        self.output_label.pack(pady=10, padx=10)

        self.output_display = ctk.CTkTextbox(self, height=75)
        self.output_display.pack(pady=5, padx=10)

        self.copy_button = ctk.CTkButton(self, text="Copy to Clipboard", font=(font_subhead, 11, weigh_head), command=self.copy_to_clipboard)
        self.copy_button.pack(pady=5)
        
    def update_key2_state(self):
        if self.level_var.get() in ["normal", "advanced"]:
            self.key2_entry.configure(state="normal")
        else:
            self.key2_entry.configure(state="disabled")
            self.key2_entry.delete(0, 'end')
    
    def validate_inputs(self, key1, key2):
        if not key1.isdigit():
            return False, "Key 1 must be an integer."
        if key2 and (" " in key2 or not key2.isalnum()):
            return False, "Key 2 must be a non-space string."
        return True, ""
    
    def submit(self):
        mode = self.mode_var.get()
        level = self.level_var.get()
        text = self.text_entry.get()
        key1 = self.key1_entry.get()
        key2 = self.key2_entry.get()
        
        is_valid, error_message = self.validate_inputs(key1, key2)
        if not is_valid:
            messagebox.showerror("Input Error", error_message)
            return
        
        key1 = int(key1)
        
        try:
            result = convert(mode, level, text, key1, key2)
            if result is None:
                raise ValueError("No result returned.")
            self.output_label.configure(text="Result:")
            self.output_display.delete("1.0", "end")
            self.output_display.insert("end", result)
        except Exception as e:
            self.output_label.configure(text="Error:")
            self.output_display.delete("1.0", "end")
            self.output_display.insert("end", str(e))
    
    def copy_to_clipboard(self):
        result_text = self.output_display.get("1.0", "end").strip()
        if result_text:
            pyperclip.copy(result_text)
            messagebox.showinfo("Clipboard", "Result copied to clipboard!")

if __name__ == "__main__":
    checkninstall()
    print('Opening App...')
    App().mainloop()
    print('App Closed')
