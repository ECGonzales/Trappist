import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# -------- Read in the data --------
df_trappist = pd.read_csv('Data/trappist_vsSptparams.txt', sep="\s+", comment='#', header=None,
                     names=["name", "SpT", "Teff", 'Teff_err', 'lbol', 'lbol_err', 'mass', 'mass_unc', 'MJ', 'MJ_unc',
                            'MH', 'MH_unc', 'MK', 'MK_unc', 'MW1', 'MW1_unc', 'MW2', 'MW2_unc'])
df_sub = pd.read_csv('../Atmospheres_paper/Data/Subdwarf_Spt_vs_Teff_new.txt', sep="\s+", comment='#', header=None,
                     names=["name", "SpT", "Teff", 'Teff_err', 'lbol', 'lbol_err', 'mass', 'mass_unc', 'MJ', 'MJ_unc',
                            'MH', 'MH_unc', 'MK', 'MK_unc', 'MW1', 'MW1_unc', 'MW2', 'MW2_unc'])
df_comb = pd.read_csv('../Atmospheres_paper/Data/Lbol+Teff-February2017_updated.txt', sep="\s+", comment='#', header=None,
                      names=["name", "Lbol", "Lbol_err", 'Teff', 'Teff_err', 'spt', 'spt_unc', 'group', 'grav'])

# ----- Remove the -100 -----------------
# df_comb.loc[df_comb['grav'] == -100]
df_comb.set_value(174, 'grav', 3)

# ---- Split combined dataframe into field (group 3) and low g groups 1,2) ----------
df_fld = df_comb[(df_comb['grav'] == 3)]
df_gamma = df_comb[(df_comb['grav'] == 1)]
df_beta = df_comb[(df_comb['grav'] == 2)]

# -------------------------------------------------------------------------------------
# ------------------------- Make Plot: Spt v Teff ------------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)  # to make sure proper size run entire code at once and change 8 to 6.45 to
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)
plt.xlim([5.5, 18.5])
plt.ylim([900, 3200])

# ------ Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xticks([6, 8, 10, 12, 14, 16, 18], ['M6','M8', 'L0', 'L2', 'L4', 'L6', 'L8'], fontsize=20)
plt.xlabel('Spectral Type', fontsize=25)
plt.ylabel('$T_\mathrm{eff}$ (K)', fontsize=25)

# ------- Add Data ------
fld = plt.scatter(df_fld['spt'], df_fld['Teff'], color='#7C7D70', s=70)
ax1.errorbar(df_fld['spt'], df_fld['Teff'], yerr=df_fld['Teff_err'], c='#7C7D70', fmt='o')
gamma = plt.scatter(df_gamma['spt'], df_gamma['Teff'], color='#9B0132', s=70, zorder=3)
ax1.errorbar(df_gamma['spt'], df_gamma['Teff'], yerr=df_gamma['Teff_err'], c='#9B0132', fmt='o', zorder=4)
beta = plt.scatter(df_beta['spt'], df_beta['Teff'], color='#D01810', marker='s', s=70, zorder=5)
ax1.errorbar(df_beta['spt'], df_beta['Teff'], yerr=df_beta['Teff_err'], c='#D01810', fmt='s', zorder=6)
sub = plt.scatter(df_sub['SpT'], df_sub['Teff'], color='blue', zorder=7, s=70)
ax1.errorbar(df_sub['SpT'], df_sub['Teff'], yerr=df_sub['Teff_err'], c='blue', fmt='o', zorder=8)

# --- Designate Trappist-1 -----
plt.scatter(df_trappist['SpT'], df_trappist['Teff'], color='k', s=700, zorder=9, marker="*")
ax1.annotate('Trappist-1', xy=(6.8, 2000), color='k', fontsize=12)

# ---- Add Legend ----
plt.legend([fld, gamma, beta, sub], ["Field", "$\gamma$", '$\\beta$', 'Subdwarfs'], frameon=False, fontsize=12)
plt.tight_layout()

plt.savefig('Figures/Spt_vs_Teff.pdf', dpi=150)
