import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas dataframes

df_trap = pd.read_csv('Data/2306-0502 (M7.5) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_trap_phot = pd.read_csv('Data/2306-0502 (M7.5) phot.txt', sep=" ",comment='#', header=None, names=["w", "f", "err"])

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
ax1.xaxis.set_minor_locator(plt.FixedLocator([0.3, 0.5, 0.6, 2, 3, 7.5, 22]))
ax1.tick_params(axis='x', which='major', labelsize=20)
ax1.tick_params(axis='x', which='minor', labelsize=20)
plt.yticks(fontsize=20)

# ------ Axes Labels --------
plt.xlabel('Wavelength ($\mu m$)', fontsize=25)
plt.ylabel('Flux  ($erg\ s^{-1} cm^{-2} A^{-1}$)', fontsize=25)

# ------ Labeling Spectra and Photometric points --------
# Old
# ax1.text(0.23, 0.4, '1256-0224', transform=ax1.transAxes, color='blue', fontsize=15)
# ax1.text(0.23, 0.35, 'Age: >> 1 Gyr', transform=ax1.transAxes, color='blue', fontsize=15)
# ax1.text(0.23, 0.3, 'Old', transform=ax1.transAxes, color='blue', fontsize=15)
# ax1.text(0.23, 0.25, 'T$_\mathrm{eff}:2344\pm 314$ K', transform=ax1.transAxes, color='blue', fontsize=15)
#
# # Field
# ax1.text(0.62, 0.2, '0024-0158', transform=ax1.transAxes, color='#7C7D70', fontsize=15)
# ax1.text(0.62, 0.15, 'Age: 500 - 10000 Myr ', transform=ax1.transAxes, color='#7C7D70', fontsize=15)
# ax1.text(0.62, 0.1, 'Field', transform=ax1.transAxes, color='#7C7D70', fontsize=15)
# ax1.text(0.62, 0.05, 'T$_\mathrm{eff}:2385\pm 77$ K', transform=ax1.transAxes, color='#7C7D70', fontsize=15)
#
# # Young
# ax1.text(0.6, 0.95, '2000-7523', transform=ax1.transAxes, color='#D01810', fontsize=15)
# ax1.text(0.6, 0.9, r'Age: 12 - 22 Myr ($\beta$ Pictoris)', transform=ax1.transAxes, color='#D01810', fontsize=15)
# # r is to deal with \a or \b as being special python characters
# ax1.text(0.6, 0.85, 'Young', transform=ax1.transAxes, color='#D01810', fontsize=15)
# ax1.text(0.6, 0.8, 'T$_\mathrm{eff}:2363\pm 74$ K', transform=ax1.transAxes, color='#D01810', fontsize=15)

plt.savefig('Figures/comparison_FieldTeff.png')