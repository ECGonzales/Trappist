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

df_field = pd.read_csv('../Atmospheres_paper/Data/Parallaxes-Normal_modified.txt', sep="\t", comment='#', header=0,
                       names=['name', 'spt', 'Pi', 'Pi_er', 'Jmagn_MKO', 'Jerr_MKO', 'Hmagn_MKO', 'Herr_MKO',
                              'Kmagn_MKO', 'Kerr_MKO', 'W1magn', 'W1err', 'W2magn', 'W2err', 'W3magn', 'W3err',
                              'W4magn', 'W4err', 'Jmagn', 'Jerr', 'Hmagn', 'Herr', 'Kmagn', 'Kerr', 'Lmag', 'Lerr'])

df_young = pd.read_csv('../Atmospheres_paper/Data/For-CMD-NEW-NEW.txt', sep='\t', comment="#", header=0,
                       names=['Grp', 'ID', 'SpT', 'lowg', 'Jmag', 'Jerr', 'H', 'Herr', 'K', 'Kerr', 'W1', 'W1er', 'W2',
                              'W2er', 'W3', 'W3er', 'W4', 'W4er', 'PI', 'Pier', 'MKOJ', 'MKOJer', 'MKOH', 'MKOHer',
                              'MKOK', 'MKOKer', 'Lband', 'Lbander'])

# ------------ remove -100s from Dataframe ---------
df_field = df_field[df_field['Kmagn'] > -100]

# -------------------------------------------------------------------------------------
# ------------------- Get abs Mag from relative mag -----------------------------------
# -------------------------------------------------------------------------------------
# --- Get Distance: Field ---
d = np.round(1000/(df_field['Pi']), 2)  # 1000/mas or 1/arcsec round to 2 decimal points
d_err = np.round((df_field['Pi_er']/(df_field['Pi']**2))*1000, 2)  # convert to arcsec from mas

# ------ Convert apparent mag to Abs Mag: Field -------
AbsK = np.round(df_field['Kmagn']-(5*np.log10(d)-5), 3)
AbsK_err = np.round(np.sqrt(df_field['Kerr'] ** 2 + 25 * (d_err/(d * np.log(10))) ** 2), 3)
df_field['AbsK'] = AbsK
df_field['AbsK_err'] = AbsK_err

# --- Get Distance: Young ---
dy = np.round(1000/(df_young['PI']), 2)  # 1000/mas or 1/arcsec round to 2 decimal points
dy_err = np.round((df_young['Pier']/(df_young['PI']**2))*1000, 2)  # convert to arcsec from mas

# ------ Convert apparent mag to Abs Mag: Young -------
AbsKy = np.round(df_young['K']-(5*np.log10(dy)-5), 3)
AbsKy_err = np.round(np.sqrt(df_young['Kerr'] ** 2 + 25 * (dy_err/(dy * np.log(10))) ** 2), 3)
df_young['AbsK'] = AbsKy
df_young['AbsK_err'] = AbsKy_err

# -------------------------------------------------------------------------------------
# ------------------------- Split Young into beta and gamma ---------------------------
# -------------------------------------------------------------------------------------
df_gamma = df_young[df_young['lowg'] == 1]
df_beta = df_young[df_young['lowg'] == 2]

# -------------------------------------------------------------------------------------
# ------------------------- Make Plot: Spt v Abs Mags K---------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)  # to make sure proper size run entire code at once and change 8 to 6.45 to
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([5, 18.5])
plt.ylim([17, 7.5])

# ------ Axes Labels --------
plt.xticks([6, 8, 10, 12, 14, 16, 18], ['M6', 'M8', 'L0', 'L2', 'L4', 'L6', 'L8'], fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel('Spectral Type', fontsize=25)
plt.ylabel('$M_K$ (2MASS)', fontsize=25)

# ----- Add data -----
fld = plt.scatter(df_field['spt'], df_field['AbsK'], color='#7C7D70', s=70)
ax1.errorbar(df_field['spt'], df_field['AbsK'], yerr=df_field['AbsK_err'], c='#7C7D70', fmt='o')
gamma = plt.scatter(df_gamma['SpT'], df_gamma['AbsK'], color='#9B0132', s=70)
ax1.errorbar(df_gamma['SpT'], df_gamma['AbsK'], yerr=df_gamma['AbsK_err'], c='#9B0132', fmt='o')
beta = plt.scatter(df_beta['SpT'], df_beta['AbsK'], color='#FF6B03', s=70, marker='o')
ax1.errorbar(df_beta['SpT'], df_beta['AbsK'], yerr=df_beta['AbsK_err'], c='#FF6B03', fmt='o')
sub = plt.scatter(df_sub['SpT'], df_sub['MK'], color='blue', s=70, zorder=5)
ax1.errorbar(df_sub['SpT'], df_sub['MK'], yerr=df_sub['MK_unc'], c='blue', fmt='o', zorder=6)
trap = plt.scatter(df_trappist['SpT'], df_trappist['MK'], color='k', s=700, zorder=7, marker="*")
ax1.errorbar(df_trappist['SpT'], df_trappist['MK'], yerr=df_trappist['MK_unc'], c='k', fmt='*', zorder=6)

# ---- Add Legend ----
plt.legend([fld, gamma, beta, sub, trap], ["Field", "$\gamma$", "$\\beta$", 'Subdwarf', "TRAPPIST-1"], frameon=False,
           fontsize=12)

plt.tight_layout()
plt.savefig('Figures/Spt_vs_K.pdf', dpi=150)
