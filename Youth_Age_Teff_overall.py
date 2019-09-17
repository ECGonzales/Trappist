import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas dataframes
df_trap = pd.read_csv('Data/Smooth_output_PS_new/youth_lowgteff/PS_Gaia_youth_2306-0502 (M7.5) SED_spexified.txt', sep=" ",
                      comment='#', header=None, names=["w", "f", "err"])
df_trap_phot = pd.read_csv('Data/PS_Gaia_youth_2306-0502 (M7.5) phot.txt', sep=" ", comment='#', header=None,
                           names=["w", "f", "err"])

# -------------- Comparison objects of the same Teff ----------------------------------
df_2000 = pd.read_csv('Data/Smooth_output_PS_new/youth_lowgteff/Gaia2000-7523 (M9gamma) SED_spexified.txt', sep=" ",
                      comment='#', header=None, names=["w", "f", "err"])
df_2000_phot = pd.read_csv('../Atmospheres_paper/Data/Gaia2000-7523 (M9gamma) phot.txt', sep=" ",comment='#', header=None,
                           names=["w", "f", "err"])

df_0608 = pd.read_csv('Data/Smooth_output_PS_new/youth_lowgteff/PS_new_0608-2753 (M8.5gamma) SED_spexified.txt', sep=" ",
                      comment='#', header=None, names=["w", "f", "err"])
df_0608_phot = pd.read_csv('Data/Young_Age_Comp/youth_lowgteff/PS_new_0608-2753 (M8.5gamma) phot.txt', sep=" ", comment='#', header=None,
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
ax1.loglog(df_2000['w'], df_2000['f'], c='#A85C05')
ax1.scatter(df_2000_phot['w'], df_2000_phot['f'], c='k', s=70)
ax1.scatter(df_2000_phot['w'], df_2000_phot['f'], c='#A85C05', s=50)
ax1.loglog(df_0608['w'], df_0608['f'], c='#D41304')
ax1.scatter(df_0608_phot['w'], df_0608_phot['f'], c='k', s=70)
ax1.scatter(df_0608_phot['w'], df_0608_phot['f'], c='#D41304', s=50)


# ----- Set axes limits, reformat ticks -----------
plt.xlim([0.5, 13])
plt.ylim([8*10**(-18), 3*10**(-14)])
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
ax1.annotate('TRAPPIST-1 (M7.5) $T_\mathrm{eff}: 2310 \pm 230$ K', xy=(2.5, 1.7*10**(-14)), color='k', fontsize=15)
ax1.annotate('J0608-2753 (L0 $\gamma$)  $T_\mathrm{eff}: 2510 \pm 250 $ K', xy=(2.5, 1.2*10**(-14)), color='#D41304',fontsize=15)
ax1.annotate('J2000-7523 (M9 $\gamma$)   $T_\mathrm{eff}: 2389 \pm 44$ K', xy=(2.5, 8.3*10**(-15)), color='#A85C05', fontsize=15)


plt.savefig('Figures/Young_Age_Lowg.pdf', dpi=150)
