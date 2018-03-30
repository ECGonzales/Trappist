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

# -------------- Drop bad points --------------
df_2154 = df_2154[(df_2154['w'] >= 1.42) & (df_2154['w'] <= 1.80)]  # May not need this is we decide to smooth a bit
df_2154 = df_2154.drop(df_2154['f'].argmin())

df_2235 = df_2235[(df_2235['w'] >= 1.42) & (df_2235['w'] <= 1.80)]
df_2235 = df_2235.drop(df_2235['f'].argmax())
df_2235 = df_2235.drop(df_2235['f'].argmin())
df_2235 = df_2235.drop(df_2235['f'].argmin())

# -------------------------------------------------------------------------------------
# ------------------------- Normalize the spectra -------------------------------------
# -------------------------------------------------------------------------------------
# Determine region good for all spectra to take the average flux over
norm_region = df_trap[(df_trap['w'] >= 1.5) & (df_trap['w'] <= 1.52)]
norm_df_trap = df_trap['f']/(np.average(norm_region['f']))

norm_region2 = df_2235[(df_2235['w'] >= 1.5) & (df_2235['w'] <= 1.52)]
norm_df_2235 = df_2235['f']/(np.average(norm_region2['f']))

norm_region7 = df_2154[(df_2154['w'] >= 1.5) & (df_2154['w'] <= 1.52)]
norm_df_2154 = df_2154['f']/(np.average(norm_region7['f']))

# -------------------------------------------------------------------------------------
# ------------------- Plotting: J band comparison -------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 8)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([1.42, 1.80])
plt.ylim([0.5, 3])
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)

# ------Tick size and Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xlabel('Wavelength ($\mu$m)', fontsize=25)
plt.ylabel('Normalized Flux ($F_\lambda$)', fontsize=25)

# -------- Add data -----------
ax1.plot(df_trap['w'], norm_df_trap, c='k')
ax1.plot(df_2235['w'], norm_df_2235 + 0.6, c='#8E01E8')
ax1.plot(df_2154['w'], norm_df_2154 + 1.2, c='#E806B7')

# ------- Label Features --------------------------
FeH = pd.DataFrame()
FeH['x'] = [1.581, 1.66]
FeH['y'] = [2.75, 2.75]
plt.plot(FeH['x'], FeH['y'], color='k')
ax1.annotate('FeH', xy=(1.61, 2.76), color='k', fontsize=15)
FeHd = pd.DataFrame()
FeHd['x'] = [1.581, 1.581]
FeHd['y'] = [2.6, 2.75]
plt.plot(FeHd['x'], FeHd['y'], color='k')

CH4 = pd.DataFrame()
CH4['x'] = [1.67, 1.75]
CH4['y'] = [2.8, 2.8]
plt.plot(CH4['x'], CH4['y'], color='k')
ax1.annotate('CH$_\mathrm{4}$', xy=(1.7, 2.82), color='k', fontsize=15)
CH4d = pd.DataFrame()
CH4d['x'] = [1.67, 1.67]
CH4d['y'] = [2.65, 2.8]
plt.plot(CH4d['x'], CH4d['y'], color='k')

plt.tight_layout()
plt.savefig('Figures/HbandLbol.png', dpi=150)

# -------------------------------------------------------------------------------------
# ------------------- Plotting: H band Stack comparison -------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 8)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([1.42, 1.80])
plt.ylim([0.5, 1.6])
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
# FeH = pd.DataFrame()
# FeH['x'] = [1.581, 1.66]
# FeH['y'] = [2.75, 2.75]
# plt.plot(FeH['x'], FeH['y'], color='k')
# ax1.annotate('FeH', xy=(1.61, 2.76), color='k', fontsize=15)
# FeHd = pd.DataFrame()
# FeHd['x'] = [1.581, 1.581]
# FeHd['y'] = [2.6, 2.75]
# plt.plot(FeHd['x'], FeHd['y'], color='k')
#
# CH4 = pd.DataFrame()
# CH4['x'] = [1.67, 1.75]
# CH4['y'] = [2.8, 2.8]
# plt.plot(CH4['x'], CH4['y'], color='k')
# ax1.annotate('CH$_\mathrm{4}$', xy=(1.7, 2.82), color='k', fontsize=15)
# CH4d = pd.DataFrame()
# CH4d['x'] = [1.67, 1.67]
# CH4d['y'] = [2.65, 2.8]
# plt.plot(CH4d['x'], CH4d['y'], color='k')

plt.tight_layout()
plt.savefig('Figures/HbandLbolstack.png', dpi=150)
