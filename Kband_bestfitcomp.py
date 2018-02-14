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
df_HD = pd.read_csv('../Atmospheres_paper/Data/HD114762B (M9sd) SED.txt', sep=" ", comment='#', header=None,
                    names=["w", "f", "err"])

# -------------------------------------------------------------------------------------
# ------------------------- Normalize the spectra -------------------------------------
# -------------------------------------------------------------------------------------
# Determine region good for all spectra to take the average flux over
norm_region = df_trap[(df_trap['w'] >= 2.16) & (df_trap['w'] <= 2.20)]
norm_df_trap = df_trap['f']/(np.average(norm_region['f']))

norm_region2 = df_2154[(df_2154['w'] >= 2.16) & (df_2154['w'] <= 2.20)]
norm_df_young = df_2154['f']/(np.average(norm_region2['f']))

norm_region3 = df_HD[(df_HD['w'] >= 2.16) & (df_HD['w'] <= 2.20)]
norm_df_old = df_HD['f']/(np.average(norm_region3['f']))

# -------------------------------------------------------------------------------------
# ------------------- Plotting: Y band comparison -------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([2.0, 2.35])
plt.ylim([0, 3])
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)


# ------Tick size and Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xlabel('Wavelength ($\mu$m)', fontsize=25)
plt.ylabel('Normalized Flux ($F_\lambda$)', fontsize=25)

# -------- Add data -----------
#ax1.plot(df_HD['w'], norm_df_old, c='blue')
ax1.plot(df_trap['w'], norm_df_trap, c='k')  #7C7D70
ax1.plot(df_2154['w'], norm_df_young + 1, c='#D01810')

# ------- Label Features --------------------------
H2O = pd.DataFrame()
H2O['x'] = [2.00, 2.20]
H2O['y'] = [2.3, 2.3]
plt.plot(H2O['x'], H2O['y'], color='k')
ax1.annotate('H$_\mathrm{2} $O', xy=(2.09, 2.35), color='k', fontsize=15)

CIA_H2 = pd.DataFrame()
CIA_H2['x'] = [2.01, 2.34]
CIA_H2['y'] = [2.7, 2.7]
plt.plot(CIA_H2['x'], CIA_H2['y'], color='k')
ax1.annotate('CIA H$_\mathrm{2} $', xy=(2.15, 2.75), color='k', fontsize=15)

CO = pd.DataFrame()
CO['x'] = [2.295, 2.34]
CO['y'] = [2.4, 2.4]
plt.plot(CO['x'], CO['y'], color='k')
ax1.annotate('CO', xy=(2.31, 2.43), color='k', fontsize=15)
COd = pd.DataFrame()
COd['x'] = [2.295, 2.295]
COd['y'] = [2.25, 2.4]
plt.plot(COd['x'], COd['y'], color='k')

plt.tight_layout()
plt.savefig('Figures/Kbandbestfit.png', dpi=150)

# --------------------------------------------------------------------------------------
# Create plot with young on top of trappist to see how different they are in that band.
# --------------------------------------------------------------------------------------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([2.0, 2.35])
plt.ylim([0.25, 1.5])
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)


# ------Tick size and Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xlabel('Wavelength ($\mu$m)', fontsize=25)
plt.ylabel('Normalized Flux ($F_\lambda$)', fontsize=25)

# -------- Add data -----------
ax1.plot(df_2154['w'], norm_df_young, c='#D01810')
ax1.plot(df_trap['w'], norm_df_trap, c='k', zorder=2)
ax1.plot(df_HD['w'], norm_df_old, c='blue', zorder=6)

# ------- Label Features --------------------------
H2O = pd.DataFrame()
H2O['x'] = [2.00, 2.20]
H2O['y'] = [1.25, 1.25]
plt.plot(H2O['x'], H2O['y'], color='k')
ax1.annotate('H$_\mathrm{2} $O', xy=(2.09, 1.27), color='k', fontsize=15)

CIA_H2 = pd.DataFrame()
CIA_H2['x'] = [2.01, 2.34]
CIA_H2['y'] = [1.35, 1.35]
plt.plot(CIA_H2['x'], CIA_H2['y'], color='k')
ax1.annotate('CIA H$_\mathrm{2} $', xy=(2.15, 1.37), color='k', fontsize=15)

CO = pd.DataFrame()
CO['x'] = [2.295, 2.34]
CO['y'] = [1.1, 1.1]
plt.plot(CO['x'], CO['y'], color='k')
ax1.annotate('CO', xy=(2.31, 1.11), color='k', fontsize=15)
COd = pd.DataFrame()
COd['x'] = [2.295, 2.295]
COd['y'] = [1, 1.1]
plt.plot(COd['x'], COd['y'], color='k')

plt.tight_layout()
plt.savefig('Figures/Kbandbestfit_stack.png', dpi=150)
