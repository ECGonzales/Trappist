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
norm_region = df_trap[(df_trap['w'] >= 1.29) & (df_trap['w'] <= 1.31)]
norm_df_trap = df_trap['f']/(np.average(norm_region['f']))

norm_region2 = df_2154[(df_2154['w'] >= 1.29) & (df_2154['w'] <= 1.31)]
norm_df_young = df_2154['f']/(np.average(norm_region2['f']))

norm_region3 = df_HD[(df_HD['w'] >= 1.29) & (df_HD['w'] <= 1.31)]
norm_df_old = df_HD['f']/(np.average(norm_region3['f']))

# -------------------------------------------------------------------------------------
# ------------------- Plotting: J band comparison -------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([1.12, 1.35])
plt.ylim([0, 3.2])
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

#TODO: Add these labels in later
# --- To make line for features ---------

plt.tight_layout()
plt.savefig('Figures/Jbandbestfit.png', dpi=150)


# --------------------------------------------------------------------------------------
# Create plot with young on top of trappist to see how different they are in that band.
# --------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([1.12, 1.35])
plt.ylim([0, 1.5])
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)


# ------Tick size and Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xlabel('Wavelength ($\mu$m)', fontsize=25)
plt.ylabel('Normalized Flux ($F_\lambda$)', fontsize=25)

# -------- Add data -----------
#ax1.plot(df_HD['w'], norm_df_old, c='blue')
ax1.plot(df_trap['w'], norm_df_trap, c='k', zorder=5)  #7C7D70
ax1.plot(df_2154['w'], norm_df_young, c='#D01810')
ax1.plot(df_HD['w'], norm_df_old, c='blue', zorder=6)

# TODO: Finish these labels in later!!!
# ------- Label Features --------------------------
NaI = pd.DataFrame()
NaI['x'] = [1.13656, 1.14269]
NaI['y'] = [0.25, 0.25]
plt.plot(NaI['x'], NaI['y'], color='k')
ax1.annotate('Na$\,$I', xy=(1.135, 0.15), color='k', fontsize=15)
# ----- Making each of the vertical lines on each end --------
NaId = pd.DataFrame()
NaId['x'] = [1.13656, 1.13656]
NaId['y'] = [0.25, 0.35]
plt.plot(NaId['x'], NaId['y'], color='k')
NaId2 = pd.DataFrame()
NaId2['x'] = [1.14269, 1.14269]
NaId2['y'] = [0.25, 0.35]
plt.plot(NaId2['x'], NaId2['y'], color='k')

# KI1 = pd.DataFrame()
# KI1['x'] = [1.16569, 1.18225]
# KI1['y'] = [0.3, 0.3]
# plt.plot(KI1['x'], KI1['y'], color='k')
# ax1.annotate('K$\,$I', xy=(1.135, 0.15), color='k', fontsize=15)
# # ----- Making each of the vertical lines on each end --------
# KI1up1 = pd.DataFrame()
# KI1up1['x'] = [1.16569, 1.16569]
# KI1up1['y'] = [0.3, 0.4]
# plt.plot(KI1up1['x'], KI1up1['y'], color='k')
# KI1up2 = pd.DataFrame()
# KI1up2['x'] = [1.18225, 1.18225]
# KI1up2['y'] = [0.3, 0.4]
# plt.plot(KI1up2['x'], KI1up2['y'], color='k')

FeH = pd.DataFrame()
FeH['x'] = [1.19, 1.24]
FeH['y'] = [1.2, 1.2]
plt.plot(FeH['x'], FeH['y'], color='k')
ax1.annotate('FeH', xy=(1.21, 1.21), color='k', fontsize=15)
FeHd = pd.DataFrame()
FeHd['x'] = [1.19, 1.19]
FeHd['y'] = [1.1, 1.2]
plt.plot(FeHd['x'], FeHd['y'], color='k')

# KI2 = pd.DataFrame()
# KI2['x'] = [1.24175, 1.25616]
# KI2['y'] = [0.6, 0.6]
# plt.plot(KI2['x'], KI2['y'], color='k')
# ax1.annotate('K$\,$I', xy=(1.135, 0.15), color='k', fontsize=15)
# KI2up1 = pd.DataFrame()
# KI2up1['x'] = [1.24175, 1.24175]
# KI2up1['y'] = [0.6, 0.7]
# plt.plot(KI2up1['x'], KI2up1['y'], color='k')
# KI2up2 = pd.DataFrame()
# KI2up2['x'] = [1.25616, 1.25616]
# KI2up2['y'] = [0.6, 0.7]
# plt.plot(KI2up2['x'], KI2up2['y'], color='k')

H2O = pd.DataFrame()
H2O['x'] = [1.32, 1.35]
H2O['y'] = [1.35, 1.35]
plt.plot(H2O['x'], H2O['y'], color='k')
ax1.annotate('H$_\mathrm{2} $O', xy=(1.325, 1.37), color='k', fontsize=15)
H2Od = pd.DataFrame()
H2Od['x'] = [1.32, 1.32]
H2Od['y'] = [1.25, 1.35]
plt.plot(H2Od['x'], H2Od['y'], color='k')

plt.tight_layout()
plt.savefig('Figures/Jbandbestfit_stack.png', dpi=150)
