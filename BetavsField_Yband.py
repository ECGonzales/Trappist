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

# -------------------------------------------------------------------------------------
# ------------------------- Normalize the spectra -------------------------------------
# -------------------------------------------------------------------------------------
# Yband
norm_region = df_trap[(df_trap['w'] >= 0.98) & (df_trap['w'] <= 0.988)]
norm_df_trap = df_trap['f']/(np.average(norm_region['f']))
norm_region2 = df_vb8[(df_vb8['w'] >= 0.98) & (df_vb8['w'] <= 0.988)]
norm_df_vb8 = df_vb8['f']/(np.average(norm_region2['f']))
norm_region7 = df_vb10[(df_vb10['w'] >= 0.98) & (df_vb10['w'] <= 0.988)]
norm_df_vb10 = df_vb10['f']/(np.average(norm_region7['f']))
norm_region8 = df_0320[(df_0320['w'] >= 0.98) & (df_0320['w'] <= 0.988)]
norm_df_0320 = df_0320['f']/(np.average(norm_region8['f']))
norm_region3 = df_0253[(df_0253['w'] >= 0.98) & (df_0253['w'] <= 0.988)]
norm_df_0253 = df_0253['f']/(np.average(norm_region3['f']))
norm_region2 = df_2235[(df_2235['w'] >= 0.98) & (df_2235['w'] <= 0.988)]
norm_df_2235 = df_2235['f']/(np.average(norm_region2['f']))
norm_region7 = df_2154[(df_2154['w'] >= 0.98) & (df_2154['w'] <= 0.988)]
norm_df_2154 = df_2154['f']/(np.average(norm_region7['f']))

# -------------------------------------------------------------------------------------
# ------------------------- Plotting: Y band comparison -------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(8.5, 11)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([0.95, 1.10])
plt.ylim([0.25, 6.6])
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)
# ------Tick size and Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xlabel('Wavelength ($\mu$m)', fontsize=25)
plt.ylabel('Normalized Flux ($F_\lambda$)', fontsize=25)
plt.tight_layout()

ax1.plot(df_trap['w'], norm_df_trap, c='k')
ax1.plot(df_trap['w'], norm_df_trap +1, c='k')
ax1.plot(df_trap['w'], norm_df_trap +2, c='k')
ax1.plot(df_trap['w'], norm_df_trap+3, c='k')
ax1.plot(df_trap['w'], norm_df_trap+4, c='k')
ax1.plot(df_trap['w'], norm_df_trap+5, c='k')

ax1.plot(df_0253['w'], norm_df_0253, c='#D01810', alpha=0.75)
ax1.plot(df_2235['w'], norm_df_2235 +1, c='#8E01E8', alpha=0.75)
ax1.plot(df_2154['w'], norm_df_2154 +2, c='#E806B7', alpha=0.75)
ax1.plot(df_0320['w'], norm_df_0320 +3, c='#1EE801', alpha=0.75)
ax1.plot(df_vb8['w'], norm_df_vb8 +4, c='#04A57F', alpha=0.75)
ax1.plot(df_vb10['w'], norm_df_vb10 +5, c='#275202', alpha=0.8)

# Add labels
ax1.annotate('J0253+3206 (M7 $\\beta$)', xy=(0.951, 1.2), color='#D01810', fontsize=15)
ax1.annotate('J2235-5906 (M8.5 $\\beta$)', xy=(0.951, 2.2), color='#8E01E8', fontsize=15)
ax1.annotate('J2154-7459 (M9.5 $\\beta$)', xy=(0.951, 3.2), color='#E806B7', fontsize=15)
ax1.annotate('J0320+1854 (M8)', xy=(0.951, 4.2), color='#1EE801', fontsize=15)
ax1.annotate('vb8 (M7)', xy=(0.951, 5.2), color='#04A57F', fontsize=15)
ax1.annotate('vb10 (M8)', xy=(0.951, 6.2), color='#275202', fontsize=15)

plt.savefig('Figures/Stack_Yband.pdf', dpi=150)
