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
norm_region = df_trap[(df_trap['w'] >= 2.16) & (df_trap['w'] <= 2.20)]
norm_df_trap = df_trap['f']/(np.average(norm_region['f']))

norm_region2 = df_vb8[(df_vb8['w'] >= 2.16) & (df_vb8['w'] <= 2.20)]
norm_df_vb8 = df_vb8['f']/(np.average(norm_region2['f']))

norm_region3 = df_twa27[(df_twa27['w'] >= 2.16) & (df_twa27['w'] <= 2.20)]
norm_df_twa27 = df_twa27['f']/(np.average(norm_region3['f']))

norm_region4 = df_twa28[(df_twa28['w'] >= 2.16) & (df_twa28['w'] <= 2.20)]
norm_df_twa28 = df_twa28['f']/(np.average(norm_region4['f']))

norm_region5 = df_twa26[(df_twa26['w'] >= 2.16) & (df_twa26['w'] <= 2.20)]
norm_df_twa26 = df_twa26['f']/(np.average(norm_region5['f']))

norm_region6 = df_twa29[(df_twa29['w'] >= 2.16) & (df_twa29['w'] <= 2.20)]
norm_df_twa29 = df_twa29['f']/(np.average(norm_region6['f']))


# -------------------------------------------------------------------------------------
# ------------------- Plotting: K band comparison -------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(8.5, 11)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([2.0, 2.35])
plt.ylim([0.5, 4.5])
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)

# ------Tick size and Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xlabel('Wavelength ($\mu$m)', fontsize=25)
plt.ylabel('Normalized Flux ($F_\lambda$)', fontsize=25)

# -------- Add data -----------
ax1.plot(df_vb8['w'], norm_df_vb8, c='#7C7D70')
ax1.plot(df_trap['w'], norm_df_trap + 0.5, c='k')
ax1.plot(df_twa27['w'], norm_df_twa27 + 1, c='#FF6C11')
ax1.plot(df_twa28['w'], norm_df_twa28 + 1.5, c='#E8470F')
ax1.plot(df_twa26['w'], norm_df_twa26 + 2, c='#FF3215')
ax1.plot(df_twa29['w'], norm_df_twa29 + 2.5, c='#E81011')

# ------- Label Features --------------------------
H2O = pd.DataFrame()
H2O['x'] = [2.00, 2.20]
H2O['y'] = [3.8, 3.8]
plt.plot(H2O['x'], H2O['y'], color='k')
ax1.annotate('H$_\mathrm{2} $O', xy=(2.09, 3.85), color='k', fontsize=15)

CIA_H2 = pd.DataFrame()
CIA_H2['x'] = [2.01, 2.34]
CIA_H2['y'] = [4.2, 4.2]
plt.plot(CIA_H2['x'], CIA_H2['y'], color='k')
ax1.annotate('CIA H$_\mathrm{2} $', xy=(2.15, 4.25), color='k', fontsize=15)

CO = pd.DataFrame()
CO['x'] = [2.295, 2.34]
CO['y'] = [3.8, 3.8]
plt.plot(CO['x'], CO['y'], color='k')
ax1.annotate('CO', xy=(2.31, 3.82), color='k', fontsize=15)
COd = pd.DataFrame()
COd['x'] = [2.295, 2.295]
COd['y'] = [3.65, 3.8]
plt.plot(COd['x'], COd['y'], color='k')

plt.tight_layout()
plt.savefig('Figures/KbandTeffcomp.png', dpi=150)
