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
norm_region = df_trap[(df_trap['w'] >= 0.98) & (df_trap['w'] <= 0.988)]
norm_df_trap = df_trap['f']/(np.average(norm_region['f']))

norm_region2 = df_1048[(df_1048['w'] >= 0.98) & (df_1048['w'] <= 0.988)]
norm_df_1048 = df_1048['f']/(np.average(norm_region2['f']))

norm_region8 = df_0853[(df_0853['w'] >= 0.98) & (df_0853['w'] <= 0.988)]
norm_df_0853 = df_0853['f']/(np.average(norm_region8['f']))

norm_region4 = df_2000[(df_2000['w'] >= 0.98) & (df_2000['w'] <= 0.988)]
norm_df_2000 = df_2000['f']/(np.average(norm_region4['f']))

norm_region5 = df_0608[(df_0608['w'] >= 0.98) & (df_0608['w'] <= 0.988)]
norm_df_0608 = df_0608['f']/(np.average(norm_region5['f']))

# -------------------------------------------------------------------------------------
# ------------- Bin to same resolution as vb10 for non spex SXD data ------------------
# -------------------------------------------------------------------------------------
speck_trap = [df_trap['w'].values, norm_df_trap.values, df_trap['err'].values]
trap_bin = rebin(speck_trap, df_vb10['w'].values)

speck_2000 = [df_2000['w'].values, norm_df_2000.values, df_2000['err'].values]
J2000_bin = rebin(speck_2000, df_vb10['w'].values)

# -------------------------------------------------------------------------------------
# ------------------- Plotting: Y band comparison -------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(8.5, 11)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([0.95, 1.10])
plt.ylim([0.25, 7])
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)

# ------Tick size and Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xlabel('Wavelength ($\mu$m)', fontsize=25)
plt.ylabel('Normalized Flux ($F_\lambda$)', fontsize=25)

# -------- Add data and Label Sources-----------
# Trappist
ax1.plot(trap_bin[0], trap_bin[1], c='k')
ax1.annotate('TRAPPIST-1 (M7.5) $T_\mathrm{eff}: 2310 \pm 230$ K', xy=(0.951, 1.3), color='k', fontsize=15)
# 1048
ax1.plot(trap_bin[0], trap_bin[1] + 1, c='k')
ax1.plot(df_1048['w'], norm_df_1048 + 1, c='#275202')
ax1.annotate('J1048-3956 (M9) $T_\mathrm{eff}: 2333 \pm 54$ K', xy=(0.951, 2.2), color='#275202', fontsize=15)
# 0853
ax1.plot(trap_bin[0], trap_bin[1] + 2, c='k')
ax1.plot(df_0853, norm_df_0853 + 2, c='#09BD8C', alpha=0.75)
ax1.annotate('J0853-0356 (M9) $T_\mathrm{eff}: 2334 \pm 54$ K', xy=(0.951, 3.25), color='#09BD8C', fontsize=15)
# 2000
ax1.plot(trap_bin[0], trap_bin[1] + 3, c='k')
ax1.plot(J2000_bin[0], J2000_bin[1] + 3, c='#A85C05', alpha=0.75)
ax1.annotate('J2000-7523 (M9 $\gamma$) $T_\mathrm{eff}: 2388 \pm 36$ K', xy=(0.951, 4.2), color='#A85C05', fontsize=15)
# 0608
ax1.plot(trap_bin[0], trap_bin[1] + 4, c='k')
ax1.plot(df_0608, norm_df_0608 + 4, c='#D41304', alpha=0.75)
ax1.annotate('J0608-2753 (L0 $\gamma$) $T_\mathrm{eff}: 2510 \pm 250$ K', xy=(0.951, 5.4), color='#D41304', fontsize=15)


# --- To make lines for features ---------
FeH1 = pd.DataFrame()
FeH1['x'] = [0.9896, 1.0]
FeH1['y'] = [6.0, 6.0]
plt.plot(FeH1['x'], FeH1['y'], color='k')
ax1.annotate('FeH', xy=(0.9896, 6.01), color='k', fontsize=15)
# -- To make a vertical line
FeH1d = pd.DataFrame()
FeH1d['x'] = [0.9896, 0.9896]
FeH1d['y'] = [5.8, 6.0]
plt.plot(FeH1d['x'], FeH1d['y'], color='k')

FeH2 = pd.DataFrame()
FeH2['x'] = [0.998, 1.085]
FeH2['y'] = [6.4, 6.4]
plt.plot(FeH2['x'], FeH2['y'], color='k')
ax1.annotate('FeH', xy=(1.03, 6.41), color='k', fontsize=15)
FeH2d = pd.DataFrame()
FeH2d['x'] = [0.998, 0.998]
FeH2d['y'] = [6.2, 6.4]
plt.plot(FeH2d['x'], FeH2d['y'], color='k')

VO = pd.DataFrame()
VO['x'] = [1.0456, 1.08]
VO['y'] = [6.0, 6.0]
plt.plot(VO['x'], VO['y'], color='k')
ax1.annotate('VO', xy=(1.06, 6.01), color='k', fontsize=15)
VOd = pd.DataFrame()
VOd['x'] = [1.0456, 1.0456]
VOd['y'] = [5.8, 6.0]
plt.plot(VOd['x'], VOd['y'], color='k')

H2O = pd.DataFrame()
H2O['x'] = [1.08, 1.099]
H2O['y'] = [6.7, 6.7]
plt.plot(H2O['x'], H2O['y'], color='k')
ax1.annotate('H$_\mathrm{2} $O', xy=(1.08, 6.75), color='k', fontsize=15)
H2Od = pd.DataFrame()
H2Od['x'] = [1.08, 1.08]
H2Od['y'] = [6.5, 6.7]
plt.plot(H2Od['x'], H2Od['y'], color='k')

plt.tight_layout()
plt.savefig('Figures/Young_Age_Yband.pdf', dpi=150)

