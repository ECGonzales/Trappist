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
df_0253 = pd.read_csv('Data/beta_comp/Gaia0253+3206 (M7beta) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
# ---- Lbol -----
df_2235 = pd.read_csv('Data/beta_comp/Gaia2235-5906 (M8.5beta) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_2235_phot = pd.read_csv('Data/beta_comp/Gaia2235-5906 (M8.5beta) phot.txt', sep=" ", comment='#', header=None,
                           names=["w", "f", "err"])
df_2154 = pd.read_csv('Data/beta_comp/Gaia2154-7459 (M9.5beta) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_2154_phot = pd.read_csv('Data/beta_comp/Gaia2154-7459 (M9.5beta) phot.txt', sep=" ", comment='#', header=None,
                           names=["w", "f", "err"])

# -------------------------------------------------------------------------------------
# ------------------------- Normalize the spectra -------------------------------------
# -------------------------------------------------------------------------------------
# Determine region good for all spectra to take the average flux over
norm_region = df_trap[(df_trap['w'] >= 0.98) & (df_trap['w'] <= 0.988)]
norm_df_trap = df_trap['f']/(np.average(norm_region['f']))

norm_region3 = df_0253[(df_0253['w'] >= 0.98) & (df_0253['w'] <= 0.988)]
norm_df_0253 = df_0253['f']/(np.average(norm_region3['f']))

norm_region2 = df_2235[(df_2235['w'] >= 0.98) & (df_2235['w'] <= 0.988)]
norm_df_2235 = df_2235['f']/(np.average(norm_region2['f']))

norm_region7 = df_2154[(df_2154['w'] >= 0.98) & (df_2154['w'] <= 0.988)]
norm_df_2154 = df_2154['f']/(np.average(norm_region7['f']))

# -------------------------------------------------------------------------------------
# ------------- Bin to same resolution as vb10 for non spex SXD data ------------------
# -------------------------------------------------------------------------------------
speck_trap = [df_trap['w'].values, norm_df_trap.values, df_trap['err'].values]
trap_bin = rebin(speck_trap, df_vb10['w'].values)

speck_2235 = [df_2235['w'].values, norm_df_2235.values, df_2235['err'].values]
J2235_bin = rebin(speck_2235, df_vb10['w'].values)

speck_2154 = [df_2154['w'].values, norm_df_2154.values, df_2154['err'].values]
J2154_bin = rebin(speck_2154, df_vb10['w'].values)

# -------------------------------------------------------------------------------------
# ------------------- Plotting: Y band comparison -------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([0.95, 1.10])
plt.ylim([0.25, 4.8])
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
ax1.plot(df_0253['w'], norm_df_0253, c='#D01810', alpha=0.75)
ax1.annotate('J0253+3206 (M7 $\\beta$)', xy=(0.951, 1.2), color='#D01810', fontsize=15)
# Trappist
ax1.plot(trap_bin[0], trap_bin[1] + 0.75, c='k')
# ax1.plot(df_trap['w'], norm_df_trap + 0.75, c='k')
ax1.annotate('TRAPPIST-1 (M7.5)', xy=(0.951, 1.9), color='k', fontsize=15)
# 2235 Lbol
ax1.plot(trap_bin[0], trap_bin[1] + 1.5, c='k')
ax1.plot(J2235_bin[0], J2235_bin[1] + 1.5, c='#8E01E8', alpha=0.75)
# ax1.plot(df_trap['w'], norm_df_trap + 1.5, c='k')
# ax1.plot(df_2235['w'], norm_df_2235 + 1.5, c='#8E01E8', alpha=0.75)
ax1.annotate('J2235-5906 (M8.5 $\\beta$)', xy=(0.951, 2.7), color='#8E01E8', fontsize=15)
# 2154 Lbol
ax1.plot(trap_bin[0], trap_bin[1] + 2.25, c='k')
ax1.plot(J2154_bin[0], J2154_bin[1] + 2.25, c='#E806B7', alpha=0.75)
# ax1.plot(df_trap['w'], norm_df_trap + 2.25, c='k')
# ax1.plot(df_2154['w'], norm_df_2154 + 2.25, c='#E806B7', alpha=0.75)
ax1.annotate('J2154-7459 (M9.5 $\\beta$)', xy=(0.951, 3.5), color='#E806B7', fontsize=15)

# --- To make lines for features ---------
FeH1 = pd.DataFrame()
FeH1['x'] = [0.9896, 1.0]
FeH1['y'] = [3.8, 3.8]
plt.plot(FeH1['x'], FeH1['y'], color='k')
ax1.annotate('FeH', xy=(0.9896, 3.81), color='k', fontsize=15)
# -- To make a vertical line
FeH1d = pd.DataFrame()
FeH1d['x'] = [0.9896, 0.9896]
FeH1d['y'] = [3.65, 3.8]
plt.plot(FeH1d['x'], FeH1d['y'], color='k')

FeH2 = pd.DataFrame()
FeH2['x'] = [0.998, 1.085]
FeH2['y'] = [4.25, 4.25]
plt.plot(FeH2['x'], FeH2['y'], color='k')
ax1.annotate('FeH', xy=(1.03, 4.27), color='k', fontsize=15)
FeH2d = pd.DataFrame()
FeH2d['x'] = [0.998, 0.998]
FeH2d['y'] = [4, 4.25]
plt.plot(FeH2d['x'], FeH2d['y'], color='k')

VO = pd.DataFrame()
VO['x'] = [1.0456, 1.08]
VO['y'] = [4, 4]
plt.plot(VO['x'], VO['y'], color='k')
ax1.annotate('VO', xy=(1.06, 4.01), color='k', fontsize=15)
VOd = pd.DataFrame()
VOd['x'] = [1.0456, 1.0456]
VOd['y'] = [3.85, 4]
plt.plot(VOd['x'], VOd['y'], color='k')

H2O = pd.DataFrame()
H2O['x'] = [1.08, 1.099]
H2O['y'] = [4.5, 4.5]
plt.plot(H2O['x'], H2O['y'], color='k')
ax1.annotate('H$_\mathrm{2} $O', xy=(1.085, 4.55), color='k', fontsize=15)
H2Od = pd.DataFrame()
H2Od['x'] = [1.08, 1.08]
H2Od['y'] = [4.35, 4.5]
plt.plot(H2Od['x'], H2Od['y'], color='k')

plt.savefig('Figures/Beta_Yband.pdf', dpi=150)
