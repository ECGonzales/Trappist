import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_trap = pd.read_csv('Data/Gaia2306-0502 (M7.5) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
# ---- Teff ----
df_0253 = pd.read_csv('Data/beta_comp/Gaia0253+3206 (M7beta) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
# ---- Lbol -----
df_2235 = pd.read_csv('Data/beta_comp/Gaia2235-5906 (M8.5beta) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_2235_phot = pd.read_csv('Data/beta_comp/Gaia2235-5906 (M8.5beta) phot.txt', sep=" ", comment='#', header=None,
                           names=["w", "f", "err"])
df_2154 = pd.read_csv('Data/beta_comp/Gaia2154-7459 (M9.5beta) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_2154_phot = pd.read_csv('Data/beta_comp/Gaia2154-7459 (M9.5beta) phot.txt', sep=" ", comment='#', header=None,
                           names=["w", "f", "err"])
df_vb8 = pd.read_csv('Data/field_comp/Gaia1655-0823 (M7) SED.txt', sep=" ", comment='#', header=None,
                     names=["w", "f", "err"])
df_vb10 = pd.read_csv('Data/field_comp/Gaia1916+0508 (M8) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_0320 = pd.read_csv('Data/field_comp/Gaia0320+1854 (M8) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])

# Yband
# norm_region = df_trap[(df_trap['w'] >= 0.98) & (df_trap['w'] <= 0.988)]
# norm_df_trap = df_trap['f']/(np.average(norm_region['f']))
# norm_region2 = df_vb8[(df_vb8['w'] >= 0.98) & (df_vb8['w'] <= 0.988)]
# norm_df_vb8 = df_vb8['f']/(np.average(norm_region2['f']))
# norm_region7 = df_vb10[(df_vb10['w'] >= 0.98) & (df_vb10['w'] <= 0.988)]
# norm_df_vb10 = df_vb10['f']/(np.average(norm_region7['f']))
# norm_region8 = df_0320[(df_0320['w'] >= 0.98) & (df_0320['w'] <= 0.988)]
# norm_df_0320 = df_0320['f']/(np.average(norm_region8['f']))
# norm_region3 = df_0253[(df_0253['w'] >= 0.98) & (df_0253['w'] <= 0.988)]
# norm_df_0253 = df_0253['f']/(np.average(norm_region3['f']))
# norm_region2 = df_2235[(df_2235['w'] >= 0.98) & (df_2235['w'] <= 0.988)]
# norm_df_2235 = df_2235['f']/(np.average(norm_region2['f']))
# norm_region7 = df_2154[(df_2154['w'] >= 0.98) & (df_2154['w'] <= 0.988)]
# norm_df_2154 = df_2154['f']/(np.average(norm_region7['f']))

# Jband
# norm_region = df_trap[(df_trap['w'] >= 1.22) & (df_trap['w'] <= 1.23)]
# norm_df_trap = df_trap['f']/(np.average(norm_region['f']))
# norm_region3 = df_0253[(df_0253['w'] >= 1.22) & (df_0253['w'] <= 1.23)]
# norm_df_0253 = df_0253['f']/(np.average(norm_region3['f']))
# norm_region2 = df_2235[(df_2235['w'] >= 1.22) & (df_2235['w'] <= 1.23)]
# norm_df_2235 = df_2235['f']/(np.average(norm_region2['f']))
# norm_region7 = df_2154[(df_2154['w'] >= 1.22) & (df_2154['w'] <= 1.23)]
# norm_df_2154 = df_2154['f']/(np.average(norm_region7['f']))
# norm_region2 = df_vb8[(df_vb8['w'] >= 1.22) & (df_vb8['w'] <= 1.23)]
# norm_df_vb8 = df_vb8['f']/(np.average(norm_region2['f']))
# norm_region7 = df_vb10[(df_vb10['w'] >= 1.22) & (df_vb10['w'] <= 1.23)]
# norm_df_vb10 = df_vb10['f']/(np.average(norm_region7['f']))
# norm_region8 = df_0320[(df_0320['w'] >= 1.22) & (df_0320['w'] <= 1.23)]
# norm_df_0320 = df_0320['f']/(np.average(norm_region8['f']))

# Hband
# norm_region = df_trap[(df_trap['w'] >= 1.5) & (df_trap['w'] <= 1.52)]
# norm_df_trap = df_trap['f']/(np.average(norm_region['f']))
# norm_region2 = df_vb8[(df_vb8['w'] >= 1.5) & (df_vb8['w'] <= 1.52)]
# norm_df_vb8 = df_vb8['f']/(np.average(norm_region2['f']))
# norm_region7 = df_vb10[(df_vb10['w'] >= 1.5) & (df_vb10['w'] <= 1.52)]
# norm_df_vb10 = df_vb10['f']/(np.average(norm_region7['f']))
# norm_region8 = df_0320[(df_0320['w'] >= 1.5) & (df_0320['w'] <= 1.52)]
# norm_df_0320 = df_0320['f']/(np.average(norm_region8['f']))
# norm_region3 = df_0253[(df_0253['w'] >= 1.5) & (df_0253['w'] <= 1.52)]
# norm_df_0253 = df_0253['f']/(np.average(norm_region3['f']))
# norm_region2 = df_2235[(df_2235['w'] >= 1.5) & (df_2235['w'] <= 1.52)]
# norm_df_2235 = df_2235['f']/(np.average(norm_region2['f']))
# norm_region7 = df_2154[(df_2154['w'] >= 1.5) & (df_2154['w'] <= 1.52)]
# norm_df_2154 = df_2154['f']/(np.average(norm_region7['f']))

# Kband
norm_region = df_trap[(df_trap['w'] >= 2.16) & (df_trap['w'] <= 2.20)]
norm_df_trap = df_trap['f']/(np.average(norm_region['f']))
norm_region2 = df_vb8[(df_vb8['w'] >= 2.16) & (df_vb8['w'] <= 2.20)]
norm_df_vb8 = df_vb8['f']/(np.average(norm_region2['f']))
norm_region7 = df_vb10[(df_vb10['w'] >= 2.16) & (df_vb10['w'] <= 2.20)]
norm_df_vb10 = df_vb10['f']/(np.average(norm_region7['f']))
norm_region8 = df_0320[(df_0320['w'] >= 2.16) & (df_0320['w'] <= 2.20)]
norm_df_0320 = df_0320['f']/(np.average(norm_region8['f']))
norm_region3 = df_0253[(df_0253['w'] >= 2.16) & (df_0253['w'] <= 2.20)]
norm_df_0253 = df_0253['f']/(np.average(norm_region3['f']))
norm_region2 = df_2235[(df_2235['w'] >= 2.16) & (df_2235['w'] <= 2.20)]
norm_df_2235 = df_2235['f']/(np.average(norm_region2['f']))
norm_region7 = df_2154[(df_2154['w'] >= 2.16) & (df_2154['w'] <= 2.20)]
norm_df_2154 = df_2154['f']/(np.average(norm_region7['f']))


# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(8.5, 11)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
# plt.xlim([0.95, 1.10])
# plt.xlim([1.12, 1.35])
# plt.xlim([1.42, 1.80])
plt.xlim([2.0, 2.35])
plt.ylim([0.25, 6.6])
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)
# ------Tick size and Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xlabel('Wavelength ($\mu$m)', fontsize=25)
plt.ylabel('Normalized Flux ($F_\lambda$)', fontsize=25)
plt.tight_layout()

ax1.plot(df_0253['w'], norm_df_0253, c='#D01810')
ax1.plot(df_2235['w'], norm_df_2235 +1, c='#8E01E8')
ax1.plot(df_2154['w'], norm_df_2154 +2, c='#E806B7')
ax1.plot(df_0320['w'], norm_df_0320 +3, c='#6A777F')
ax1.plot(df_vb8['w'], norm_df_vb8 +4, c='#7C7D70')
ax1.plot(df_vb10['w'], norm_df_vb10 +5, c='#A0B2BF')

ax1.plot(df_trap['w'], norm_df_trap, c='k')
ax1.plot(df_trap['w'], norm_df_trap +1, c='k')
ax1.plot(df_trap['w'], norm_df_trap +2, c='k')
ax1.plot(df_trap['w'], norm_df_trap+3, c='k')
ax1.plot(df_trap['w'], norm_df_trap+4, c='k')
ax1.plot(df_trap['w'], norm_df_trap+5, c='k')