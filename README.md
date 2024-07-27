# Secure Password Manager

## Overview

This Password Manager is a tool designed for secure storage and management of passwords. It employs advanced cryptographic techniques to ensure the confidentiality and integrity of sensitive data.

## Security Features

1. **Password Confidentiality**
   - Uses AES encryption in EAX mode, providing authenticated encryption
   - Ensures confidentiality, data integrity, and protection against replay attacks
   - Encryption key is derived from the master password using scrypt, enhancing security

2. **Address Confidentiality**
   - Implements SHA-256 hashing for storing addresses
   - Only hash values are stored in the database, preserving the confidentiality of original addresses

3. **Data Integrity**
   - Employs authenticated encryption (AES in EAX mode)
   - Generates an authentication tag for each encrypted password
   - Verifies integrity during decryption, preventing undetected alterations and substitution attacks

## Prerequisites

- Python 3.x
- Required packages:
  ```
  pip install pycryptodome typer
  ```

## Usage

### Initializing the Password Manager
```
python3 password_manager.py init "<master_password>"
```

### Storing a Password
```
python3 password_manager.py put "<master_password>" "<address>" "<password>"
```

### Retrieving a Password
```
python3 password_manager.py get "<master_password>" "<address>"
```

### Updating the Master Password
```
python3 password_manager.py reinit "<old_master_password>" "<new_master_password>"
```

### Resetting the Password Manager
```
python3 password_manager.py reset "<master_password>"
```

### Accessing Help
```
python3 password_manager.py --help
```

## Technical Details

- **Encryption**: AES (Advanced Encryption Standard) in EAX (Encrypt-then-Authenticate-then-Translate) mode
- **Hashing**: SHA-256 (Secure Hash Algorithm 256-bit)
- **Key Derivation**: scrypt function for generating encryption keys from the master password

## Security Considerations

- The security of the system is fundamentally dependent on the strength and confidentiality of the master password
- Regularly update your master password to maintain optimal security
- Ensure your system is free from malware and keyloggers

## Future Enhancements

- Implement a password strength checker
- Add multi-factor authentication
- Develop a graphical user interface for improved usability

## Disclaimer

This tool is designed for personal use and educational purposes. Always follow best practices for password management and regularly back up your data.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
