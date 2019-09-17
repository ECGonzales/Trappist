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

# Comparison objects with same Teff
# ----Field---
df_vb8 = pd.read_csv('Data/field_comp/PS_new_1655-0823 (M7) SED.txt', sep=" ", comment='#', header=None,
                       names=["w", "f", "err"])
df_vb10 = pd.read_csv('Data/field_comp/PS_new_1916+0508 (M8) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_0320 = pd.read_csv('Data/field_comp/PS_new_0320+1854 (M8) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
# ----Young----
df_0436 = pd.read_csv('Data/young_comp/Young_teff/Gaia0436-4114 (M8betagamma) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_0608 = pd.read_csv('Data/young_comp/Young_teff/PS_new_0608-2753 (M8.5gamma) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])

# -------- Drop a few spikes aka bad points (may not need with smoothing)----------------
df_0436 = df_0436[(df_0436['w'] >= 1.42) & (df_0436['w'] <= 1.80)]
# Four bad points
df_0436 = df_0436.drop(df_0436['f'].argmax())
df_0436 = df_0436.drop(df_0436['f'].argmax())
df_0436 = df_0436.drop(df_0436['f'].argmax())
df_0436 = df_0436.drop(df_0436['f'].argmax())

# -------------------------------------------------------------------------------------
# ------------------------- Normalize the spectra -------------------------------------
# -------------------------------------------------------------------------------------
# Determine region good for all spectra to take the average flux over
norm_region = df_trap[(df_trap['w'] >= 1.5) & (df_trap['w'] <= 1.52)]
norm_df_trap = df_trap['f']/(np.average(norm_region['f']))

norm_region2 = df_vb8[(df_vb8['w'] >= 1.5) & (df_vb8['w'] <= 1.52)]
norm_df_vb8 = df_vb8['f']/(np.average(norm_region2['f']))

norm_region7 = df_vb10[(df_vb10['w'] >= 1.5) & (df_vb10['w'] <= 1.52)]
norm_df_vb10 = df_vb10['f']/(np.average(norm_region7['f']))

norm_region8 = df_0320[(df_0320['w'] >= 1.5) & (df_0320['w'] <= 1.52)]
norm_df_0320 = df_0320['f']/(np.average(norm_region8['f']))

norm_region4 = df_0436[(df_0436['w'] >= 1.5) & (df_0436['w'] <= 1.52)]
norm_df_0436 = df_0436['f']/(np.average(norm_region4['f']))

norm_region5 = df_0608[(df_0608['w'] >= 1.5) & (df_0608['w'] <= 1.52)]
norm_df_0608 = df_0608['f']/(np.average(norm_region5['f']))

