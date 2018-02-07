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

# -------------- Comparison objects of the same Teff (young) ----------------------------------
df_1207 = pd.read_csv('Data/young_comp/1207-3932A (M8) SED.txt', sep=" ", comment='#', header=None,
                       names=["w", "f", "err"])
df_1207_phot = pd.read_csv('Data/young_comp/1207-3932A (M8) phot.txt', sep=" ", comment='#', header=None,
                            names=["w", "f", "err"])
df_0436 = pd.read_csv('Data/young_comp/0436-4114 (M8betagamma) SED.txt', sep=" ", comment='#', header=None,
                       names=["w", "f", "err"])
df_0436_phot = pd.read_csv('Data/young_comp/0436-4114 (M8betagamma) phot.txt', sep=" ", comment='#', header=None,
                            names=["w", "f", "err"])
df_0032 = pd.read_csv('Data/young_comp/1655-0823 (M7) SED.txt', sep=" ", comment='#', header=None,
                       names=["w", "f", "err"])
df_0032_phot = pd.read_csv('Data/young_comp/1655-0823 (M7) phot.txt', sep=" ", comment='#', header=None,
                            names=["w", "f", "err"])
df_2154 = pd.read_csv('Data/young_comp/1655-0823 (M7) SED.txt', sep=" ", comment='#', header=None,
                       names=["w", "f", "err"])
df_2154_phot = pd.read_csv('Data/young_comp/1655-0823 (M7) phot.txt', sep=" ", comment='#', header=None,
                            names=["w", "f", "err"])
df_1102 = pd.read_csv('Data/young_comp/1655-0823 (M7) SED.txt', sep=" ", comment='#', header=None,
                       names=["w", "f", "err"])
df_1102_phot = pd.read_csv('Data/young_comp/1655-0823 (M7) phot.txt', sep=" ", comment='#', header=None,
                            names=["w", "f", "err"])
df_1139 = pd.read_csv('Data/young_comp/1655-0823 (M7) SED.txt', sep=" ", comment='#', header=None,
                       names=["w", "f", "err"])
df_1139_phot = pd.read_csv('Data/young_comp/1655-0823 (M7) phot.txt', sep=" ", comment='#', header=None,
                            names=["w", "f", "err"])
df_1245 = pd.read_csv('Data/young_comp/1655-0823 (M7) SED.txt', sep=" ", comment='#', header=None,
                       names=["w", "f", "err"])
df_1245_phot = pd.read_csv('Data/young_comp/1655-0823 (M7) phot.txt', sep=" ", comment='#', header=None,
                            names=["w", "f", "err"])
#TODO: Finish updating paths for text files

# -------------------------------------------------------------------------------------
# ------------------- Plotting: Young Comparison of same Teff -------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)  # to make sure proper size run entire code at once and change 8 to 6.45 to
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)  # match other plots on github (the size will change if done in pieces
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)

# -------- Add data -----------
ax1.loglog(df_1207['w'], df_1207['f'], c='#04A57F')
ax1.scatter(df_1207_phot['w'], df_1207_phot['f'], c='k', s=70)  # The ones with size 70 are to give the circles a
ax1.scatter(df_1207_phot['w'], df_1207_phot['f'], c='#04A57F', s=50)        # black border
ax1.loglog(df_trap['w'], df_trap['f'], c='k', zorder=9)
ax1.scatter(df_trap_phot['w'], df_trap_phot['f'], c='k', s=70, zorder=10)
ax1.loglog(df_0436['w'], df_0436['f'], c='#09D5D6')
ax1.scatter(df_0436_phot['w'], df_0436_phot['f'], c='k', s=70)
ax1.scatter(df_0436_phot['w'], df_0436_phot['f'], c='#09D5D6', s=50)