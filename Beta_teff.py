import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas dataframes

df_trap = pd.read_csv('Data/Smooth_output_PS/betateffoverall/PS_2306-0502 (M7.5) SED_spexified.txt', sep=" ",
                      comment='#', header=None, names=["w", "f", "err"])
df_trap_phot = pd.read_csv('Data/PS_2306-0502 (M7.5) phot.txt', sep=" ", comment='#', header=None,
                           names=["w", "f", "err"])
# -------------- Comparison objects of the same Teff (betas) ----------------------------------
# df_0253 = pd.read_csv('Data/beta_comp/Gaia0253+3206 (M7beta) SED.txt', sep=" ", comment='#', header=None,
#                       names=["w", "f", "err"])
# df_0253_phot = pd.read_csv('Data/beta_comp/Gaia0253+3206 (M7beta) phot.txt', sep=" ", comment='#', header=None,
#                            names=["w", "f", "err"])
df_0953 = pd.read_csv('Data/Smooth_output_PS/betateffoverall/PS_0953-1014 (L0gamma) SED_spexified.txt', sep=" ", comment='#',
                      header=None, names=["w", "f", "err"])
df_0953_phot = pd.read_csv('Data/beta_comp/PS_0953-1014 (L0gamma) phot.txt', sep=" ", comment='#', header=None,
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

# Comparisons (Hot-->cool)
# ax1.loglog(df_0253['w'], df_0253['f'], c='#D01810')
# ax1.scatter(df_0253_phot['w'], df_0253_phot['f'], c='k', s=70)
# y0253 = ax1.scatter(df_0253_phot['w'], df_0253_phot['f'], c='#D01810', s=50)   c='#F58404

ax1.loglog(df_0953['w'], df_0953['f'], c='#D01810')
ax1.scatter(df_0953_phot['w'], df_0953_phot['f'], c='k', s=70)
y0953 = ax1.scatter(df_0953_phot['w'], df_0953_phot['f'], c='#D01810', s=50)

# ----- Set axes limits, reformat ticks -----------
plt.xlim([0.5, 14])
plt.ylim([10**(-17), 3*10**(-14)])
ax1.xaxis.set_major_formatter(ScalarFormatter())
ax1.xaxis.set_minor_formatter(ScalarFormatter())
ax1.xaxis.set_minor_locator(plt.FixedLocator([0.5, 0.7, 2, 3, 7.5, 14]))
ax1.tick_params(axis='both', which='major', labelsize=20, length=8, width=1.1)
ax1.tick_params(axis='both', which='minor', labelsize=20, length=4, width=1.1)
plt.yticks(fontsize=20)

# ------ Axes Labels and layout--------
plt.xlabel('Wavelength ($\mu m$)', fontsize=25)
plt.ylabel('Flux ($erg\ s^{-1} cm^{-2} A^{-1}$)', fontsize=25)
plt.tight_layout()

# ------ Labeling Objects --------
ax1.annotate('TRAPPIST-1 (M7.5) $T_\mathrm{eff}: 2626 \pm 34$ K', xy=(2.5, 2*10**(-14)), color='k', fontsize=15)
# ax1.annotate('J0253+3206 (M7$\\beta$), $T_\mathrm{eff}: 2581 \pm 265$ K', xy=(2, 2*10**(-14)), color='#D01810',
# fontsize=15)
ax1.annotate('J0953-1014 (M9 $\\beta$) $T_\mathrm{eff}: 2450 \pm 260$ K', xy=(2.5, 1.4*10**(-14)), color='#D01810',
             fontsize=15)

plt.savefig('Figures/beta_teff.pdf', dpi=150)
