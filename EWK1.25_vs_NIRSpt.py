import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerTuple

# ------------------------------------------------------------------------------------
# ------------------- Read in Indices and polynomials ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas dataframes
df = pd.read_csv('Data/Indices/indices_final.tsv', sep="\t", comment='#', header=0)
# names=[Shortname, Spectra, Lit. OPT SPT,	opt grav, Lit NIR SpT, nir grav, Final Gravity low,	FInal gravity Med.,
# FEH_Z, E_FEH_Z, VO_Z, E_VO_Z, FEH_J,	E_FEH_J, KI_J, E_KI_J, HCONT, E_HCONT, NAI,	E_NAI, KI_169, E_KI_169, KI_177,
# E_KI_177, KI_244, E_KI_244, KI_253,	E_KI_253]

df_comp = pd.read_csv('Data/Martin_EW_tab.txt', sep='\t', comment='#', header=0)

# Calculate error for EW line and drop greater than 20%
df['EW_KI_253err']=df['E_KI_253']/df['KI_253']
df = df[(df['EW_KI_253err'] <= .2)]

# Separate the data into field, gamma, and beta, and medium res.
df_gamma = df[(df['nir grav'] == 'g') & (df['Spectra'] != 'prism')]
df_beta = df[(df['nir grav'] == 'b') & (df['Spectra'] != 'prism')]
df_field = df[(df['nir grav'] == 'f') & (df['Spectra'] != 'prism')]
df_field2 = df[(df['opt grav'] == 'f') & (df['nir grav'].isnull()) & (df['Spectra'] != 'prism')]
df_field_opt = df_field2[df_field2['Shortname'] != '2306-0502']

df_subd = df[(df['opt grav'] == 'sd') & (df['Spectra'] != 'prism')]

# Split Martin data by gravity
df_comp = df_comp[df_comp['SpT_num'] <= 12]
df_comp_field = df_comp[(df_comp['Type'] == "FLD-G") & (df_comp['Spt_attachement'].isnull())]
df_comp_beta = df_comp[(df_comp['Type'] == "INT-G") & (df_comp['Spt_attachement'].isnull())]
df_comp_gamma = df_comp[(df_comp['Type'] == "VL-G")]

# --------------------------------------------------------------------------------------
# -----------------------------Plot up the indices KI 1.253-----------------------------
# --------------------------------------------------------------------------------------
fig = plt.figure()
ax1 = fig.add_subplot(111)
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)
fig.set_size_inches(10, 6.45)

# ------Tick size and Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.ylabel('K I 1.253 EW ($\AA$)', fontsize=25)
plt.xlabel('NIR Spectral Type', fontsize=25)
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xticks([6, 7, 8, 9, 10, 11, 12], ['M6', "M7", 'M8', 'M9', 'L0', 'L1', 'L2'], fontsize=20)
plt.xlim([5.8, 12.2])
plt.ylim([-1.5, 11])


# plot data
gamma = plt.scatter(df_gamma['SpT_used'], df_gamma['KI_253'], color='#9B0132', s=200, zorder=4, edgecolors='k')
ax1.errorbar(df_gamma['SpT_used'], df_gamma['KI_253'], yerr=df_gamma['E_KI_253'], c='#9B0132', fmt='o', zorder=3)

beta = plt.scatter(df_beta['SpT_used'], df_beta['KI_253'], color='#FF6B03', s=200, zorder=4, edgecolors='k')
ax1.errorbar(df_beta['SpT_used'], df_beta['KI_253'], yerr=df_beta['E_KI_253'], c='#FF6B03', fmt='o', zorder=3)

fld = plt.scatter(df_field['SpT_used'], df_field['KI_253'], color='#7C7D70', s=200, zorder=4, edgecolors='k')
ax1.errorbar(df_field['SpT_used'], df_field['KI_253'], yerr=df_field['E_KI_253'], c='#7C7D70', fmt='o', zorder=3)

fld_opt = plt.scatter(df_field_opt['SpT_used'], df_field_opt['KI_253'], color='#ABBDC4', s=200, zorder=4, edgecolors='k')
ax1.errorbar(df_field_opt['SpT_used'], df_field_opt['KI_253'], yerr=df_field_opt['E_KI_253'], c='#ABBDC4', fmt='o',
             zorder=3)

# sd = plt.scatter(df_subd['SpT_used'], df_subd['FEH_Z'], color='blue', s=70)
# ax1.errorbar(df_subd['SpT_used'], df_subd['FEH_Z'], yerr=df_subd['E_FEH_Z'], c='blue', fmt='o')

# --- Designate Trappist-1 -----
# FIRE
trap_f = plt.scatter(df_field2['SpT_used'][24], df_field2['KI_253'][24], color='k', s=900, zorder=2, marker="*")
ax1.errorbar(df_field2['SpT_used'][24], df_field2['KI_253'][24], yerr=df_field2['E_KI_169'][24], c='k', zorder=2,
             fmt='o')
# SXD
trap_s = plt.scatter(df_field2['SpT_used'][25], df_field2['KI_253'][25], color='k', s=500, zorder=2, marker="o")
ax1.errorbar(df_field2['SpT_used'][25], df_field2['KI_253'][25], yerr=df_field2['E_KI_253'][25], c='k', zorder=2,
             fmt='o')

#  ----- Plot comparisons -----
gamma_m = plt.scatter(df_comp_gamma['SpT_num'], df_comp_gamma['K1.2529'], color='#9B0132', s=20, zorder=4, marker="s")
ax1.errorbar(df_comp_gamma['SpT_num'], df_comp_gamma['K1.2529'], yerr=df_comp_gamma['e_K1.2529'], c='#9B0132', fmt='s', zorder=3)
#
beta_m = plt.scatter(df_comp_beta['SpT_num'], df_comp_beta['K1.2529'], color='#FF6B03', s=20, zorder=4, marker="s")
ax1.errorbar(df_comp_beta['SpT_num'], df_comp_beta['K1.2529'], yerr=df_comp_beta['e_K1.2529'], c='#FF6B03', fmt='s', zorder=3)
#
fld_m = plt.scatter(df_comp_field['SpT_num'], df_comp_field['K1.2529'], color='#7C7D70', s=20, zorder=4, marker="s")
ax1.errorbar(df_comp_field['SpT_num'], df_comp_field['K1.2529'], yerr=df_comp_field['e_K1.2529'], c='#7C7D70', fmt='s', zorder=3)


# This is to make the multiple points on the legend that are smaller than the ones in the plot, therefore need to
# run in python 3.
trap_sm = plt.scatter([], [], color='k', s=200, zorder=1, marker="o")
trap_fm = plt.scatter([], [], color='k', s=400, zorder=1, marker="*")

# ---- Add Legend ----
plt.legend([fld, fld_opt, gamma, beta, (trap_fm, trap_sm),fld_m], ["Field", "Field (opt Spt)", "$\gamma$", '$\\beta$', 'TRAPPIST-1', "Martin 2017"],
           handler_map={tuple: HandlerTuple(ndivide=None, pad=1.5)}, frameon=False, fontsize=12)

plt.tight_layout()
plt.savefig('Figures/KI_253_vs_NIRSpt.pdf', dpi=150)
