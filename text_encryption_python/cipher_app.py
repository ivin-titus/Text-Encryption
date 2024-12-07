import customtkinter as ctk
from tkinter import messagebox
import pyperclip  
from cipher_cli import convert  
from package_check import checkninstall

class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        
        self.title("©️ 2024 Ivin Titus")
        self.geometry("420x820")
        # self.iconbitmap("logo.ico")

        font_subhead = "Helvetica"
        size_subhead = 15
        weigh_head = "bold"
        size_button = 11

        ctk.CTkLabel(self, text="Text Encryption", font=("Poppins", 30, weigh_head), anchor="center").pack(pady=20)

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
