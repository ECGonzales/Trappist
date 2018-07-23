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
df_0953 = pd.read_csv('Data/young_comp/Gaia0953-1014 (L0gamma) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_0953_phot = pd.read_csv('Data/young_comp/Gaia0953-1014 (L0gamma) phot.txt', sep=" ", comment='#', header=None,
                           names=["w", "f", "err"])
df_0608 = pd.read_csv('Data/young_comp/Gaia0608-2753 (M8.5gamma) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_0608_phot = pd.read_csv('Data/young_comp/Gaia0608-2753 (M8.5gamma) phot.txt', sep=" ", comment='#', header=None,
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

# Comparisons (Hot-->cool)
ax1.loglog(df_1247['w'], df_1247['f'], c='#E80901', zorder=20)
ax1.scatter(df_1247_phot['w'], df_1247_phot['f'], c='k', s=70)  # The ones with size 70 are to give the circles a
y1247 = ax1.scatter(df_1247_phot['w'], df_1247_phot['f'], c='#E80901', s=50)        # black border

ax1.loglog(df_0608['w'], df_0608['f'], c='#FF6B03')
ax1.scatter(df_0608_phot['w'], df_0608_phot['f'], c='k', s=70)  # The ones with size 70 are to give the circles a
ax1.scatter(df_0608_phot['w'], df_0608_phot['f'], c='#FF6B03', s=50)

ax1.loglog(df_0953['w'], df_0953['f'], c='#9B0132')
ax1.scatter(df_0953_phot['w'], df_0953_phot['f'], c='k', s=70)  # The ones with size 70 are to give the circles a
ax1.scatter(df_0953_phot['w'], df_0953_phot['f'], c='#9B0132', s=50)

# ----- Set axes limits, reformat ticks -----------
plt.xlim([0.5, 23])
plt.ylim([10**(-18), 5*10**(-14)])
ax1.xaxis.set_major_formatter(ScalarFormatter())
ax1.xaxis.set_minor_formatter(ScalarFormatter())
ax1.xaxis.set_minor_locator(plt.FixedLocator([0.5, 0.7, 2, 3, 7.5, 23]))
ax1.tick_params(axis='both', which='major', labelsize=20, length=8, width=1.1)
ax1.tick_params(axis='both', which='minor', labelsize=20, length=4, width=1.1)
plt.yticks(fontsize=20)

# ------ Axes Labels --------
plt.xlabel('Wavelength ($\mu m$)', fontsize=25)
plt.ylabel('Flux ($erg\ s^{-1} cm^{-2} A^{-1}$)', fontsize=25)
plt.tight_layout()

# ------ Labeling Objects --------
ax1.annotate('J1247-3816 (M9 $\gamma$)     $T_\mathrm{eff}: 2627 \pm 291$ K', xy=(3, 3*10**(-14)), color='#E80901', fontsize=15)
ax1.annotate('J0608-2753 (M8.5 $\gamma$)  $T_\mathrm{eff}: 2493 \pm 253$ K', xy=(3, 1.8*10**(-14)), color='#FF6B03', fontsize=15)
ax1.annotate('J0953-1014 (M9 $\gamma$)     $T_\mathrm{eff}: 2430 \pm 255$ K', xy=(3, 1.05*10**(-14)), color='#9B0132', fontsize=15)
ax1.annotate('Trappist-1 (M7.5)       $T_\mathrm{eff}: 2584 \pm 34$ K', xy=(3, 6*10**(-15)), color='k', fontsize=15)

plt.savefig('Figures/young_comp_teff.pdf', dpi=150)

# Create the red optical zoom in
plt.xlim([0.65, 1])
plt.ylim([10**(-16), 5*10**(-14)])
ax1.xaxis.set_minor_locator(plt.FixedLocator([0.65, 0.7, 0.8, 0.9]))
fig.set_size_inches(11.32, 8.59)
plt.savefig('Figures/Young _teff_zoom.pdf', dpi=150)
