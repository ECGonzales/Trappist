import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas dataframes

df_trap = pd.read_csv('Data/FIRE2306-0502 (M7.5) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])

# -------------- Comparison objects of the same Teff (old) ----------------------------------
df_GJ660 = pd.read_csv('Data/old_comp/spectra_gj6601b.txt', sep="\t", comment='#', header=0,
                       names=["w", "f", "err"])
df_1013 = pd.read_csv('../Atmospheres_paper/Data/1013-1356 (-) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])

# -------------------------------------------------------------------------------------
# ---------------------- Remove Tails ------------------------------------------------
# -------------------------------------------------------------------------------------
df_GJ660 = df_GJ660[(df_GJ660['w'] > 0.7) & (df_GJ660['w'] <= 3)]

# -------------------------------------------------------------------------------------
# ------------------------- Normalize the spectra -------------------------------------
# -------------------------------------------------------------------------------------
# Determine region good for all spectra to take the average flux over
norm_region = df_trap[(df_trap['w'] >= 0.98) & (df_trap['w'] <= 0.988)]
norm_df_trap = df_trap['f']/(np.average(norm_region['f']))

norm_region2 = df_GJ660[(df_GJ660['w'] >= 0.98) & (df_GJ660['w'] <= 0.988)]
norm_df_GJ660 = df_GJ660['f']/(np.average(norm_region2['f']))

norm_region3 = df_1013[(df_1013['w'] >= 0.98) & (df_1013['w'] <= 0.988)]
norm_df_1013 = df_1013['f']/(np.average(norm_region3['f']))

# -------------------------------------------------------------------------------------
# ------------------- Plotting: Y band comparison -------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([0.95, 1.10])
plt.ylim([0, 2])
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)


# ------Tick size and Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xlabel('Wavelength ($\mu$m)', fontsize=25)
plt.ylabel('Normalized Flux ($F_\lambda$)', fontsize=25)

# -------- Add data -----------
ax1.plot(df_trap['w'], norm_df_trap, c='k')  # #7C7D70
ax1.plot(df_GJ660['w'], norm_df_GJ660, c='#07D1E8')
ax1.plot(df_1013['w'], norm_df_1013, c='#0822FF')

# --- To make line for features ---------
FeH1 = pd.DataFrame()
FeH1['x'] = [0.9896, 1.0]
FeH1['y'] = [1.32, 1.32]
plt.plot(FeH1['x'], FeH1['y'], color='k')
ax1.annotate('FeH', xy=(0.99, 1.33), color='k', fontsize=15)
# -- To make a vertical line
FeH1d = pd.DataFrame()
FeH1d['x'] = [0.9896, 0.9896]
FeH1d['y'] = [1.22, 1.32]
plt.plot(FeH1d['x'], FeH1d['y'], color='k')

FeH2 = pd.DataFrame()
FeH2['x'] = [0.998, 1.085]
FeH2['y'] = [1.75, 1.75]
plt.plot(FeH2['x'], FeH2['y'], color='k')
ax1.annotate('FeH', xy=(1.04, 1.76), color='k', fontsize=15)
FeH2d = pd.DataFrame()
FeH2d['x'] = [0.998, 0.998]
FeH2d['y'] = [1.65, 1.75]
plt.plot(FeH2d['x'], FeH2d['y'], color='k')

VO = pd.DataFrame()
VO['x'] = [1.0456, 1.08]
VO['y'] = [1.65, 1.65]
plt.plot(VO['x'], VO['y'], color='k')
ax1.annotate('VO', xy=(1.06, 1.66), color='k', fontsize=15)
VOd = pd.DataFrame()
VOd['x'] = [1.0456, 1.0456]
VOd['y'] = [1.58, 1.65]
plt.plot(VOd['x'], VOd['y'], color='k')

H2O = pd.DataFrame()
H2O['x'] = [1.08, 1.099]
H2O['y'] = [1.89, 1.89]
plt.plot(H2O['x'], H2O['y'], color='k')
ax1.annotate('H$_\mathrm{2} $O', xy=(1.085, 1.91), color='k', fontsize=15)
H2Od = pd.DataFrame()
H2Od['x'] = [1.08, 1.08]
H2Od['y'] = [1.79, 1.89]
plt.plot(H2Od['x'], H2Od['y'], color='k')

plt.tight_layout()
plt.savefig('Figures/Ybandoldcomp_stack.png', dpi=150)
