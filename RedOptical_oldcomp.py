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
norm_region = df_trap[(df_trap['w'] >= 0.825) & (df_trap['w'] <= 0.840)]
norm_df_trap = df_trap['f']/(np.average(norm_region['f']))

norm_region2 = df_GJ660[(df_GJ660['w'] >= 0.825) & (df_GJ660['w'] <= 0.840)]
norm_df_GJ660 = df_GJ660['f']/(np.average(norm_region2['f']))

norm_region3 = df_1013[(df_1013['w'] >= 0.825) & (df_1013['w'] <= 0.840)]
norm_df_1013 = df_1013['f']/(np.average(norm_region3['f']))

# -------------------------------------------------------------------------------------
# ------------------- Plotting: Y band comparison -------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([0.6, 0.9])
plt.ylim([0, 3])
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)


# ------Tick size and Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xlabel('Wavelength ($\mu$m)', fontsize=25)
plt.ylabel('Normalized Flux ($F_\lambda$)', fontsize=25)

# -------- Add data -----------
ax1.plot(df_trap['w'], norm_df_trap, c='k', zorder=2)  # #7C7D70
ax1.plot(df_GJ660['w'], norm_df_GJ660 + 0.5, c='#07D1E8', zorder=3)
ax1.plot(df_1013['w'], norm_df_1013 + 1.2, c='#0822FF')

# TODO: Add features to the plot!!
# --- To make line for features ---------

plt.tight_layout()
plt.savefig('Figures/Redoptbandoldcomp.png', dpi=150)

# -----------Stacked Plot for shape comparison ------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([0.6, 0.9])
plt.ylim([0, 1.6])
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)


# ------Tick size and Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xlabel('Wavelength ($\mu$m)', fontsize=25)
plt.ylabel('Normalized Flux ($F_\lambda$)', fontsize=25)

# -------- Add data -----------
ax1.plot(df_trap['w'], norm_df_trap, c='k', zorder=5)  # #7C7D70
ax1.plot(df_GJ660['w'], norm_df_GJ660, c='#07D1E8', zorder=6)
ax1.plot(df_1013['w'], norm_df_1013, c='#0822FF')

plt.tight_layout()
plt.savefig('Figures/Redoptbandoldcomp_stack.png', dpi=150)
