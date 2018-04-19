import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas dataframes
df_trap = pd.read_csv('Data/FIRE2306-0502 (M7.5) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])

# Comparison objects with same Teff
# ----Field---
df_vb8 = pd.read_csv('Data/field_comp/1655-0823 (M7) SED.txt', sep=" ", comment='#', header=None,
                     names=["w", "f", "err"])
df_vb10 = pd.read_csv('Data/field_comp/1916+0508 (M8) SED.txt', sep=" ", comment='#', header=None,
                       names=["w", "f", "err"])
df_0320 = pd.read_csv('Data/field_comp/0320+1854 (M8) SED.txt', sep=" ", comment='#', header=None,
                       names=["w", "f", "err"])
# ----Young----
df_twa27 = pd.read_csv('Data/young_comp/1207-3932A (M8) SED.txt', sep=" ", comment='#', header=None,
                       names=["w", "f", "err"])
df_twa28 = pd.read_csv('Data/young_comp/1102-3430 (M8.5gamma) SED.txt', sep=" ", comment='#', header=None,
                       names=["w", "f", "err"])
df_twa26 = pd.read_csv('Data/young_comp/FIRE1139-3159 (M9gamma) SED.txt', sep=" ", comment='#', header=None,
                       names=["w", "f", "err"])
df_twa29 = pd.read_csv('Data/young_comp/FIRE1245-4429 (M9.5) SED.txt', sep=" ", comment='#', header=None,
                       names=["w", "f", "err"])

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

norm_region3 = df_twa27[(df_twa27['w'] >= 1.5) & (df_twa27['w'] <= 1.52)]
norm_df_twa27 = df_twa27['f']/(np.average(norm_region3['f']))

norm_region4 = df_twa28[(df_twa28['w'] >= 1.5) & (df_twa28['w'] <= 1.52)]
norm_df_twa28 = df_twa28['f']/(np.average(norm_region4['f']))

norm_region5 = df_twa26[(df_twa26['w'] >= 1.5) & (df_twa26['w'] <= 1.52)]
norm_df_twa26 = df_twa26['f']/(np.average(norm_region5['f']))

norm_region6 = df_twa29[(df_twa29['w'] >= 1.5) & (df_twa29['w'] <= 1.52)]
norm_df_twa29 = df_twa29['f']/(np.average(norm_region6['f']))

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

# -------- Add data -----------
ax1.plot(df_0320['w'], norm_df_0320, c='#A0B2BF')
ax1.plot(df_vb10['w'], norm_df_vb10 + 0.3, c='#6A777F')
ax1.plot(df_vb8['w'], norm_df_vb8 + 0.6, c='#7C7D70')
ax1.plot(df_trap['w'], norm_df_trap + 0.9, c='k')
ax1.plot(df_twa27['w'], norm_df_twa27 + 1.3, c='#FF6C11')
ax1.plot(df_twa28['w'], norm_df_twa28 + 1.6, c='#E8470F')
ax1.plot(df_twa26['w'], norm_df_twa26 + 1.9, c='#FF3215')
ax1.plot(df_twa29['w'], norm_df_twa29 + 2.3, c='#E81011')

# ------- Label Features --------------------------
H2O1 = pd.DataFrame()
H2O1['x'] = [1.3, 1.51]
H2O1['y'] = [3.6, 3.6]
plt.plot(H2O1['x'], H2O1['y'], color='k')
ax1.annotate('H$_\mathrm{2}$O', xy=(1.45, 3.65), color='k', fontsize=15)

FeH = pd.DataFrame()
FeH['x'] = [1.581, 1.66]
FeH['y'] = [4, 4]
plt.plot(FeH['x'], FeH['y'], color='k')
ax1.annotate('FeH', xy=(1.581, 4.01), color='k', fontsize=15)
FeHd = pd.DataFrame()
FeHd['x'] = [1.581, 1.581]
FeHd['y'] = [3.85, 4]
plt.plot(FeHd['x'], FeHd['y'], color='k')

H2O = pd.DataFrame()
H2O['x'] = [1.75, 2.05]
H2O['y'] = [4.25, 4.25]
plt.plot(H2O['x'], H2O['y'], color='k')
ax1.annotate('H$_\mathrm{2}$O', xy=(1.76, 4.28), color='k', fontsize=15)
H2Od = pd.DataFrame()
H2Od['x'] = [1.75, 1.75]
H2Od['y'] = [4.1, 4.25]
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
