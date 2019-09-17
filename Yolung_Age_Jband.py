import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from SEDkit.utilities import rebin_spec as rebin

# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas dataframes
df_trap = pd.read_csv('Data/PS_Gaia_2306-0502 (M7.5) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
# ---- For binning -----
df_vb10 = pd.read_csv('Data/field_comp/PS_new_1916+0508 (M8) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])

# Comparison objects with same Teff
# ----Field---
df_1048 = pd.read_csv('Data/Young_Age_Comp/youth_field/Gaia1048-3956 (M9) SED.txt', sep=" ",comment='#', header=None,
                           names=["w", "f", "err"])
df_0853 = pd.read_csv('Data/Young_Age_Comp/youth_field/PS_new_0853-0329 (M9) SED.txt', sep=" ",comment='#', header=None,
                           names=["w", "f", "err"])
# ----Young----
df_2000 = pd.read_csv('../Atmospheres_paper/Data/Gaia2000-7523 (M9gamma) SED.txt', sep=" ",comment='#', header=None,
                           names=["w", "f", "err"])
df_0608 = pd.read_csv('Data/young_comp/Young_teff/PS_new_0608-2753 (M8.5gamma) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])

# -------------------------------------------------------------------------------------
# ------------------------- Normalize the spectra -------------------------------------
# -------------------------------------------------------------------------------------
# Determine region good for all spectra to take the average flux over
norm_region = df_trap[(df_trap['w'] >= 1.22) & (df_trap['w'] <= 1.23)]
norm_df_trap = df_trap['f']/(np.average(norm_region['f']))

norm_region2 = df_1048[(df_1048['w'] >= 1.22) & (df_1048['w'] <= 1.23)]
norm_df_1048 = df_1048['f']/(np.average(norm_region2['f']))

norm_region8 = df_0853[(df_0853['w'] >= 1.22) & (df_0853['w'] <= 1.23)]
norm_df_0853 = df_0853['f']/(np.average(norm_region8['f']))

norm_region4 = df_2000[(df_2000['w'] >= 1.22) & (df_2000['w'] <= 1.23)]
norm_df_2000 = df_2000['f']/(np.average(norm_region4['f']))

norm_region5 = df_0608[(df_0608['w'] >= 1.22) & (df_0608['w'] <= 1.23)]
norm_df_0608 = df_0608['f']/(np.average(norm_region5['f']))

# -------------------------------------------------------------------------------------
# ------------- Bin to same resolution as vb10 for non spex SXD data ------------------
# -------------------------------------------------------------------------------------
speck_trap = [df_trap['w'].values, norm_df_trap.values, df_trap['err'].values]
trap_bin = rebin(speck_trap, df_vb10['w'].values)

speck_2000 = [df_2000['w'].values, norm_df_2000.values, df_2000['err'].values]
J2000_bin = rebin(speck_2000, df_vb10['w'].values)

# -------------------------------------------------------------------------------------
# ---------------------- Plotting: J band comparison ----------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(8.5, 11)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([1.12, 1.35])
plt.ylim([0.25, 6])
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)

# ------Tick size, Axes Labels, and layout --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xlabel('Wavelength ($\mu$m)', fontsize=25)
plt.ylabel('Normalized Flux ($F_\lambda$)', fontsize=25)
plt.tight_layout()

# -------- Add data and Label Sources-----------
# Trappist
ax1.plot(trap_bin[0], trap_bin[1], c='k')
ax1.annotate('TRAPPIST-1 (M7.5) $T_\mathrm{eff}: 2310 \pm 230$ K', xy=(1.121, 1.15), color='k', fontsize=15)
# 1048
ax1.plot(trap_bin[0], trap_bin[1] + 1, c='k')
ax1.plot(df_1048['w'], norm_df_1048 + 1, c='#275202')
ax1.annotate('J1048-3956 (M9) $T_\mathrm{eff}: 2330 \pm 60$ K', xy=(1.121, 2.15), color='#275202', fontsize=15)
# 0853
ax1.plot(trap_bin[0], trap_bin[1] + 2, c='k')
ax1.plot(df_0853, norm_df_0853 + 2, c='#09BD8C', alpha=0.75)
ax1.annotate('J0853-0356 (M9) $T_\mathrm{eff}: 2330 \pm 70$ K', xy=(1.121, 3.15), color='#09BD8C', fontsize=15)
# 2000
ax1.plot(trap_bin[0], trap_bin[1] + 3, c='k')
# ax1.plot(df_trap['w'], norm_df_trap + 3.5, c='k')
ax1.plot(J2000_bin[0], J2000_bin[1] + 3, c='#A85C05', alpha=0.75)
ax1.annotate('J2000-7523 (M9 $\gamma$) $T_\mathrm{eff}: 2389 \pm 44$ K', xy=(1.121, 4.15), color='#A85C05', fontsize=15)
# 0608
ax1.plot(trap_bin[0], trap_bin[1] + 4, c='k')
ax1.plot(df_0608, norm_df_0608 + 4, c='#D41304', alpha=0.75)
ax1.annotate('J0608-2753 (L0 $\gamma$) $T_\mathrm{eff}: 2510 \pm 250$ K', xy=(1.121, 5.15), color='#D41304', fontsize=15)


# ------- Label Features --------------------------
NaI = pd.DataFrame()
NaI['x'] = [1.1383850, 1.1383850]
NaI['y'] = [5.3, 5.5]
plt.plot(NaI['x'], NaI['y'], color='k')
ax1.annotate('Na$\,$I', xy=(1.133, 5.52), color='k', fontsize=15)
NaId = pd.DataFrame()
NaId['x'] = [1.1408517, 1.1408517]
NaId['y'] = [5.3, 5.5]
plt.plot(NaId['x'], NaId['y'], color='k')
NaIhor = pd.DataFrame()
NaIhor['x'] = [1.1383850, 1.1408517]
NaIhor['y'] = [5.5, 5.5]
plt.plot(NaIhor['x'], NaIhor['y'], color='k')

KI1 = pd.DataFrame()
KI1['x'] = [1.1692427, 1.1692427]
KI1['y'] = [5.3, 5.5]
plt.plot(KI1['x'], KI1['y'], color='k')
ax1.annotate('K$\,$I', xy=(1.17, 5.52), color='k', fontsize=15)
KI1up1 = pd.DataFrame()
KI1up1['x'] = [1.1778406, 1.1778406]
KI1up1['y'] = [5.3, 5.5]
plt.plot(KI1up1['x'], KI1up1['y'], color='k')
KI1hor = pd.DataFrame()
KI1hor['x'] = [1.1692427, 1.1778406]
KI1hor['y'] = [5.5, 5.5]
plt.plot(KI1hor['x'], KI1hor['y'], color='k')

FeH = pd.DataFrame()
FeH['x'] = [1.19, 1.24]
FeH['y'] = [5.7, 5.7]
plt.plot(FeH['x'], FeH['y'], color='k')
ax1.annotate('FeH', xy=(1.2, 5.72), color='k', fontsize=15)
FeHd = pd.DataFrame()
FeHd['x'] = [1.19, 1.19]
FeHd['y'] = [5.5, 5.7]
plt.plot(FeHd['x'], FeHd['y'], color='k')

KI2 = pd.DataFrame()
KI2['x'] = [1.2436839, 1.2528860]
KI2['y'] = [5.5, 5.5]
plt.plot(KI2['x'], KI2['y'], color='k')
ax1.annotate('K$\,$I', xy=(1.245, 5.52), color='k', fontsize=15)
KI2up1 = pd.DataFrame()
KI2up1['x'] = [1.2436839, 1.2436839]
KI2up1['y'] = [5.3, 5.5]
plt.plot(KI2up1['x'], KI2up1['y'], color='k')
KI2up2 = pd.DataFrame()
KI2up2['x'] = [1.2528860, 1.2528860]
KI2up2['y'] = [5.3, 5.5]
plt.plot(KI2up2['x'], KI2up2['y'], color='k')

H2O = pd.DataFrame()
H2O['x'] = [1.32, 1.35]
H2O['y'] = [5.5, 5.5]
plt.plot(H2O['x'], H2O['y'], color='k')
ax1.annotate('H$_\mathrm{2} $O', xy=(1.33, 5.55), color='k', fontsize=15)
H2Od = pd.DataFrame()
H2Od['x'] = [1.32, 1.32]
H2Od['y'] = [5.3, 5.5]
plt.plot(H2Od['x'], H2Od['y'], color='k')

plt.savefig('Figures/Young_Age_Jband.pdf', dpi=150)
