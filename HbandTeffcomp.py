import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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


# -------- Drop a few spikes aka bad points (may not need with smoothing)----------------
df_0953 = df_0953[(df_0953['w'] >= 1.42) & (df_0953['w'] <= 1.80)]
# Four bad points
df_0953 = df_0953.drop(df_0953['f'].argmax())
df_0953 = df_0953.drop(df_0953['f'].argmax())
df_0953 = df_0953.drop(df_0953['f'].argmax())
df_0953 = df_0953.drop(df_0953['f'].argmax())

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

norm_region4 = df_0953[(df_0953['w'] >= 1.5) & (df_0953['w'] <= 1.52)]
norm_df_0953 = df_0953['f']/(np.average(norm_region4['f']))

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
ax1.plot(df_0953['w'], norm_df_0953, c='#9B0132')
ax1.annotate('J0953-1014 (M9 $\gamma$) $T_\mathrm{eff}: 2430 \pm 255$ K', xy=(1.421, 0.7), color='#9B0132', fontsize=13)
ax1.plot(df_0608['w'], norm_df_0608 + 0.5, c='#FF6B03')
ax1.annotate('J0608-2753 (M8.5 $\gamma$) $T_\mathrm{eff}: 2471 \pm 255$ K', xy=(1.421, 1.9), color='#FF6B03', fontsize=13)
ax1.plot(df_vb10['w'], norm_df_vb10 + 1.2, c='#A0B2BF')
ax1.annotate('vb10 (M8) $T_\mathrm{eff}: 2542 \pm 45$ K', xy=(1.421, 2.35), color='#A0B2BF', fontsize=13)
ax1.plot(df_trap['w'], norm_df_trap + 1.7, c='k')
ax1.annotate('Trappist-1 (M7.5) $T_\mathrm{eff}: 2582 \pm 34$ K', xy=(1.421, 2.95), color='k', fontsize=13)
ax1.plot(df_0320['w'], norm_df_0320 + 2.2, c='#6A777F')
ax1.annotate('J0320+1854 (M8) $T_\mathrm{eff}: 2615 \pm 34$ K', xy=(1.421, 3.4), color='#6A777F', fontsize=13)
ax1.plot(df_vb8['w'], norm_df_vb8 + 2.7, c='#7C7D70')
ax1.annotate('vb8 (M7) $T_\mathrm{eff}: 2642 \pm 34$ K', xy=(1.421, 3.9), color='#7C7D70', fontsize=13)

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
plt.savefig('Figures/Hbandteffcomp.png', dpi=150)
