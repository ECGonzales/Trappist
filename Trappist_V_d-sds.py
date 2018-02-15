import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np

# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas dataframes

df_trap = pd.read_csv('Data/smoothed2306-0502 (M7.5) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_trap_phot = pd.read_csv('Data/FIRE2306-0502 (M7.5) phot.txt', sep=" ", comment='#', header=None,
                           names=["w", "f", "err"])

# ------ d/sd comparisons (shape is most similar) -----------------------
df_GJ660 = pd.read_csv('Data/old_comp/spectra_gj6601b.txt', sep="\t", comment='#', header=0,
                       names=["w", "f", "err"])
df_GJ660_phot = pd.read_csv('Data/old_comp/phot_gj6601b.txt', sep="\t", comment='#', header=0,
                            names=["w", "f", "err"])
df_HD = pd.read_csv('../Atmospheres_paper/Data/HD114762B (M9sd) SED.txt', sep=" ", comment='#', header=None,
                    names=["w", "f", "err"])
df_HD_phot = pd.read_csv('../Atmospheres_paper/Data/HD114762B (M9sd) phot.txt', sep=" ", comment='#', header=None,
                         names=["w", "f", "err"])

# -------------------------------------------------------------------------------------
# ------------------------- Normalize the spectra -------------------------------------
# -------------------------------------------------------------------------------------
# Determine region good for all spectra to take the average flux over
max = np.max(df_trap['f'])
norm_df_trap = df_trap['f']/max

max1 = np.max(df_GJ660['f'])
norm_df_GJ660 = df_GJ660['f']/max1

max2 = np.max(df_HD['f'])
norm_df_HD = df_HD['f']/max2

# -------------------------------------------------------------------------------------
# ------------------- Plotting: Old Comparison of same Teff -------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)  # to make sure proper size run entire code at once and change 8 to 6.45 to
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)  # match other plots on github (the size will change if done in pieces
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)

# -------- Add data -----------
ax1.loglog(df_trap['w'], norm_df_trap, c='k', zorder=22)
#ax1.scatter(df_trap_phot['w'], df_trap_phot['f'], c='k', s=70, zorder=23)

ax1.loglog(df_GJ660['w'], norm_df_GJ660, c='#07D1E8')
#ax1.scatter(df_GJ660_phot['w'], df_GJ660_phot['f'], c='k', s=70)
#ax1.scatter(df_GJ660_phot['w'], df_GJ660_phot['f'], c='#07D1E8', s=50)

ax1.loglog(df_HD['w'], norm_df_HD, c='#05A3FF', zorder=24)     # 200K warmer,but strangle fits very well
#ax1.scatter(df_HD_phot['w'], df_HD_phot['f'], c='k', s=70)
#ax1.scatter(df_HD_phot['w'], df_HD_phot['f'], c='#05A3FF', s=50)

# ----- Set axes limits, reformat ticks -----------
plt.xlim([0.9, 2.35])
plt.ylim([10**(-1), 1.5])
ax1.xaxis.set_major_formatter(ScalarFormatter())
ax1.xaxis.set_minor_formatter(ScalarFormatter())
ax1.xaxis.set_minor_locator(plt.FixedLocator([0.5, 0.7, 2, 3, 13]))
ax1.tick_params(axis='both', which='major', labelsize=20, length=8, width=1.1)
ax1.tick_params(axis='both', which='minor', labelsize=20, length=4, width=1.1)
plt.yticks(fontsize=20)

# ------ Axes Labels --------
plt.xlabel('Wavelength ($\mu m$)', fontsize=25)
plt.ylabel('Flux  ($erg\ s^{-1} cm^{-2} A^{-1}$)', fontsize=25)

# ------ Labeling Objects --------
ax1.annotate('Trappist-1 (M7.5) ', xy=(3, 10**(-14)), color='k', fontsize=15)
ax1.annotate('$T_\mathrm{eff}: 2589 \pm 49$ K', xy=(3, 6*10**(-15)), color='k', fontsize=15)
ax1.annotate('J1013-1356 (sdM9.5)', xy=(3, 3*10**(-17)), color='#0822FF', fontsize=15)
ax1.annotate('$T_\mathrm{eff}: 2606 \pm 32$ K', xy=(3, 1.7*10**(-17)), color='#0822FF', fontsize=15)
ax1.annotate('GJ660.1B (d/sdM7)', xy=(1, 6*10**(-16)), color='#07D1E8', fontsize=15)
ax1.annotate('$T_\mathrm{eff}: 2642 \pm 102$ K', xy=(1, 3.5*10**(-16)), color='#07D1E8', fontsize=15)


plt.tight_layout()
plt.savefig('Figures/olf_comp.png', dpi=150)