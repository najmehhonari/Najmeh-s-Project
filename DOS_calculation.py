#Split the DOSCAR file into TDOS and PDOS files.
#DOS for spin up & down have the same positive sign.

with open('/Users/nhonari/DOS/DOSCAR', 'r') as doscar, open('/Users/nhonari/DOS/TDOS', 'w') as tdos, open('/Users/nhonari/DOS/PDOS', 'w') as pdos:
   # lines = doscar.readlines()
    for i, line in enumerate(doscar):
        if i >= 6 and i <= 3005:
            tdos.write(line)
        elif i>3005:
            pdos.write(line)
            
#Split the PDOS of each atom for LYC
#DOS for spin up & down have the same positive sign

output_file="/Users/nhonari/DOS/pdoss/DOS_{}.txt"
with open("/Users/nhonari/DOS/PDOS",'r') as file:
    lines11 = file.readlines()
    index= int(len(lines11)/3001)
    for i in range(index):
        with open(output_file.format(i),'w') as file:
            for line in lines11[3001*i+1:3001*(i+1)]:
                file.write(line)
