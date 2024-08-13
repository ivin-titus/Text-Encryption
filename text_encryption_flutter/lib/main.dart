import 'dart:io';
import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

String simpleDecrypt(String word, int key) {
  List<String> cypher = [];

  for (int i = 0; i < word.length; i++) {
    String char = word[i];
    if (RegExp(r'[a-zA-Z]').hasMatch(char)) {
      int base = char.codeUnitAt(0) >= 'a'.codeUnitAt(0)
          ? 'a'.codeUnitAt(0)
          : 'A'.codeUnitAt(0);
      String decryptedChar = String.fromCharCode(
          (char.codeUnitAt(0) - base + 26 - key) % 26 + base);
      cypher.add(decryptedChar);
    } else {
      cypher.add(char);
    }
  }

  return cypher.join('');
}

String simpleEncrypt(String word, int key) {
  List<String> cypher = [];

  for (int i = 0; i < word.length; i++) {
    String char = word[i];
    if (RegExp(r'[a-zA-Z]').hasMatch(char)) {
      int base = char.codeUnitAt(0) >= 'a'.codeUnitAt(0)
          ? 'a'.codeUnitAt(0)
          : 'A'.codeUnitAt(0);
      String encryptedChar =
          String.fromCharCode((char.codeUnitAt(0) - base + key) % 26 + base);
      cypher.add(encryptedChar);
    } else {
      cypher.add(char);
    }
  }

  return cypher.join('');
}

String normalEncrypt(String text, int intKey, String strKey) {
  String encryptedText = "";
  int strKeyIndex = 0;

  for (int i = 0; i < text.length; i++) {
    String char = text[i];
    if (RegExp(r'[a-zA-Z]').hasMatch(char)) {
      int shift =
          (strKey.codeUnitAt(strKeyIndex) - 'a'.codeUnitAt(0) + intKey) % 26;
      if (char.codeUnitAt(0) >= 'A'.codeUnitAt(0) &&
          char.codeUnitAt(0) <= 'Z'.codeUnitAt(0)) {
        encryptedText += String.fromCharCode(
            (char.codeUnitAt(0) + shift - 'A'.codeUnitAt(0)) % 26 +
                'A'.codeUnitAt(0));
      } else {
        encryptedText += String.fromCharCode(
            (char.codeUnitAt(0) + shift - 'a'.codeUnitAt(0)) % 26 +
                'a'.codeUnitAt(0));
      }
      strKeyIndex = (strKeyIndex + 1) % strKey.length;
    } else {
      encryptedText += char;
    }
  }
  return encryptedText;
}

String normalDecrypt(String encryptedText, int intKey, String strKey) {
  String decryptedText = "";
  int strKeyIndex = 0;

  for (int i = 0; i < encryptedText.length; i++) {
    String char = encryptedText[i];
    if (RegExp(r'[a-zA-Z]').hasMatch(char)) {
      int shift =
          (strKey.codeUnitAt(strKeyIndex) - 'a'.codeUnitAt(0) + intKey) % 26;
      if (char.codeUnitAt(0) >= 'A'.codeUnitAt(0) &&
          char.codeUnitAt(0) <= 'Z'.codeUnitAt(0)) {
        decryptedText += String.fromCharCode(
            (char.codeUnitAt(0) - shift - 'A'.codeUnitAt(0)) % 26 +
                'A'.codeUnitAt(0));
      } else {
        decryptedText += String.fromCharCode(
            (char.codeUnitAt(0) - shift - 'a'.codeUnitAt(0)) % 26 +
                'a'.codeUnitAt(0));
      }
      strKeyIndex = (strKeyIndex + 1) % strKey.length;
    } else {
      decryptedText += char;
    }
  }
  return decryptedText;
}

int deriveKey(String strKey) {
  return strKey.codeUnits.fold(0, (sum, char) => sum + char);
}

String advancedEncrypt(String text, int intKey, String strKey) {
  String encryptedText = "";
  int derivedKey = deriveKey(strKey);
  for (int i = 0; i < text.length; i++) {
    int charCode = text.codeUnitAt(i);
    encryptedText += String.fromCharCode(charCode + derivedKey + intKey);
  }
  return encryptedText;
}

