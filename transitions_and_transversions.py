# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 17:42:08 2024

@author: gbulb
"""
dict_strings={}
dict_strings['Rosalind_0209']='GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGAAGTACGGGCATCAACCCAGTT'
dict_strings['Rosalind_2200']='TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGCGGTACGAGTGTTCCTTTGGGT'

def strings(dict_strings): 
    vals=[]
    for value in dict_strings.values():
        vals.append(value)
    return vals
s,t=strings(dict_strings)
class calc_ratio:
    def __init__(self,s,t):
        self.s=s
        self.t=t
    def transitions(s,t):
        transition_total=0        
        for i in range(len(s)):
            if s[i]=='A' and t[i]=='G':
               transition_total+=1
            elif s[i]=='G' and t[i]=='A':
                transition_total+=1
            elif s[i]=='C' and t[i]=='T':
                transition_total+=1
            elif s[i]=='T' and t[i]=='C':
                transition_total+=1
        return transition_total

    def transversions(s,t):
        transversion_total=0        
        for i in range(len(s)):
            if s[i]=='A' and t[i]=='C':
               transversion_total+=1
            elif s[i]=='C' and t[i]=='A':
                transversion_total+=1
            elif s[i]=='C' and t[i]=='G':
                transversion_total+=1
            elif s[i]=='G' and t[i]=='C':
               transversion_total+=1
            elif s[i]=='T' and t[i]=='A':
                 transversion_total+=1
            elif s[i]=='A' and t[i]=='T':
                   transversion_total+=1
            elif s[i]=='T' and t[i]=='G':
                 transversion_total+=1
            elif s[i]=='G' and t[i]=='T':
                transversion_total+=1
        return transversion_total

    def ratio_transition_over_transvertion(transition_num,transversion_num):
        ratio=transition_num/transversion_num
        return ratio

    
    
if __name__=="__main__":
   transition_num, transversion_num=calc_ratio.transitions(s,t), calc_ratio.transversions(s,t)
   print(calc_ratio.ratio_transition_over_transvertion(transition_num,transversion_num))
    
