import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------------
# ------------------- Read in Indices and polynomials ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas dataframes
df = pd.read_csv('Data/Indices/indices.tsv', sep="\t", comment='#', header=0)
# names=[Shortname, Spectra, Lit. OPT SPT,	opt grav, Lit NIR SpT, nir grav, Final Gravity low,	FInal gravity Med.,	FEH_Z,
# E_FEH_Z, VO_Z, E_VO_Z, FEH_J,	E_FEH_J, KI_J, E_KI_J, HCONT, E_HCONT, NAI,	E_NAI, KI_169, E_KI_169, KI_177, E_KI_177,
# KI_244, E_KI_244, KI_253,	E_KI_253]

df_poly = pd.read_csv('Data/Indices/indexfits.txt', sep="\t", comment='#', header=0)


# Separate the data into field, gamma, and beta
df_gamma = df[(df['nir grav'] == 'g')]
df_beta = df[(df['nir grav'] == 'b')]
df_field = df[(df['nir grav'] == 'f')]
df_field2 = df[(df['opt grav'] == 'f') & (df['nir grav'].isnull())]
df_subd = df[(df['opt grav'] == 'sd')]


# Create the polynomial shaded zones
hcont_up = df_poly['hcont']+df_poly['hconte']
hcont_down = df_poly['hcont']-df_poly['hconte']



fig = plt.figure()
ax1 = fig.add_subplot(111)
plt.plot(df_poly['spts'], df_poly['hcont'])
# plt.plot(df_poly['spts'], hcont_up)
# plt.plot(df_poly['spts'], hcont_down)
ax1.fill_between(df_poly['spts'], hcont_up, hcont_down, alpha=.25, color='#17becf')