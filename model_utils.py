import numpy as np
import os
from os.path import join, exists

block_bias_def = "&BIAS_DEF dv_max="

block_bias_d = "&BIAS_INFO cont_name='D' bias_fun='LIN' bias_val=0 1.0 11/ \n"
block_bias_g = "&BIAS_INFO cont_name='G' bias_fun='LIN' bias_val=0 1.0 11/ \n"

block_out = "&OUTPUT band_lev=0  elpa_lev=1  inqu_lev=0 name="
barra_final = '/ \n'

block_bias_s = "&BIAS_INFO cont_name='S' bias_fun='TAB' bias_val="
block_bias_gb = "&BIAS_INFO cont_name='GB' bias_fun='TAB' bias_val="
block_bias_gs = "&BIAS_INFO cont_name='GS' bias_fun='TAB' bias_val="

def gen_bias_array(steps):
	#steps = 0.1, 0.2, 0.5
	#total = 11, 6, 3
	total = 1/steps + 1
	array = np.linspace(0.0, 1.0, num=total)
	return array

def format_number(num):
	return "{:0.1f}".format(num)

def gen_bias_block(dv_max, vs, vgb, vgs):
	block = '\n'
	block += block_bias_def + str(dv_max) + barra_final
	block += block_bias_s + str(vs) + barra_final
	block += block_bias_d
	block += block_bias_gb + str(vgb) + barra_final
	block += block_bias_gs + str(vgs) + barra_final
	block += block_bias_g
	#print(block)
	return block

def write_file(output_path, contents, dv_max, vs, vgb, vgs):
	block_bias = gen_bias_block(dv_max, vs, vgb, vgs)

	filename = str(vs) + '_' + str(vgb) + '_' + str(vgs)
	filename= filename.replace('.', '')
	block_output = '\n' + block_out + "'" + filename + "'" + barra_final
	filename += '.inp'

	with open(join(output_path, filename),'w') as out:
		out.writelines([contents])
		out.writelines([block_bias])
		out.writelines([block_output])
