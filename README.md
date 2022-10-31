# KIJ Digital Signature

## Instalasi
1. `sudo pip install --no-input virtualenv`
2. Jalankan `source venv/bin/activate` untuk masuk ke dalam environtment virtualenv
3. `pip install -r requirements.txt`
4. Di dalam environtment virtualenv, jalankan `python3 app/main.py`
5. Untuk keluar dari environtment virtualenv, tulis `deactivate` pada terminal

## Base Path
* *Base root path* untuk file (`.pdf`), *key-pair* (`.pem`), dan *signature*
sesuai dengan *directory path* yang diberikan pada file `/app/constant.py`.  
* *Base root path* untuk file (`.pdf`) dan *signature* bisa di-override dengan memasukkan *absolute path* sebagai input.
* Nama file untuk *private key* dan *public key* sesuai dengan nama yang diberikan pada file `/app/constant.py`.
