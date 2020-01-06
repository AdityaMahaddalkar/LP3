
from Utilities import *
from Encrypt import *
from Decrypt import *


if __name__=='__main__':
    
    
    
    
    text_1=input("Enter sentence : ")
    
    key="0100101011110101"

    stream=convert_sentence_to_16_bit_stream(text_1)
    #print(stream)
    
    #print(len(stream))
    
    Key0,Key1,Key2=generate_key(key=key)
    
    ciphertext=[]
    print()
    print('*'*20+'Encryption phase'+'*'*20)
    print()
    for block in stream:
            
    
        encrypt=Encrypt(text=block,Key0=Key0,Key1=Key1,Key2=Key2)
        ciphertext.append(encrypt.encrypt_text())
    
    print('Ciphertext==')
    print(''.join(ciphertext))
    
    
    print()
    print('*'*20+'Decryption phase'+'*'*20)
    print()
    
    final_text=[]
    for block in ciphertext:
        decrypt=Decrypt(ciphertext=block,Key0=Key0,Key1=Key1,Key2=Key2)
        final_text.append(decrypt.decrypt_text())
    #print(final_text)
    ans=convert_16_bit_stream_to_sentence(final_text)
    if ans==text_1:
        print('Decryption Successful!!!!')
        print('Original text : {}'.format(text_1))
        print('Decrypted text : {}'.format(ans))
    else:
        print('Error')
    print()
    print('*'*15+"End of Decryption phase"+'*'*15)
    
    
        
    '''

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
        
    '''    