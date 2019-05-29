import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas dataframes

df_trap = pd.read_csv('Data/Smooth_output_PS/oldoverall/PS_2306-0502 (M7.5) SED_spexified.txt', sep=" ",
                      comment='#', header=None, names=["w", "f", "err"])
df_trap_phot = pd.read_csv('Data/PS_2306-0502 (M7.5) phot.txt', sep=" ",comment='#', header=None,
                           names=["w", "f", "err"])

# -------------- Comparison objects of the same Teff (old) ----------------------------------
df_1013 = pd.read_csv('Data/Smooth_output_PS/oldoverall/PS_1013-1356 (M9.5sd) SED_spexified.txt', sep=" ",
                      comment='#', header=None, names=["w", "f", "err"])
df_1013_phot = pd.read_csv('Data/old_comp/PS_1013-1356 (M9.5sd) phot.txt', sep=" ", comment='#',
                           header=None, names=["w", "f", "err"])
# df_GJ660 = pd.read_csv('Data/Smooth_output_PS/oldoverall/PSspectra_gj6601b_est_spexified.txt', sep=" ", comment='#',
#                        header=0,names=["w", "f", "err"])
# df_GJ660_phot = pd.read_csv('Data/old_comp/PSphot_gj6601b_est.txt', sep=",", comment='#', header=0,
#                             names=["w", "f", "err"])

# -------------------------------------------------------------------------------------
# ---------------------- Remove Tails ------------------------------------------------
# -------------------------------------------------------------------------------------
# df_GJ660 = df_GJ660[(df_GJ660['w'] > 0.7) & (df_GJ660['w'] <= 3)]

# -------------------------------------------------------------------------------------
# ------------------- Plotting: Old Comparison of same Teff -------------------------------
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
ax1.scatter(df_trap_phot['w'], df_trap_phot['f'], c='k', s=70, zorder=23)

ax1.loglog(df_1013['w'], df_1013['f'], c='#0822FF')
ax1.scatter(df_1013_phot['w'], df_1013_phot['f'], c='k', s=70)  # The ones with size 70 are to give the circles a
ax1.scatter(df_1013_phot['w'], df_1013_phot['f'], c='#0822FF', s=50)        # black border
#
# ax1.loglog(df_GJ660['w'], df_GJ660['f'], c='#07D1E8')
# ax1.scatter(df_GJ660_phot['w'], df_GJ660_phot['f'], c='k', s=70)
# ax1.scatter(df_GJ660_phot['w'], df_GJ660_phot['f'], c='#07D1E8', s=50)

# ----- Set axes limits, reformat ticks -----------
plt.xlim([0.5, 13])
plt.ylim([10**(-17), 2*10**(-14)])
ax1.xaxis.set_major_formatter(ScalarFormatter())
ax1.xaxis.set_minor_formatter(ScalarFormatter())
ax1.xaxis.set_minor_locator(plt.FixedLocator([0.5, 0.7, 2, 3, 13]))
ax1.tick_params(axis='both', which='major', labelsize=20, length=8, width=1.1)
ax1.tick_params(axis='both', which='minor', labelsize=20, length=4, width=1.1)
plt.yticks(fontsize=20)

# ------ Axes Labels --------
plt.xlabel('Wavelength ($\mu m$)', fontsize=25)
plt.ylabel('Flux  ($erg\ s^{-1} cm^{-2} A^{-1}$)', fontsize=25)

# ------ Labeling Objects --------
ax1.annotate('TRAPPIST-1 (M7.5)      $T_\mathrm{eff}: 2626 \pm 34$ K,  $L_\mathrm{bol}: -3.210 \pm 0.012$', xy=(0.52, 2.3*10**(-17)), color='k', fontsize=15)

ax1.annotate('J1013-1356 (sdM9.5)  $T_\mathrm{eff}: 2628 \pm 22$ K,  $L_\mathrm{bol}: -3.303 \pm 0.026$', xy=(0.52, 1.6*10**(-17)), color='#0822FF', fontsize=15)

# ax1.annotate('GJ 660.1B (d/sdM7)    $T_\mathrm{eff}: 2642 \pm 102$ K, $L_\mathrm{bol}: -3.286 \pm 0.063$', xy=(0.52, 1.1*10**(-17)), color='#07D1E8', fontsize=15)



plt.tight_layout()
plt.savefig('Figures/old_comp.pdf', dpi=150)
