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

# Comparison objects with same Teff
# ----Field---
df_vb8 = pd.read_csv('Data/field_comp/Gaia1655-0823 (M7) SED.txt', sep=" ", comment='#', header=None,
                       names=["w", "f", "err"])
df_vb10 = pd.read_csv('Data/field_comp/Gaia1916+0508 (M8) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_0320 = pd.read_csv('Data/field_comp/Gaia0320+1854 (M8) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
# ----Young----
df_0436 = pd.read_csv('Data/young_comp/0436-4114 (M8betagamma) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_0608 = pd.read_csv('Data/young_comp/Gaia0608-2753 (M8.5gamma) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])

# -------------------------------------------------------------------------------------
# ------------------------- Normalize the spectra -------------------------------------
# -------------------------------------------------------------------------------------
# Determine region good for all spectra to take the average flux over
norm_region = df_trap[(df_trap['w'] >= 2.16) & (df_trap['w'] <= 2.20)]
norm_df_trap = df_trap['f']/(np.average(norm_region['f']))

norm_region2 = df_vb8[(df_vb8['w'] >= 2.16) & (df_vb8['w'] <= 2.20)]
norm_df_vb8 = df_vb8['f']/(np.average(norm_region2['f']))

norm_region7 = df_vb10[(df_vb10['w'] >= 2.16) & (df_vb10['w'] <= 2.20)]
norm_df_vb10 = df_vb10['f']/(np.average(norm_region7['f']))

norm_region8 = df_0320[(df_0320['w'] >= 2.16) & (df_0320['w'] <= 2.20)]
norm_df_0320 = df_0320['f']/(np.average(norm_region8['f']))

norm_region4 = df_0436[(df_0436['w'] >= 2.16) & (df_0436['w'] <= 2.20)]
norm_df_0436 = df_0436['f']/(np.average(norm_region4['f']))

norm_region5 = df_0608[(df_0608['w'] >= 2.16) & (df_0608['w'] <= 2.20)]
norm_df_0608 = df_0608['f']/(np.average(norm_region5['f']))

# -------------------------------------------------------------------------------------
# ------------- Bin to same resolution as vb10 for non spex SXD data ------------------
# -------------------------------------------------------------------------------------
speck_trap = [df_trap['w'].values, norm_df_trap.values, df_trap['err'].values]
trap_bin = rebin(speck_trap, df_vb10['w'].values)

speck_0436 = [df_0436['w'].values, norm_df_0436.values, df_0436['err'].values]
J0436_bin = rebin(speck_0436, df_vb10['w'].values)

speck_0608 = [df_0608['w'].values, norm_df_0608.values, df_0608['err'].values]
J0608_bin = rebin(speck_0608, df_vb10['w'].values)

# -------------------------------------------------------------------------------------
# ------------------- Plotting: K band comparison -------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(8.5, 11)  # make figure size skinner to get more curvature of K-band 5 x 11 is ok
plt.xlim([2.0, 2.35])
plt.ylim([0.5, 4.5])
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)

# ------Tick size and Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xlabel('Wavelength ($\mu$m)', fontsize=25)
plt.ylabel('Normalized Flux ($F_\lambda$)', fontsize=25)
plt.tight_layout()

