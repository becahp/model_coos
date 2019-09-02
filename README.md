# Multiple input files creator

This project is intended to create of multiple input file for COOS (wave-function based simulation framework for modeling ballistic nanotube transistors) with different bias configuration.
Five bias contacts can be configured: source 'S', drain 'D', back gate 'GB', program gate 'GS' and control gate 'G'.
In this version, just the source, back gate and program gate contacts are modifieble.
Drain and control gate are fixed:

&BIAS_INFO cont_name='D' bias_fun='LIN' bias_val=0 1.0 11/ 
&BIAS_INFO cont_name='G' bias_fun='LIN' bias_val=0 1.0 11/ 

## input.inp
Contains unchanged settings that will be copied to all created input files.
Mostly: region definition, discretization, contact, cnt, dd and tunnel.

## nHP_lin_v1.inp
Basic input file used for this project

## model.py

## model_utils.py

