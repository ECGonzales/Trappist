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
df_0102 = pd.read_csv('Data/field_comp/Gaia0102-3737 (M8) SED.txt', sep=" ", comment='#', header=None,  # LHS 132
                       names=["w", "f", "err"])
df_0102_phot = pd.read_csv('Data/field_comp/Gaia0102-3737 (M8) phot.txt', sep=" ", comment='#', header=None,
                            names=["w", "f", "err"])
df_vb8 = pd.read_csv('Data/field_comp/Gaia1655-0823 (M7) SED.txt', sep=" ", comment='#', header=None,  # vb8
                       names=["w", "f", "err"])
df_vb8_phot = pd.read_csv('Data/field_comp/Gaia1655-0823 (M7) phot.txt', sep=" ", comment='#', header=None,
                            names=["w", "f", "err"])
df_vb10 = pd.read_csv('Data/field_comp/Gaia1916+0508 (M8) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_vb10_phot = pd.read_csv('Data/field_comp/Gaia1916+0508 (M8) phot.txt', sep=" ", comment='#', header=None,
                           names=["w", "f", "err"])
df_0320 = pd.read_csv('Data/field_comp/Gaia0320+1854 (M8) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_0320_phot = pd.read_csv('Data/field_comp/Gaia0320+1854 (M8) phot.txt', sep=" ", comment='#', header=None,
                           names=["w", "f", "err"])
df_LHS3003 = pd.read_csv('Data/field_comp/1456-2809 (M7) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_LHS3003_phot = pd.read_csv('Data/field_comp/1456-2809 (M7) phot.txt', sep=" ", comment='#', header=None,
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
ax1.loglog(df_vb8['w'], df_vb8['f'], c='#04A57F')  # Greys: #353B40 Greens:#04A57F
ax1.scatter(df_vb8_phot['w'], df_vb8_phot['f'], c='k', s=70)
ax1.scatter(df_vb8_phot['w'], df_vb8_phot['f'], c='#04A57F', s=50)  # Greys: #353B40 Greens:#04A57F
ax1.loglog(df_trap['w'], df_trap['f'], c='k', zorder=9)
ax1.scatter(df_trap_phot['w'], df_trap_phot['f'], c='k', s=70, zorder=10)
ax1.loglog(df_0102['w'], df_0102['f'], c='green')  # Greys: #6A777F Greens: green
ax1.scatter(df_0102_phot['w'], df_0102_phot['f'], c='k', s=70)
ax1.scatter(df_0102_phot['w'], df_0102_phot['f'], c='green', s=50)  # Greys: #6A777F Greens: green
ax1.loglog(df_vb10['w'], df_vb10['f'], c='#275202')  # Greys: #A0B2BF Greens: #275202
ax1.scatter(df_vb10_phot['w'], df_vb10_phot['f'], c='k', s=70)
ax1.scatter(df_vb10_phot['w'], df_vb10_phot['f'], c='#275202', s=50)  # Greys: #A0B2BF Greens: #275202
ax1.loglog(df_0320['w'], df_0320['f'], c='#1EE801')  # Greys: #C0D5E5 Greens: #1EE801
ax1.scatter(df_0320_phot['w'], df_0320_phot['f'], c='k', s=70)
ax1.scatter(df_0320_phot['w'], df_0320_phot['f'], c='#1EE801', s=50)  # Greys: #C0D5E5 Greens: #1EE801
ax1.loglog(df_LHS3003['w'], df_LHS3003['f'], c='#09D5D6')  # Greys: #D5EDFF Greens: #09D5D6
ax1.scatter(df_LHS3003_phot['w'], df_LHS3003_phot['f'], c='k', s=70)
ax1.scatter(df_LHS3003_phot['w'], df_LHS3003_phot['f'], c='#09D5D6', s=50)  # Greys: #D5EDFF Greens: #09D5D6

#ax1.scatter(df_trap_phot['w'], df_trap_phot['f'], c='#7C7D70', s=50, zorder=10)


# ----- Set axes limits, reformat ticks -----------
plt.xlim([0.3, 31])
plt.ylim([4*10**(-20), 3*10**(-14)])
ax1.xaxis.set_major_formatter(ScalarFormatter())
ax1.xaxis.set_minor_formatter(ScalarFormatter())
ax1.xaxis.set_minor_locator(plt.FixedLocator([0.3, 0.6, 2, 3, 7.5, 31]))
ax1.tick_params(axis='both', which='major', labelsize=20, length=8, width=1.1)
ax1.tick_params(axis='both', which='minor', labelsize=20, length=4, width=1.1)
plt.yticks(fontsize=20)

# ------ Axes Labels --------
plt.xlabel('Wavelength ($\mu m$)', fontsize=25)
plt.ylabel('Flux  ($erg\ s^{-1} cm^{-2} A^{-1}$)', fontsize=25)

plt.tight_layout()

# ------ Labeling Spectra and Photometric points --------
ax1.annotate('Trappist-1 (M7.5) $T_\mathrm{eff}: 2581 \pm 34$ K', xy=(2.7, 10**(-14)), color='k', fontsize=15)
ax1.annotate('$L_\mathrm{bol}: -3.255 \pm 0.002$', xy=(8, 5.2*10**(-15)), color='k', fontsize=15)
ax1.annotate('vb8 (M7)               $T_\mathrm{eff}: 2642 \pm 34$ K, $L_\mathrm{bol}: -3.192 \pm 0.002$',
             xy=(0.32, 2*10**(-18)), color='#04A57F', fontsize=15)
ax1.annotate('LHS 3003 (M7)      $T_\mathrm{eff}: 2618 \pm 34$ K, $L_\mathrm{bol}: -3.223 \pm 0.002$',
             xy=(0.32, 10**(-18)), color='#09D5D6', fontsize=15)
ax1.annotate('J0320+1854 (M8) $T_\mathrm{eff}: 2615 \pm 34$ K, $L_\mathrm{bol}: -3.225 \pm 0.002$',
             xy=(0.32, 5*10**(-19)), color='#1EE801', fontsize=15)
ax1.annotate('LHS 132 (M8)        $T_\mathrm{eff}: 2579 \pm 34$ K, $L_\mathrm{bol}: -3.264 \pm 0.002$',
             xy=(0.32, 2.5*10**(-19)), color='green', fontsize=15)
ax1.annotate('vb10 (M8)             $T_\mathrm{eff}: 2542 \pm 45$ K, $L_\mathrm{bol}: -3.297 \pm 0.002$',
             xy=(0.32, 10**(-19)), color='#275202', fontsize=15)

plt.savefig('Figures/comparison_FieldTeff.pdf')

# To Make the zoom in red optical
plt.xlim([0.65, 1])
plt.ylim([10**(-16), 3*10**(-14)])
ax1.xaxis.set_minor_locator(plt.FixedLocator([0.65, 0.7, 0.8, 0.9]))
fig.set_size_inches(11.32, 8.59)
plt.savefig('Figures/comparison_FieldTeff_zoom.pdf', dpi=150)


# To Make the temp dependent region zoom in
plt.xlim([1.27, 1.8])
plt.ylim([4.75*10**(-15), 2*10**(-14)])
ax1.xaxis.set_minor_locator(plt.FixedLocator([1.27,1.42,1.70,1.80]))
fig.set_size_inches(11.32, 8.59)
plt.tight_layout()
plt.savefig('Figures/comparison_FieldTeffdepregion_zoom.pdf', dpi=150)
