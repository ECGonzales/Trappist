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
df_2154 = pd.read_csv('Data/lbol_comp/Split2154-7459 (M9.5beta) SED.txt', sep=" ", comment='#', header=None,
                       names=["w", "f", "err"])
df_2154_phot = pd.read_csv('Data/lbol_comp/Split2154-7459 (M9.5beta) phot.txt', sep=" ", comment='#', header=None,
                            names=["w", "f", "err"])


# -------------- Drop bad points --------------
df_2154 = df_2154.drop(df_2154['f'].argmax())
df_2154 = df_2154.drop(df_2154['f'].argmax())
df_2154 = df_2154.drop(df_2154['f'].argmax())
# -------------------------------------------------------------------------------------
# ------------------------- Normalize the spectra -------------------------------------
# -------------------------------------------------------------------------------------
# Determine region good for all spectra to take the average flux over
norm_region = df_trap[(df_trap['w'] >= 1.22) & (df_trap['w'] <= 1.23)]
norm_df_trap = df_trap['f']/(np.average(norm_region['f']))

norm_region2 = df_2235[(df_2235['w'] >= 1.22) & (df_2235['w'] <= 1.23)]
norm_df_2235 = df_2235['f']/(np.average(norm_region2['f']))

norm_region7 = df_2154[(df_2154['w'] >= 1.22) & (df_2154['w'] <= 1.23)]
norm_df_2154 = df_2154['f']/(np.average(norm_region7['f']))

# -------------------------------------------------------------------------------------
# ------------------- Plotting: J band comparison -------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 8)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([1.12, 1.35])
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
NaI = pd.DataFrame()
NaI['x'] = [1.13656, 1.14269]
NaI['y'] = [0.3, 0.3]
plt.plot(NaI['x'], NaI['y'], color='k')
ax1.text(0.0625, 0.04, 'Na$\,$I', transform=ax1.transAxes, color='k', fontsize=15)
# ----- Making each of the vertical lines on each end --------
NaId = pd.DataFrame()
NaId['x'] = [1.13656, 1.13656]
NaId['y'] = [0.3, 0.4]
plt.plot(NaId['x'], NaId['y'], color='k')
NaId2 = pd.DataFrame()
NaId2['x'] = [1.14269, 1.14269]
NaId2['y'] = [0.3, 0.4]
plt.plot(NaId2['x'], NaId2['y'], color='k')

KI1 = pd.DataFrame()
KI1['x'] = [1.16569, 1.18225]
KI1['y'] = [0.25, 0.25]
plt.plot(KI1['x'], KI1['y'], color='k')
ax1.text(0.22, 0.03, 'K$\,$I', transform=ax1.transAxes, color='k', fontsize=15)
# ----- Making each of the vertical lines on each end --------
KI1up1 = pd.DataFrame()
KI1up1['x'] = [1.16569, 1.16569]
KI1up1['y'] = [0.25, 0.4]
plt.plot(KI1up1['x'], KI1up1['y'], color='k')
KI1up2 = pd.DataFrame()
KI1up2['x'] = [1.18225, 1.18225]
KI1up2['y'] = [0.25, 0.4]
plt.plot(KI1up2['x'], KI1up2['y'], color='k')

FeH = pd.DataFrame()
FeH['x'] = [1.19, 1.24]
FeH['y'] = [2.7, 2.7]
plt.plot(FeH['x'], FeH['y'], color='k')
ax1.text(0.38, 0.78, 'FeH', transform=ax1.transAxes, color='k', fontsize=15)
FeHd = pd.DataFrame()
FeHd['x'] = [1.19, 1.19]
FeHd['y'] = [2.55, 2.7]
plt.plot(FeHd['x'], FeHd['y'], color='k')

KI2 = pd.DataFrame()
KI2['x'] = [1.24175, 1.25616]
KI2['y'] = [0.3, 0.3]
plt.plot(KI2['x'], KI2['y'], color='k')
ax1.text(0.54, 0.04, 'K$\,$I', transform=ax1.transAxes, color='k', fontsize=15)
KI2up1 = pd.DataFrame()
KI2up1['x'] = [1.24175, 1.24175]
KI2up1['y'] = [0.3, 0.4]
plt.plot(KI2up1['x'], KI2up1['y'], color='k')
KI2up2 = pd.DataFrame()
KI2up2['x'] = [1.25616, 1.25616]
KI2up2['y'] = [0.3, 0.4]
plt.plot(KI2up2['x'], KI2up2['y'], color='k')

