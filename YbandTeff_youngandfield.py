import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from SEDkit.utilities import rebin_spec as rebin

# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas dataframes
df_trap = pd.read_csv('Data/PS_2306-0502 (M7.5) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])

# Comparison objects with same Teff
# ----Field---
df_vb8 = pd.read_csv('Data/field_comp/PS_1655-0823 (M7) SED.txt', sep=" ", comment='#', header=None,
                       names=["w", "f", "err"])
df_vb10 = pd.read_csv('Data/field_comp/PS_1916+0508 (M8) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_0320 = pd.read_csv('Data/field_comp/PS_0320+1854 (M8) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
# ----Young----
df_0436 = pd.read_csv('Data/young_comp/0436-4114 (M8betagamma) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_0608 = pd.read_csv('Data/young_comp/PS_0608-2753 (M8.5gamma) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])

# -------------------------------------------------------------------------------------
# ------------------------- Normalize the spectra -------------------------------------
# -------------------------------------------------------------------------------------
# Determine region good for all spectra to take the average flux over
norm_region = df_trap[(df_trap['w'] >= 0.98) & (df_trap['w'] <= 0.988)]
norm_df_trap = df_trap['f']/(np.average(norm_region['f']))

norm_region2 = df_vb8[(df_vb8['w'] >= 0.98) & (df_vb8['w'] <= 0.988)]
norm_df_vb8 = df_vb8['f']/(np.average(norm_region2['f']))

norm_region7 = df_vb10[(df_vb10['w'] >= 0.98) & (df_vb10['w'] <= 0.988)]
norm_df_vb10 = df_vb10['f']/(np.average(norm_region7['f']))

norm_region8 = df_0320[(df_0320['w'] >= 0.98) & (df_0320['w'] <= 0.988)]
norm_df_0320 = df_0320['f']/(np.average(norm_region8['f']))

norm_region4 = df_0436[(df_0436['w'] >= 0.98) & (df_0436['w'] <= 0.988)]
norm_df_0436 = df_0436['f']/(np.average(norm_region4['f']))

norm_region5 = df_0608[(df_0608['w'] >= 0.98) & (df_0608['w'] <= 0.988)]
norm_df_0608 = df_0608['f']/(np.average(norm_region5['f']))

# -------------------------------------------------------------------------------------
# ------------- Bin to same resolution as vb10 for non spex SXD data ------------------
# -------------------------------------------------------------------------------------
speck_trap = [df_trap['w'].values, norm_df_trap.values, df_trap['err'].values]
trap_bin = rebin(speck_trap, df_vb10['w'].values)

# speck_0436 = [df_0436['w'].values, norm_df_0436.values, df_0436['err'].values]
# J0436_bin = rebin(speck_0436, df_vb10['w'].values)

speck_0608 = [df_0608['w'].values, norm_df_0608.values, df_0608['err'].values]
J0608_bin = rebin(speck_0608, df_vb10['w'].values)

# -------------------------------------------------------------------------------------
# ------------------- Plotting: Y band comparison -------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(8.5, 11)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([0.95, 1.10])
plt.ylim([0.25, 7.6])
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)

# ------Tick size and Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xlabel('Wavelength ($\mu$m)', fontsize=25)
plt.ylabel('Normalized Flux ($F_\lambda$)', fontsize=25)

