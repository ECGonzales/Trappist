import pandas as pd
import matplotlib.pyplot as plt

# -------- Read in the data --------
df_trappist = pd.read_csv('Data/trappist_vsSptparams.txt', sep="\s+", comment='#', header=None,
                          names=["name", "SpT", "Teff", 'Teff_err', 'lbol', 'lbol_err', 'mass', 'mass_unc', 'MJ',
                                 'MJ_unc', 'MH', 'MH_unc', 'MK', 'MK_unc', 'MW1', 'MW1_unc', 'MW2', 'MW2_unc'])
df_sub = pd.read_csv('../Atmospheres_paper/Data/Subdwarf_Spt_vs_Teff_new.txt', sep="\s+", comment='#', header=None,
                     names=["name", "SpT", "Teff", 'Teff_err', 'lbol', 'lbol_err', 'mass', 'mass_unc', 'MJ', 'MJ_unc',
                            'MH', 'MH_unc', 'MK', 'MK_unc', 'MW1', 'MW1_unc', 'MW2', 'MW2_unc'])
df_comb = pd.read_csv('../Atmospheres_paper/Data/Lbol+Teff-February2017_updated.txt', sep="\s+", comment='#',
                      header=None, names=["name", "Lbol", "Lbol_err", 'Teff', 'Teff_err', 'spt', 'spt_unc', 'group',
                                          'grav'])

# ----- Remove the -100 -----------------
# df_comb.loc[df_comb['grav'] == -100]
df_comb.set_value(174, 'grav', 3)

# ---- Split combined dataframe into field (group 3) and low g groups 1,2) ----------
df_fld = df_comb[(df_comb['grav'] == 3)]
df_gamma = df_comb[(df_comb['grav'] == 1)]
df_beta = df_comb[(df_comb['grav'] == 2)]

# -------------------------------------------------------------------------------------
# ------------------------- Make Plot: Spt v Lbol ------------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)  # to make sure proper size run entire code at once and change 8 to 6.45 to
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)
plt.xlim([5.5, 18.5])
plt.ylim([-5, -2.3])

# ------ Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xticks([6, 8, 10, 12, 14, 16, 18], ['M6', 'M8', 'L0', 'L2', 'L4', 'L6', 'L8'], fontsize=20)
plt.xlabel('Optical Spectral Type', fontsize=25)
plt.ylabel('log($L_\mathrm{bol}$/$L_\odot$)', fontsize=25)

# ------- Add Data ------
fld = plt.scatter(df_fld['spt'], df_fld['Lbol'], color='#7C7D70', s=70)
ax1.errorbar(df_fld['spt'], df_fld['Lbol'], yerr=df_fld['Lbol_err'], c='#7C7D70', fmt='o')
gamma = plt.scatter(df_gamma['spt'], df_gamma['Lbol'], color='#9B0132', s=70, zorder=3)
ax1.errorbar(df_gamma['spt'], df_gamma['Lbol'], yerr=df_gamma['Lbol_err'], c='#9B0132', fmt='o', zorder=4)
beta = plt.scatter(df_beta['spt'], df_beta['Lbol'], color='#FF6B03', marker='o', s=70, zorder=5)
ax1.errorbar(df_beta['spt'], df_beta['Lbol'], yerr=df_beta['Lbol_err'], c='#FF6B03', fmt='o', zorder=6)
sub = plt.scatter(df_sub['SpT'], df_sub['lbol'], color='blue', zorder=7, s=70)
ax1.errorbar(df_sub['SpT'], df_sub['lbol'], yerr=df_sub['lbol_err'], c='blue', fmt='o', zorder=8)

# --- Designate Trappist-1 -----
trap = plt.scatter(df_trappist['SpT'], df_trappist['lbol'], color='k', s=700, zorder=9, marker="*")
# -- pointer---
# pointer = pd.DataFrame()
# pointer['x'] = [6, 7.2]
# pointer['y'] = [-3.68, -3.35]
# ax1.plot(pointer['x'], pointer['y'], color='k')
#
# ax1.annotate('TRAPPIST-1', xy=(5.6, -3.8), color='k', fontsize=12)

# ---- Add Legend ----
plt.legend([fld, gamma, beta, sub, trap], ["Field", "$\gamma$", '$\\beta$', 'Subdwarfs', 'TRAPPIST-1'], frameon=False, fontsize=12)
plt.tight_layout()

plt.savefig('Figures/Spt_vs_Lbol.pdf', dpi=150)
