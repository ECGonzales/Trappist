import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas dataframes

df_trap = pd.read_csv('Data/FIRE2306-0502 (M7.5) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_trap_phot = pd.read_csv('Data/FIRE2306-0502 (M7.5) phot.txt', sep=" ", comment='#', header=None,
                           names=["w", "f", "err"])
df_2154 = pd.read_csv('Data/young_comp/2154-7459 (M9.5beta) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_2154_phot = pd.read_csv('Data/young_comp/2154-7459 (M9.5beta) phot.txt', sep=" ", comment='#', header=None,
                           names=["w", "f", "err"])
df_HD = pd.read_csv('../Atmospheres_paper/Data/HD114762B (M9sd) SED.txt', sep=" ", comment='#', header=None,
                    names=["w", "f", "err"])
df_HD_phot = pd.read_csv('../Atmospheres_paper/Data/HD114762B (M9sd) phot.txt', sep=" ", comment='#', header=None,
                         names=["w", "f", "err"])

# -------------------------------------------------------------------------------------
# ---------------------- Remove Tails ------------------------------------------------
# -------------------------------------------------------------------------------------
df_HD = df_HD[(df_HD['w'] > 0.91) & (df_HD['w'] <= 3)]

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
ax1.loglog(df_trap['w'], df_trap['f'], c='k', zorder=22)
ax1.scatter(df_trap_phot['w'], df_trap_phot['f'], c='k', s=70, zorder=23)
ax1.loglog(df_2154['w'], df_2154['f'], c='#D01810')
ax1.scatter(df_2154_phot['w'], df_2154_phot['f'], c='k', s=70)
ax1.scatter(df_2154_phot['w'], df_2154_phot['f'], c='#D01810', s=50)
ax1.loglog(df_HD['w'], df_HD['f'], c='blue')
ax1.scatter(df_HD_phot['w'], df_HD_phot['f'], c='k', s=70)
ax1.scatter(df_HD_phot['w'], df_HD_phot['f'], c='blue', s=50)

# ----- Set axes limits, reformat ticks -----------
plt.xlim([0.5, 13])
plt.ylim([10**(-17), 2*10**(-14)])
ax1.xaxis.set_major_formatter(ScalarFormatter())
ax1.xaxis.set_minor_formatter(ScalarFormatter())
ax1.xaxis.set_minor_locator(plt.FixedLocator([0.5, 0.7, 2, 3, 5, 13]))
ax1.tick_params(axis='both', which='major', labelsize=20, length=8, width=1.1)
ax1.tick_params(axis='both', which='minor', labelsize=20, length=4, width=1.1)
plt.yticks(fontsize=20)

# ------ Axes Labels --------
plt.xlabel('Wavelength ($\mu m$)', fontsize=25)
plt.ylabel('Flux  ($erg\ s^{-1} cm^{-2} A^{-1}$)', fontsize=25)

# ------ Labeling Objects --------
ax1.annotate('Trappist-1 (M7.5) ', xy=(3, 10**(-14)), color='k', fontsize=15)
ax1.annotate('$T_\mathrm{eff}: 2589 \pm 49$ K', xy=(3, 6*10**(-15)), color='k', fontsize=15)
ax1.annotate('J2154$-$7459 (M9 $\\beta$)', xy=(5.3, 6*10**(-16)), color='#D01810', fontsize=15)
ax1.annotate('$T_\mathrm{eff}: 2310 \pm 396$ K', xy=(5.3, 3.6*10**(-16)), color='#D01810', fontsize=15)
ax1.annotate('HD114762B (d/sdM9)', xy=(1, 10**(-16)), color='blue', fontsize=15)
ax1.annotate('$T_\mathrm{eff}: 2870 \pm 50$ K', xy=(1, 7*10**(-17)), color='blue', fontsize=15)

plt.tight_layout()
plt.savefig('Figures/bestfit_comp.png', dpi=150)
