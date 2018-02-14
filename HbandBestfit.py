import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas dataframes

df_trap = pd.read_csv('Data/FIRE2306-0502 (M7.5) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])

# Comparison objects that fit the overall SED shape the best
df_2154 = pd.read_csv('Data/young_comp/FIRE2154-7459 (M9.5beta) SED1.txt', sep=" ", comment='#', header=0,
                      names=["w", "f", "err"])
# df_HD = pd.read_csv('../Atmospheres_paper/Data/HD114762B (M9sd) SED.txt', sep=" ", comment='#', header=None,
#                     names=["w", "f", "err"])

# -------------------------------------------------------------------------------------
# ------------------------- Normalize the spectra -------------------------------------
# -------------------------------------------------------------------------------------
# Determine region good for all spectra to take the average flux over
norm_region = df_trap[(df_trap['w'] >= 1.5) & (df_trap['w'] <= 1.52)]
norm_df_trap = df_trap['f']/(np.average(norm_region['f']))

norm_region2 = df_2154[(df_2154['w'] >= 1.5) & (df_2154['w'] <= 1.52)]
norm_df_young = df_2154['f']/(np.average(norm_region2['f']))

# norm_region3 = df_HD[(df_HD['w'] >= 1.29) & (df_HD['w'] <= 1.31)]
# norm_df_old = df_HD['f']/(np.average(norm_region3['f']))

# -------------------------------------------------------------------------------------
# ------------------- Plotting: Y band comparison -------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([1.42, 1.80])
plt.ylim([0, 3])
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)


# ------Tick size and Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xlabel('Wavelength ($\mu$m)', fontsize=25)
plt.ylabel('Normalized Flux ($F_\lambda$)', fontsize=25)

# -------- Add data -----------
#ax1.plot(df_HD['w'], norm_df_old, c='blue')
ax1.plot(df_trap['w'], norm_df_trap, c='k')  ##7C7D70
ax1.plot(df_2154['w'], norm_df_young + 1, c='#D01810')

# ------- Label Features --------------------------
FeH = pd.DataFrame()
FeH['x'] = [1.581, 1.66]
FeH['y'] = [2.5, 2.5]
plt.plot(FeH['x'], FeH['y'], color='k')
ax1.annotate('FeH', xy=(1.6, 2.51), color='k', fontsize=15)
FeHd = pd.DataFrame()
FeHd['x'] = [1.581, 1.581]
FeHd['y'] = [2.35, 2.5]
plt.plot(FeHd['x'], FeHd['y'], color='k')

CH4 = pd.DataFrame()
CH4['x'] = [1.67, 1.75]
CH4['y'] = [2.7, 2.7]
plt.plot(CH4['x'], CH4['y'], color='k')
ax1.annotate('CH$_\mathrm{4}$', xy=(1.70, 2.72), color='k', fontsize=15)
CH4d = pd.DataFrame()
CH4d['x'] = [1.67, 1.67]
CH4d['y'] = [2.5, 2.7]
plt.plot(CH4d['x'], CH4d['y'], color='k')

plt.tight_layout()
plt.savefig('Figures/Hbandbestfit.png', dpi=150)