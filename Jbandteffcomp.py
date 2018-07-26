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
df_0953 = pd.read_csv('Data/young_comp/Gaia0953-1014 (L0gamma) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_0608 = pd.read_csv('Data/young_comp/Gaia0608-2753 (M8.5gamma) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])

# -------------------------------------------------------------------------------------
# ------------------------- Normalize the spectra -------------------------------------
# -------------------------------------------------------------------------------------
# Determine region good for all spectra to take the average flux over
norm_region = df_trap[(df_trap['w'] >= 1.22) & (df_trap['w'] <= 1.23)]
norm_df_trap = df_trap['f']/(np.average(norm_region['f']))

norm_region2 = df_vb8[(df_vb8['w'] >= 1.22) & (df_vb8['w'] <= 1.23)]
norm_df_vb8 = df_vb8['f']/(np.average(norm_region2['f']))

norm_region7 = df_vb10[(df_vb10['w'] >= 1.22) & (df_vb10['w'] <= 1.23)]
norm_df_vb10 = df_vb10['f']/(np.average(norm_region7['f']))

norm_region8 = df_0320[(df_0320['w'] >= 1.22) & (df_0320['w'] <= 1.23)]
norm_df_0320 = df_0320['f']/(np.average(norm_region8['f']))

norm_region3 = df_0953[(df_0953['w'] >= 1.22) & (df_0953['w'] <= 1.23)]
norm_df_0953 = df_0953['f']/(np.average(norm_region3['f']))

norm_region4 = df_0608[(df_0608['w'] >= 1.22) & (df_0608['w'] <= 1.23)]
norm_df_0608 = df_0608['f']/(np.average(norm_region4['f']))

# -------------------------------------------------------------------------------------
# ------------- Bin to same resolution as vb10 for non spex SXD data ------------------
# -------------------------------------------------------------------------------------
speck_trap = [df_trap['w'].values, norm_df_trap.values, df_trap['err'].values]
trap_bin = rebin(speck_trap, df_vb10['w'].values)

speck_0953 = [df_0953['w'].values, norm_df_0953.values, df_0953['err'].values]
J0953_bin = rebin(speck_0953, df_vb10['w'].values)

speck_0608 = [df_0608['w'].values, norm_df_0608.values, df_0608['err'].values]
J0608_bin = rebin(speck_0608, df_vb10['w'].values)

# -------------------------------------------------------------------------------------
# ---------------------- Plotting: J band comparison ----------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(8.5, 11)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([1.12, 1.35])
plt.ylim([0.25, 7])
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)

# ------Tick size, Axes Labels, and layout --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xlabel('Wavelength ($\mu$m)', fontsize=25)
plt.ylabel('Normalized Flux ($F_\lambda$)', fontsize=25)
plt.tight_layout()

# -------- Add data and Label Sources-----------
# 0953
ax1.plot(trap_bin[0], trap_bin[1], c='k')
ax1.plot(J0953_bin[0], J0953_bin[1], c='#9B0132', alpha=0.75)
# ax1.plot(df_trap['w'], norm_df_trap, c='k')
# ax1.plot(df_0953['w'], norm_df_0953, c='#9B0132', alpha=0.75)
ax1.annotate('J0953-1014 (M9 $\gamma$) $T_\mathrm{eff}: 2430 \pm 255$ K', xy=(1.121, 1.2), color='#9B0132', fontsize=13)
# 0608
ax1.plot(trap_bin[0], trap_bin[1] + 1, c='k')
ax1.plot(J0608_bin[0], J0608_bin[1] + 1 , c='#FF6B03', alpha=0.75)
# ax1.plot(df_trap['w'], norm_df_trap + 1, c='k')
# ax1.plot(df_0608['w'], norm_df_0608 + 1, c='#FF6B03', alpha=0.75)
ax1.annotate('J0608-2753 (M8.5 $\gamma$) $T_\mathrm{eff}: 2493 \pm 253$ K', xy=(1.121, 2.2), color='#FF6B03', fontsize=13)
# vb10
ax1.plot(trap_bin[0], trap_bin[1] +2, c='k')
# ax1.plot(df_trap['w'], norm_df_trap + 2, c='k')
ax1.plot(df_vb10['w'], norm_df_vb10 + 2, c='#275202', alpha=0.75)
ax1.annotate('vb10 (M8) $T_\mathrm{eff}: 2541 \pm 45$ K', xy=(1.121, 3.2), color='#275202', fontsize=13)
# Trappist
ax1.plot(trap_bin[0], trap_bin[1] + 3, c='k')
# ax1.plot(df_trap['w'], norm_df_trap + 3, c='k')
ax1.annotate('TRAPPIST-1 (M7.5) $T_\mathrm{eff}: 2584 \pm 34$ K', xy=(1.121, 4.2), color='k', fontsize=13)
# 0320
ax1.plot(trap_bin[0], trap_bin[1] + 4, c='k')
# ax1.plot(df_trap['w'], norm_df_trap + 4, c='k')
ax1.plot(df_0320['w'], norm_df_0320 + 4, c='#1EE801', alpha=0.75)
ax1.annotate('J0320+1854 (M8) $T_\mathrm{eff}: 2615 \pm 34$ K', xy=(1.121, 5.2), color='#1EE801', fontsize=13)
# vb8
ax1.plot(trap_bin[0], trap_bin[1] + 5, c='k')
# ax1.plot(df_trap['w'], norm_df_trap + 5, c='k')
ax1.plot(df_vb8['w'], norm_df_vb8 + 5, c='#04A57F', alpha=0.8)
ax1.annotate('vb8 (M7) $T_\mathrm{eff}: 2642 \pm 34$ K', xy=(1.121, 6.2), color='#04A57F', fontsize=13)


