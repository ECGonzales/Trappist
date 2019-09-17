import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas dataframes
df_trap = pd.read_csv('Data/Smooth_output_PS_new/youth_old/PS_Gaia_youth_2306-0502 (M7.5) SED_spexified.txt', sep=" ",
                      comment='#', header=None, names=["w", "f", "err"])
df_trap_phot = pd.read_csv('Data/PS_Gaia_youth_2306-0502 (M7.5) phot.txt', sep=" ", comment='#', header=None,
                           names=["w", "f", "err"])
# -------------- Comparison objects of the same Teff ----------------------------------
df_1256 = pd.read_csv('Data/Smooth_output_PS_new/youth_old/PS_new_1256-0224 (L3.5sd) SED_spexified.txt', sep=" ",
                      comment='#', header=None, names=["w", "f", "err"])
df_1256_phot = pd.read_csv('Data/Young_Age_Comp/youth_old/PS_new_1256-0224 (L3.5sd) phot.txt', sep=" ",comment='#', header=None,
                           names=["w", "f", "err"])

df_1444 = pd.read_csv('Data/Smooth_output_PS_new/youth_old/no_opt_PS1444-2019 (M9sd) SED_spexified.txt', sep=" ",
                      comment='#', header=None, names=["w", "f", "err"])
df_1444_phot = pd.read_csv('Data/Young_Age_Comp/youth_old/no_opt_PS1444-2019 (M9sd) phot.txt', sep=" ", comment='#', header=None,
                           names=["w", "f", "err"])

df_GJ660 = pd.read_csv('Data/Smooth_output_PS_new/youth_old/PS_corrected_gj6601b_spectra_spexified.txt', sep=" ", comment='#',
                       header=0,names=["w", "f", "err"])
df_GJ660_phot = pd.read_csv('Data/Young_Age_Comp/youth_old/PS_corrected_gj6601b_phot.txt', sep=",", comment='#', header=0,
                            names=["w", "f", "err"])

# -------------------------------------------------------------------------------------
# ---------------------- Remove Tails ------------------------------------------------
# -------------------------------------------------------------------------------------
df_GJ660 = df_GJ660[(df_GJ660['w'] > 0.7) & (df_GJ660['w'] <= 3)]

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
ax1.loglog(df_1256['w'], df_1256['f'], c='#5005BD')
ax1.scatter(df_1256_phot['w'], df_1256_phot['f'], c='k', s=70)
ax1.scatter(df_1256_phot['w'], df_1256_phot['f'], c='#5005BD', s=50)
ax1.loglog(df_1444['w'], df_1444['f'], c='mediumblue')
ax1.scatter(df_1444_phot['w'], df_1444_phot['f'], c='k', s=70)
ax1.scatter(df_1444_phot['w'], df_1444_phot['f'], c='mediumblue', s=50)
ax1.loglog(df_GJ660['w'], df_GJ660['f'], c='#07D1E8')
ax1.scatter(df_GJ660_phot['w'], df_GJ660_phot['f'], c='k', s=70)
ax1.scatter(df_GJ660_phot['w'], df_GJ660_phot['f'], c='#07D1E8', s=50)


# ----- Set axes limits, reformat ticks -----------
plt.xlim([0.5, 13])
plt.ylim([6*10**(-18), 2*10**(-14)])
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
ax1.annotate('TRAPPIST-1 (M7.5)   $T_\mathrm{eff}: 2310 \pm 230$ K', xy=(2.5, 1.2*10**(-14)), color='k', fontsize=15)
ax1.annotate('J1256-0224 (sdL3.5)  $T_\mathrm{eff}: 2301 \pm 71 $ K', xy=(2.5, 8.5*10**(-15)), color='#5005BD',fontsize=15)
ax1.annotate('GJ 660.1B (d/sdM7)    $T_\mathrm{eff}: 2409 \pm 91$ K', xy=(2.5, 6*10**(-15)), color='#07D1E8', fontsize=15)
ax1.annotate('J1444-2019 (sdM9)    $T_\mathrm{eff}: 2442 \pm 68$ K', xy=(2.5, 4*10**(-15)), color='mediumblue', fontsize=15)

plt.savefig('Figures/Young_Age_Subdwarfs.pdf', dpi=150)
