import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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
df_1207_phot = pd.read_csv('Data/young_comp/1207-3900 (L0gamma) phot.txt', sep=" ", comment='#', header=None,
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
norm_region = df_trap[(df_trap['w'] >= 2.16) & (df_trap['w'] <= 2.20)]
norm_df_trap = df_trap['f']/(np.average(norm_region['f']))

norm_region2 = df_vb8[(df_vb8['w'] >= 2.16) & (df_vb8['w'] <= 2.20)]
norm_df_vb8 = df_vb8['f']/(np.average(norm_region2['f']))

norm_region3 = df_vb10[(df_vb10['w'] >= 2.16) & (df_vb10['w'] <= 2.20)]
norm_df_vb10 = df_vb10['f']/(np.average(norm_region3['f']))

norm_region4 = df_0320[(df_0320['w'] >= 2.16) & (df_0320['w'] <= 2.20)]
norm_df_0320 = df_0320['f']/(np.average(norm_region4['f']))

norm_region5 = df_1207[(df_1207['w'] >= 2.16) & (df_1207['w'] <= 2.20)]
norm_df_1207 = df_1207['f']/(np.average(norm_region5['f']))

norm_region6 = df_0443[(df_0443['w'] >= 2.16) & (df_0443['w'] <= 2.20)]
norm_df_0443 = df_0443['f']/(np.average(norm_region6['f']))

norm_region7 = df_0518[(df_0518['w'] >= 2.16) & (df_0518['w'] <= 2.20)]
norm_df_0518 = df_0518['f']/(np.average(norm_region7['f']))

# -------------------------------------------------------------------------------------
# ------------------- Plotting: J band comparison -------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(8.5, 11)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([2.0, 2.35])
plt.ylim([0.5, 8.5])
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)

# ------Tick size and Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xlabel('Wavelength ($\mu$m)', fontsize=25)
plt.ylabel('Normalized Flux ($F_\lambda$)', fontsize=25)

# -------- Add data -----------
# 1207
ax1.plot(df_trap['w'], norm_df_trap, c='k')
ax1.plot(df_1207['w'], norm_df_1207, c='#1036CF', alpha=0.75)
ax1.annotate('J1207-3900 (L0 $\gamma$) $L_\mathrm{bol}: -3.337 \pm 0.053$', xy=(2.001, 1.2), color='#1036CF', fontsize=13)
# 0518
ax1.plot(df_trap['w'], norm_df_trap + 1, c='k')
ax1.plot(df_0518['w'], norm_df_0518 + 1, c='#5518C2', alpha=0.75)
ax1.annotate('J0518-2756 (L1 $\gamma$) $L_\mathrm{bol}: -3.328 \pm 0.041$', xy=(2.001, 2.2), color='#5518C2', fontsize=13)
# vb10
ax1.plot(df_trap['w'], norm_df_trap + 2, c='k')
ax1.plot(df_vb10['w'], norm_df_vb10 + 2, c='#275202', alpha=0.8)
ax1.annotate('vb10 (M8) $L_\mathrm{bol}: -3.301 \pm 0.002$', xy=(2.001, 3.2), color='#275202', fontsize=13)
# Trappist
ax1.plot(df_trap['w'], norm_df_trap + 3, c='k')
ax1.annotate('Trappist-1 (M7.5) $L_\mathrm{bol}: -3.255 \pm 0.002$', xy=(2.001, 4.2), color='k', fontsize=13)
# 320
ax1.plot(df_trap['w'], norm_df_trap + 4, c='k')
ax1.plot(df_0320['w'], norm_df_0320 + 4, c='#1EE801', alpha=0.75)
ax1.annotate('J0320+1854 (M8) $L_\mathrm{bol}: -3.225 \pm 0.002$', xy=(2.001, 5.2), color='#1EE801', fontsize=13)
# 0443
ax1.plot(df_trap['w'], norm_df_trap + 5, c='k')
ax1.plot(df_0443['w'], norm_df_0443 + 5, c='#E71BF8', alpha=0.75)
ax1.annotate('J0443+0002 (M9 $\gamma$) $L_\mathrm{bol}: -3.194\pm 0.003$', xy=(2.001, 6.2), color='#E71BF8', fontsize=13)
# vb8
ax1.plot(df_trap['w'], norm_df_trap + 6, c='k')
ax1.plot(df_vb8['w'], norm_df_vb8 + 6, c='#04A57F', alpha=0.75)
ax1.annotate('vb8 (M7) $L_\mathrm{bol}: -3.2 \pm 0.007$', xy=(2.001, 7.2), color='#04A57F', fontsize=13)

# ------- Label Features --------------------------
H2O = pd.DataFrame()
H2O['x'] = [2.00, 2.05]
H2O['y'] = [7.6, 7.6]
plt.plot(H2O['x'], H2O['y'], color='k')
ax1.annotate('H$_\mathrm{2}$O', xy=(2.02, 7.65), color='k', fontsize=15)

CIA_H2 = pd.DataFrame()
CIA_H2['x'] = [2.01, 2.34]
CIA_H2['y'] = [8, 8]
plt.plot(CIA_H2['x'], CIA_H2['y'], color='k')
ax1.annotate('CIA H$_\mathrm{2} $', xy=(2.15, 8.05), color='k', fontsize=15)

NaI = pd.DataFrame()
NaI['x'] = [2.20, 2.211]
NaI['y'] = [3.5, 3.5]
plt.plot(NaI['x'], NaI['y'], color='k')
ax1.annotate('Na$\,$I', xy=(2.195, 3.3), color='k', fontsize=15)
# ----- Making each of the vertical lines on each end --------
NaId = pd.DataFrame()
NaId['x'] = [2.20, 2.20]
NaId['y'] = [3.5, 3.6]
plt.plot(NaId['x'], NaId['y'], color='k')
NaId2 = pd.DataFrame()
NaId2['x'] = [2.211, 2.211]
NaId2['y'] = [3.5, 3.6]
plt.plot(NaId2['x'], NaId2['y'], color='k')

CO = pd.DataFrame()
CO['x'] = [2.295, 2.34]
CO['y'] = [7.6, 7.6]
plt.plot(CO['x'], CO['y'], color='k')
ax1.annotate('CO', xy=(2.31, 7.61), color='k', fontsize=15)
COd = pd.DataFrame()
COd['x'] = [2.295, 2.295]
COd['y'] = [7.4, 7.6]
plt.plot(COd['x'], COd['y'], color='k')

plt.tight_layout()
plt.savefig('Figures/KbandLbol.pdf', dpi=150)

# -------------------------------------------------------------------------------------
# ------------------- Plotting: K band stack comparison -------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
# fig = plt.figure()
# ax1 = fig.add_subplot(111)
# fig.set_size_inches(10, 8)
# plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
# plt.xlim([2.0, 2.35])
# plt.ylim([0.4, 1.5])
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
# plt.tight_layout()
# plt.savefig('Figures/KbandLbolstack.png', dpi=150)