# ------- Label Features --------------------------
NaI = pd.DataFrame()
NaI['x'] = [1.1383850, 1.1383850]
NaI['y'] = [6.5, 6.7]
plt.plot(NaI['x'], NaI['y'], color='k')
ax1.annotate('Na$\,$I', xy=(1.133, 6.75), color='k', fontsize=15)
NaId = pd.DataFrame()
NaId['x'] = [1.1408517, 1.1408517]
NaId['y'] = [6.5, 6.7]
plt.plot(NaId['x'], NaId['y'], color='k')
NaIhor = pd.DataFrame()
NaIhor['x'] = [1.1383850, 1.1408517]
NaIhor['y'] = [6.7, 6.7]
plt.plot(NaIhor['x'], NaIhor['y'], color='k')

KI1 = pd.DataFrame()
KI1['x'] = [1.1692427, 1.1692427]
KI1['y'] = [6.5, 6.7]
plt.plot(KI1['x'], KI1['y'], color='k')
ax1.annotate('K$\,$I', xy=(1.17, 6.75), color='k', fontsize=15)
KI1up1 = pd.DataFrame()
KI1up1['x'] = [1.1778406, 1.1778406]
KI1up1['y'] = [6.5, 6.7]
plt.plot(KI1up1['x'], KI1up1['y'], color='k')
KI1hor = pd.DataFrame()
KI1hor['x'] = [1.1692427, 1.1778406]
KI1hor['y'] = [6.7, 6.7]
plt.plot(KI1hor['x'], KI1hor['y'], color='k')

FeH = pd.DataFrame()
FeH['x'] = [1.19, 1.24]
FeH['y'] = [6.7, 6.7]
plt.plot(FeH['x'], FeH['y'], color='k')
ax1.annotate('FeH', xy=(1.2, 6.75), color='k', fontsize=15)
FeHd = pd.DataFrame()
FeHd['x'] = [1.19, 1.19]
FeHd['y'] = [6.5, 6.7]
plt.plot(FeHd['x'], FeHd['y'], color='k')

KI2 = pd.DataFrame()
KI2['x'] = [1.2436839, 1.2528860]
KI2['y'] = [6.5, 6.5]
plt.plot(KI2['x'], KI2['y'], color='k')
ax1.annotate('K$\,$I', xy=(1.245, 6.55), color='k', fontsize=15)
KI2up1 = pd.DataFrame()
KI2up1['x'] = [1.2436839, 1.2436839]
KI2up1['y'] = [6.3, 6.5]
plt.plot(KI2up1['x'], KI2up1['y'], color='k')
KI2up2 = pd.DataFrame()
KI2up2['x'] = [1.2528860, 1.2528860]
KI2up2['y'] = [6.3, 6.5]
plt.plot(KI2up2['x'], KI2up2['y'], color='k')

H2O = pd.DataFrame()
H2O['x'] = [1.32, 1.35]
H2O['y'] = [6.35, 6.35]
plt.plot(H2O['x'], H2O['y'], color='k')
ax1.annotate('H$_\mathrm{2} $O', xy=(1.33, 6.4), color='k', fontsize=15)
H2Od = pd.DataFrame()
H2Od['x'] = [1.32, 1.32]
H2Od['y'] = [6.2, 6.35]
plt.plot(H2Od['x'], H2Od['y'], color='k')

plt.savefig('Figures/Jbandteffcomp.pdf', dpi=150)
