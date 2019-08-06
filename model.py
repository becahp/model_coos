from model_utils import *

input ='input.inp'
output ='teste.inp'

inFile = open(input,"r")
contents = inFile.read()

#print(contents)
teste1 = block_bias(0.1)
teste2 = block_bias(0.2)
teste3 = block_bias(0.5)
with open(output,'w') as out:
    #out.writelines([block_dd, block_bias_g,new_s] )
    out.writelines([contents] )
    out.writelines([teste1, teste2, teste3] )
