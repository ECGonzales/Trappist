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
# ------------------- Plotting: Y band comparison -------------------------------
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
ax1.plot(df_trap['w'], norm_df_trap, c='#7C7D70')
ax1.plot(df_2154['w'], norm_df_young + 1, c='#D01810')

#TODO: Add these labels in later
# --- To make line for features ---------

plt.tight_layout()
plt.savefig('Figures/Jbandbestfit.png', dpi=150)