import unittest
from unittest.mock import patch, MagicMock
import customtkinter as ctk
import pyperclip
from tkinter import messagebox
from cipher_cli import convert
from cipher_app import App

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = App()
        
    def tearDown(self):
        self.app.destroy()

    @patch('cipher_cli.convert')
    def test_submit_encrypt_simple(self, mock_convert):
        mock_convert.return_value = "simple_encrypted"
        
        # Set up the GUI state
        self.app.mode_var.set("encrypt")
        self.app.level_var.set("simple")
        self.app.text_entry.insert(0, "test text")
        self.app.key1_entry.insert(0, "1234")
        
        # Simulate clicking the convert button
        self.app.submit()
        
        # Check if the convert function was called with correct arguments
        mock_convert.assert_called_once_with("encrypt", "simple", "test text", 1234, "")
        
        # Check the output display
        result_text = self.app.output_display.get("1.0", "end").strip()
        self.assertEqual(result_text, "simple_encrypted")
    
    @patch('cipher_cli.convert')
    def test_submit_encrypt_normal(self, mock_convert):
        mock_convert.return_value = "normal_encrypted"
        
        # Set up the GUI state
        self.app.mode_var.set("encrypt")
        self.app.level_var.set("normal")
        self.app.text_entry.insert(0, "test text")
        self.app.key1_entry.insert(0, "1234")
        self.app.key2_entry.configure(state="normal")
        self.app.key2_entry.insert(0, "key2")
        
        # Simulate clicking the convert button
        self.app.submit()
        
        # Check if the convert function was called with correct arguments
        mock_convert.assert_called_once_with("encrypt", "normal", "test text", 1234, "key2")
        
        # Check the output display
        result_text = self.app.output_display.get("1.0", "end").strip()
        self.assertEqual(result_text, "normal_encrypted")

    @patch('cipher_cli.convert')
    def test_submit_invalid_key1(self, mock_convert):
        # Set up the GUI state
        self.app.mode_var.set("encrypt")
        self.app.level_var.set("simple")
        self.app.text_entry.insert(0, "test text")
        self.app.key1_entry.insert(0, "invalid")
        
        with patch.object(messagebox, 'showerror') as mock_showerror:
            # Simulate clicking the convert button
            self.app.submit()
            
            # Check if the error message was shown
            mock_showerror.assert_called_once_with("Input Error", "Key 1 must be an integer.")
            
            # Check that convert was not called
            mock_convert.assert_not_called()

    @patch('cipher_cli.convert')
    def test_submit_invalid_key2(self, mock_convert):
        # Set up the GUI state
        self.app.mode_var.set("encrypt")
        self.app.level_var.set("normal")
        self.app.text_entry.insert(0, "test text")
        self.app.key1_entry.insert(0, "1234")
        self.app.key2_entry.configure(state="normal")
        self.app.key2_entry.insert(0, "invalid key2")
        
        with patch.object(messagebox, 'showerror') as mock_showerror:
            # Simulate clicking the convert button
            self.app.submit()
            
            # Check if the error message was shown
            mock_showerror.assert_called_once_with("Input Error", "Key 2 must be a non-space string.")
            
            # Check that convert was not called
            mock_convert.assert_not_called()

    @patch('pyperclip.copy')
    def test_copy_to_clipboard(self, mock_copy):
        # Simulate setting the output display text
        self.app.output_display.insert("1.0", "test result")
        
        with patch.object(messagebox, 'showinfo') as mock_showinfo:
            # Simulate clicking the copy button
            self.app.copy_to_clipboard()
            
            # Check if pyperclip.copy was called with the correct text
            mock_copy.assert_called_once_with("test result")
            
            # Check if the info message was shown
            mock_showinfo.assert_called_once_with("Clipboard", "Result copied to clipboard!")

if __name__ == "__main__":
    unittest.main()
