import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas dataframes

df_trap = pd.read_csv('Data/FIRE2306-0502 (M7.5) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_trap_phot = pd.read_csv('Data/FIRE2306-0502 (M7.5) phot.txt', sep=" ",comment='#', header=None, names=["w", "f", "err"])

# -------------- Comparison objects of the same Teff ----------------------------------
df_0102 = pd.read_csv('Data/field_comp/0102-3737 (M8) SED.txt', sep=" ", comment='#', header=None,
                       names=["w", "f", "err"])
df_0102_phot = pd.read_csv('Data/field_comp/0102-3737 (M8) phot.txt', sep=" ", comment='#', header=None,
                            names=["w", "f", "err"])
df_1655 = pd.read_csv('Data/field_comp/1655-0823 (M7) SED.txt', sep=" ", comment='#', header=None,
                       names=["w", "f", "err"])
df_1655_phot = pd.read_csv('Data/field_comp/1655-0823 (M7) phot.txt', sep=" ", comment='#', header=None,
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

# -------- Add data -----------
ax1.loglog(df_1655['w'], df_1655['f'], c='#04A57F')
ax1.scatter(df_1655_phot['w'], df_1655_phot['f'], c='k', s=70)  # The ones with size 70 are to give the circles a
ax1.scatter(df_1655_phot['w'], df_1655_phot['f'], c='#04A57F', s=50)        # black border
ax1.loglog(df_trap['w'], df_trap['f'], c='k', zorder=9)
ax1.scatter(df_trap_phot['w'], df_trap_phot['f'], c='k', s=70, zorder=10)
ax1.loglog(df_0102['w'], df_0102['f'], c='#09D5D6')
ax1.scatter(df_0102_phot['w'], df_0102_phot['f'], c='k', s=70)
ax1.scatter(df_0102_phot['w'], df_0102_phot['f'], c='#09D5D6', s=50)
#ax1.scatter(df_trap_phot['w'], df_trap_phot['f'], c='#7C7D70', s=50, zorder=10)


# ----- Set axes limits, reformat ticks -----------
plt.xlim([0.3, 24])
plt.ylim([1*10**(-18), 3*10**(-14)])
ax1.xaxis.set_major_formatter(ScalarFormatter())
ax1.xaxis.set_minor_formatter(ScalarFormatter())
ax1.xaxis.set_minor_locator(plt.FixedLocator([0.3, 0.6, 2, 3, 7.5, 22]))
ax1.tick_params(axis='both', which='major', labelsize=20, length=8, width=1.1)
ax1.tick_params(axis='both', which='minor', labelsize=20, length=4, width=1.1)
plt.yticks(fontsize=20)

# ------ Axes Labels --------
plt.xlabel('Wavelength ($\mu m$)', fontsize=25)
plt.ylabel('Flux  ($erg\ s^{-1} cm^{-2} A^{-1}$)', fontsize=25)

# ------ Labeling Spectra and Photometric points --------
ax1.annotate('Trappist-1 (M7.5) $T_\mathrm{eff}: 2589 \pm 49$ K', xy=(2.85, 10**(-14)), color='k', fontsize=15)
ax1.annotate('vb8 (M7) $T_\mathrm{eff}: 2641 \pm 36$ K', xy=(3.1, 5.2*10**(-15)), color='#04A57F', fontsize=15)
ax1.annotate('LHS 132 (M8) $T_\mathrm{eff}: 2636 \pm 63$ K', xy=(3.1, 3*10**(-15)), color='#09D5D6', fontsize=15)

#TODO: Try a different color scheme maybe shades of grey for field objects?

plt.tight_layout()
plt.savefig('Figures/comparison_FieldTeff.png')