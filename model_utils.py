block_bias_def = "&BIAS_DEF dv_max="

block_bias_d = "&BIAS_INFO cont_name='D' bias_fun='LIN' bias_val=0 1.0 11/"
block_bias_g = "&BIAS_INFO cont_name='G' bias_fun='LIN' bias_val=0 1.0 11/"

block_bias_out = "&OUTPUT band_lev=0  elpa_lev=1  inqu_lev=0 name="
barra_final = '/ \n'

#gerar combinacoes
block_bias_s = "&BIAS_INFO cont_name='S' bias_fun='LIN'"
block_bias_gs = "&BIAS_INFO cont_name='GS' bias_fun='LIN'"
block_bias_gd = "&BIAS_INFO cont_name='GD' bias_fun='LIN'"

'''
name convention:

- passos de 0.5V
- passos de 0.2V
- passos de 0.1V
- Vs_Vgb_Vgs : nome da pasta
	- inp e elpa

- dv_max = 0.1
    11 passos cada
- dv_max = 0.2
    6 passos cada
- dv_max = 0.5
    3 passos cada
'''

#bias_fun = " bias_fun= LIN"
#bias_val = " bias_val="

def block_bias(steps):
    #steps = 0.1, 0.2, 0.5
    total = 1/steps + 1
    bias_val= "0 1.0 " + str(total) + "/ \n"
    return bias_val

'''
&BIAS_DEF dv_max=0.1/
&BIAS_INFO cont_name='S' bias_fun='LIN' bias_val=0 1.0 11/
&BIAS_INFO cont_name='D' bias_fun='LIN' bias_val=0 1.0 11/
&BIAS_INFO cont_name='GB' bias_fun='LIN' bias_val=0 1.0 11/
&BIAS_INFO cont_name='GS' bias_fun='LIN' bias_val=0 1.0 11/
&BIAS_INFO cont_name='G' bias_fun='LIN' bias_val=0 1.0 11/

&OUTPUT band_lev=0  elpa_lev=1  inqu_lev=0 name='nHP_lin_v1'/
'''
