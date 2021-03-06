import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas dataframes

df_trap = pd.read_csv('Data/Smooth_output_PS_new/BetaLboloverall/PS_Gaia_2306-0502 (M7.5) SED_spexified.txt', sep=" ",
                      comment='#', header=None, names=["w", "f", "err"])
df_trap_phot = pd.read_csv('Data/PS_Gaia_2306-0502 (M7.5) phot.txt', sep=" ", comment='#', header=None,
                           names=["w", "f", "err"])

# -------------- Comparison objects of the same Teff ----------------------------------
df_2235 = pd.read_csv('Data/Smooth_output_PS_new/BetaLboloverall/Gaia2235-5906 (M8.5beta) SED_spexified.txt', sep=" ", comment='#',
                      header=None, names=["w", "f", "err"])
df_2235_phot = pd.read_csv('Data/beta_comp/BetaLboloverall/Gaia2235-5906 (M8.5beta) phot.txt', sep=" ", comment='#', header=None,
                           names=["w", "f", "err"])
# df_2154 = pd.read_csv('Data/paper1_trappist/Lbol_comp/Gaia2154-7459 (M9.5beta) SED_spexified.txt', sep=" ",
#                        comment='#', header=None, names=["w", "f", "err"])
# df_2154_phot = pd.read_csv('Data/beta_comp/Gaia2154-7459 (M9.5beta) phot.txt', sep=" ", comment='#', header=None,
#                             names=["w", "f", "err"])
df_0714 = pd.read_csv('Data/Smooth_output_PS_new/BetaLboloverall/PS_new_0714+3702 (M8) SED_spexified.txt', sep=" ", comment='#',
                      header=None, names=["w", "f", "err"])
df_0714_phot = pd.read_csv('Data/beta_comp/BetaLboloverall/PS_new_0714+3702 (M8) phot.txt', sep=" ", comment='#', header=None,
                            names=["w", "f", "err"])


# -------------------------------------------------------------------------------------
# ------------------- Plotting: Field Comparison of similar Lbol ----------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)  # to make sure proper size run entire code at once and change 8 to 6.45 to
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)  # match other plots on github (the size will change if done in pieces
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)

# -------- Add data -----------
ax1.loglog(df_trap['w'], df_trap['f'], c='k', zorder=3)
ax1.scatter(df_trap_phot['w'], df_trap_phot['f'], c='k', s=70, zorder=6)
ax1.loglog(df_2235['w'], df_2235['f'], c='#8E01E8', zorder=1)
ax1.scatter(df_2235_phot['w'], df_2235_phot['f'], c='k', s=70, zorder=4)
ax1.scatter(df_2235_phot['w'], df_2235_phot['f'], c='#8E01E8', s=50, zorder=5)
# ax1.loglog(df_2154['w'], df_2154['f'], c='#E806B7', zorder=2)
# ax1.scatter(df_2154_phot['w'], df_2154_phot['f'], c='k', s=70, zorder=4)
# ax1.scatter(df_2154_phot['w'], df_2154_phot['f'], c='#E806B7', s=50,zorder=5)
ax1.loglog(df_0714['w'], df_0714['f'], c='#E806B7', zorder=7) # old color #0E0084
ax1.scatter(df_0714_phot['w'], df_0714_phot['f'], c='k', s=70, zorder=4)
ax1.scatter(df_0714_phot['w'], df_0714_phot['f'], c='#E806B7', s=50, zorder=5)

# ----- Set axes limits, reformat ticks -----------
plt.xlim([0.5, 12])
plt.ylim([1*10**(-17), 3*10**(-14)])
ax1.xaxis.set_major_formatter(ScalarFormatter())
ax1.xaxis.set_minor_formatter(ScalarFormatter())
ax1.xaxis.set_minor_locator(plt.FixedLocator([0.5, 0.7, 2, 3, 4]))
ax1.tick_params(axis='both', which='major', labelsize=20, length=8, width=1.1)
ax1.tick_params(axis='both', which='minor', labelsize=20, length=4, width=1.1)
plt.yticks(fontsize=20)

# ------ Axes Labels --------
plt.xlabel('Wavelength ($\mu m$)', fontsize=25)
plt.ylabel('Flux  ($erg\ s^{-1} cm^{-2} A^{-1}$)', fontsize=25)

# ------ Labeling Spectra and Photometric points --------
# 0714 Age: <500 Myr'
ax1.annotate('J0714+3702 (M8)       $L_\mathrm{bol}: -3.286 \pm 0.012$', xy=(1.95, 9*10**(-15)), color='#E806B7', fontsize=15)
# J2235 41-49 Myr (Tuc-Hor)
ax1.annotate('J2235-5906 (M8.5 $\\beta$)  $L_\mathrm{bol}: -3.214 \pm 0.027$', xy=(1.95, 1.4*10**(-14)), color='#8E01E8',fontsize=15)
# Trappist-1
ax1.annotate('TRAPPIST-1 (M7.5)     $L_\mathrm{bol}: -3.216 \pm 0.016$', xy=(1.95, 2*10**(-14)), color='k', fontsize=15)
# J2154
# ax1.annotate('J2154-7459 (M9.5 $\\beta$)', xy=(4, 2.3*10**(-15)), color='#E806B7', fontsize=15)
# ax1.annotate('Age: 41-49 Myr (Tuc-Hor)', xy=(4, 1.5*10**(-15)), color='#E806B7', fontsize=15)
# ax1.annotate('$L_\mathrm{bol}: -3.196 \pm 0.012$', xy=(4, 10**(-15)), color='#E806B7', fontsize=15)

plt.tight_layout()
plt.savefig('Figures/Lbol_beta.pdf')