H2O = pd.DataFrame()
H2O['x'] = [1.32, 1.35]
H2O['y'] = [3.1, 3.1]
plt.plot(H2O['x'], H2O['y'], color='k')
ax1.text(0.9, 0.9, 'H$_\mathrm{2} $O', transform=ax1.transAxes, color='k', fontsize=15)
H2Od = pd.DataFrame()
H2Od['x'] = [1.32, 1.32]
H2Od['y'] = [3, 3.1]
plt.plot(H2Od['x'], H2Od['y'], color='k')

plt.tight_layout()
plt.savefig('Figures/Jbandlbolcomp.png', dpi=150)

# -------------------------------------------------------------------------------------
# ------------------- Plotting: J band stack comparison -------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 8)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([1.12, 1.35])
plt.ylim([0, 1.75])
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

# ------- Label Features --------------------------
NaI = pd.DataFrame()
NaI['x'] = [1.13656, 1.14269]
NaI['y'] = [0.3, 0.3]
plt.plot(NaI['x'], NaI['y'], color='k')
ax1.text(0.0625, 0.13, 'Na$\,$I', transform=ax1.transAxes, color='k', fontsize=15)
# ----- Making each of the vertical lines on each end --------
NaId = pd.DataFrame()
NaId['x'] = [1.13656, 1.13656]
NaId['y'] = [0.3, 0.4]
plt.plot(NaId['x'], NaId['y'], color='k')
NaId2 = pd.DataFrame()
NaId2['x'] = [1.14269, 1.14269]
NaId2['y'] = [0.3, 0.4]
plt.plot(NaId2['x'], NaId2['y'], color='k')

KI1 = pd.DataFrame()
KI1['x'] = [1.16569, 1.18225]
KI1['y'] = [0.25, 0.25]
plt.plot(KI1['x'], KI1['y'], color='k')
ax1.text(0.22, 0.11, 'K$\,$I', transform=ax1.transAxes, color='k', fontsize=15)
# ----- Making each of the vertical lines on each end --------
KI1up1 = pd.DataFrame()
KI1up1['x'] = [1.16569, 1.16569]
KI1up1['y'] = [0.25, 0.4]
plt.plot(KI1up1['x'], KI1up1['y'], color='k')
KI1up2 = pd.DataFrame()
KI1up2['x'] = [1.18225, 1.18225]
KI1up2['y'] = [0.25, 0.4]
plt.plot(KI1up2['x'], KI1up2['y'], color='k')

FeH = pd.DataFrame()
FeH['x'] = [1.19, 1.24]
FeH['y'] = [1.3, 1.3]
plt.plot(FeH['x'], FeH['y'], color='k')
ax1.text(0.38, 0.75, 'FeH', transform=ax1.transAxes, color='k', fontsize=15)
FeHd = pd.DataFrame()
FeHd['x'] = [1.19, 1.19]
FeHd['y'] = [1.15, 1.3]
plt.plot(FeHd['x'], FeHd['y'], color='k')

KI2 = pd.DataFrame()
KI2['x'] = [1.24175, 1.25616]
KI2['y'] = [0.3, 0.3]
plt.plot(KI2['x'], KI2['y'], color='k')
ax1.text(0.54, 0.13, 'K$\,$I', transform=ax1.transAxes, color='k', fontsize=15)
KI2up1 = pd.DataFrame()
KI2up1['x'] = [1.24175, 1.24175]
KI2up1['y'] = [0.3, 0.4]
plt.plot(KI2up1['x'], KI2up1['y'], color='k')
KI2up2 = pd.DataFrame()
KI2up2['x'] = [1.25616, 1.25616]
KI2up2['y'] = [0.3, 0.4]
plt.plot(KI2up2['x'], KI2up2['y'], color='k')

H2O = pd.DataFrame()
H2O['x'] = [1.32, 1.35]
H2O['y'] = [1.55, 1.55]
plt.plot(H2O['x'], H2O['y'], color='k')
ax1.text(0.9, 0.9, 'H$_\mathrm{2} $O', transform=ax1.transAxes, color='k', fontsize=15)
H2Od = pd.DataFrame()
H2Od['x'] = [1.32, 1.32]
H2Od['y'] = [1.48, 1.55]
plt.plot(H2Od['x'], H2Od['y'], color='k')

plt.tight_layout()
plt.savefig('Figures/Jbandlbolstackcomp.png', dpi=150)
