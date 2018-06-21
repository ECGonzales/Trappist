import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas dataframes

df_trap = pd.read_csv('Data/FIRE2306-0502 (M7.5) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_trap_phot = pd.read_csv('Data/FIRE2306-0502 (M7.5) phot.txt', sep=" ",comment='#', header=None, names=["w", "f", "err"])

# ---- Field ----
df_vb8 = pd.read_csv('Data/field_comp/1655-0823 (M7) SED.txt', sep=" ", comment='#', header=None,
                       names=["w", "f", "err"])
df_vb10 = pd.read_csv('Data/field_comp/1916+0508 (M8) SED.txt', sep=" ", comment='#', header=None,
                       names=["w", "f", "err"])
df_0320 = pd.read_csv('Data/field_comp/0320+1854 (M8) SED.txt', sep=" ", comment='#', header=None,
                       names=["w", "f", "err"])
# --- Young ------
df_1207 = pd.read_csv('Data/young_comp/1207-3900 (L0gamma) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_1207_phot = pd.read_csv('Data/young_comp/1207-3900 (L0gamma) phot.txt', sep=" ", comment='#', header=None,
                           names=["w", "f", "err"])
df_0443 = pd.read_csv('Data/young_comp/0443+0002 (M9gamma) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_0443_phot = pd.read_csv('Data/young_comp/0443+0002 (M9gamma) phot.txt', sep=" ", comment='#', header=None,
                           names=["w", "f", "err"])
df_0518 = pd.read_csv('Data/young_comp/0518-2756 (L1gamma) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_0518_phot = pd.read_csv('Data/young_comp/0518-2756 (L1gamma) phot.txt', sep=" ", comment='#', header=None,
                           names=["w", "f", "err"])

# -------------------------------------------------------------------------------------
# ------------------------- Normalize the spectra -------------------------------------
# -------------------------------------------------------------------------------------
# Determine region good for all spectra to take the average flux over
norm_region = df_trap[(df_trap['w'] >= 0.98) & (df_trap['w'] <= 0.988)]
norm_df_trap = df_trap['f']/(np.average(norm_region['f']))

norm_region2 = df_vb8[(df_vb8['w'] >= 0.98) & (df_vb8['w'] <= 0.988)]
norm_df_vb8 = df_vb8['f']/(np.average(norm_region2['f']))

norm_region3 = df_vb10[(df_vb10['w'] >= 0.98) & (df_vb10['w'] <= 0.988)]
norm_df_vb10 = df_vb10['f']/(np.average(norm_region3['f']))

norm_region4 = df_0320[(df_0320['w'] >= 0.98) & (df_0320['w'] <= 0.988)]
norm_df_0320 = df_0320['f']/(np.average(norm_region4['f']))

norm_region5 = df_1207[(df_1207['w'] >= 0.98) & (df_1207['w'] <= 0.988)]
norm_df_1207 = df_1207['f']/(np.average(norm_region5['f']))

norm_region6 = df_0443[(df_0443['w'] >= 0.98) & (df_0443['w'] <= 0.988)]
norm_df_0443 = df_0443['f']/(np.average(norm_region6['f']))

norm_region7 = df_0518[(df_0518['w'] >= 0.98) & (df_0518['w'] <= 0.988)]
norm_df_0518 = df_0518['f']/(np.average(norm_region7['f']))


# -------------------------------------------------------------------------------------
# ------------------- Plotting: Y band comparison -------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 8)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([0.95, 1.10])
plt.ylim([0.5, 3.7])
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)

# ------Tick size and Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xlabel('Wavelength ($\mu$m)', fontsize=25)
plt.ylabel('Normalized Flux ($F_\lambda$)', fontsize=25)

# -------- Add data -----------
ax1.plot(df_0320['w'], norm_df_0320 + 3.5, c='#6A777F')
ax1.annotate('J0320+1854 (M8) $L_\mathrm{bol}: -3.337 \pm 0.053$', xy=(0.951, 4.65), color='#6A777F', fontsize=13)

ax1.plot(df_vb8['w'], norm_df_vb8 + 4.3, c='#7C7D70')
ax1.annotate('vb8 (M7) $L_\mathrm{bol}: -3.337 \pm 0.053$', xy=(0.951, 5.4), color='#7C7D70', fontsize=13)


ax1.plot(df_0320['w'], norm_df_0320 + 3.5, c='#6A777F')
ax1.annotate('J0320+1854 (M8) $L_\mathrm{bol}: -3.337 \pm 0.053$', xy=(0.951, 4.65), color='#6A777F', fontsize=13)


ax1.plot(df_trap['w'], norm_df_trap, c='k')
ax1.annotate('Trappist-1 (M7.5) $L_\mathrm{bol}: -3.337 \pm 0.053$', xy=(0.951, 3.7), color='k', fontsize=13)

ax1.plot(df_vb10['w'], norm_df_vb10 + 1.8, c='#A0B2BF')
ax1.annotate('vb10 (M8) $L_\mathrm{bol}: -3.301 \pm 0.002$', xy=(0.951, 2.9), color='#A0B2BF', fontsize=13)

ax1.plot(df_0518['w'], norm_df_0518 + 4.3, c='#7C7D70')
ax1.annotate('J0518-2756 (L1 $\gamma$) $L_\mathrm{bol}: -3.328 \pm 0.041$', xy=(0.951, 5.4), color='#7C7D70', fontsize=13)

