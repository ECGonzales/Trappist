import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas dataframes
df_trap = pd.read_csv('Data/Gaia2306-0502 (M7.5) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_trap_phot = pd.read_csv('Data/Gaia2306-0502 (M7.5) phot.txt', sep=" ",comment='#', header=None, names=["w", "f", "err"])

# -------------- Comparison objects of the same Teff ----------------------------------
df_0102 = pd.read_csv('Data/field_comp/Gaia0102-3737 (M8) SED.txt', sep=" ", comment='#', header=None,  # LHS 132. INT-G
                       names=["w", "f", "err"])
df_0102_phot = pd.read_csv('Data/field_comp/Gaia0102-3737 (M8) phot.txt', sep=" ", comment='#', header=None,
                            names=["w", "f", "err"])

df_2341 = pd.read_csv('Data/RebuttleSources/2341-1133 (-) SED.txt', sep=" ", comment='#', header=None,  #M8 INT-G
                       names=["w", "f", "err"])
df_2341_phot = pd.read_csv('Data/RebuttleSources/2341-1133 (-) phot.txt', sep=" ", comment='#', header=None,
                            names=["w", "f", "err"])

df_2352 = pd.read_csv('Data/RebuttleSources/2352-1100 (-) SED.txt', sep=" ", comment='#', header=None,  # Young AB Dor
                       names=["w", "f", "err"])
df_2352_phot = pd.read_csv('Data/RebuttleSources/2352-1100 (-) phot.txt', sep=" ", comment='#', header=None,
                            names=["w", "f", "err"])

# -------------------------------------------------------------------------------------
# ------------------- Plotting: Field Comparison of same Teff -------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)  # to make sure proper size run entire code at once and change 8 to 6.45 to
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)  # match other plots on github (the size will change if done in pieces
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)

# -------- Add data -----------  # Greys look horrible for the overall
ax1.loglog(df_trap['w'], df_trap['f'], c='k',)
ax1.scatter(df_trap_phot['w'], df_trap_phot['f'], c='k', s=70)
ax1.loglog(df_0102['w'], df_0102['f'], c='#E08B11')
ax1.scatter(df_0102_phot['w'], df_0102_phot['f'], c='k', s=70)
ax1.scatter(df_0102_phot['w'], df_0102_phot['f'], c='#E08B11', s=50)
ax1.loglog(df_2341['w'], df_2341['f'], c='#E05714')
ax1.scatter(df_2341_phot['w'], df_2341_phot['f'], c='k', s=70)
ax1.scatter(df_2341_phot['w'], df_2341_phot['f'], c='#E05714', s=50)
ax1.loglog(df_2352['w'], df_2352['f'], c='#CC2015')
ax1.scatter(df_2352_phot['w'], df_2352_phot['f'], c='k', s=70)
ax1.scatter(df_2352_phot['w'], df_2352_phot['f'], c='#CC2015', s=50)

# ----- Set axes limits, reformat ticks -----------
plt.xlim([0.3, 13])
plt.ylim([10**(-17), 5*10**(-14)])
ax1.xaxis.set_major_formatter(ScalarFormatter())
ax1.xaxis.set_minor_formatter(ScalarFormatter())
ax1.xaxis.set_minor_locator(plt.FixedLocator([0.3, 0.6, 2, 3, 4, 13]))
ax1.tick_params(axis='both', which='major', labelsize=20, length=8, width=1.1)
ax1.tick_params(axis='both', which='minor', labelsize=20, length=4, width=1.1)
plt.yticks(fontsize=20)

# ------ Axes Labels --------
plt.xlabel('Wavelength ($\mu m$)', fontsize=25)
plt.ylabel('Flux  ($erg\ s^{-1} cm^{-2} A^{-1}$)', fontsize=25)

plt.tight_layout()

# ------ Labeling Spectra and Photometric points -------- #TODO:Smooth and move labels
ax1.annotate('LHS 132 (M8) $T_\mathrm{eff}: 2579 \pm 34$ K, $L_\mathrm{bol}: -3.264 \pm 0.002$',
             xy=(0.7, 1.1*10**(-17)), color='#E08B11', fontsize=15)
ax1.annotate('J2341-1133 (M8) $T_\mathrm{eff}: 2878 \pm 37$ K, $L_\mathrm{bol}: -2.946 \pm 0.011$',
             xy=(0.7, 1.8*10**(-17)), color='#E05714', fontsize=15)
ax1.annotate('J2352-1100 (M8 $\\beta$) $T_\mathrm{eff}: 2910 \pm 56$ K, $L_\mathrm{bol}: -2.793 \pm 0.018$',
             xy=(0.7, 2.9*10**(-17)), color='#CC2015', fontsize=15)

ax1.annotate('TRAPPIST-1 (M7.5) $T_\mathrm{eff}: 2584 \pm 34$ K ', xy=(1.7, 3.5*10**(-14)), color='k', fontsize=15)
ax1.annotate('$L_\mathrm{bol}: -3.253 \pm 0.002$', xy=(4.5, 2.5*10**(-14)), color='k', fontsize=15)


plt.savefig('Figures/comparison_Rebuttle.pdf', dpi=150)
