import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# -------- Read in the data --------
df_trappist = pd.read_csv('Data/trappist_vsSptparams.txt', sep="\s+", comment='#', header=None,
                     names=["name", "SpT", "Teff", 'Teff_err', 'lbol', 'lbol_err', 'mass', 'mass_unc', 'MJ', 'MJ_unc',
                            'MH', 'MH_unc', 'MK', 'MK_unc', 'MW1', 'MW1_unc', 'MW2', 'MW2_unc'])
df_sub = pd.read_csv('Data/Subdwarf_Spt_vs_Teff_PSupdate.txt', sep="\s+", comment='#', header=None,
                     names=["name", "SpT", "Teff", 'Teff_err', 'lbol', 'lbol_err', 'mass', 'mass_unc', 'MJ', 'MJ_unc',
                            'MH', 'MH_unc', 'MK', 'MK_unc', 'MW1', 'MW1_unc', 'MW2', 'MW2_unc'])
df_young = pd.read_csv('Data/young_masses.txt', sep="\s+", comment='#', header=None,
                       names=['name', 'spt', 'mass', 'mass_unc', 'Teff', 'Teff_unc'])
df_fld = pd.read_csv('Data/field_masses.txt', sep="\t", comment='#', header=None,
                       names=['name', 'spt', 'mass', 'mass_unc', 'Teff', 'Teff_unc'])
# TODO: Can I make this plot or is in necessary?? Need to get gravities for young
# -------------------------------------------------------------------------------------
# ------------------------- Make Plot: Spt v Mass ------------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)  # to make sure proper size run entire code at once and change 8 to 6.45 to
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)
plt.xlim([5.8, 19.2]) # sample goes into T's keep all or only relavent to subs?
plt.ylim([0, 175])

# ------ Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xticks([6, 8, 10, 12, 14, 16, 18], ['M6','M8', 'L0', 'L2', 'L4', 'L6', 'L8'], fontsize=20)
plt.xlabel('Spectral Type', fontsize=25)
plt.ylabel('Mass ($M_\mathrm{Jup}$)', fontsize=25)

# ------- Add Data ------
fld = plt.scatter(df_fld['spt'], df_fld['mass'], color='#7C7D70', s=70)
ax1.errorbar(df_fld['spt'], df_fld['mass'], yerr=df_fld['mass_unc'], c='#7C7D70', fmt='o')
gamma = plt.scatter(df_gamma['spt'], df_gamma['mass'], color='#9B0132', s=70, zorder=3)
ax1.errorbar(df_gamma['spt'], df_gamma['mass'], yerr=df_gamma['mass_unc'], c='#9B0132', fmt='o', zorder=4)
beta = plt.scatter(df_beta['spt'], df_beta['mass'], color='#D01810', marker='s', s=70, zorder=5)
ax1.errorbar(df_beta['spt'], df_beta['mass'], yerr=df_beta['mass_unc'], c='#D01810', fmt='s', zorder=6)
sub = plt.scatter(df_sub['SpT'], df_sub['mass'], color='blue', zorder=7, s=70)
ax1.errorbar(df_sub['SpT'], df_sub['mass'], yerr=df_sub['mass_unc'], c='blue', fmt='o', zorder=8)

# --- Designate Trappist-1 -----
plt.scatter(df_trappist['SpT'], df_trappist['mass'], color='k', s=700, zorder=9, marker="*")
ax1.errorbar(df_trappist['SpT'], df_trappist['mass'], yerr=df_trappist['mass_unc'], c='blue', fmt='o', zorder=10)
ax1.annotate('Trappist-1', xy=(6.8, 2000), color='k', fontsize=12)

# ---- Add Legend ----
plt.legend([fld, gamma, beta, sub], ["Field", "$\gamma$", '$\\beta$', 'Subdwarfs'], frameon=False, fontsize=12)
plt.tight_layout()

plt.savefig('Figures/Spt_vs_mass.pdf', dpi=150)