ax1.plot(df_1207['w'], norm_df_1207 + 1.8, c='#A0B2BF')
ax1.annotate('J1207-3900 (L0 $\gamma$) $L_\mathrm{bol}: -3.337 \pm 0.053$', xy=(0.951, 2.9), color='#A0B2BF', fontsize=13)

# --- To make lines for features ---------
FeH1 = pd.DataFrame()
FeH1['x'] = [0.9896, 1.0]
FeH1['y'] = [2.8, 2.8]
plt.plot(FeH1['x'], FeH1['y'], color='k')
ax1.annotate('FeH', xy=(0.9896, 2.81), color='k', fontsize=15)
# -- To make a vertical line
FeH1d = pd.DataFrame()
FeH1d['x'] = [0.9896, 0.9896]
FeH1d['y'] = [2.7, 2.8]
plt.plot(FeH1d['x'], FeH1d['y'], color='k')

FeH2 = pd.DataFrame()
FeH2['x'] = [0.998, 1.085]
FeH2['y'] = [3.15, 3.15]
plt.plot(FeH2['x'], FeH2['y'], color='k')
ax1.annotate('FeH', xy=(1.03, 3.17), color='k', fontsize=15)
FeH2d = pd.DataFrame()
FeH2d['x'] = [0.998, 0.998]
FeH2d['y'] = [3, 3.15]
plt.plot(FeH2d['x'], FeH2d['y'], color='k')

VO = pd.DataFrame()
VO['x'] = [1.0456, 1.08]
VO['y'] = [3.3, 3.3]
plt.plot(VO['x'], VO['y'], color='k')
ax1.annotate('VO', xy=(1.06, 3.31), color='k', fontsize=15)
VOd = pd.DataFrame()
VOd['x'] = [1.0456, 1.0456]
VOd['y'] = [3.3, 3.2]
plt.plot(VOd['x'], VOd['y'], color='k')

H2O = pd.DataFrame()
H2O['x'] = [1.08, 1.099]
H2O['y'] = [3.5, 3.5]
plt.plot(H2O['x'], H2O['y'], color='k')
ax1.annotate('H$_\mathrm{2} $O', xy=(1.085, 3.55), color='k', fontsize=15)
H2Od = pd.DataFrame()
H2Od['x'] = [1.08, 1.08]
H2Od['y'] = [3.35, 3.5]
plt.plot(H2Od['x'], H2Od['y'], color='k')

plt.tight_layout()
plt.savefig('Figures/Ybandlbolcomp.png', dpi=150)


# -------------------------------------------------------------------------------------
# ------------------- Plotting: Y band Stack comparison -------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 8)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([0.95, 1.10])
plt.ylim([0.4, 2])
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)

# ------Tick size and Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xlabel('Wavelength ($\mu$m)', fontsize=25)
plt.ylabel('Normalized Flux ($F_\lambda$)', fontsize=25)

# -------- Add data -----------
ax1.plot(df_2235['w'], norm_df_2235, c='#8E01E8')
ax1.plot(df_2154['w'], norm_df_2154, c='#E806B7')
ax1.plot(df_trap['w'], norm_df_trap, c='k')

# --- To make lines for features ---------
FeH1 = pd.DataFrame()
FeH1['x'] = [0.9896, 1.0]
FeH1['y'] = [1.3, 1.3]
plt.plot(FeH1['x'], FeH1['y'], color='k')
ax1.annotate('FeH', xy=(0.9896, 1.31), color='k', fontsize=15)
# -- To make a vertical line
FeH1d = pd.DataFrame()
FeH1d['x'] = [0.9896, 0.9896]
FeH1d['y'] = [1.2, 1.3]
plt.plot(FeH1d['x'], FeH1d['y'], color='k')

FeH2 = pd.DataFrame()
FeH2['x'] = [0.998, 1.085]
FeH2['y'] = [1.6, 1.6]
plt.plot(FeH2['x'], FeH2['y'], color='k')
ax1.annotate('FeH', xy=(1.03, 1.61), color='k', fontsize=15)
FeH2d = pd.DataFrame()
FeH2d['x'] = [0.998, 0.998]
FeH2d['y'] = [1.4, 1.6]
plt.plot(FeH2d['x'], FeH2d['y'], color='k')

VO = pd.DataFrame()
VO['x'] = [1.0456, 1.08]
VO['y'] = [1.75, 1.75]
plt.plot(VO['x'], VO['y'], color='k')
ax1.annotate('VO', xy=(1.06, 1.76), color='k', fontsize=15)
VOd = pd.DataFrame()
VOd['x'] = [1.0456, 1.0456]
VOd['y'] = [1.65, 1.75]
plt.plot(VOd['x'], VOd['y'], color='k')

H2O = pd.DataFrame()
H2O['x'] = [1.08, 1.099]
H2O['y'] = [1.9, 1.9]
plt.plot(H2O['x'], H2O['y'], color='k')
ax1.annotate('H$_\mathrm{2} $O', xy=(1.085, 1.91), color='k', fontsize=15)
H2Od = pd.DataFrame()
H2Od['x'] = [1.08, 1.08]
H2Od['y'] = [1.8, 1.9]
plt.plot(H2Od['x'], H2Od['y'], color='k')

plt.tight_layout()
plt.savefig('Figures/Ybandlbolstackcomp.png', dpi=150)
