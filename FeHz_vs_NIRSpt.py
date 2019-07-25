import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerTuple
# import scipy.io as sci

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

# -------------- How to Deal with reading in an idl .sav file and converting to a dataframe -----------------
# polys = sci.readsav('Data/Indices/indexfits.sav')
#
# #Check format of .sav file
# polys.keys()
# # zfeh, vo, hcont, ki,
#
# # create dataframe of polynomials
# spts = polys['sptbins']
#
# df_poly = pd.DataFrame()
# df_poly['spts']=spts
# df_poly['vo']=polys['fieldfits'][1][2]
# df_poly['hcont']=polys['fieldfits'][2][2]
# df_poly['KiJ']=polys['fieldfits'][3][2]
# df_poly['zfehe']=polys['fieldfits'][0][3]
# df_poly['voe']=polys['fieldfits'][1][3]
# df_poly['hconte']=polys['fieldfits'][2][3]
# df_poly['KiJe']=polys['fieldfits'][3][3]
#
# df_poly.to_csv('Data/indexfits.txt', index=False, sep='\t')
# -----------------------------------------------------------------------------------------------------------

# Separate the data into field, gamma, and beta
df_gamma = df[(df['nir grav'] == 'g')]
df_beta = df[(df['nir grav'] == 'b')]
df_field = df[(df['nir grav'] == 'f')]
df_field2 = df[(df['opt grav'] == 'f') & (df['nir grav'].isnull())]
df_field_opt = df_field2[df_field2['Shortname'] != '2306-0502']
df_subd = df[(df['opt grav'] == 'sd')]
df_subd2 = df[(df['nir grav'] == 'sd')]


# Create the polynomial shaded zones
zfeh_up = df_poly['zfeh']+df_poly['zfehe']
zfeh_down = df_poly['zfeh']-df_poly['zfehe']

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
plt.ylabel('FeH$_Z$ index', fontsize=25)
plt.xlabel('NIR Spectral Type', fontsize=25)
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xticks([6,7, 8, 9, 10,11, 12], ['M6', "M7", 'M8','M9', 'L0','L1', 'L2'], fontsize=20)
plt.xlim([6, 12])
plt.ylim([0.999, 1.3])

# plot polynomials
plt.plot(df_poly['spts'], df_poly['zfeh'])
ax1.fill_between(df_poly['spts'], zfeh_up, zfeh_down, alpha=.25, color='#17becf')

# Create the dashed line seperating betas and gammas
plt.plot(df_line['SpT'], df_line['FeHz'], color='k', linestyle='dashed', linewidth=0.65)
# plot data
gamma = plt.scatter(df_gamma['SpT_used'], df_gamma['FEH_Z'], color='#9B0132', s=70, zorder=3)
ax1.errorbar(df_gamma['SpT_used'], df_gamma['FEH_Z'], yerr=df_gamma['E_FEH_Z'], c='#9B0132', fmt='o', zorder=2)

beta = plt.scatter(df_beta['SpT_used'], df_beta['FEH_Z'], color='#FF6B03', s=70, zorder=3)
ax1.errorbar(df_beta['SpT_used'], df_beta['FEH_Z'], yerr=df_beta['E_FEH_Z'], c='#FF6B03', fmt='o', zorder=2)

fld = plt.scatter(df_field['SpT_used'], df_field['FEH_Z'], color='#7C7D70', s=70, zorder=3)
ax1.errorbar(df_field['SpT_used'], df_field['FEH_Z'], yerr=df_field['E_FEH_Z'], c='#7C7D70', fmt='o', zorder=2)

fld_opt = plt.scatter(df_field_opt['SpT_used'], df_field_opt['FEH_Z'], color='#ABBDC4', s=70, zorder=3)
ax1.errorbar(df_field_opt['SpT_used'], df_field_opt['FEH_Z'], yerr=df_field_opt['E_FEH_Z'], c='#ABBDC4', fmt='o', zorder=2)

# sd = plt.scatter(df_subd['SpT_used'], df_subd['FEH_Z'], color='blue', s=70)
# ax1.errorbar(df_subd['SpT_used'], df_subd['FEH_Z'], yerr=df_subd['E_FEH_Z'], c='blue', fmt='o')

# sd_nir = plt.scatter(df_subd2['SpT_used'], df_subd2['FEH_Z'], color='mediumblue', s=70)
# ax1.errorbar(df_subd2['SpT_used'], df_subd2['FEH_Z'], yerr=df_subd2['E_FEH_Z'], c='mediumblue', fmt='o')


# --- Designate Trappist-1, error bars smaller than point size -----
# Prism
trap_p = plt.scatter(df_field2['SpT_used'][23], df_field2['FEH_Z'][23], color='k', s=200, zorder=1, marker="s")
ax1.errorbar(df_field2['SpT_used'][23], df_field2['FEH_Z'][23], yerr=df_field2['E_FEH_Z'][23], c='k', zorder=1, fmt='o')
# FIRE
trap_f = plt.scatter(df_field2['SpT_used'][24], df_field2['FEH_Z'][24], color='k', s=700, zorder=1, marker="*")
ax1.errorbar(df_field2['SpT_used'][24], df_field2['FEH_Z'][24], yerr=df_field2['E_FEH_Z'][24], c='k', zorder=1, fmt='o')
# SXD
trap_s = plt.scatter(df_field2['SpT_used'][25], df_field2['FEH_Z'][25], color='k', s=200, zorder=1, marker="o")
ax1.errorbar(df_field2['SpT_used'][25], df_field2['FEH_Z'][25], yerr=df_field2['E_FEH_Z'][25], c='k', zorder=1, fmt='o')

# This is to make the multiple points on the legend, therefore need to run in python 3.
trap_sm = plt.scatter([], [], color='k', s=70, zorder=1, marker="o")
trap_fm = plt.scatter([], [], color='k', s=250, zorder=1, marker="*")
trap_pm = plt.scatter([], [], color='k', s=70, zorder=1, marker="s")
# ---- Add Legend ----
plt.legend([fld, fld_opt, gamma, beta, (trap_fm, trap_sm, trap_pm)], ["Field", "Field (opt Spt)", "$\gamma$", '$\\beta$', 'TRAPPIST-1'],
           handler_map={tuple: HandlerTuple(ndivide=None, pad=1.4)}, frameon=False, fontsize=12)



#plt.legend([fld, fld_opt, gamma, beta, trap_s], ["Field", "Field (opt Spt)", "$\gamma$", '$\\beta$', 'TRAPPIST-1'],
          # frameon=False, fontsize=12)

plt.tight_layout()

plt.savefig('Figures/FeHz_vs_NIRSpt.pdf', dpi=150)
