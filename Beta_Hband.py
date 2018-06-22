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

# -------------- Drop bad points --------------
df_2154 = df_2154[(df_2154['w'] >= 1.47) & (df_2154['w'] <= 1.80)]  # May not need this is we decide to smooth a bit
df_2154 = df_2154.drop(df_2154['f'].argmin())

df_2235 = df_2235[(df_2235['w'] >= 1.47) & (df_2235['w'] <= 1.80)]
df_2235 = df_2235.drop(df_2235['f'].argmax())
df_2235 = df_2235.drop(df_2235['f'].argmin())
df_2235 = df_2235.drop(df_2235['f'].argmin())
df_0253 = df_0253[(df_0253['w'] >= 1.42) & (df_0253['w'] <= 1.8)]
df_0253 = df_0253.drop(df_0253['f'].argmax())


# -------------------------------------------------------------------------------------
# ------------------------- Normalize the spectra -------------------------------------
# -------------------------------------------------------------------------------------
# Determine region good for all spectra to take the average flux over
norm_region = df_trap[(df_trap['w'] >= 1.5) & (df_trap['w'] <= 1.52)]
norm_df_trap = df_trap['f']/(np.average(norm_region['f']))

norm_region3 = df_0253[(df_0253['w'] >= 1.5) & (df_0253['w'] <= 1.52)]
norm_df_0253 = df_0253['f']/(np.average(norm_region3['f']))

norm_region2 = df_2235[(df_2235['w'] >= 1.5) & (df_2235['w'] <= 1.52)]
norm_df_2235 = df_2235['f']/(np.average(norm_region2['f']))

norm_region7 = df_2154[(df_2154['w'] >= 1.5) & (df_2154['w'] <= 1.52)]
norm_df_2154 = df_2154['f']/(np.average(norm_region7['f']))

# -------------------------------------------------------------------------------------
# ------------------- Plotting: Y band comparison -------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([1.42, 1.80])
plt.ylim([0.5, 4])
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)

# ------Tick size and Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xlabel('Wavelength ($\mu$m)', fontsize=25)
plt.ylabel('Normalized Flux ($F_\lambda$)', fontsize=25)
plt.tight_layout()

# -------- Add data and Label Sources-----------
# 0253 Teff
ax1.plot(df_0253['w'], norm_df_0253, c='#D01810')
ax1.annotate('J0253+3206 (M7 $\\beta$)', xy=(1.421, 1.2), color='#D01810', fontsize=13)
# Trappist
ax1.plot(df_trap['w'], norm_df_trap + 0.75, c='k')
ax1.annotate('Trappist-1 (M7.5)', xy=(1.421, 2), color='k', fontsize=13)
# 2235 Lbol
ax1.plot(df_2235['w'], norm_df_2235 + 1.5, c='#8E01E8')
ax1.annotate('J2235-5906 (M8.5 $\\beta$)', xy=(1.421, 2.8), color='#8E01E8', fontsize=15)
# 2154 Lbol
ax1.plot(df_2154['w'], norm_df_2154 + 2.3, c='#E806B7')
ax1.annotate('J2154-7459 (M9.5 $\\beta$)', xy=(1.421, 3.55), color='#E806B7', fontsize=15)

# ------- Label Features --------------------------
H2O1 = pd.DataFrame()
H2O1['x'] = [1.3, 1.51]
H2O1['y'] = [3.8, 3.8]
plt.plot(H2O1['x'], H2O1['y'], color='k')
ax1.annotate('H$_\mathrm{2}$O', xy=(1.45, 3.85), color='k', fontsize=15)

FeH = pd.DataFrame()
FeH['x'] = [1.581, 1.66]
FeH['y'] = [3.85, 3.85]
plt.plot(FeH['x'], FeH['y'], color='k')
ax1.annotate('FeH', xy=(1.581, 3.86), color='k', fontsize=15)
FeHd = pd.DataFrame()
FeHd['x'] = [1.581, 1.581]
FeHd['y'] = [3.7, 3.85]
plt.plot(FeHd['x'], FeHd['y'], color='k')

H2O = pd.DataFrame()
H2O['x'] = [1.75, 2.05]
H2O['y'] = [3.8, 3.8]
plt.plot(H2O['x'], H2O['y'], color='k')
ax1.annotate('H$_\mathrm{2}$O', xy=(1.76, 3.85), color='k', fontsize=15)
H2Od = pd.DataFrame()
H2Od['x'] = [1.75, 1.75]
H2Od['y'] = [3.65, 3.8]
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

plt.savefig('Figures/Beta_Hband.png', dpi=150)