# -------- Add data and Label Sources-----------
# 0608
ax1.plot(trap_bin[0], trap_bin[1], c='k')
ax1.plot(J0608_bin[0], J0608_bin[1], c='#FF6B03', alpha=0.75)
# ax1.plot(df_trap['w'], norm_df_trap + 0.8, c='k')
# ax1.plot(df_0608['w'], norm_df_0608 + 0.8, c='#FF6B03', alpha=0.75)
ax1.annotate('J0608-2753 (L0 $\gamma$) $T_\mathrm{eff}: 2520 \pm 250$ K', xy=(0.951, 1.5), color='#FF6B03', fontsize=15)
# vb10
ax1.plot(trap_bin[0], trap_bin[1] + 1.2, c='k')
# ax1.plot(df_trap['w'], norm_df_trap + 1.8, c='k')
ax1.plot(df_vb10['w'], norm_df_vb10 + 1.2, c='#275202', alpha=0.75)
ax1.annotate('vB 10 (M8) $T_\mathrm{eff}: 2524 \pm 45$ K', xy=(0.951, 2.4), color='#275202', fontsize=15)
# 0436
ax1.plot(trap_bin[0], trap_bin[1] + 2.2, c='k')
ax1.plot(df_0436, norm_df_0436 + 2.2, c='#9B0132', alpha=0.75)
# ax1.plot(df_trap['w'], norm_df_trap, c='k')
# ax1.plot(df_0436['w'], norm_df_0436, c='#9B0132', alpha=0.75)
ax1.annotate('J0436-4114 (M9 $\gamma$) $T_\mathrm{eff}: 2570 \pm 260$ K', xy=(0.951, 3.45), color='#9B0132', fontsize=15)
# 0320
ax1.plot(trap_bin[0], trap_bin[1] + 3.2, c='k')
# ax1.plot(df_trap['w'], norm_df_trap + 3.5, c='k')
ax1.plot(df_0320['w'], norm_df_0320 + 3.2, c='#1EE801', alpha=0.75)
ax1.annotate('J0320+1854 (M8) $T_\mathrm{eff}: 2612 \pm 34$ K', xy=(0.951, 4.45), color='#1EE801', fontsize=15)
# Trappist
ax1.plot(trap_bin[0], trap_bin[1] + 4.2, c='k')
# ax1.plot(df_trap['w'], norm_df_trap + 2.5, c='k')
ax1.annotate('TRAPPIST-1 (M7.5) $T_\mathrm{eff}: 2626 \pm 34$ K', xy=(0.951, 5.5), color='k', fontsize=15)
# vb8
ax1.plot(trap_bin[0], trap_bin[1] + 5.2, c='k')
# ax1.plot(df_trap['w'], norm_df_trap + 4.3, c='k')
ax1.plot(df_vb8['w'], norm_df_vb8 + 5.2, c='#04A57F', alpha=0.8)
ax1.annotate('vB 8 (M7) $T_\mathrm{eff}: 2652 \pm 34$ K', xy=(0.951, 6.4), color='#04A57F', fontsize=15)

# --- To make lines for features ---------
FeH1 = pd.DataFrame()
FeH1['x'] = [0.9896, 1.0]
FeH1['y'] = [6.8, 6.8]
plt.plot(FeH1['x'], FeH1['y'], color='k')
ax1.annotate('FeH', xy=(0.9896, 6.81), color='k', fontsize=15)
# -- To make a vertical line
FeH1d = pd.DataFrame()
FeH1d['x'] = [0.9896, 0.9896]
FeH1d['y'] = [6.6, 6.8]
plt.plot(FeH1d['x'], FeH1d['y'], color='k')

FeH2 = pd.DataFrame()
FeH2['x'] = [0.998, 1.085]
FeH2['y'] = [7.15, 7.15]
plt.plot(FeH2['x'], FeH2['y'], color='k')
ax1.annotate('FeH', xy=(1.03, 7.16), color='k', fontsize=15)
FeH2d = pd.DataFrame()
FeH2d['x'] = [0.998, 0.998]
FeH2d['y'] = [7, 7.15]
plt.plot(FeH2d['x'], FeH2d['y'], color='k')

VO = pd.DataFrame()
VO['x'] = [1.0456, 1.08]
VO['y'] = [6.85, 6.85]
plt.plot(VO['x'], VO['y'], color='k')
ax1.annotate('VO', xy=(1.06, 6.86), color='k', fontsize=15)
VOd = pd.DataFrame()
VOd['x'] = [1.0456, 1.0456]
VOd['y'] = [6.7, 6.85]
plt.plot(VOd['x'], VOd['y'], color='k')

H2O = pd.DataFrame()
H2O['x'] = [1.08, 1.099]
H2O['y'] = [7.35, 7.35]
plt.plot(H2O['x'], H2O['y'], color='k')
ax1.annotate('H$_\mathrm{2} $O', xy=(1.08, 7.385), color='k', fontsize=15)
H2Od = pd.DataFrame()
H2Od['x'] = [1.08, 1.08]
H2Od['y'] = [7.2, 7.35]
plt.plot(H2Od['x'], H2Od['y'], color='k')

plt.tight_layout()
plt.savefig('Figures/Ybandteffcomp.pdf', dpi=150)

