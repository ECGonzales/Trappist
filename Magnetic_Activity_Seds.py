import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas dataframes
df_trap = pd.read_csv('Data/Smooth_output/Fieldoverall/Gaia2306-0502_(M7.5)_SED_spexify_spexified.txt', sep=" ",
                      comment='#', header=None, names=["w", "f", "err"])
df_trap_phot = pd.read_csv('Data/Gaia2306-0502 (M7.5) phot.txt', sep=" ",comment='#', header=None,
                           names=["w", "f", "err"])

# -------------- Comparison objects of the same Teff ----------------------------------
# LHS 132. INT-G
df_0102 = pd.read_csv('Data/Smooth_output/Rebuttal/Gaia0102-3737 (M8) SED_spexified.txt', sep=" ", comment='#',
                       header=None, names=["w", "f", "err"])
df_0102_phot = pd.read_csv('Data/field_comp/Gaia0102-3737 (M8) phot.txt', sep=" ", comment='#', header=None,
                            names=["w", "f", "err"])
# LP 888-18 (0331-3042)
df_0331 = pd.read_csv('Data/Smooth_output1/Filed/0331-3042(M7.5)SED_spexify_spexified.txt', sep=" ", comment='#', header=None,
                       names=["w", "f", "err"])
df_0331_phot = pd.read_csv('Data/0331-3042 (M7.5) phot.txt', sep=" ", comment='#', header=None,
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
ax1.loglog(df_0331['w'], df_0331['f'], c='#449B05')
ax1.scatter(df_0331_phot['w'], df_0331_phot['f'], c='k', s=70)
ax1.scatter(df_0331_phot['w'], df_0331_phot['f'], c='#449B05', s=50)



# ----- Set axes limits, reformat ticks -----------
plt.xlim([0.5, 13])
plt.ylim([10**(-17), 2*10**(-14)])
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
ax1.annotate('LHS 132 (M8)         $T_\mathrm{eff}: 2579 \pm 34$ K, $L_\mathrm{bol}: -3.264 \pm 0.002$',
             xy=(0.52, 1.1*10**(-17)), color='#E08B11', fontsize=15)
ax1.annotate('J0331-3042 (M7.5) $T_\mathrm{eff}: 2612 \pm 34$ K, $L_\mathrm{bol}: -3.227 \pm 0.003$',
             xy=(0.52, 1.8*10**(-17)), color='#449B05', fontsize=15)
ax1.annotate('TRAPPIST-1 (M7.5) $T_\mathrm{eff}: 2584 \pm 34$ K, $L_\mathrm{bol}: -3.253 \pm 0.002$',
             xy=(0.52, 2.75*10**(-17)), color='k', fontsize=15)

plt.savefig('Figures/comparison_MagneticActivity.pdf', dpi=150)
