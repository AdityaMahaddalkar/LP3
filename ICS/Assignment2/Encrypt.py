from Utilities import *


class Encrypt:
    def __init__(self,text,Key0,Key1,Key2):
        self.text=text                #text to be encrypted
        self.Key0=Key0
        self.Key1=Key1
        self.Key2=Key2
        self.encrypt=text
        self.keys=[self.Key0,self.Key1,self.Key2]
        
    def mix_columns(self,word):
        '''
        C=M*S
        [C00,C01]      [1,4]     [S00,S01] 
                    =         * 
        [C10,C11]      [4,1]     [S10,S11]
        
        output=C00+C10+C01+C11 (add column wise)
        
        '''
        m=[[1,4],[4,1]]
        s=[[word[:4],word[4:8]],[word[8:12],word[12:]]]

        ans=[[0,0],[0,0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    ans[i][j]^=mul(m[i][k],binary_to_int(s[k][j]))
                ans[i][j]=int_to_binary(ans[i][j])
        res=""
        for i in range(2):
            for j in range(2):
                res+=ans[j][i]
        #print(res)
        return res
        #mix_columns("0010111011101110")
    def Simulate_Rounds(self):
        #Simulate 2 Rounds
        rnd=0
        while rnd <=2:
            step=1
            print('\t'+'-'*20+' Round '+str(rnd)+' '+'-'*20)
            
            #Step 1 : Substitute nibbles (Round 1 and 2)
            if rnd==1 or rnd==2:
                self.encrypt=SubNib(S_box,self.encrypt[:8])+SubNib(S_box,self.encrypt[8:])
                print('\t'+"Step {}(Substitute Nibbles) : {}".format(step,print_fun(self.encrypt)))
                step+=1

            #Step 2 : Shift Row i.e Swap Nibbles 2 and 4(Round 1 and 2)
            if rnd==1 or rnd==2:
                self.encrypt=self.encrypt[:4]+self.encrypt[12:]+self.encrypt[8:12]+self.encrypt[4:8]
                print('\t'+"Step {}(Shift Row) : {}".format(step,print_fun(self.encrypt)))
                step+=1

            #Step 3 : Mix column (Round 1 only)
            if rnd==1:
                self.encrypt=self.mix_columns(self.encrypt)
                print('\t'+"Step {}(Mix Columns) : {}".format(step,print_fun(self.encrypt)))
                step+=1

            #Step 4 : Add Round  Key (All rounds)
            self.encrypt=String_Xor(self.encrypt,self.keys[rnd])
            print('\t'+"Step {}(Add Round Key) : {}".format(step,print_fun(self.encrypt)))
            
            print('\t'+'After Round '+str(rnd)+' : '+print_fun(self.encrypt))
            rnd+=1
            
        
    def encrypt_text(self):
        self.Simulate_Rounds()
        return self.encrypt
