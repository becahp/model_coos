import numpy as np
import os
from os.path import join, exists

block_bias_def = "&BIAS_DEF dv_max="

block_bias_d = "&BIAS_INFO cont_name='D' bias_fun='LIN' bias_val=0 1.0 11/ \n"
block_bias_g = "&BIAS_INFO cont_name='G' bias_fun='LIN' bias_val=0 1.0 11/ \n"

block_out = "&OUTPUT band_lev=0  elpa_lev=1  inqu_lev=0 spectrum_lev=0 name="
barra_final = '/ \n'

block_bias_s = "&BIAS_INFO cont_name='S' bias_fun='TAB' bias_val="
block_bias_gb = "&BIAS_INFO cont_name='GB' bias_fun='TAB' bias_val="
block_bias_gs = "&BIAS_INFO cont_name='GS' bias_fun='TAB' bias_val="

def gen_bias_array(steps):
    """Returns array containing all bias values
    Expects to receive 0.1, 0.2 or 0.5 as number of steps
    Calculates bias values from 0.0 to 1.0 based on number of steps
    But first, it calculates total of values from respect number of steps: 11, 6 or 3
    """
	total = 1/steps + 1
	array = np.linspace(0.0, 1.0, num=total)
	return array

def format_number(num):
    """Returns string with number formatted
    Format is {:0.1f}, so it returns a decimal number with 1 character after the decimal point.
    Ex: 0.6001 is 0.6
    """
	return "{:0.1f}".format(num)

def make_new_dir(output_path, name):
	"""Creates a new folder under given path to store files
	Expects output path and name of new folder
	"""
	path = join(output_path, name)
	if not exists(path):
	    os.makedirs(path)

	return path

def gen_bias_block(dv_max, vs, vgb, vgs):
    """Returns bias block to be written
    Receives the final values of dv_max, source bias (vs), back gate bias (vbg) and gate bias (vgs)
    """
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
    """Write the final input file
    Receives the output path to save the file, the contents (fixed values of the input file)
    Calls gen_bias_block to create the bias block
    Creates the output line of the input file
    Writes everything in one file
    """	
	block_bias = gen_bias_block(dv_max, vs, vgb, vgs)

	filename = str(vs) + '_' + str(vgb) + '_' + str(vgs)
	filename= filename.replace('.', '')
	block_output = '\n' + block_out + "'" + filename + "'" + barra_final
	filename += '.inp'

	with open(join(output_path, filename),'w') as out:
		out.writelines([contents])
		out.writelines([block_bias])
		out.writelines([block_output])
