import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from SEDkit.utilities import rebin_spec as rebin

# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas dataframes
df_trap = pd.read_csv('Data/Gaia2306-0502 (M7.5) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
# for smoothing purposes
df_vb10 = pd.read_csv('Data/field_comp/Gaia1916+0508 (M8) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
# ---- Teff ----
df_0953 = pd.read_csv('Data/beta_comp/Gaia0953-1014 (L0gamma) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
# ---- Lbol -----
df_2235 = pd.read_csv('Data/beta_comp/Gaia2235-5906 (M8.5beta) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_2235_phot = pd.read_csv('Data/beta_comp/Gaia2235-5906 (M8.5beta) phot.txt', sep=" ", comment='#', header=None,
                           names=["w", "f", "err"])
# df_2154 = pd.read_csv('Data/beta_comp/Gaia2154-7459 (M9.5beta) SED.txt', sep=" ", comment='#', header=None,
#                       names=["w", "f", "err"])
# df_2154_phot = pd.read_csv('Data/beta_comp/Gaia2154-7459 (M9.5beta) phot.txt', sep=" ", comment='#', header=None,
#                            names=["w", "f", "err"])

# -------------------------------------------------------------------------------------
# ------------------------- Normalize the spectra -------------------------------------
# -------------------------------------------------------------------------------------
# Determine region good for all spectra to take the average flux over
norm_region = df_trap[(df_trap['w'] >= 2.16) & (df_trap['w'] <= 2.20)]
norm_df_trap = df_trap['f']/(np.average(norm_region['f']))

norm_region3 = df_0953[(df_0953['w'] >= 2.16) & (df_0953['w'] <= 2.20)]
norm_df_0953 = df_0953['f']/(np.average(norm_region3['f']))

norm_region2 = df_2235[(df_2235['w'] >= 2.16) & (df_2235['w'] <= 2.20)]
norm_df_2235 = df_2235['f']/(np.average(norm_region2['f']))

# norm_region7 = df_2154[(df_2154['w'] >= 2.16) & (df_2154['w'] <= 2.20)]
# norm_df_2154 = df_2154['f']/(np.average(norm_region7['f']))

# -------------------------------------------------------------------------------------
# ------------- Bin to same resolution as vb10 for non spex SXD data ------------------
# -------------------------------------------------------------------------------------
speck_trap = [df_trap['w'].values, norm_df_trap.values, df_trap['err'].values]
trap_bin = rebin(speck_trap, df_vb10['w'].values)

# speck_0253 = [df_0253['w'].values, norm_df_0253.values, df_0253['err'].values]
# J0253_bin = rebin(speck_0253, df_vb10['w'].values)

speck_2235 = [df_2235['w'].values, norm_df_2235.values, df_2235['err'].values]
J2235_bin = rebin(speck_2235, df_vb10['w'].values)

speck_0953 = [df_0953['w'].values, norm_df_0953.values, df_0953['err'].values]
J0953_bin = rebin(speck_0953, df_vb10['w'].values)

# speck_2154 = [df_2154['w'].values, norm_df_2154.values, df_2154['err'].values]
# J2154_bin = rebin(speck_2154, df_vb10['w'].values)

# -------------------------------------------------------------------------------------
# ------------------- Plotting: Y band comparison -------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([2.0, 2.35])
plt.ylim([0.5, 3.5])
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)

# ------Tick size and Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xlabel('Wavelength ($\mu$m)', fontsize=25)
plt.ylabel('Normalized Flux ($F_\lambda$)', fontsize=25)
plt.tight_layout()

# -------- Add data and Label Sources-----------
# 0253 Teff
ax1.plot(trap_bin[0], trap_bin[1], c='k')
# ax1.plot(df_trap['w'], norm_df_trap, c='k')
ax1.plot(J0953_bin[0], J0953_bin[1], c='#D01810', alpha=0.75)
ax1.annotate('J0953-1014 (M9 $\\beta$)', xy=(2.001, 1.25), color='#D01810', fontsize=15)
# Trappist
ax1.plot(trap_bin[0], trap_bin[1] + 0.75, c='k')
# ax1.plot(df_trap['w'], norm_df_trap + 0.75, c='k')
ax1.annotate('TRAPPIST-1 (M7.5)', xy=(2.001, 1.9), color='k', fontsize=15)
# 2235 Lbol
ax1.plot(J2235_bin[0], J2235_bin[1] + 1.5, c='#8E01E8', alpha=0.75)
ax1.plot(trap_bin[0], trap_bin[1] + 1.5, c='k')
# ax1.plot(df_trap['w'], norm_df_trap + 1.5, c='k')
# ax1.plot(df_2235['w'], norm_df_2235 + 1.5, c='#8E01E8', alpha=0.75)
ax1.annotate('J2235-5906 (M8.5 $\\beta$)', xy=(2.001, 2.7), color='#8E01E8', fontsize=15)
# 2154 Lbol
# ax1.plot(trap_bin[0], trap_bin[1] + 2.3, c='k')
# ax1.plot(J2154_bin[0], J2154_bin[1] + 2.3, c='#E806B7', alpha=0.75)
# ax1.plot(df_trap['w'], norm_df_trap + 2.3, c='k')
# ax1.plot(df_2154['w'], norm_df_2154 + 2.3, c='#E806B7', alpha=0.75)
# ax1.annotate('J2154-7459 (M9.5 $\\beta$)', xy=(2.001, 3.4), color='#E806B7', fontsize=15)

# ------- Label Features --------------------------
H2O = pd.DataFrame()
H2O['x'] = [2.00, 2.05]
H2O['y'] = [3, 3]
plt.plot(H2O['x'], H2O['y'], color='k')
ax1.annotate('H$_\mathrm{2} $O', xy=(2.02, 3.05), color='k', fontsize=15)

CIA_H2 = pd.DataFrame()
CIA_H2['x'] = [2.01, 2.34]
CIA_H2['y'] = [3.25, 3.25]
plt.plot(CIA_H2['x'], CIA_H2['y'], color='k')
ax1.annotate('CIA H$_\mathrm{2} $', xy=(2.15, 3.3), color='k', fontsize=15)

NaI = pd.DataFrame()
NaI['x'] = [2.20, 2.211]
NaI['y'] = [1.43, 1.43]
plt.plot(NaI['x'], NaI['y'], color='k')
ax1.annotate('Na$\,$I', xy=(2.197, 1.25), color='k', fontsize=15)
# ----- Making each of the vertical lines on each end --------
NaId = pd.DataFrame()
NaId['x'] = [2.20, 2.20]
NaId['y'] = [1.43, 1.55]
plt.plot(NaId['x'], NaId['y'], color='k')
NaId2 = pd.DataFrame()
NaId2['x'] = [2.211, 2.211]
NaId2['y'] = [1.43, 1.55]
plt.plot(NaId2['x'], NaId2['y'], color='k')

CO = pd.DataFrame()
CO['x'] = [2.29352, 2.34]
CO['y'] = [3, 3]
plt.plot(CO['x'], CO['y'], color='k')
ax1.annotate('CO', xy=(2.31, 3.02), color='k', fontsize=15)
COd = pd.DataFrame()
COd['x'] = [2.29352, 2.29352]
COd['y'] = [2.8, 3]
plt.plot(COd['x'], COd['y'], color='k')

plt.savefig('Figures/Beta_Kband.pdf', dpi=150)
