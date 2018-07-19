import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas dataframes
df_trap = pd.read_csv('Data/Gaia2306-0502 (M7.5) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
# ---- Teff ----
df_0253 = pd.read_csv('Data/beta_comp/Gaia0253+3206 (M7beta) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
# ---- Lbol -----
df_2235 = pd.read_csv('Data/beta_comp/Gaia2235-5906 (M8.5beta) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_2235_phot = pd.read_csv('Data/beta_comp/Gaia2235-5906 (M8.5beta) phot.txt', sep=" ", comment='#', header=None,
                           names=["w", "f", "err"])
df_2154 = pd.read_csv('Data/beta_comp/Gaia2154-7459 (M9.5beta) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_2154_phot = pd.read_csv('Data/beta_comp/Gaia2154-7459 (M9.5beta) phot.txt', sep=" ", comment='#', header=None,
                           names=["w", "f", "err"])

# -------- Drop a few spikes aka bad points (may not need with smoothing)----------------
df_2235 = df_2235[(df_2235['w'] >= 1.12) & (df_2235['w'] <= 1.35)]
# bad points
df_2235 = df_2235.drop(df_2235['f'].argmax())
df_2235 = df_2235.drop(df_2235['f'].argmax())
df_2235 = df_2235.drop(df_2235['f'].argmax())
df_2235 = df_2235.drop(df_2235['f'].argmax())
df_2235 = df_2235.drop(df_2235['f'].argmax())
df_2235 = df_2235.drop(df_2235['f'].argmax())
df_2235 = df_2235.drop(df_2235['f'].argmax())
# drop spike
df_2154 = df_2154[(df_2154['w'] >= 1.12) & (df_2154['w'] <= 1.35)]
df_2154 = df_2154.drop(df_2154['f'].argmax())
df_2154 = df_2154.drop(df_2154['f'].argmax())


# -------------------------------------------------------------------------------------
# ------------------------- Normalize the spectra -------------------------------------
# -------------------------------------------------------------------------------------
# Determine region good for all spectra to take the average flux over
norm_region = df_trap[(df_trap['w'] >= 1.22) & (df_trap['w'] <= 1.23)]
norm_df_trap = df_trap['f']/(np.average(norm_region['f']))

norm_region3 = df_0253[(df_0253['w'] >= 1.22) & (df_0253['w'] <= 1.23)]
norm_df_0253 = df_0253['f']/(np.average(norm_region3['f']))

norm_region2 = df_2235[(df_2235['w'] >= 1.22) & (df_2235['w'] <= 1.23)]
norm_df_2235 = df_2235['f']/(np.average(norm_region2['f']))

norm_region7 = df_2154[(df_2154['w'] >= 1.22) & (df_2154['w'] <= 1.23)]
norm_df_2154 = df_2154['f']/(np.average(norm_region7['f']))

# -------------------------------------------------------------------------------------
# ------------------- Plotting: Y band comparison -------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([1.12, 1.35])
plt.ylim([0.25, 6])
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)

# ------Tick size and Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xlabel('Wavelength ($\mu$m)', fontsize=25)
plt.ylabel('Normalized Flux ($F_\lambda$)', fontsize=25)
plt.tight_layout()

# -------- Add data and Label Sources-----------
# 0253 Teff
ax1.plot(df_trap['w'], norm_df_trap, c='k')
ax1.plot(df_0253['w'], norm_df_0253, c='#D01810', alpha=0.75)
ax1.annotate('J0253+3206 (M7 $\\beta$)', xy=(1.121, 1.2), color='#D01810', fontsize=15)
# Trappist
ax1.plot(df_trap['w'], norm_df_trap + 1.1, c='k')
ax1.annotate('Trappist-1 (M7.5)', xy=(1.121, 2.45), color='k', fontsize=15)
# 2235 Lbol
ax1.plot(df_trap['w'], norm_df_trap + 2.2, c='k')
ax1.plot(df_2235['w'], norm_df_2235 + 2.2, c='#8E01E8', alpha=0.75)
ax1.annotate('J2235-5906 (M8.5 $\\beta$)', xy=(1.121, 3.55), color='#8E01E8', fontsize=15)
# 2154 Lbol
ax1.plot(df_trap['w'], norm_df_trap + 3.4, c='k')
ax1.plot(df_2154['w'], norm_df_2154 + 3.4, c='#E806B7', alpha=0.75)
ax1.annotate('J2154-7459 (M9.5 $\\beta$)', xy=(1.121, 5), color='#E806B7', fontsize=15)

# ------- Label Features --------------------------
NaI = pd.DataFrame()
NaI['x'] = [1.1383850, 1.1383850]
NaI['y'] = [5.4, 5.6]
plt.plot(NaI['x'], NaI['y'], color='k')
ax1.annotate('Na$\,$I', xy=(1.133, 5.65), color='k', fontsize=15)
NaId = pd.DataFrame()
NaId['x'] = [1.1408517, 1.1408517]
NaId['y'] = [5.4, 5.6]
plt.plot(NaId['x'], NaId['y'], color='k')
NaIhor = pd.DataFrame()
NaIhor['x'] = [1.1383850, 1.1408517]
NaIhor['y'] = [5.6, 5.6]
plt.plot(NaIhor['x'], NaIhor['y'], color='k')

KI1 = pd.DataFrame()
KI1['x'] = [1.1692427, 1.1692427]
KI1['y'] = [5.4, 5.6]
plt.plot(KI1['x'], KI1['y'], color='k')
ax1.annotate('K$\,$I', xy=(1.17, 5.65), color='k', fontsize=15)
KI1up1 = pd.DataFrame()
KI1up1['x'] = [1.1778406, 1.1778406]
KI1up1['y'] = [5.4, 5.6]
plt.plot(KI1up1['x'], KI1up1['y'], color='k')
KI1hor = pd.DataFrame()
KI1hor['x'] = [1.1692427, 1.1778406]
KI1hor['y'] = [5.6, 5.6]
plt.plot(KI1hor['x'], KI1hor['y'], color='k')

FeH = pd.DataFrame()
FeH['x'] = [1.19, 1.24]
FeH['y'] = [5, 5]
plt.plot(FeH['x'], FeH['y'], color='k')
ax1.annotate('FeH', xy=(1.2, 5.05), color='k', fontsize=15)
FeHd = pd.DataFrame()
FeHd['x'] = [1.19, 1.19]
FeHd['y'] = [4.8, 5]
plt.plot(FeHd['x'], FeHd['y'], color='k')

KI2 = pd.DataFrame()
KI2['x'] = [1.2436839, 1.2528860]
KI2['y'] = [5, 5]
plt.plot(KI2['x'], KI2['y'], color='k')
ax1.annotate('K$\,$I', xy=(1.245, 5.05), color='k', fontsize=15)
KI2up1 = pd.DataFrame()
KI2up1['x'] = [1.2436839, 1.2436839]
KI2up1['y'] = [4.8, 5]
plt.plot(KI2up1['x'], KI2up1['y'], color='k')
KI2up2 = pd.DataFrame()
KI2up2['x'] = [1.2528860, 1.2528860]
KI2up2['y'] = [4.8, 5]
plt.plot(KI2up2['x'], KI2up2['y'], color='k')

H2O = pd.DataFrame()
H2O['x'] = [1.32, 1.35]
H2O['y'] = [5.25, 5.25]
plt.plot(H2O['x'], H2O['y'], color='k')
ax1.annotate('H$_\mathrm{2} $O', xy=(1.33, 5.3), color='k', fontsize=15)
H2Od = pd.DataFrame()
H2Od['x'] = [1.32, 1.32]
H2Od['y'] = [5, 5.25]
plt.plot(H2Od['x'], H2Od['y'], color='k')

plt.savefig('Figures/Beta_Jband.pdf', dpi=150)
