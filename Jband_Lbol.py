import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from SEDkit.utilities import rebin_spec as rebin

# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas dataframes

df_trap = pd.read_csv('Data/Gaia2306-0502 (M7.5) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_trap_phot = pd.read_csv('Data/Gaia2306-0502 (M7.5) phot.txt', sep=" ",comment='#', header=None, names=["w", "f", "err"])

# ---- Field ----
df_vb8 = pd.read_csv('Data/field_comp/Gaia1655-0823 (M7) SED.txt', sep=" ", comment='#', header=None,  # vb8
                       names=["w", "f", "err"])
df_vb10 = pd.read_csv('Data/field_comp/Gaia1916+0508 (M8) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_0320 = pd.read_csv('Data/field_comp/Gaia0320+1854 (M8) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
# --- Young ------
df_1207 = pd.read_csv('Data/young_comp/Gaia1207-3900 (L0gamma) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_1207_phot = pd.read_csv('Data/young_comp/Gaia1207-3900 (L0gamma) phot.txt', sep=" ", comment='#', header=None,
                           names=["w", "f", "err"])
# df_0443 = pd.read_csv('Data/young_comp/0443+0002 (M9gamma) SED.txt', sep=" ", comment='#', header=None,
#                       names=["w", "f", "err"])
# df_0443_phot = pd.read_csv('Data/young_comp/0443+0002 (M9gamma) phot.txt', sep=" ", comment='#', header=None,
#                            names=["w", "f", "err"])
# Checking with the SXD to see differences
df_0443 = pd.read_csv('Data/young_comp/Gaia0443+0002 (M9gamma) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_0443_phot = pd.read_csv('Data/young_comp/Gaia0443+0002 (M9gamma) phot.txt', sep=" ", comment='#', header=None,
                           names=["w", "f", "err"])
df_0518 = pd.read_csv('Data/young_comp/Gaia0518-2756 (L1gamma) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_0518_phot = pd.read_csv('Data/young_comp/Gaia0518-2756 (L1gamma) phot.txt', sep=" ", comment='#', header=None,
                           names=["w", "f", "err"])

# -------------------------------------------------------------------------------------
# ------------------------- Normalize the spectra -------------------------------------
# -------------------------------------------------------------------------------------
# Determine region good for all spectra to take the average flux over
norm_region = df_trap[(df_trap['w'] >= 1.22) & (df_trap['w'] <= 1.23)]
norm_df_trap = df_trap['f']/(np.average(norm_region['f']))

norm_region2 = df_vb8[(df_vb8['w'] >= 1.22) & (df_vb8['w'] <= 1.23)]
norm_df_vb8 = df_vb8['f']/(np.average(norm_region2['f']))

norm_region3 = df_vb10[(df_vb10['w'] >= 1.22) & (df_vb10['w'] <= 1.23)]
norm_df_vb10 = df_vb10['f']/(np.average(norm_region3['f']))

norm_region4 = df_0320[(df_0320['w'] >= 1.22) & (df_0320['w'] <= 1.23)]
norm_df_0320 = df_0320['f']/(np.average(norm_region4['f']))

norm_region5 = df_1207[(df_1207['w'] >= 1.22) & (df_1207['w'] <= 1.23)]
norm_df_1207 = df_1207['f']/(np.average(norm_region5['f']))

norm_region6 = df_0443[(df_0443['w'] >= 1.22) & (df_0443['w'] <= 1.23)]
norm_df_0443 = df_0443['f']/(np.average(norm_region6['f']))

norm_region7 = df_0518[(df_0518['w'] >= 1.22) & (df_0518['w'] <= 1.23)]
norm_df_0518 = df_0518['f']/(np.average(norm_region7['f']))

# -------------------------------------------------------------------------------------
# ------------- Bin to same resolution as vb10 for non spex SXD data ------------------
# -------------------------------------------------------------------------------------
speck_trap = [df_trap['w'].values, norm_df_trap.values, df_trap['err'].values]
trap_bin = rebin(speck_trap, df_vb10['w'].values)

speck_1207 = [df_1207['w'].values, norm_df_1207.values, df_1207['err'].values]
J1207_bin = rebin(speck_1207, df_vb10['w'].values)

speck_0443 = [df_0443['w'].values, norm_df_0443.values, df_0443['err'].values]
J0443_bin = rebin(speck_0443, df_vb10['w'].values)

speck_0518 = [df_0518['w'].values, norm_df_0518.values, df_0518['err'].values]
J0518_bin = rebin(speck_0518, df_vb10['w'].values)

# -------------------------------------------------------------------------------------
# ------------------- Plotting: J band comparison -------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(8.5, 11)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([1.12, 1.35])
plt.ylim([0, 8.5])
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)

# ------Tick size and Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xlabel('Wavelength ($\mu$m)', fontsize=25)
plt.ylabel('Normalized Flux ($F_\lambda$)', fontsize=25)

# -------- Add data -----------
# 1207
ax1.plot(trap_bin[0], trap_bin[1], c='k')
ax1.plot(J1207_bin[0], J1207_bin[1], c='#1036CF', alpha=0.75)
# ax1.plot(df_trap['w'], norm_df_trap, c='k')
# ax1.plot(df_1207['w'], norm_df_1207, c='#1036CF', alpha=0.75)
ax1.annotate('J1207-3900 (L1 $\gamma$) $L_\mathrm{bol}: -3.336 \pm 0.053$', xy=(1.121, 1.3), color='#1036CF', fontsize=14)
# 0518
ax1.plot(trap_bin[0], trap_bin[1] + 1.1, c='k')
ax1.plot(J0518_bin[0], J0518_bin[1] + 1.1, c='#5518C2', alpha=0.75)
# ax1.plot(df_trap['w'], norm_df_trap + 1, c='k')
# ax1.plot(df_0518['w'], norm_df_0518 + 1.1, c='#5518C2', alpha=0.75)
ax1.annotate('J0518-2756 (L1 $\gamma$) $L_\mathrm{bol}: -3.328 \pm 0.041$', xy=(1.121, 2.3), color='#5518C2', fontsize=14)
# vb10
ax1.plot(trap_bin[0], trap_bin[1] + 2.1, c='k')
# ax1.plot(df_trap['w'], norm_df_trap + 2.1, c='k')
ax1.plot(df_vb10['w'], norm_df_vb10 + 2.1, c='#275202', alpha=0.8)
ax1.annotate('vB 10 (M8) $L_\mathrm{bol}: -3.298 \pm 0.002$', xy=(1.121, 3.3), color='#275202', fontsize=14)
# Trappist
ax1.plot(trap_bin[0], trap_bin[1] + 3.1, c='k')
# ax1.plot(df_trap['w'], norm_df_trap + 3.1, c='k')
ax1.annotate('TRAPPIST-1 (M7.5) $L_\mathrm{bol}: -3.255 \pm 0.002$', xy=(1.121, 4.3), color='k', fontsize=14)
# 320
ax1.plot(trap_bin[0], trap_bin[1] + 4.1, c='k')
# ax1.plot(df_trap['w'], norm_df_trap + 4.1, c='k')
ax1.plot(df_0320['w'], norm_df_0320 + 4.1, c='#1EE801', alpha=0.75)
ax1.annotate('J0320+1854 (M8) $L_\mathrm{bol}: -3.225 \pm 0.002$', xy=(1.121, 5.3), color='#1EE801', fontsize=14)
# 0443
ax1.plot(trap_bin[0], trap_bin[1] + 5.1, c='k')
ax1.plot(J0443_bin[0], J0443_bin[1] + 5.1, c='#E71BF8', alpha=0.75)
# ax1.plot(df_trap['w'], norm_df_trap + 5.1, c='k')
# ax1.plot(df_0443['w'], norm_df_0443 + 5.1, c='#E71BF8', alpha=0.75)
ax1.annotate('J0443+0002 (L0 $\gamma$) $L_\mathrm{bol}: -3.194\pm 0.003$', xy=(1.121, 6.3), color='#E71BF8', fontsize=14)
# vb8
ax1.plot(trap_bin[0], trap_bin[1] + 6.2, c='k')
# ax1.plot(df_trap['w'], norm_df_trap + 6.5, c='k')
ax1.plot(df_vb8['w'], norm_df_vb8 + 6.2, c='#04A57F', alpha=0.75)
ax1.annotate('vB 8 (M7) $L_\mathrm{bol}: -3.192 \pm 0.002$', xy=(1.121, 7.5), color='#04A57F', fontsize=14)

# ------- Label Features --------------------------
NaI = pd.DataFrame()
NaI['x'] = [1.1383850, 1.1383850]
NaI['y'] = [8, 8.2]
plt.plot(NaI['x'], NaI['y'], color='k')
ax1.annotate('Na$\,$I', xy=(1.133, 8.25), color='k', fontsize=15)
NaId = pd.DataFrame()
NaId['x'] = [1.1408517, 1.1408517]
NaId['y'] = [8, 8.2]
plt.plot(NaId['x'], NaId['y'], color='k')
NaIhor = pd.DataFrame()
NaIhor['x'] = [1.1383850, 1.1408517]
NaIhor['y'] = [8.2, 8.2]
plt.plot(NaIhor['x'], NaIhor['y'], color='k')

KI1 = pd.DataFrame()
KI1['x'] = [1.1692427, 1.1692427]
KI1['y'] = [8, 8.2]
plt.plot(KI1['x'], KI1['y'], color='k')
ax1.annotate('K$\,$I', xy=(1.17, 8.25), color='k', fontsize=15)
KI1up1 = pd.DataFrame()
KI1up1['x'] = [1.1778406, 1.1778406]
KI1up1['y'] = [8, 8.2]
plt.plot(KI1up1['x'], KI1up1['y'], color='k')
KI1hor = pd.DataFrame()
KI1hor['x'] = [1.1692427, 1.1778406]
KI1hor['y'] = [8.2, 8.2]
plt.plot(KI1hor['x'], KI1hor['y'], color='k')

FeH = pd.DataFrame()
FeH['x'] = [1.19, 1.24]
FeH['y'] = [8.2, 8.2]
plt.plot(FeH['x'], FeH['y'], color='k')
ax1.annotate('FeH', xy=(1.2, 8.25), color='k', fontsize=15)
FeHd = pd.DataFrame()
FeHd['x'] = [1.19, 1.19]
FeHd['y'] = [8, 8.2]
plt.plot(FeHd['x'], FeHd['y'], color='k')

KI2 = pd.DataFrame()
KI2['x'] = [1.2436839, 1.2528860]
KI2['y'] = [8, 8]
plt.plot(KI2['x'], KI2['y'], color='k')
ax1.annotate('K$\,$I', xy=(1.245, 8.05), color='k', fontsize=15)
KI2up1 = pd.DataFrame()
KI2up1['x'] = [1.2436839, 1.2436839]
KI2up1['y'] = [7.8, 8]
plt.plot(KI2up1['x'], KI2up1['y'], color='k')
KI2up2 = pd.DataFrame()
KI2up2['x'] = [1.2528860, 1.2528860]
KI2up2['y'] = [7.8, 8]
plt.plot(KI2up2['x'], KI2up2['y'], color='k')

H2O = pd.DataFrame()
H2O['x'] = [1.32, 1.35]
H2O['y'] = [8, 8]
plt.plot(H2O['x'], H2O['y'], color='k')
ax1.annotate('H$_\mathrm{2} $O', xy=(1.33, 8.05), color='k', fontsize=15)
H2Od = pd.DataFrame()
H2Od['x'] = [1.32, 1.32]
H2Od['y'] = [7.8, 8]
plt.plot(H2Od['x'], H2Od['y'], color='k')

plt.tight_layout()
plt.savefig('Figures/Jbandlbolcomp.pdf', dpi=150)

# -------------------------------------------------------------------------------------
# ------------------- Plotting: J band stack comparison -------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
# fig = plt.figure()
# ax1 = fig.add_subplot(111)
# fig.set_size_inches(10, 8)
# plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
# plt.xlim([1.12, 1.35])
# plt.ylim([0, 1.75])
# for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
#     ax1.spines[axis].set_linewidth(1.1)
#
# # ------Tick size and Axes Labels --------
# ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
# plt.xlabel('Wavelength ($\mu$m)', fontsize=25)
# plt.ylabel('Normalized Flux ($F_\lambda$)', fontsize=25)
#
# # -------- Add data -----------
# ax1.plot(df_2235['w'], norm_df_2235, c='#8E01E8')
# ax1.plot(df_2154['w'], norm_df_2154, c='#E806B7')
# ax1.plot(df_trap['w'], norm_df_trap, c='k')
#
# # ------- Label Features --------------------------
# NaI = pd.DataFrame()
# NaI['x'] = [1.13656, 1.14269]
# NaI['y'] = [0.3, 0.3]
# plt.plot(NaI['x'], NaI['y'], color='k')
# ax1.text(0.0625, 0.13, 'Na$\,$I', transform=ax1.transAxes, color='k', fontsize=15)
# # ----- Making each of the vertical lines on each end --------
# NaId = pd.DataFrame()
# NaId['x'] = [1.13656, 1.13656]
# NaId['y'] = [0.3, 0.4]
# plt.plot(NaId['x'], NaId['y'], color='k')
# NaId2 = pd.DataFrame()
# NaId2['x'] = [1.14269, 1.14269]
# NaId2['y'] = [0.3, 0.4]
# plt.plot(NaId2['x'], NaId2['y'], color='k')
#
# KI1 = pd.DataFrame()
# KI1['x'] = [1.16569, 1.18225]
# KI1['y'] = [0.25, 0.25]
# plt.plot(KI1['x'], KI1['y'], color='k')
# ax1.text(0.22, 0.11, 'K$\,$I', transform=ax1.transAxes, color='k', fontsize=15)
# # ----- Making each of the vertical lines on each end --------
# KI1up1 = pd.DataFrame()
# KI1up1['x'] = [1.16569, 1.16569]
# KI1up1['y'] = [0.25, 0.4]
# plt.plot(KI1up1['x'], KI1up1['y'], color='k')
# KI1up2 = pd.DataFrame()
# KI1up2['x'] = [1.18225, 1.18225]
# KI1up2['y'] = [0.25, 0.4]
# plt.plot(KI1up2['x'], KI1up2['y'], color='k')
#
# FeH = pd.DataFrame()
# FeH['x'] = [1.19, 1.24]
# FeH['y'] = [1.3, 1.3]
# plt.plot(FeH['x'], FeH['y'], color='k')
# ax1.text(0.38, 0.75, 'FeH', transform=ax1.transAxes, color='k', fontsize=15)
# FeHd = pd.DataFrame()
# FeHd['x'] = [1.19, 1.19]
# FeHd['y'] = [1.15, 1.3]
# plt.plot(FeHd['x'], FeHd['y'], color='k')
#
# KI2 = pd.DataFrame()
# KI2['x'] = [1.24175, 1.25616]
# KI2['y'] = [0.3, 0.3]
# plt.plot(KI2['x'], KI2['y'], color='k')
# ax1.text(0.54, 0.13, 'K$\,$I', transform=ax1.transAxes, color='k', fontsize=15)
# KI2up1 = pd.DataFrame()
# KI2up1['x'] = [1.24175, 1.24175]
# KI2up1['y'] = [0.3, 0.4]
# plt.plot(KI2up1['x'], KI2up1['y'], color='k')
# KI2up2 = pd.DataFrame()
# KI2up2['x'] = [1.25616, 1.25616]
# KI2up2['y'] = [0.3, 0.4]
# plt.plot(KI2up2['x'], KI2up2['y'], color='k')
#
# H2O = pd.DataFrame()
# H2O['x'] = [1.32, 1.35]
# H2O['y'] = [1.55, 1.55]
# plt.plot(H2O['x'], H2O['y'], color='k')
# ax1.text(0.9, 0.9, 'H$_\mathrm{2} $O', transform=ax1.transAxes, color='k', fontsize=15)
# H2Od = pd.DataFrame()
# H2Od['x'] = [1.32, 1.32]
# H2Od['y'] = [1.48, 1.55]
# plt.plot(H2Od['x'], H2Od['y'], color='k')
#
# plt.tight_layout()
# plt.savefig('Figures/Jbandlbolstackcomp.pdf', dpi=150)
