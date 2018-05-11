import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas dataframes

df_trap = pd.read_csv('Data/Gaia2306-0502 (M7.5) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_trap_phot = pd.read_csv('Data/Gaia2306-0502 (M7.5) phot.txt', sep=" ", comment='#', header=None,
                           names=["w", "f", "err"])

# -------------- Comparison objects of the same Teff (young) ----------------------------------
df_1247 = pd.read_csv('Data/young_comp/Gaia1247-3816 (M9gamma) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_1247_phot = pd.read_csv('Data/young_comp/Gaia1247-3816 (M9gamma) phot.txt', sep=" ", comment='#', header=None,
                           names=["w", "f", "err"])
df_0436 = pd.read_csv('Data/young_comp/Gaia0436-4114 (M8betagamma) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_0436_phot = pd.read_csv('Data/young_comp/Gaia0436-4114 (M8betagamma) phot.txt', sep=" ", comment='#', header=None,
                           names=["w", "f", "err"])
df_0253 = pd.read_csv('Data/young_comp/Gaia0253+3206 (M7beta) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_0253_phot = pd.read_csv('Data/young_comp/Gaia0253+3206 (M7beta) phot.txt', sep=" ", comment='#', header=None,
                           names=["w", "f", "err"])

# -------------------------------------------------------------------------------------
# ------------------- Plotting: Young Comparison of same Teff -------------------------
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
trap = ax1.scatter(df_trap_phot['w'], df_trap_phot['f'], c='k', s=70, zorder=23)

# Low unc
ax1.loglog(df_1247['w'], df_1247['f'], c='#FFAA03')
ax1.scatter(df_1247_phot['w'], df_1247_phot['f'], c='k', s=70)  # The ones with size 70 are to give the circles a
y1247 = ax1.scatter(df_1247_phot['w'], df_1247_phot['f'], c='#FFAA03', s=50)        # black border

ax1.loglog(df_0436['w'], df_0436['f'], c='#FF6007')
ax1.scatter(df_0436_phot['w'], df_0436_phot['f'], c='k', s=70)
y0436 = ax1.scatter(df_0436_phot['w'], df_0436_phot['f'], c='#FF6007', s=50)

ax1.loglog(df_0253['w'], df_0253['f'], c='#9B1301')
ax1.scatter(df_0253_phot['w'], df_0253_phot['f'], c='k', s=70)
y0253 = ax1.scatter(df_0253_phot['w'], df_0253_phot['f'], c='#9B1301', s=50)  # medium unc


# ----- Set axes limits, reformat ticks -----------
plt.xlim([0.3, 23])
plt.ylim([10**(-17), 5*10**(-14)])
ax1.xaxis.set_major_formatter(ScalarFormatter())
ax1.xaxis.set_minor_formatter(ScalarFormatter())
ax1.xaxis.set_minor_locator(plt.FixedLocator([0.3, 0.7, 2, 3, 7.5, 23]))
ax1.tick_params(axis='both', which='major', labelsize=20, length=8, width=1.1)
ax1.tick_params(axis='both', which='minor', labelsize=20, length=4, width=1.1)
plt.yticks(fontsize=20)

# ------ Axes Labels --------
plt.xlabel('Wavelength ($\mu m$)', fontsize=25)
plt.ylabel('Flux ($erg\ s^{-1} cm^{-2} A^{-1}$)', fontsize=25)


# ------ Labeling Objects --------
ax1.annotate('Trappist-1 (M7.5), $T_\mathrm{eff}: 2582 \pm 34$ K', xy=(2.9, 3*10**(-14)), color='k', fontsize=15)
ax1.annotate('J1247-3816 (IR:M9 $\gamma$), $T_\mathrm{eff}: 2627 \pm 291$ K', xy=(2.3, 2*10**(-14)), color='#FFAA03', fontsize=15)
ax1.annotate('J0436-4114 (M8 $\\beta$), $T_\mathrm{eff}: 2557 \pm 257$ K', xy=(2.6, 1.3*10**(-14)), color='#FF6007', fontsize=15)
ax1.annotate('J0253+3206 (M9), $T_\mathrm{eff}: 2581 \pm 265$ K', xy=(2.8, 8*10**(-15)), color='#9B1301', fontsize=15)

plt.tight_layout()
plt.savefig('Figures/young_comp.png', dpi=150)

