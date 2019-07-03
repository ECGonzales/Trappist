import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas dataframes

df_trap = pd.read_csv('Data/Smooth_output_PS_new/teegarden/PS_Gaia_2306-0502 (M7.5) SED_spexified.txt', sep=" ", comment='#',
                      header=None, names=["w", "f", "err"])
df_trap_phot = pd.read_csv('Data/PS_Gaia_2306-0502 (M7.5) phot.txt', sep=" ", comment='#', header=None,
                           names=["w", "f", "err"])

# -------------- Comparison objects of the same Teff (young) ----------------------------------
df_tee = pd.read_csv('Data/Smooth_output_PS_new/teegarden/0253+1652 (M6.5) SED_spexified.txt', sep=" ",
                      comment='#', header=None, names=["w", "f", "err"])
df_tee_phot = pd.read_csv('Data/teegarden/0253+1652 (M6.5) phot.txt', sep=" ", comment='#', header=None,
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

# Teegarden's Star
ax1.loglog(df_tee['w'], df_tee['f'], c='#15E89E', zorder=20)
ax1.scatter(df_tee_phot['w'], df_tee_phot['f'], c='k', s=70)  # The ones with size 70 are to give the circles a
teegarden = ax1.scatter(df_tee_phot['w'], df_tee_phot['f'], c='#15E89E', s=50)        # black border

# ----- Set axes limits, reformat ticks -----------
plt.xlim([0.5, 23])
plt.ylim([10**(-18), 3*10**(-14)])
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
ax1.annotate('TRAPPIST-1 (M7.5)  $T_\mathrm{eff}: 2629 \pm 34$ K', xy=(2.5, 1.7*10**(-14)), color='k', fontsize=15)
ax1.annotate("Teegarden's Star (M7.5 $\\beta$)  $T_\mathrm{eff}: 2718 \pm 34$ K", xy=(2.5, 1*10**(-14)), color='#15E89E',
             fontsize=15)

plt.savefig('Figures/Tee_comp.pdf', dpi=150)