String advancedDecrypt(String encryptedText, int intKey, String strKey) {
  String decryptedText = "";
  int derivedKey = deriveKey(strKey);
  for (int i = 0; i < encryptedText.length; i++) {
    int charCode = encryptedText.codeUnitAt(i);
    // Check if the decrypted character is within the valid Unicode range
    int decryptedCharCode = charCode - derivedKey - intKey;
    if (decryptedCharCode >= 0 && decryptedCharCode <= 0x10FFFF) {
      decryptedText += String.fromCharCode(decryptedCharCode);
    } else {
      // If not, append a replacement character
      decryptedText += '\uFFFD';
    }
  }
  return decryptedText;
}

void usage() {
  print(
      '''Usage : dart filename.dart mode level key1 key2[optional] ( if its command line operation )
  Allowed modes : encrypt , decrypt
  Allowed Levels : simple, normal, advanced
  Key1 : Required - only integer value allowed
  Key2: Required if level is normal or advanced, only string value allowed(no special characters or whitespace allowed) ''');
}

String encrypt(String level, String text, int key1, [String? key2]) {
  if (level == 'simple') {
    return simpleEncrypt(text, key1);
  } else if (level == 'normal') {
    if (key2 == null) {
      print('\nError on Encrypt : Key2 Missing ');
      throw TypeError;
    }
    return normalEncrypt(text, key1, key2);
  } else if (level == 'advanced') {
    if (key2 == null) {
      print('\nError on Encrypt : Key2 Missing ');
      throw TypeError;
    }
    return advancedEncrypt(text, key1, key2);
  } else {
    print('\nError on Encrypt : Invalid Level ');
    throw TypeError;
  }
}

String decrypt(String level, String text, int key1, [String? key2]) {
  if (level == 'simple') {
    return simpleDecrypt(text, key1);
  } else if (level == 'normal') {
    if (key2 == null) {
      print('\nError on Decrypt : Key2 Missing');
      throw TypeError;
    }
    return normalDecrypt(text, key1, key2);
  } else if (level == 'advanced') {
    if (key2 == null) {
      print('\nError on Decrypt : Key2 Missing');
      throw TypeError;
    }
    return advancedDecrypt(text, key1, key2);
  } else {
    print('\nError on Decrypt : Invalid Level');
    throw TypeError;
  }
}

String convert(String mode, String level, String text, int key1,
    [String? key2]) {
  if (mode == 'encrypt') {
    return encrypt(level, text, key1, key2);
  } else if (mode == 'decrypt') {
    return decrypt(level, text, key1, key2);
  } else {
    print('\nError on Convert : Invalid Mode');
    throw TypeError;
  }
}

class App extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Text Encryption',
      themeMode: ThemeMode.system, // Set theme according to system
      theme: ThemeData(
        brightness: Brightness.light,
        primarySwatch: Colors.blue,
      ),
      darkTheme: ThemeData(
        brightness: Brightness.dark,
        primarySwatch: Colors.blue,
      ),
      home: Scaffold(
        appBar: AppBar(
          title: Text(
            'Text Encryption',
            style: TextStyle(fontWeight: FontWeight.bold),
          ),
        ),
        body: EncryptionForm(),
      ),
    );
  }
}

class EncryptionForm extends StatefulWidget {
  @override
  _EncryptionFormState createState() => _EncryptionFormState();
}

class _EncryptionFormState extends State<EncryptionForm> {
  String mode = 'encrypt';
  String level = 'simple';
  String text = '';
  String key1 = '';
  String key2 = '';
  String result = '';

  void updateKey2State() {
    setState(() {
      if (level == 'normal' || level == 'advanced') {
        key2 = '';
      }
    });
  }

  bool validateInputs(String key1, String key2) {
    if (int.tryParse(key1) == null) {
      return false;
    }
    if (level != 'simple' &&
        (key2.isEmpty ||
            key2.contains(' ') ||
            !RegExp(r'^[a-zA-Z]+$').hasMatch(key2))) {
      return false;
    }
    return true;
  }

