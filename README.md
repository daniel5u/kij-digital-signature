# KIJ Digital Signature
Python program to sign and verify digital signature on PDF usign RSA cipher and hash function.  
This program can also generate public and private key.  
Supported hash functions are listed below:
* SHA1
* SHA224
* SHA256
* SHA384
* SHA512

## Instalation
1. `pip install --no-input virtualenv`
2. Run `source venv/bin/activate` to enter virtualenv environtment
3. `pip install -r requirements.txt`
4. In virtualenv environtment, run `python3 app/main.py`
5. To exit virtualenv environtment, run `deactivate`

On PyCharm, mark `/app` directory as `Source Root` to avoid getting red line under imports.

## Base Root Path
* Base root path for file (`.pdf`) and key-pair (`.pem`) is equal to the given *directory path* in `/app/constant.py`.  
* Base root path for file (`.pdf`) can be overridden by inserting absolute path as input.
* Private key and public key filename is equal to the fiven name in `/app/constant.py`.
