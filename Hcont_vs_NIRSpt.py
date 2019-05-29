import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------------
# ------------------- Read in Indices and polynomials ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas dataframes
df = pd.read_csv('Data/Indices/indices_final.tsv', sep="\t", comment='#', header=0)
# names=[Shortname, Spectra, Lit. OPT SPT,	opt grav, Lit NIR SpT, nir grav, Final Gravity low,	FInal gravity Med.,	FEH_Z,
# E_FEH_Z, VO_Z, E_VO_Z, FEH_J,	E_FEH_J, KI_J, E_KI_J, HCONT, E_HCONT, NAI,	E_NAI, KI_169, E_KI_169, KI_177, E_KI_177,
# KI_244, E_KI_244, KI_253,	E_KI_253]

df_poly = pd.read_csv('Data/Indices/indexfits.txt', sep="\t", comment='#', header=0)
df_line = pd.read_csv('Data/Indices/AL13_dottedlines_indices_EW.txt', sep='\t', comment='#', header=0)


# Separate the data into field, gamma, and beta
df_gamma = df[(df['nir grav'] == 'g')]
df_beta = df[(df['nir grav'] == 'b')]
df_field = df[(df['nir grav'] == 'f')]
df_field2 = df[(df['opt grav'] == 'f') & (df['nir grav'].isnull())]
df_field_opt = df_field2[df_field2['Shortname'] != '2306-0502']
df_subd = df[(df['opt grav'] == 'sd')]
df_subd2 = df[(df['nir grav'] == 'sd')]

# Create the polynomial shaded zones
hcont_up = df_poly['hcont']+df_poly['hconte']
hcont_down = df_poly['hcont']-df_poly['hconte']

# --------------------------------------------------------------------------------------
# -----------------------------Plot up the indices -------------------------------------
# --------------------------------------------------------------------------------------
fig = plt.figure()
ax1 = fig.add_subplot(111)
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)
fig.set_size_inches(10, 6.45)

# ------Tick size and Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.ylabel('$H$-cont index', fontsize=25)
plt.xlabel('NIR Spectral Type', fontsize=25)
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xticks([6,7, 8, 9, 10,11, 12], ['M6', "M7", 'M8','M9', 'L0','L1', 'L2'], fontsize=20)
plt.xlim([6, 12])
plt.ylim([0.90, 1.05])

# plot polynomials
plt.plot(df_poly['spts'], df_poly['hcont'])
ax1.fill_between(df_poly['spts'], hcont_up, hcont_down, alpha=.25, color='#17becf')
# Create the dashed line seperating betas and gammas
plt.plot(df_line['SpT'], df_line['Hcont'], color='k', linestyle='dashed', linewidth=0.65)

# plot data
gamma = plt.scatter(df_gamma['SpT_used'], df_gamma['HCONT'], color='#9B0132', s=70, zorder=4)
ax1.errorbar(df_gamma['SpT_used'], df_gamma['HCONT'], yerr=df_gamma['E_HCONT'], c='#9B0132', fmt='o', zorder=3)

beta = plt.scatter(df_beta['SpT_used'], df_beta['HCONT'], color='#FF6B03', s=70, zorder=4)
ax1.errorbar(df_beta['SpT_used'], df_beta['HCONT'], yerr=df_beta['E_HCONT'], c='#FF6B03', fmt='o', zorder=3)

fld = plt.scatter(df_field['SpT_used'], df_field['HCONT'], color='#7C7D70', s=70, zorder=4)
ax1.errorbar(df_field['SpT_used'], df_field['HCONT'], yerr=df_field['E_HCONT'], c='#7C7D70', fmt='o', zorder=3)

fld_opt = plt.scatter(df_field_opt['SpT_used'], df_field_opt['HCONT'], color='#ABBDC4', s=70, zorder=4)
ax1.errorbar(df_field_opt['SpT_used'], df_field_opt['HCONT'], yerr=df_field_opt['E_HCONT'], c='#ABBDC4', fmt='o', zorder=3)

# sd = plt.scatter(df_subd['SpT_used'], df_subd['HCONT'], color='blue', s=70)
# ax1.errorbar(df_subd['SpT_used'], df_subd['HCONT'], yerr=df_subd['E_FEH_Z'], c='blue', fmt='o')

# --- Designate Trappist-1 -----
# Prism
trap_p = plt.scatter(df_field2['SpT_used'][23], df_field2['HCONT'][23], color='k', s=200, zorder=2, marker="s")
ax1.errorbar(df_field2['SpT_used'][23], df_field2['HCONT'][23], yerr=df_field2['E_HCONT'][23], c='k', zorder=2, fmt='o')
# FIRE
trap_f = plt.scatter(df_field2['SpT_used'][24], df_field2['HCONT'][24], color='k', s=700, zorder=2, marker="*")
ax1.errorbar(df_field2['SpT_used'][24], df_field2['HCONT'][24], yerr=df_field2['E_HCONT'][24], c='k', zorder=2, fmt='o')
# SXD
trap_s = plt.scatter(df_field2['SpT_used'][25], df_field2['HCONT'][25], color='k', s=200, zorder=2, marker="o")
ax1.errorbar(df_field2['SpT_used'][25], df_field2['HCONT'][25], yerr=df_field2['E_HCONT'][25], c='k', zorder=2, fmt='o')

# ---- Add Legend ----
plt.legend([fld, fld_opt, gamma, beta, trap_s], ["Field", "Field (opt Spt)", "$\gamma$", '$\\beta$', 'TRAPPIST-1'],
           frameon=False, fontsize=12)

plt.tight_layout()
plt.savefig('Figures/Hcont_vs_NIRSpt.pdf', dpi=150)
