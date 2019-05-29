import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas dataframes
df_trap = pd.read_csv('Data/Smooth_output_PS/youth_field/PS_2306-0502 (M7.5) SED_spexified.txt', sep=" ",
                      comment='#', header=None, names=["w", "f", "err"])
df_trap_phot = pd.read_csv('Data/Gaia2306-0502 (M7.5) phot.txt', sep=" ",comment='#', header=None,
                           names=["w", "f", "err"])

# -------------- Comparison objects of the same Teff ----------------------------------
df_1048 = pd.read_csv('Data/Smooth_output_PS/youth_field/Gaia1048-3956 (M9) SED_spexified.txt', sep=" ",
                      comment='#', header=None, names=["w", "f", "err"])
df_1048_phot = pd.read_csv('Data/Young_Age_Comp/Gaia1048-3956 (M9) phot.txt', sep=" ",comment='#', header=None,
                           names=["w", "f", "err"])

df_1835 = pd.read_csv('Data/Smooth_output_PS/youth_field/PS_1835+3259 (M8.5) SED_spexified.txt', sep=" ",
                      comment='#', header=None, names=["w", "f", "err"])
df_1835_phot = pd.read_csv('Data/Young_Age_Comp/PS_1835+3259 (M8.5) phot.txt', sep=" ",comment='#', header=None,
                           names=["w", "f", "err"])

df_0853 = pd.read_csv('Data/Smooth_output_PS/youth_field/PS_0853-0329 (M9) SED_spexified.txt', sep=" ",
                      comment='#', header=None, names=["w", "f", "err"])
df_0853_phot = pd.read_csv('Data/Young_Age_Comp/PS_0853-0329 (M9) phot.txt', sep=" ",comment='#', header=None,
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
ax1.loglog(df_1048['w'], df_1048['f'], c='#09BD8C')
ax1.scatter(df_1048_phot['w'], df_1048_phot['f'], c='k', s=70)
ax1.scatter(df_1048_phot['w'], df_1048_phot['f'], c='#09BD8C', s=50)
ax1.loglog(df_0853['w'], df_0853['f'], c='#1CA844')
ax1.scatter(df_0853_phot['w'], df_0853_phot['f'], c='k', s=70)
ax1.scatter(df_0853_phot['w'], df_0853_phot['f'], c='#1CA844', s=50)
ax1.loglog(df_1835['w'], df_1835['f'], c='#7A7614')
ax1.scatter(df_1835_phot['w'], df_1835_phot['f'], c='k', s=70)
ax1.scatter(df_1835_phot['w'], df_1835_phot['f'], c='#7A7614', s=50)

# ----- Set axes limits, reformat ticks -----------
plt.xlim([0.5, 13])
plt.ylim([8*10**(-18), 2*10**(-14)])
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
ax1.annotate('TRAPPIST-1 (M7.5) $T_\mathrm{eff}: 2319 \pm 232$ K', xy=(2.5, 1.2*10**(-14)), color='k', fontsize=15)
ax1.annotate('J1048-3956 (M9)    $T_\mathrm{eff}: 2333 \pm 54$ K', xy=(2.5, 8.5*10**(-15)), color='#09BD8C', fontsize=15)
ax1.annotate('J0853-0329 (M9)    $T_\mathrm{eff}: 2332 \pm 55$ K', xy=(2.5, 6*10**(-15)), color='#1CA844', fontsize=15)
ax1.annotate('J1835+3295 (M9)  $T_\mathrm{eff}: 2311 \pm 54$ K', xy=(2.5, 4*10**(-15)), color='#7A7614', fontsize=15)


plt.savefig('Figures/Young_Age_Field.pdf', dpi=150)