# Try normalizing the peak of the H-band, It didn't make things stand out more. Keep with original
# h_bandtrap = df_trap[(df_trap['w'] >= 1.42) & (df_trap['w'] <= 1.8)]
# norm_df_trap = df_trap['f']/(np.max(h_bandtrap['f']))
#
# h_bandvb8 = df_vb8[(df_vb8['w'] >= 1.42) & (df_vb8['w'] <= 1.8)]
# norm_df_vb8 = df_vb8['f']/(np.max(h_bandvb8['f']))
#
# h_bandtwa27 = df_twa27[(df_twa27['w'] >= 1.42) & (df_twa27['w'] <= 1.8)]
# norm_df_twa27 = df_twa27['f']/(np.max(h_bandtwa27['f']))
#
# h_bandtwa28 = df_twa28[(df_twa28['w'] >= 1.42) & (df_twa28['w'] <= 1.8)]
# norm_df_twa28 = df_twa28['f']/(np.max(h_bandtwa28['f']))
#
# h_bandtwa26 = df_twa26[(df_twa26['w'] >= 1.42) & (df_twa26['w'] <= 1.8)]
# norm_df_twa26 = df_twa26['f']/(np.max(h_bandtwa26['f']))
#
# h_bandtwa29 = df_twa29[(df_twa29['w'] >= 1.42) & (df_twa29['w'] <= 1.8)]
# norm_df_twa29 = df_twa29['f']/(np.max(h_bandtwa29['f']))

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
# ------------------- Plotting: H band comparison -------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(8.5, 11)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([1.42, 1.80])
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
# ax1.plot(df_trap['w'], norm_df_trap + 0.5, c='k')
# ax1.plot(df_0608['w'], norm_df_0608 + 0.5, c='#FF6B03', alpha=0.75)
ax1.annotate('J0608-2753 (L0 $\gamma$) $T_\mathrm{eff}: 2510 \pm 250$ K', xy=(1.421, 1.45), color='#FF6B03', fontsize=15)
# vb10
ax1.plot(trap_bin[0], trap_bin[1] + 0.75, c='k')
# ax1.plot(df_trap['w'], norm_df_trap + 1.2, c='k')
ax1.plot(df_vb10['w'], norm_df_vb10 + 0.75, c='#275202', alpha=0.75)
ax1.annotate('vB 10 (M8) $T_\mathrm{eff}: 2540 \pm 52$ K', xy=(1.421, 2), color='#275202', fontsize=15)
# 0436
ax1.plot(trap_bin[0], trap_bin[1] + 1.3, c='k')
ax1.plot(J0436_bin[0], J0436_bin[1] +1.3, c='#9B0132', alpha=0.75)
# ax1.plot(df_trap['w'], norm_df_trap , c='k')
# ax1.plot(df_0436['w'], norm_df_0436, c='#9B0132', alpha=0.75)
ax1.annotate('J0436-4114 (M9 $\gamma$) $T_\mathrm{eff}: 2560 \pm 260$ K', xy=(1.421, 2.55), color='#9B0132', fontsize=15)
# 0320
ax1.plot(trap_bin[0], trap_bin[1] + 1.8, c='k')
# ax1.plot(df_trap['w'], norm_df_trap + 2.2, c='k')
ax1.plot(df_0320['w'], norm_df_0320 + 1.8, c='#1EE801', alpha=0.75)
ax1.annotate('J0320+1854 (M8) $T_\mathrm{eff}: 2613 \pm 35$ K', xy=(1.421, 3.05), color='#1EE801', fontsize=15)
# Trappist
ax1.plot(trap_bin[0], trap_bin[1] + 2.3, c='k')
# ax1.plot(df_trap['w'], norm_df_trap + 1.7, c='k')
ax1.annotate('Trappist-1 (M7.5) $T_\mathrm{eff}: 2628 \pm 42$ K', xy=(1.421, 3.55), color='k', fontsize=15)
# vb8
ax1.plot(trap_bin[0], trap_bin[1] + 2.8, c='k')
# ax1.plot(df_trap['w'], norm_df_trap + 2.7, c='k')
ax1.plot(df_vb8['w'], norm_df_vb8 + 2.8, c='#04A57F', alpha=0.8)
ax1.annotate('vB 8 (M7) $T_\mathrm{eff}: 2642 \pm 35$ K', xy=(1.421, 4), color='#04A57F', fontsize=15)

# ------- Label Features --------------------------
H2O1 = pd.DataFrame()
H2O1['x'] = [1.3, 1.51]
H2O1['y'] = [4.1, 4.1]
plt.plot(H2O1['x'], H2O1['y'], color='k')
ax1.annotate('H$_\mathrm{2}$O', xy=(1.45, 4.15), color='k', fontsize=15)

FeH = pd.DataFrame()
FeH['x'] = [1.581, 1.66]
FeH['y'] = [4.2, 4.2]
plt.plot(FeH['x'], FeH['y'], color='k')
ax1.annotate('FeH', xy=(1.581, 4.21), color='k', fontsize=15)
FeHd = pd.DataFrame()
FeHd['x'] = [1.581, 1.581]
FeHd['y'] = [4.05, 4.2]
plt.plot(FeHd['x'], FeHd['y'], color='k')

H2O = pd.DataFrame()
H2O['x'] = [1.75, 2.05]
H2O['y'] = [4.1, 4.1]
plt.plot(H2O['x'], H2O['y'], color='k')
ax1.annotate('H$_\mathrm{2}$O', xy=(1.76, 4.15), color='k', fontsize=15)
H2Od = pd.DataFrame()
H2Od['x'] = [1.75, 1.75]
H2Od['y'] = [3.95, 4.1]
plt.plot(H2Od['x'], H2Od['y'], color='k')

# CH4 = pd.DataFrame()
# CH4['x'] = [1.67, 1.75]
# CH4['y'] = [4.25, 4.25]
# plt.plot(CH4['x'], CH4['y'], color='k')
# ax1.annotate('CH$_\mathrm{4}$', xy=(1.67, 4.28), color='k', fontsize=15)
# CH4d = pd.DataFrame()
# CH4d['x'] = [1.67, 1.67]
# CH4d['y'] = [4.1, 4.25]
# plt.plot(CH4d['x'], CH4d['y'], color='k')

plt.tight_layout()
plt.savefig('Figures/Hbandteffcomp.pdf', dpi=150)
