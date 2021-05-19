# Ransomware
Ransomware Application coded in Python used to simulate a ransomware attack against a target computer

KeyGenAndEncrypt.py

The role of this program is to generate public and private key that will be used later in the Ransomware and Recovery programs. Public key is stored in “Ransompubkey.pem” and private key is stored in “Ransomprvkey.pem”. 

Ransomware.py

This program is mainly responsible for the encryption of files stored in in the same directory as the Ransomware.py in the victim's computer.

The process of the program is as follows: 
- First we get a random 256 bit key(AES_key) . 
- Then a cipher is generated using that key and used to encrypt text files stored in the same directory as the Ransomware.py. 
- Next, we encrypt the key that was used generated randomly earlier, and using the public key generated earlier and stored in “Ransompubkey.pem”, we will encrypt the key and store it in a “key.bin” file. 
- Next, within the program, the AES key is deallocated and deleted away
- Next we generate a ransom note that displays a generated text file with instructions for the victim. This is stored in a file called RANSOMNOTE.txt
- Lastly, all pye files will be commented out and a copy of the code in Ransomware.py will be printed in the pye files.


Recovery.py

This program has 2 roles. Decrypt “Key.bin” file and Decrypt text files previously encrypted by “Ransomware.py”

First, the program will decrypt the AES key using the private key that was stored 
in the ransomprvkey.pem file. This AES key is found in the key.bin file that was
previously sent back to the hacker by the victim after paying the ransom. This decrypted
key is encoded and then stored a txt file call key.txt

Secondly, We will use the AES key to create a cipher in AES CBC mode and we will decrypt the text files that we encrypted earlier on during the runtime of the Ransomware.py main program


HOW TO RUN: 
Program should be runned in the order as follows:
1.	KeyGenAndEncrypt.py
2.	Ransomware.py
3.	Recovery.py