  void submit() {
    if (!validateInputs(key1, key2)) {
      ScaffoldMessenger.of(context)
          .showSnackBar(SnackBar(content: Text('Input Error')));
      return;
    }
    if ((level == 'normal' || level == 'advanced') && key2.isEmpty) {
      showDialog(
        context: context,
        builder: (BuildContext context) {
          return AlertDialog(
            title: Text('Warning'),
            content: Text('Please enter Key 2 for Normal and Advanced levels'),
            actions: [
              TextButton(
                child: Text('OK'),
                onPressed: () {
                  Navigator.of(context).pop();
                },
              ),
            ],
          );
        },
      );
      return;
    }
    int key1Int = int.parse(key1);
    try {
      String res =
          convert(mode, level, text, key1Int, key2.isEmpty ? null : key2);
      setState(() {
        result = res;
      });
    } catch (e) {
      setState(() {
        result = 'Error: $e';
        mode = 'encrypt';
        level = 'simple';
        text = '';
        key1 = '';
        key2 = '';
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(16.0),
      child: Column(
        children: [
          SizedBox(height: 18), // Add some space between buttons

          Text(
            'Mode',
            style: TextStyle(
              fontWeight: FontWeight.bold,
              fontSize: 18,
            ),
          ),
          Row(
            children: [
              Radio(
                value: 'encrypt',
                groupValue: mode,
                onChanged: (value) {
                  setState(() {
                    mode = value.toString();
                  });
                },
              ),
              Text('Encrypt'),
              Radio(
                value: 'decrypt',
                groupValue: mode,
                onChanged: (value) {
                  setState(() {
                    mode = value.toString();
                  });
                },
              ),
              Text('Decrypt'),
            ],
          ),
          SizedBox(height: 18), // Add some space between buttons
          Text(
            'Level',
            style: TextStyle(
              fontWeight: FontWeight.bold,
              fontSize: 18,
            ),
          ),
          Row(
            children: [
              Radio(
                value: 'simple',
                groupValue: level,
                onChanged: (value) {
                  setState(() {
                    level = value.toString();
                    updateKey2State();
                  });
                },
              ),
              SizedBox(height: 18), // Add some space between buttons
              Text('Simple'),
              Radio(
                value: 'normal',
                groupValue: level,
                onChanged: (value) {
                  setState(() {
                    level = value.toString();
                    updateKey2State();
                  });
                },
              ),
              Text('Normal'),
              Radio(
                value: 'advanced',
                groupValue: level,
                onChanged: (value) {
                  setState(() {
                    level = value.toString();
                    updateKey2State();
                  });
                },
              ),
              Text('Advanced'),
            ],
          ),
          SizedBox(height: 18), // Add some space between buttons
          TextField(
            decoration: InputDecoration(labelText: 'Text'),
            onChanged: (value) {
              text = value;
            },
          ),
          SizedBox(height: 18), // Add some space between buttons
          TextField(
            decoration: InputDecoration(labelText: 'Key 1'),
            onChanged: (value) {
              key1 = value;
            },
          ),
          SizedBox(height: 18), // Add some space between buttons
          if (level == 'normal' || level == 'advanced')
            TextField(
              decoration: InputDecoration(labelText: 'Key 2'),
              onChanged: (value) {
                key2 = value;
              },
            ),
          SizedBox(height: 18), // Add some space between buttons

          ElevatedButton(
            onPressed: submit,
            child: Text('Convert'),
          ),
          TextField(
            readOnly: true,
            decoration: InputDecoration(labelText: 'Result'),
            controller: TextEditingController(text: result),
          ),
          SizedBox(height: 18),

          ElevatedButton(
            onPressed: () {
              Clipboard.setData(ClipboardData(text: result));
              ScaffoldMessenger.of(context)
                  .showSnackBar(SnackBar(content: Text('Copied to clipboard')));
            },
            child: Text('Copy to Clipboard'),
          ),
          SizedBox(height: 206.3), // Add some space between buttons
          Text("©️ Ivin Techz 2024")
        ],
      ),
    );
  }
}

void main() {
  runApp(App());
}
