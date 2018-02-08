import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas dataframes

df_trap = pd.read_csv('Data/FIRE2306-0502 (M7.5) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_trap_phot = pd.read_csv('Data/FIRE2306-0502 (M7.5) phot.txt', sep=" ", comment='#', header=None,
                           names=["w", "f", "err"])

# -------------- Comparison objects of the same Teff (young) ----------------------------------
df_1207 = pd.read_csv('Data/young_comp/1207-3932A (M8) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_1207_phot = pd.read_csv('Data/young_comp/1207-3932A (M8) phot.txt', sep=" ", comment='#', header=None,
                           names=["w", "f", "err"])
df_1102 = pd.read_csv('Data/young_comp/1102-3430 (M8.5gamma) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_1102_phot = pd.read_csv('Data/young_comp/1102-3430 (M8.5gamma) phot.txt', sep=" ", comment='#', header=None,
                           names=["w", "f", "err"])

# ---- Large Unc -----
df_0436 = pd.read_csv('Data/young_comp/0436-4114 (M8betagamma) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_0436_phot = pd.read_csv('Data/young_comp/0436-4114 (M8betagamma) phot.txt', sep=" ", comment='#', header=None,
                           names=["w", "f", "err"])
df_0032 = pd.read_csv('Data/young_comp/0032-4405 (L0gamma) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_0032_phot = pd.read_csv('Data/young_comp/0032-4405 (L0gamma) phot.txt', sep=" ", comment='#', header=None,
                           names=["w", "f", "err"])
df_2154 = pd.read_csv('Data/young_comp/2154-7459 (M9.5beta) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_2154_phot = pd.read_csv('Data/young_comp/2154-7459 (M9.5beta) phot.txt', sep=" ", comment='#', header=None,
                           names=["w", "f", "err"])

# ----- Fire data -----
df_1139 = pd.read_csv('Data/young_comp/FIRE1139-3159 (M9gamma) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_1139_phot = pd.read_csv('Data/young_comp/FIRE1139-3159 (M9gamma) phot.txt', sep=" ", comment='#', header=None,
                           names=["w", "f", "err"])
df_1245 = pd.read_csv('Data/young_comp/FIRE1245-4429 (M9.5) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_1245_phot = pd.read_csv('Data/young_comp/FIRE1245-4429 (M9.5) phot.txt', sep=" ", comment='#', header=None,
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

# Low unc
ax1.loglog(df_1207['w'], df_1207['f'], c='#FF6C11')
ax1.scatter(df_1207_phot['w'], df_1207_phot['f'], c='k', s=70)  # The ones with size 70 are to give the circles a
TWA27 = ax1.scatter(df_1207_phot['w'], df_1207_phot['f'], c='#FF6C11', s=50)        # black border

ax1.loglog(df_1102['w'], df_1102['f'], c='#E8470F')
ax1.scatter(df_1102_phot['w'], df_1102_phot['f'], c='k', s=70)
TWA28 = ax1.scatter(df_1102_phot['w'], df_1102_phot['f'], c='#E8470F', s=50)

ax1.loglog(df_1139['w'], df_1139['f'], c='#FF3215')
ax1.scatter(df_1139_phot['w'], df_1139_phot['f'], c='k', s=70)
TWA26 = ax1.scatter(df_1139_phot['w'], df_1139_phot['f'], c='#FF3215', s=50)  # medium unc

ax1.loglog(df_1245['w'], df_1245['f'], c='#E81011')
ax1.scatter(df_1245_phot['w'], df_1245_phot['f'], c='k', s=70)
TWA29 = ax1.scatter(df_1245_phot['w'], df_1245_phot['f'], c='#E81011', s=50)  # medium unc

# ----- Set axes limits, reformat ticks -----------
plt.xlim([0.5, 32])
plt.ylim([5*10**(-20), 10**(-13)])
ax1.xaxis.set_major_formatter(ScalarFormatter())
ax1.xaxis.set_minor_formatter(ScalarFormatter())
ax1.xaxis.set_minor_locator(plt.FixedLocator([0.5, 0.7, 2, 3, 7.5, 22, 32]))
ax1.tick_params(axis='both', which='major', labelsize=20, length=8, width=1.1)
ax1.tick_params(axis='both', which='minor', labelsize=20, length=4, width=1.1)
plt.yticks(fontsize=20)

# ------ Axes Labels --------
plt.xlabel('Wavelength ($\mu m$)', fontsize=25)
plt.ylabel('Flux  ($erg\ s^{-1} cm^{-2} A^{-1}$)', fontsize=25)

plt.legend([trap, TWA27, TWA28, TWA26, TWA29], ['Trappist-1', "TWA27A", 'TWA28', 'TWA26', 'TWA29'])
plt.tight_layout()
plt.savefig('Figures/young_comp_small_unc.png', dpi=150)

# ---------- Create plot with the large uncertainty objects -------------
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
# High unc
ax1.loglog(df_0436['w'], df_0436['f'], c='#9B0447')
ax1.scatter(df_0436_phot['w'], df_0436_phot['f'], c='k', s=70)
TM0436 = ax1.scatter(df_0436_phot['w'], df_0436_phot['f'], c='#9B0447', s=50)

ax1.loglog(df_0032['w'], df_0032['f'], c='#E80EB2')
ax1.scatter(df_0032_phot['w'], df_0032_phot['f'], c='k', s=70)
TM0032 = ax1.scatter(df_0032_phot['w'], df_0032_phot['f'], c='#E80EB2', s=50)

ax1.loglog(df_2154['w'], df_2154['f'], c='#FF105A')
ax1.scatter(df_2154_phot['w'], df_2154_phot['f'], c='k', s=70)
TM2145 = ax1.scatter(df_2154_phot['w'], df_2154_phot['f'], c='#FF105A', s=50)

# ----- Set axes limits, reformat ticks -----------
plt.xlim([0.5, 13])
plt.ylim([10**(-19), 10**(-13)])
ax1.xaxis.set_major_formatter(ScalarFormatter())
ax1.xaxis.set_minor_formatter(ScalarFormatter())
ax1.xaxis.set_minor_locator(plt.FixedLocator([0.5, 0.7, 2, 3, 13]))
ax1.tick_params(axis='both', which='major', labelsize=20, length=8, width=1.1)
ax1.tick_params(axis='both', which='minor', labelsize=20, length=4, width=1.1)
plt.yticks(fontsize=20)

# ------ Axes Labels --------
plt.xlabel('Wavelength ($\mu m$)', fontsize=25)
plt.ylabel('Flux  ($erg\ s^{-1} cm^{-2} A^{-1}$)', fontsize=25)

plt.legend([trap, TM0436, TM0032, TM2145], ['Trappist-1', 'J0436-4114', "J0032-4405", 'J2145-7459'])
plt.tight_layout()
plt.savefig('Figures/young_comp_large_unc.png', dpi=150)
