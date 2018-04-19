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
norm_region = df_trap[(df_trap['w'] >= 1.22) & (df_trap['w'] <= 1.23)]
norm_df_trap = df_trap['f']/(np.average(norm_region['f']))

norm_region2 = df_vb8[(df_vb8['w'] >= 1.22) & (df_vb8['w'] <= 1.23)]
norm_df_vb8 = df_vb8['f']/(np.average(norm_region2['f']))

norm_region7 = df_vb10[(df_vb10['w'] >= 1.22) & (df_vb10['w'] <= 1.23)]
norm_df_vb10 = df_vb10['f']/(np.average(norm_region7['f']))

norm_region8 = df_0320[(df_0320['w'] >= 1.22) & (df_0320['w'] <= 1.23)]
norm_df_0320 = df_0320['f']/(np.average(norm_region8['f']))

norm_region3 = df_twa27[(df_twa27['w'] >= 1.22) & (df_twa27['w'] <= 1.23)]
norm_df_twa27 = df_twa27['f']/(np.average(norm_region3['f']))

norm_region4 = df_twa28[(df_twa28['w'] >= 1.22) & (df_twa28['w'] <= 1.23)]
norm_df_twa28 = df_twa28['f']/(np.average(norm_region4['f']))

norm_region5 = df_twa26[(df_twa26['w'] >= 1.22) & (df_twa26['w'] <= 1.23)]
norm_df_twa26 = df_twa26['f']/(np.average(norm_region5['f']))

norm_region6 = df_twa29[(df_twa29['w'] >= 1.22) & (df_twa29['w'] <= 1.23)]
norm_df_twa29 = df_twa29['f']/(np.average(norm_region6['f']))

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

# ------Tick size and Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xlabel('Wavelength ($\mu$m)', fontsize=25)
plt.ylabel('Normalized Flux ($F_\lambda$)', fontsize=25)

# -------- Add data -----------
ax1.plot(df_0320['w'], norm_df_0320, c='#A0B2BF')
ax1.plot(df_vb10['w'], norm_df_vb10 + 0.6, c='#6A777F')
ax1.plot(df_vb8['w'], norm_df_vb8 + 1.1, c='#7C7D70')
ax1.plot(df_trap['w'], norm_df_trap + 1.8, c='k')
ax1.plot(df_twa27['w'], norm_df_twa27 + 2.3, c='#FF6C11')
ax1.plot(df_twa28['w'], norm_df_twa28 + 2.75, c='#E8470F')
ax1.plot(df_twa26['w'], norm_df_twa26 + 3.25, c='#FF3215')
ax1.plot(df_twa29['w'], norm_df_twa29 + 4, c='#E81011')

# ------- Label Features --------------------------
NaI = pd.DataFrame()
NaI['x'] = [1.13656, 1.14269]
NaI['y'] = [0.43, 0.43]
plt.plot(NaI['x'], NaI['y'], color='k')
ax1.annotate('Na$\,$I', xy=(1.133, .265), color='k', fontsize=15)
# ----- Making each of the vertical lines on each end --------
NaId = pd.DataFrame()
NaId['x'] = [1.13656, 1.13656]
NaId['y'] = [0.43, 0.53]
plt.plot(NaId['x'], NaId['y'], color='k')
NaId2 = pd.DataFrame()
NaId2['x'] = [1.14269, 1.14269]
NaId2['y'] = [0.43, 0.53]
plt.plot(NaId2['x'], NaId2['y'], color='k')

KI1 = pd.DataFrame()
KI1['x'] = [1.16569, 1.18225]
KI1['y'] = [0.4, 0.4]
plt.plot(KI1['x'], KI1['y'], color='k')
ax1.annotate('K$\,$I', xy=(1.17, .265), color='k', fontsize=15)
# ----- Making each of the vertical lines on each end --------
KI1up1 = pd.DataFrame()
KI1up1['x'] = [1.16569, 1.16569]
KI1up1['y'] = [0.4, 0.53]
plt.plot(KI1up1['x'], KI1up1['y'], color='k')
KI1up2 = pd.DataFrame()
KI1up2['x'] = [1.18225, 1.18225]
KI1up2['y'] = [0.4, 0.53]
plt.plot(KI1up2['x'], KI1up2['y'], color='k')

FeH = pd.DataFrame()
FeH['x'] = [1.19, 1.24]
FeH['y'] = [5.25, 5.25]
plt.plot(FeH['x'], FeH['y'], color='k')
ax1.annotate('FeH', xy=(1.2, 5.3), color='k', fontsize=15)
FeHd = pd.DataFrame()
FeHd['x'] = [1.19, 1.19]
FeHd['y'] = [5.25, 5.1]
plt.plot(FeHd['x'], FeHd['y'], color='k')

KI2 = pd.DataFrame()
KI2['x'] = [1.24175, 1.25616]
KI2['y'] = [0.5, 0.5]
plt.plot(KI2['x'], KI2['y'], color='k')
ax1.annotate('K$\,$I', xy=(1.245, 0.35), color='k', fontsize=15)
KI2up1 = pd.DataFrame()
KI2up1['x'] = [1.24175, 1.24175]
KI2up1['y'] = [0.5, 0.6]
plt.plot(KI2up1['x'], KI2up1['y'], color='k')
KI2up2 = pd.DataFrame()
KI2up2['x'] = [1.25616, 1.25616]
KI2up2['y'] = [0.5, 0.6]
plt.plot(KI2up2['x'], KI2up2['y'], color='k')

H2O = pd.DataFrame()
H2O['x'] = [1.32, 1.35]
H2O['y'] = [5.35, 5.35]
plt.plot(H2O['x'], H2O['y'], color='k')
ax1.annotate('H$_\mathrm{2} $O', xy=(1.33, 5.4), color='k', fontsize=15)
H2Od = pd.DataFrame()
H2Od['x'] = [1.32, 1.32]
H2Od['y'] = [5.2, 5.35]
plt.plot(H2Od['x'], H2Od['y'], color='k')

plt.tight_layout()
plt.savefig('Figures/Jbandteffcomp.png', dpi=150)
