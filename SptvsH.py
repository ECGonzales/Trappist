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

df_field = pd.read_csv('../Atmospheres_paper/Data/Parallaxes-Normal_modified.txt', sep="\t", comment='#', header=0,
                       names=['name', 'spt', 'Pi', 'Pi_er', 'Jmagn_MKO', 'Jerr_MKO', 'Hmagn_MKO', 'Herr_MKO',
                              'Kmagn_MKO', 'Kerr_MKO', 'W1magn', 'W1err', 'W2magn', 'W2err', 'W3magn', 'W3err',
                              'W4magn', 'W4err', 'Jmagn', 'Jerr', 'Hmagn', 'Herr', 'Kmagn', 'Kerr', 'Lmag', 'Lerr'])

df_young = pd.read_csv('../Atmospheres_paper/Data/For-CMD-NEW-NEW.txt', sep='\t', comment="#", header=0,
                       names=['Grp', 'ID', 'SpT', 'lowg', 'Jmag', 'Jerr', 'H', 'Herr', 'K', 'Kerr', 'W1', 'W1er', 'W2',
                              'W2er', 'W3', 'W3er', 'W4', 'W4er', 'PI', 'Pier', 'MKOJ', 'MKOJer', 'MKOH', 'MKOHer',
                              'MKOK', 'MKOKer', 'Lband', 'Lbander'])

# ------------ remove -100s from Dataframe ---------
df_field = df_field[df_field['Hmagn'] > -100]

# -------------------------------------------------------------------------------------
# ------------------- Get abs Mag from relative mag -----------------------------------
# -------------------------------------------------------------------------------------
# --- Get Distance: Field ---
d = np.round(1000/(df_field['Pi']), 2)  # 1000/mas or 1/arcsec round to 2 decimal points
d_err = np.round((df_field['Pi_er']/(df_field['Pi']**2))*1000, 2)  # convert to arcsec from mas

# ------ Convert apparent mag to Abs Mag: Field -------
AbsH = np.round(df_field['Hmagn']-(5*np.log10(d)-5), 3)
AbsH_err = np.round(np.sqrt(df_field['Herr'] ** 2 + 25 * (d_err/(d * np.log(10))) ** 2), 3)
df_field['AbsH'] = AbsH
df_field['AbsH_err'] = AbsH_err

# --- Get Distance: Young ---
dy = np.round(1000/(df_young['PI']), 2)  # 1000/mas or 1/arcsec round to 2 decimal points
dy_err = np.round((df_young['Pier']/(df_young['PI']**2))*1000, 2)  # convert to arcsec from mas

# ------ Convert apparent mag to Abs Mag: Young -------
AbsHy = np.round(df_young['H']-(5*np.log10(dy)-5), 3)
AbsHy_err = np.round(np.sqrt(df_young['Herr'] ** 2 + 25 * (dy_err/(dy * np.log(10))) ** 2), 3)
df_young['AbsH'] = AbsHy
df_young['AbsH_err'] = AbsHy_err

# -------------------------------------------------------------------------------------
# ------------------------- Split Young into beta and gamma ---------------------------
# -------------------------------------------------------------------------------------
df_gamma = df_young[df_young['lowg'] == 1]
df_beta = df_young[df_young['lowg'] == 2]

# -----------------------------------------------------------------------------------------
# ------------------------- Make Plot: Spt v Abs Mags H------------------------------------
# -----------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)  # to make sure proper size run entire code at once and change 8 to 6.45 to
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)
plt.xlim([5, 18.5])
plt.ylim([17, 7.5])

# ------ Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xticks([6, 8, 10, 12, 14, 16, 18], ['M6', 'M8', 'L0', 'L2', 'L4', 'L6', 'L8'], fontsize=20)
plt.xlabel('Optical Spectral Type', fontsize=25)
plt.ylabel('$M_H$ (2MASS)', fontsize=25)

# ----- Add data -----
fld = plt.scatter(df_field['spt'], df_field['AbsH'], color='#7C7D70', s=70)
ax1.errorbar(df_field['spt'], df_field['AbsH'], yerr=df_field['AbsH_err'], c='#7C7D70', fmt='o')
gamma = plt.scatter(df_gamma['SpT'], df_gamma['AbsH'], color='#9B0132', s=70)
ax1.errorbar(df_gamma['SpT'], df_gamma['AbsH'], yerr=df_gamma['AbsH_err'], c='#9B0132', fmt='o')
beta = plt.scatter(df_beta['SpT'], df_beta['AbsH'], color='#FF6B03', s=70, marker='o')
ax1.errorbar(df_beta['SpT'], df_beta['AbsH'], yerr=df_beta['AbsH_err'], c='#FF6B03', fmt='o')
sub = plt.scatter(df_sub['SpT'], df_sub['MH'], color='blue', s=70, zorder=5)
ax1.errorbar(df_sub['SpT'], df_sub['MH'], yerr=df_sub['MH_unc'], c='blue', fmt='o', zorder=6)
trap = plt.scatter(df_trappist['SpT'], df_trappist['MH'], color='k', s=700, zorder=7, marker="*")
ax1.errorbar(df_trappist['SpT'], df_trappist['MH'], yerr=df_trappist['MH_unc'], c='k', fmt='*', zorder=6)

# ---- Add Legend ----
plt.legend([fld, gamma, beta, sub, trap], ["Field", "$\gamma$", "$\\beta$", 'Subdwarf', "TRAPPIST-1"], frameon=False,
           fontsize=12)

plt.tight_layout()
plt.savefig('Figures/Spt_vs_H.pdf', dpi=150)
