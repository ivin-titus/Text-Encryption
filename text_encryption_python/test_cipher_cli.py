import unittest
from unittest.mock import patch, MagicMock
import sys
from io import StringIO
from cipher_cli import encrypt, decrypt, convert, usage


simple = MagicMock()
normal = MagicMock()
advanced = MagicMock()

simple.encrypt = MagicMock(return_value="simple_encrypted")
simple.decrypt = MagicMock(return_value="simple_decrypted")

normal.encrypt = MagicMock(return_value="normal_encrypted")
normal.decrypt = MagicMock(return_value="normal_decrypted")

advanced.encrypt = MagicMock(return_value="advanced_encrypted")
advanced.decrypt = MagicMock(return_value="advanced_decrypted")


class TestCipherFunctions(unittest.TestCase):

    def test_encrypt_simple(self):
        result = encrypt('simple', 'test', 1234)
        self.assertEqual(result, "simple_encrypted")

    def test_encrypt_normal(self):
        result = encrypt('normal', 'test', 1234, 'key2')
        self.assertEqual(result, "normal_encrypted")

    def test_encrypt_advanced(self):
        result = encrypt('advanced', 'test', 1234, 'key2')
        self.assertEqual(result, "advanced_encrypted")

    def test_decrypt_simple(self):
        result = decrypt('simple', 'test', 1234)
        self.assertEqual(result, "simple_decrypted")

    def test_decrypt_normal(self):
        result = decrypt('normal', 'test', 1234, 'key2')
        self.assertEqual(result, "normal_decrypted")

    def test_decrypt_advanced(self):
        result = decrypt('advanced', 'test', 1234, 'key2')
        self.assertEqual(result, "advanced_decrypted")

    def test_convert_encrypt_simple(self):
        result = convert('encrypt', 'simple', 'test', 1234, None)
        self.assertEqual(result, "simple_encrypted")

    def test_convert_encrypt_normal(self):
        result = convert('encrypt', 'normal', 'test', 1234, 'key2')
        self.assertEqual(result, "normal_encrypted")

    def test_convert_encrypt_advanced(self):
        result = convert('encrypt', 'advanced', 'test', 1234, 'key2')
        self.assertEqual(result, "advanced_encrypted")

    def test_convert_decrypt_simple(self):
        result = convert('decrypt', 'simple', 'test', 1234, None)
        self.assertEqual(result, "simple_decrypted")

    def test_convert_decrypt_normal(self):
        result = convert('decrypt', 'normal', 'test', 1234, 'key2')
        self.assertEqual(result, "normal_decrypted")

    def test_convert_decrypt_advanced(self):
        result = convert('decrypt', 'advanced', 'test', 1234, 'key2')
        self.assertEqual(result, "advanced_decrypted")

    def test_invalid_encrypt(self):
        with self.assertRaises(TypeError):
            encrypt('invalid', 'test', 1234)

    def test_invalid_decrypt(self):
        with self.assertRaises(TypeError):
            decrypt('invalid', 'test', 1234)

    def test_invalid_convert(self):
        with self.assertRaises(TypeError):
            convert('invalid', 'simple', 'test', 1234, None)

    def test_usage(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        usage()
        sys.stdout = sys.__stdout__
        self.assertIn("Usage : python filename.py mode level key1 key2[optional]", captured_output.getvalue())

if __name__ == "__main__":
    unittest.main()
