from model_utils import *

#get fixed content from input.inp
input ='input.inp'
inFile = open(input,"r")
contents = inFile.read()
inFile.close()

#expected steps
steps = [0.5, 0.2, 0.1]
dv_max = steps[2] #change here

#create directory to store files
path = os.getcwd()
directory = join(path, str(dv_max))

if not exists(directory):
    os.makedirs(directory)

#create list of bias values
list = gen_bias_array(dv_max)
#print(list)

#main logic to create multiple files
for vs in list:
    for vgb in list:
        for vgs in list:
            #bias values have to be formatted for constancy
            block_vs = format_number(vs)
            block_vgb = format_number(vgb)
            block_vgs = format_number(vgs)

            block = gen_bias_block(dv_max, block_vs, block_vgb, block_vgs)
            write_file(directory, contents, dv_max, block_vs, block_vgb, block_vgs)
            print(block)
