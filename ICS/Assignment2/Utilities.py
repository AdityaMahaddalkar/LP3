#Utilities Required

#1 S-box
S_box={
    
    "0000":"1001",
    "0001":"0100",
    "0010":"1010",
    "0011":"1011",
    "0100":"1101",
    "0101":"0001",
    "0110":"1000",
    "0111":"0101",
    "1000":"0110",
    "1001":"0010",
    "1010":"0000",
    "1011":"0011",
    "1100":"1100",
    "1101":"1110",
    "1110":"1111",
    "1111":"0111",
    
    
}

#2 Inverse S-box
# For inverse S-box substitution in decryption

key_list=list(S_box.keys())
value_list=list(S_box.values())

Inverse_S_box={}
for i in range(len(key_list)):
    Inverse_S_box[value_list[i]]=key_list[i]
#print(Inverse_S_box['1010'])

#Fancy printing the nibbles
def print_fun(s):
    i=0
    ans=""
    while i<len(s):
        ans+=s[i:i+4]+" "
        i+=4
    return ans
#print_fun("10101010")

#Utility  functions

#1 Rotate nibbles in a byte
def RotateNibble(byte):
    first,second=byte[:4],byte[4:]
    first,second=second,first
    #byte=first+second
    #print(byte)
    return first+second


#2 Substitute a nibble using either S-box mapping or Inverse S-box mapping

def SubNib(mapping,byte):
    first,second=byte[:4],byte[4:]
    first=mapping[first]
    second=mapping[second]
    #word=first+second
    #print(word)
    return first+second
#SubNib(S_box,"01011111")

#3 XOR of two words
def String_Xor(word1,word2):
    t1=list(map(int,list(word1)))
    t2=list(map(int,list(word2)))
    
    ans=[str(x^y) for x,y in zip(t1,t2)]
    #print("".join(ans))
    return "".join(ans)
#String_Xor("01001010","10000000")
    
#4 Multiplication based on GF(16)

def mul(a,b):

    bits=[1<<0,1<<1,1<<2,1<<3,1<<4,1<<5,1<<6,1<<7]
    if a==0 or b==0:
        return 0
    elif a==1:
        return b
    elif b==1:
        return a
    res=0
    for i in range(4):
        for j in range(4):
            if((a & bits[i])!=0 and (b&bits[j])):
                res^=bits[i+j]
    
    if res>=8:
        ok=False
        while not ok:
            ok=True
            for i in range(4,7):
                if res & bits[i]!=0:
                    res^=bits[i]
                    j=i-4
                    res^=bits[j]
                    res^=bits[j+1]
                    ok=False
    return res

#5 Convert bitsting to int
def binary_to_int(nibble):
    res=0
    p=len(nibble)-1
    num=list(map(int,list(nibble)))
    for i in num:
        res+=((2**p)*i)
        p-=1
    return res
#binary_to_int("10001")


#6 Convert int to bitstring

def int_to_binary(num):
    ans=[]
    while num>0:
        ans.append(str(num%2))
        num=int(num/2)
    while(len(ans)!=4):
        ans.append('0')
    ans.reverse()
    return "".join(ans)
#int_to_binary(3)


#7 Generate keys for each round

'''
2 rounds are simulated 
Hence 3 keys are required
'''

def generate_key(key):
    w0=key[:8]
    w1=key[8:]
    w2=""
    w3=""
    w4=""
    w5=""

    print("w0 : {}\nw1 : {}".format(print_fun(w0),print_fun(w1)))

    w2=String_Xor(String_Xor("10000000",SubNib(S_box,RotateNibble(w1))),w0)
    print("w2 : {}".format(print_fun(w2)))

    w3=String_Xor(w2,w1)
    print("w3 : {}".format(print_fun(w3)))

    w4=String_Xor(String_Xor("00110000",SubNib(S_box,RotateNibble(w3))),w2)
    print("w4 : {}".format(print_fun(w4)))

    w5=String_Xor(w4,w3)
    print("w5 : {}".format(print_fun(w5)))
    
    Key0=w0+w1
    Key1=w2+w3
    Key2=w4+w5
    
    print('-'*20+' Keys '+'-'*20)
    print("Key 0 (w0+w1) : {}".format(print_fun(Key0)))
    print("Key 1 (w2+w3) : {}".format(print_fun(Key1)))
    print("Key 2 (w4+w5) : {}".format(print_fun(Key2)))
    
    return Key0,Key1,Key2
