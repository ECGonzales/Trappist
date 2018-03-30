import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas dataframes

df_trap = pd.read_csv('Data/FIRE2306-0502 (M7.5) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_trap_phot = pd.read_csv('Data/FIRE2306-0502 (M7.5) phot.txt', sep=" ",comment='#', header=None, names=["w", "f", "err"])

# -------------- Comparison objects of the same Teff ----------------------------------
df_2235 = pd.read_csv('Data/lbol_comp/Lbol2235-5906 (M8.5beta) SED.txt', sep=" ", comment='#', header=None,
                       names=["w", "f", "err"])
df_2235_phot = pd.read_csv('Data/lbol_comp/Lbol2235-5906 (M8.5beta) phot.txt', sep=" ", comment='#', header=None,
                            names=["w", "f", "err"])
df_2154 = pd.read_csv('Data/lbol_comp/cleanLbolFIRE2154-7459_SED_03222018.txt', sep="\t", comment='#', header=1,
                       names=["w", "f", "err"])
df_2154_phot = pd.read_csv('Data/lbol_comp/LbolFIRE2154-7459_phot_03222018.txt', sep="\t", comment='#', header=None,
                            names=["w", "f", "err"])

# -------------------------------------------------------------------------------------
# ---------------------- Remove Tails ------------------------------------------------
# -------------------------------------------------------------------------------------
df_2154 = df_2154[(df_2154['w'] > 0.81) & (df_2154['w'] <= 3)]

# -------------------------------------------------------------------------------------
# ------------------------- Normalize the spectra -------------------------------------
# -------------------------------------------------------------------------------------
# Determine region good for all spectra to take the average flux over
norm_region = df_trap[(df_trap['w'] >= 2.16) & (df_trap['w'] <= 2.20)]
norm_df_trap = df_trap['f']/(np.average(norm_region['f']))

norm_region2 = df_2235[(df_2235['w'] >= 2.16) & (df_2235['w'] <= 2.20)]
norm_df_2235 = df_2235['f']/(np.average(norm_region2['f']))

norm_region7 = df_2154[(df_2154['w'] >= 2.16) & (df_2154['w'] <= 2.20)]
norm_df_2154 = df_2154['f']/(np.average(norm_region7['f']))

# -------------------------------------------------------------------------------------
# ------------------- Plotting: K band comparison -------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 8)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([2.0, 2.35])
plt.ylim([0, 3.5])
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)

# ------Tick size and Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xlabel('Wavelength ($\mu$m)', fontsize=25)
plt.ylabel('Normalized Flux ($F_\lambda$)', fontsize=25)

# -------- Add data -----------
ax1.plot(df_trap['w'], norm_df_trap, c='k')
ax1.plot(df_2235['w'], norm_df_2235 + 0.75, c='#8E01E8')
ax1.plot(df_2154['w'], norm_df_2154 + 1.5, c='#E806B7')

# ------- Label Features --------------------------
H2O = pd.DataFrame()
H2O['x'] = [2.00, 2.20]
H2O['y'] = [2.84, 2.84]
plt.plot(H2O['x'], H2O['y'], color='k')
ax1.text(0.25, 0.825, 'H$_\mathrm{2} $O', transform=ax1.transAxes, color='k', fontsize=15)

CIA_H2 = pd.DataFrame()
CIA_H2['x'] = [2.01, 2.34]
CIA_H2['y'] = [3.2, 3.2]
plt.plot(CIA_H2['x'], CIA_H2['y'], color='k')
ax1.text(0.45, 0.925, 'CIA H$_\mathrm{2} $', transform=ax1.transAxes, color='k', fontsize=15)

CO = pd.DataFrame()
CO['x'] = [2.295, 2.34]
CO['y'] = [2.95, 2.95]
plt.plot(CO['x'], CO['y'], color='k')
ax1.text(0.88, 0.85, 'CO', transform=ax1.transAxes, color='k', fontsize=15)
COd = pd.DataFrame()
COd['x'] = [2.295, 2.295]
COd['y'] = [2.8, 2.95]
plt.plot(COd['x'], COd['y'], color='k')

plt.tight_layout()
plt.savefig('Figures/KbandLbol.png', dpi=150)

# -------------------------------------------------------------------------------------
# ------------------- Plotting: K band stack comparison -------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 8)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([2.0, 2.35])
plt.ylim([0.4, 1.5])
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)

# ------Tick size and Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xlabel('Wavelength ($\mu$m)', fontsize=25)
plt.ylabel('Normalized Flux ($F_\lambda$)', fontsize=25)

# -------- Add data -----------
ax1.plot(df_2235['w'], norm_df_2235, c='#8E01E8')
ax1.plot(df_2154['w'], norm_df_2154, c='#E806B7')
ax1.plot(df_trap['w'], norm_df_trap, c='k')

plt.tight_layout()
plt.savefig('Figures/KbandLbolstack.png', dpi=150)
