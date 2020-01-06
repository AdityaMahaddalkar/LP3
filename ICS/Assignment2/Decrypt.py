from Utilities import *


class Decrypt:
    def __init__(self,ciphertext,Key0,Key1,Key2):
        self.ciphertext=ciphertext                #text to be encrypted
        self.Key0=Key0
        self.Key1=Key1
        self.Key2=Key2
        self.text=ciphertext
        self.keys=[self.Key0,self.Key1,self.Key2]
        
    def inverse_mix_columns(self,word):
        '''
        C=M*S
        [C00,C01]      [9,2]     [S00,S10] 
                    =         * 
        [C10,C11]      [2,9]     [S01,S11]
        
        output=C00+C01+C10+C11 (add row wise)
        
        '''
        m=[[9,2],[2,9]]
        s=[[word[:4],word[8:12]],[word[4:8],word[12:]]]

        ans=[[0,0],[0,0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    ans[i][j]^=mul(m[i][k],binary_to_int(s[k][j]))
                ans[i][j]=int_to_binary(ans[i][j])
        res=""
        for i in range(2):
            for j in range(2):
                res+=ans[i][j]
        #print(res)
        return res
        #inverse_mix_columns("1111011000110011")
    
    def Simulate_Rounds(self):
        #Simulate 2 Rounds
        rnd=2
        while rnd >=0:
            step=1
            #print('\t'+'-'*10+'Reversing Round '+str(rnd)+' '+'-'*10)
            
            #Step 1 : Add Round  Key (All rounds)
            self.ciphertext=String_Xor(self.ciphertext,self.keys[rnd])
            #print('\t'+"Step {}(Add Round Key) : {}".format(step,print_fun(self.ciphertext)))
            
            step+=1
            
            #Step 2 : Inverse Mix column (Round 1 only)
            if rnd==1:
                self.ciphertext=self.inverse_mix_columns(self.ciphertext)
                #print('\t'+"Step {}(Mix Columns) : {}".format(step,print_fun(self.ciphertext)))
                step+=1
            

            
            #Step 3 : Inverse Shift row same as shift row (swap nibbles 2 and 4)

            if rnd==1 or rnd==2:
                self.ciphertext=self.ciphertext[:4]+self.ciphertext[12:]+self.ciphertext[8:12]+self.ciphertext[4:8]
                #print('\t'+"Step {}(Shift Row) : {}".format(step,print_fun(self.ciphertext)))
                step+=1

            
            #Step 4 : Substitute nibbles (Round 1 and 2)
            if rnd==1 or rnd==2:
                self.ciphertext=SubNib(Inverse_S_box,self.ciphertext[:8])+SubNib(Inverse_S_box,self.ciphertext[8:])
                #print('\t'+"Step {}(Substitute Nibbles) : {}".format(step,print_fun(self.ciphertext)))
                step+=1

            
            #print('\tAfter Round '+str(rnd)+' : '+print_fun(self.ciphertext))
            
            rnd-=1
            
            
        
    def decrypt_text(self):
        self.Simulate_Rounds()
        return self.ciphertext
