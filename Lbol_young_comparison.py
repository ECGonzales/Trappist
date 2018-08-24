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
df_1207 = pd.read_csv('Data/young_comp/1207-3900 (L0gamma) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_1207_phot = pd.read_csv('Data/young_comp/1207-3900 (L0gamma) phot.txt', sep=" ", comment='#', header=None,
                           names=["w", "f", "err"])
# df_0443 = pd.read_csv('Data/young_comp/0443+0002 (M9gamma) SED.txt', sep=" ", comment='#', header=None,
#                       names=["w", "f", "err"])
# df_0443_phot = pd.read_csv('Data/young_comp/0443+0002 (M9gamma) phot.txt', sep=" ", comment='#', header=None,
#                            names=["w", "f", "err"])
# Checking with the SXD to see differences
df_0443 = pd.read_csv('Data/young_comp/Jonathan0443+0002 (M9gamma) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_0443_phot = pd.read_csv('Data/young_comp/Jonathan0443+0002 (M9gamma) phot.txt', sep=" ", comment='#', header=None,
                           names=["w", "f", "err"])
df_0518 = pd.read_csv('Data/young_comp/0518-2756 (L1gamma) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_0518_phot = pd.read_csv('Data/young_comp/0518-2756 (L1gamma) phot.txt', sep=" ", comment='#', header=None,
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

# Comparisons (Bright-->faint)
ax1.loglog(df_0443['w'], df_0443['f'], c='#E71BF8')
ax1.scatter(df_0443_phot['w'], df_0443_phot['f'], c='k', s=70)  # The ones with size 70 are to give the circles a
ax1.scatter(df_0443_phot['w'], df_0443_phot['f'], c='#E71BF8', s=50)

ax1.loglog(df_0518['w'], df_0518['f'], c='#5518C2')
ax1.scatter(df_0518_phot['w'], df_0518_phot['f'], c='k', s=70)  # The ones with size 70 are to give the circles a
ax1.scatter(df_0518_phot['w'], df_0518_phot['f'], c='#5518C2', s=50)

ax1.loglog(df_1207['w'], df_1207['f'], c='#1036CF', zorder=20)
ax1.scatter(df_1207_phot['w'], df_1207_phot['f'], c='k', s=70)  # The ones with size 70 are to give the circles a
ax1.scatter(df_1207_phot['w'], df_1207_phot['f'], c='#1036CF', s=50)        # black border

# ----- Set axes limits, reformat ticks -----------
plt.xlim([0.5, 14])
plt.ylim([10**(-18), 5*10**(-14)])
ax1.xaxis.set_major_formatter(ScalarFormatter())
ax1.xaxis.set_minor_formatter(ScalarFormatter())
ax1.xaxis.set_minor_locator(plt.FixedLocator([0.5, 0.7, 2, 3, 4, 14]))
ax1.tick_params(axis='both', which='major', labelsize=20, length=8, width=1.1)
ax1.tick_params(axis='both', which='minor', labelsize=20, length=4, width=1.1)
plt.yticks(fontsize=20)

# ------ Axes Labels --------
plt.xlabel('Wavelength ($\mu m$)', fontsize=25)
plt.ylabel('Flux ($erg\ s^{-1} cm^{-2} A^{-1}$)', fontsize=25)
plt.tight_layout()

# ------ Labeling Objects --------
ax1.annotate('TRAPPIST-1 (M7.5)', xy=(5, 2*10**(-14)), color='k', fontsize=15)
ax1.annotate('Age: 500-10000 Myr', xy=(5, 1.3*10**(-14)), color='k', fontsize=15)
ax1.annotate('$L_\mathrm{bol}: -3.253 \pm 0.002$', xy=(5, 0.75*10**(-14)), color='k', fontsize=15)
# J0443
ax1.annotate('J0443+0002 (L0 VL-G)', xy=(5, 3*10**(-15)), color='#E71BF8', fontsize=15)
ax1.annotate('Age: 21-27 Myr ($\\beta$ Pic)', xy=(5, 1.7*10**(-15)), color='#E71BF8', fontsize=15)
ax1.annotate('$L_\mathrm{bol}: -3.194\pm 0.003$', xy=(5, 1*10**(-15)), color='#E71BF8', fontsize=15)
# J0518
ax1.annotate('J0518-2756 (L1 VL-G)', xy=(3, 3.5*10**(-17)), color='#5518C2', fontsize=15)
ax1.annotate('Age: 38-48 Myr (Columba)', xy=(3, 2*10**(-17)), color='#5518C2', fontsize=15)
ax1.annotate('$L_\mathrm{bol}: -3.328 \pm 0.041$', xy=(3, 1.2*10**(-17)), color='#5518C2', fontsize=15)
#1207
ax1.annotate('J1207-3900 (L1 VL-G)', xy=(0.8, 10**(-17)), color='#1036CF', fontsize=15)
ax1.annotate('Age: 7-13 Myr (TW Hydra)', xy=(0.8, 6*10**(-18)), color='#1036CF', fontsize=15)
ax1.annotate('$L_\mathrm{bol}: -3.336 \pm 0.053$', xy=(0.8, 3.5*10**(-18)), color='#1036CF', fontsize=15)

plt.savefig('Figures/young_comp_lbol.pdf', dpi=150)
