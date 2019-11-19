import sys
import pandas as pd
import numpy as np

#***Statistics of chemical shift values for random coil (D. S. Wishart et al. Biochemistry 1992, 31, 1647-1651)
shift_dic = {"ALA":4.35, 
             "CYS":4.65,
             "ASP":4.76,
             "GLU":4.29,
             "PHE":4.66,
             "GLY":3.97,
             "HIS":4.63,
             "ILE":3.95,
             "LYS":4.36,
             "LEU":4.17,
             "MET":4.52,
             "ASN":4.75,
             "PRO":4.44,
             "GLN":4.37,
             "ARG":4.38,
             "SER":4.50,
             "THR":4.35,
             "VAL":3.95,
             "TRP":4.70,
             "TYR":4.60 
            }

df = pd.read_csv(sys.argv[1], delim_whitespace=True)
#for sample
#df = pd.read_csv("sample/p53_chem_shift.txt", delim_whitespace=True)

bool_for_ha = df["atomName"] == "HA"  # True for rows of atomName == "HA"
ha_rows     = df[bool_for_ha]         #Extract True rows from the original data frame 
shift_ha    = ha_rows[ ["residueNo", "residueName", "shift/ppm", "atomName"] ]
print (shift_ha)


chem_index = []
for index, col in shift_ha.iterrows():
#  print col["residueName"], col["shift/ppm"], col["atomName"]
 
  delta_shift = col["shift/ppm"] - shift_dic[col["residueName"]]

  # The following criteria is based on D. S. Wishart et al. Biochemistry 1992, 31, 1647-1651
  if  delta_shift  >=  0.1:
    print(col["residueNo"], col["residueName"], " is  1")
    chem_index.append(1)

  elif delta_shift <= -0.1:
    print(col["residueNo"], col["residueName"], " is -1")
    chem_index.append(-1)

  elif delta_shift > -0.1 and delta_shift < 0.1:
    print(col["residueNo"], col["residueName"], " is  0")
    chem_index.append(0)

import matplotlib.pyplot as plt
plt.bar([i for i in range(15)],chem_index)

plt.show()