# -------- Add data and Label Sources-----------
# 0608
ax1.plot(trap_bin[0], trap_bin[1], c='k')
ax1.plot(J0608_bin[0], J0608_bin[1], c='#FF6B03', alpha=0.75)
# ax1.plot(df_trap['w'], norm_df_trap + 0.6, c='k')
# ax1.plot(df_0608['w'], norm_df_0608 + 0.6, c='#FF6B03', alpha=0.75)
ax1.annotate('J0608-2753 (L0 VL-G) $T_\mathrm{eff}: 2471 \pm 255$ K', xy=(2.001, 1.15), color='#FF6B03', fontsize=15)
# vb10
ax1.plot(trap_bin[0], trap_bin[1] + 0.6, c='k')
# ax1.plot(df_trap['w'], norm_df_trap + 1, c='k')
ax1.plot(df_vb10['w'], norm_df_vb10 + 0.6, c='#275202', alpha=0.75)
ax1.annotate('vB 10 (M8) $T_\mathrm{eff}: 2541 \pm 45$ K', xy=(2.001, 1.67), color='#275202', fontsize=15)
# 0436
ax1.plot(trap_bin[0], trap_bin[1] + 1.1, c='k')
ax1.plot(J0436_bin[0], J0436_bin[1] + 1.1, c='#9B0132', alpha=0.75)
# ax1.plot(df_trap['w'], norm_df_trap , c='k')
# ax1.plot(df_0436['w'], norm_df_0436, c='#9B0132', alpha=0.75)
ax1.annotate('J0436-4114 (M9 VL-G) $T_\mathrm{eff}: 2565 \pm 257$ K', xy=(2.001, 2.2), color='#9B0132', fontsize=15)
# Trappist
ax1.plot(trap_bin[0], trap_bin[1] + 1.7, c='k')
# ax1.plot(df_trap['w'], norm_df_trap + 1.7, c='k')
ax1.annotate('TRAPPIST-1 (M7.5) $T_\mathrm{eff}: 2584 \pm 34$ K', xy=(2.001, 2.8), color='k', fontsize=15)
# 0320
ax1.plot(trap_bin[0], trap_bin[1] + 2.25, c='k')
# ax1.plot(df_trap['w'], norm_df_trap + 2.25, c='k')
ax1.plot(df_0320['w'], norm_df_0320 + 2.25, c='#1EE801', alpha=0.75)
ax1.annotate('J0320+1854 (M8) $T_\mathrm{eff}: 2615 \pm 34$ K', xy=(2.001, 3.4), color='#1EE801', fontsize=15)
# vb8
ax1.plot(trap_bin[0], trap_bin[1] + 2.8, c='k')
# ax1.plot(df_trap['w'], norm_df_trap + 2.7, c='k')
ax1.plot(df_vb8['w'], norm_df_vb8 + 2.8, c='#04A57F', alpha=0.8)
ax1.annotate('vB 8 (M7) $T_\mathrm{eff}: 2642 \pm 34$ K', xy=(2.001, 3.95), color='#04A57F', fontsize=15)

# ------- Label Features --------------------------
H2O = pd.DataFrame()
H2O['x'] = [2.00, 2.05]
H2O['y'] = [4.05, 4.05]
plt.plot(H2O['x'], H2O['y'], color='k')
ax1.annotate('H$_\mathrm{2} $O', xy=(2.02, 4.07), color='k', fontsize=15)

CIA_H2 = pd.DataFrame()
CIA_H2['x'] = [2.01, 2.34]
CIA_H2['y'] = [4.2, 4.2]
plt.plot(CIA_H2['x'], CIA_H2['y'], color='k')
ax1.annotate('CIA H$_\mathrm{2} $', xy=(2.15, 4.22), color='k', fontsize=15)

NaI = pd.DataFrame()
NaI['x'] = [2.20, 2.211]
NaI['y'] = [2.4, 2.4]
plt.plot(NaI['x'], NaI['y'], color='k')
ax1.annotate('Na$\,$I', xy=(2.195, 2.3), color='k', fontsize=15)
# ----- Making each of the vertical lines on each end --------
NaId = pd.DataFrame()
NaId['x'] = [2.20, 2.20]
NaId['y'] = [2.4, 2.5]
plt.plot(NaId['x'], NaId['y'], color='k')
NaId2 = pd.DataFrame()
NaId2['x'] = [2.211, 2.211]
NaId2['y'] = [2.4, 2.5]
plt.plot(NaId2['x'], NaId2['y'], color='k')

CO = pd.DataFrame()
CO['x'] = [2.29352, 2.34]
CO['y'] = [4, 4]
plt.plot(CO['x'], CO['y'], color='k')
ax1.annotate('CO', xy=(2.31, 4.02), color='k', fontsize=15)
COd = pd.DataFrame()
COd['x'] = [2.29352, 2.29352]
COd['y'] = [3.8, 4]
plt.plot(COd['x'], COd['y'], color='k')

plt.tight_layout()
plt.savefig('Figures/KbandTeffcomp.pdf', dpi=150)
