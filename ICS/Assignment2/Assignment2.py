
from Utilities import *
from Encrypt import *
from Decrypt import *

if __name__=='__main__':

    key="0100101011110101"
    
    text="1101011100101000"


    Key0,Key1,Key2=generate_key(key=key)
    
    print()
    print('*'*20+'Encryption phase'+'*'*20)
    print()
    
    
    
    encrypt=Encrypt(text=text,Key0=Key0,Key1=Key1,Key2=Key2)
    ciphertext=encrypt.encrypt_text()
    
    print()
    print("Ciphertext : {}".format(print_fun(ciphertext)))
    print()
    print('*'*15+"End of Encryption phase"+'*'*15)
    
    
    
    print()
    print('*'*20+'Decryption phase'+'*'*20)
    print()
    
    decrypt=Decrypt(ciphertext=ciphertext,Key0=Key0,Key1=Key1,Key2=Key2)
    final_text=decrypt.decrypt_text()

    print()
    if final_text==text:
        print('Decryption Successful!!!')
        print('Original text : {}'.format(print_fun(text)))
        print('Decrypted text : {}'.format(print_fun(final_text)))
    else:
        print('Error')
    print()
    print('*'*15+"End of Decryption phase"+'*'*15)
        