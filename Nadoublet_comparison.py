import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas dataframes
df_trap = pd.read_csv('Data/paper1_trappist/Nadoublet/Gaia2306-0502 (M7.5) SED_smoothed.txt', sep=" ", comment='#',
                      header=None, names=["w", "f", "err"])

# -------------- Subdwarfs ----------------------------------
df_LHS = pd.read_csv('Data/paper1_trappist/Nadoublet/Gaia1439+1839 (M7sd) SED_smoothed.txt', sep=" ",
                     comment='#', header=None, names=["w", "f", "err"])
df_1610 = pd.read_csv('Data/paper1_trappist/Nadoublet/Gaia1610-0040 (M7sd) SED_smoothed.txt', sep=" ",
                      comment='#', header=None, names=["w", "f", "err"])
df_2036 = pd.read_csv('Data/paper1_trappist/Nadoublet/2036+5059 (M7.5sd) SED_smoothed.txt', sep=" ",
                      comment='#', header=None, names=["w", "f", "err"])

# -------------------------------------------------------------------------------------
# --------- Normalize the spectra to same as before for 1256 --------------------------
# -------------------------------------------------------------------------------------
# Determine region good for all spectra to take the average flux over
norm_region = df_trap[(df_trap['w'] >= 1.29) & (df_trap['w'] <= 1.31)]
norm_df_trap = df_trap['f']/(np.average(norm_region['f']))

norm_region_LHS = df_LHS[(df_LHS['w'] >= 1.29) & (df_LHS['w'] <= 1.31)]
norm_df_LHS = df_LHS['f']/(np.average(norm_region_LHS['f']))

norm_region_1610 = df_1610[(df_1610['w'] >= 1.29) & (df_1610['w'] <= 1.31)]
norm_df_1610 = df_1610['f']/(np.average(norm_region_1610['f']))

norm_region_2036 = df_2036[(df_2036['w'] >= 1.29) & (df_2036['w'] <= 1.31)]
norm_df_2036 = df_2036['f']/(np.average(norm_region_2036['f']))

# Plot up the Na I lines
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(8, 10)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)
plt.xlim([1.12, 1.16])   # plotting for only high res for K doublets
plt.ylim([0, 4.5])

# ------ Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xlabel('Wavelength ($\mu m$)', fontsize=25)
plt.ylabel('Normalized Flux  ($F_\lambda$)', fontsize=25)

# -------- Add data -----------
ax1.plot(df_trap['w'], norm_df_trap, c="k")
ax1.plot(df_LHS['w'], norm_df_LHS + 1, c='#01A1D6')                                 # sdM7 2775
ax1.plot(df_1610['w'], norm_df_1610 + 2, c='#04A57F')                               # sdM7 2852
ax1.plot(df_2036['w'], norm_df_2036 + 3, c='#F7BE0F')                               # sdM7.5 3049


# ------- Label Sources -------------
ax1.annotate('TRAPPIST-1 T$_\mathrm{eff}: 2584 \pm 34$ K', xy=(1.139, 1.2), color='k', fontsize=15)
ax1.annotate('LHS 377 T$_\mathrm{eff}: 2739 \pm 6$ K', xy=(1.139, 2.2), color='#01A1D6', fontsize=15)
ax1.annotate('J1610-0040 T$_\mathrm{eff}: 2890 \pm 20$ K', xy=(1.139, 3.2), color='#04A57F', fontsize=15)
ax1.annotate('J2036+5059 T$_\mathrm{eff}: 2983 \pm 22$ K', xy=(1.139, 4.2), color='#F7BE0F', fontsize=15)

plt.tight_layout()
plt.savefig('Figures/NaIdoublet_compwithsub.pdf', dpi=150)
