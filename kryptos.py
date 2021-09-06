
import numpy as np

class Krux:
    
    def __init__(self):
        # Complete
        self.k_1 = "EMUFPHZLRFAXYUSDJKZLDKRNSHGNFIVJYQTQUXQBQVYUVLLTREVJYQTMKYRDMFD"
        # Complete
        self.k_2 = "VFPJUDEEHZWETZYVGWHKKQETGFQJNCEGGWHKK?DQMCPFQZDQMMIAGPFXHQRLGTIMVMZJANQLVKQEDAGDVFRPJUNGEUNAQZGZLECGYUXUEENJTBJLBQCRTBJDFHRRYIZETKZEMVDUFKSJHKFWHKUWQLSZFTIHHDDDUVH?DWKBFUFPWNTDFIYCUQZEREEVLDKFEZMOQQJLTTUGSYQPFEUNLAVIDXFLGGTEZ?FKZBSFDQVGOGIPUFXHHDRKFFHQNTGPUAECNUVPDJMQCLQUMUNEDFQELZZVRRGKFFVOEEXBDMVPNFQXEZLGREDNQFMPNZGLFLPMRJQYALMGNUVPDXVKPDQUMEBEDMHDAFMJGZNUPLGESWJLLAETG"
        # Complete
        self.k_3 = "ENDYAHROHNLSRHEOCPTEOIBIDYSHNAIACHTNREYULDSLLSLLNOHSNOSMRWXMNETPRNGATIHNRARPESLNNELEBLPIIACAEWMTWNDITEENRAHCTENEUDRETNHAEOETFOLSEDTIWENHAEIOYTEYQHEENCTAYCREIFTBRSPAMHHEWENATAMATEGYEERLBTEEFOASFIOTUETUAEOTOARMAEERTNRTIBSEDDNIAAHTTMSTEWPIEROAGRIEWFEBAECTDDHILCEIHSITEGOEAOSDDRYDLORITRKLMLEHAGTDHARDPNEOHMGFMFEUHEECDMRIPFEIMEHNLSSTTRTVDOHW?"
        self.k_4 = "OBKRUOXOGHULBSOLIFBBWFLRVQQPRNGKSSOTWTQSJQSSEKZZWATJKLUDIAWINFBNYPVTTMZFPKWGDKZXTJCDIGKUHUAUEKCAR"
        self.k_5 = ""
        self.kalpha = "KRYPTOSABCDEFGHIJLMNQUVWXZ"
        self.alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.pk_1 = "PALIMPSEST" # 10 Count Word
        self.pk_2 = "ABSCISSA" # 8 Count Word
        self.pk_3 = " SLOWLY\n DESPARATLY SLOWLY\n THE REMAINS OF PASSAGE DEBRIS THAT ENCUMBERED THE LOWER PART OF THE DOORWAY WAS REMOVED\n WITH TREMBLING HANDS I MADE A TINY BREACH IN THE UPPER LEFT HAND CORNER\n AND THEN WIDENING THE HOLE A LITTLE I INSERTED THE CANDLE AND PEERED IN\n THE HOT AIR ESCAPING FROM THE CHAMBER CAUSED THE FLAME TO FLICKER\n BUT PRESENTLY DETAILS OF THE ROOM WITHIN EMERGED FROM THE MIST\n X CAN YOU SEE ANYTHING Q?" # A Series of Transformations
        self.pk_4a = "EASTNORTHEAST" # 22<=34
        self.pk_4b = "BERLINCLOCK" # 64<=74

# Shift input string to the left
    def string_shift(self, st_arg):
        return st_arg[1::] + st_arg[0]

# Clean the string of question marks '?'
    def clean_q(self, st_arg):
        tmp = ""
        for char in st_arg:
            if char in self.alpha:
                tmp += char
        
        return tmp

 # Create the Vegnir Cipher Table   
    def veng_table(self):
        tmp_tot = self.kalpha
        tmp_prt = self.kalpha
        for i in range(0,25):
            tmp_prt = self.string_shift(tmp_prt)
            tmp_tot += tmp_prt
        
        return np.array(list(tmp_tot)).reshape(26,26)

# Find the row number based on key value
    def find_row(self, num, pk=1 ):
        
        if pk == 1:
            return self.kalpha.find(self.pk_1[num])
        else:
            return self.kalpha.find(self.pk_2[num])

# Find the column number based on row 
    def find_col(self, row, num, pk=1):
        
        if pk == 1:
            for i in range(len(row)):
                if self.k_1[num] == row[i]:
                    return i
        else:
            for i in range(len(row)):
                if self.k_2[num] == row[i]:
                    return i

# Find the key value for the specific column number          
    def find_val(self, num):
        
        return self.kalpha[num]

# Solve K1 or K2 
    def vc_solve12(self, vct, pk=1 ):

        answer = ""

        if pk == 1:
            # Algorithm for decription
            for i in range(0,len(self.k_1)):
                r = self.find_row(i%10, pk)
                c = self.find_col(vct[r], i, pk)
                answer +=  self.find_val(c)

        elif pk == 2:
            # Remove '?' from string
            self.k_2 = self.clean_q(self.k_2)
  
            for i in range(0,len(self.k_2)):
                r = self.find_row(i%8, pk)
                c = self.find_col(vct[r], i, pk)
                answer +=  self.find_val(c)
        
        return answer

# Solve K3
    def vc_solve3(self):

        print("\n\n Correct Answer: \n")
        print(self.pk_3)
        print("\n Decrypted Anser: \n")

        ans = self.clean_q(self.k_3)
        ans = np.array(list(ans)).reshape(14,24)
        ans = np.rot90(ans, k=1)
        ans = np.array(ans).reshape(42,8)
        ans = np.rot90(ans, k=1)

        return ans.flatten()




