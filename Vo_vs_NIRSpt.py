import pandas as pd
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
vo_up = df_poly['vo']+df_poly['voe']
vo_down = df_poly['vo']-df_poly['voe']

# --------------------------------------------------------------------------------------
# -----------------------------Plot up the indices -------------------------------------
# --------------------------------------------------------------------------------------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)

# ------Tick size and Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.ylabel('VO$_Z$ index', fontsize=25)
plt.xlabel('NIR Spectral Type', fontsize=25)
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xticks([6,7, 8, 9, 10,11, 12], ['M6', "M7", 'M8','M9', 'L0','L1', 'L2'], fontsize=20)
plt.xlim([5.8, 12])
plt.ylim([0.999, 1.55])

# plot polynomials
plt.plot(df_poly['spts'], df_poly['vo'])
ax1.fill_between(df_poly['spts'], vo_up, vo_down, alpha=.25, color='#17becf')


# plot data
gamma = plt.scatter(df_gamma['SpT_used'], df_gamma['VO_Z'], color='#9B0132', s=70, zorder=4)
ax1.errorbar(df_gamma['SpT_used'], df_gamma['VO_Z'], yerr=df_gamma['E_VO_Z'], c='#9B0132', fmt='o', zorder=3)

beta = plt.scatter(df_beta['SpT_used'], df_beta['VO_Z'], color='#D01810', s=70, zorder=4)
ax1.errorbar(df_beta['SpT_used'], df_beta['VO_Z'], yerr=df_beta['E_VO_Z'], c='#D01810', fmt='o', zorder=3)

fld = plt.scatter(df_field['SpT_used'], df_field['VO_Z'], color='#7C7D70', s=70, zorder=4)
ax1.errorbar(df_field['SpT_used'], df_field['VO_Z'], yerr=df_field['E_VO_Z'], c='#7C7D70', fmt='o', zorder=3)

fld_opt = plt.scatter(df_field2['SpT_used'], df_field2['VO_Z'], color='#ABBDC4', s=70, zorder=4)
ax1.errorbar(df_field2['SpT_used'], df_field2['VO_Z'], yerr=df_field2['E_VO_Z'], c='#ABBDC4', fmt='o', zorder=3)

# --- Designate Trappist-1 -----
# Prism
trap_p = plt.scatter(df_field2['SpT_used'][25], df_field2['VO_Z'][25], color='k', s=700, zorder=2, marker="*")
ax1.errorbar(df_field2['SpT_used'][25], df_field2['VO_Z'][25], yerr=df_field2['E_VO_Z'][25], c='k', zorder=2, fmt='o')
# FIRE
trap_f = plt.scatter(df_field2['SpT_used'][26], df_field2['VO_Z'][26], color='k', s=200, zorder=2, marker="s")
ax1.errorbar(df_field2['SpT_used'][26], df_field2['VO_Z'][26], yerr=df_field2['E_VO_Z'][26], c='k', zorder=2, fmt='o')
# SXD
trap_s = plt.scatter(df_field2['SpT_used'][27], df_field2['VO_Z'][27], color='k', s=200, zorder=2, marker="o")
ax1.errorbar(df_field2['SpT_used'][27], df_field2['VO_Z'][27], yerr=df_field2['E_VO_Z'][27], c='k', zorder=2, fmt='o')


# ---- Add Legend ----
plt.legend([fld, fld_opt, gamma, beta, trap_p], ["Field", "Field (opt Spt)", "$\gamma$", '$\\beta$', 'TRAPPIST-1'],
           frameon=False, fontsize=12)

plt.tight_layout()
plt.savefig('Figures/Vo_vs_NIRSpt.pdf', dpi=150)

