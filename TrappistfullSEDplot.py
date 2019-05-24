import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter


# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# -------------------------------------------------------------------------------------

# ------------ 1256-0224 (Poster in SED)----------------
# Read in as pandas dataframe
df = pd.read_csv('Data/PS_2306-0502 (M7.5) SED.txt', sep=" ", comment='#', header=None,
                 names=["w", "f", "err"])
df2 = pd.read_csv('Data/PS_2306-0502 (M7.5) phot.txt', sep=" ", comment='#', names=["w", "f", "err"])

# -------------------------------------------------------------------------------------
# ------------------------- Plotting --------------------------------------------------
# -------------------------------------------------------------------------------------

# -------- Generate spectral regime SED plot ---------------------------
# Make subarrays for color coding
opt = df[(df['w'] <= 0.8306)]
overlap = df[(df['w'] >= 0.8305) & (df['w'] <= 0.95)]
nir = df[(df['w'] >= 0.8305)]

# ----- Setup plot layout ---------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)  # This makes sure that the labels aren't cut off
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)

# ----- Plot Spectra -----------
ax1.loglog(opt['w'], opt['f'], c='#0179FF')
ax1.loglog(overlap['w'], overlap['f'], c='#009B45', lw=5, alpha=0.5)
ax1.loglog(overlap['w'], overlap['f'], c='#0179FF', alpha=0.85)  # alpha=0.3 for transparency
ax1.loglog(nir['w'], nir['f'], c='#009B45')

# ----- Plot Photometric points -----
ax1.scatter(df2['w'][0], df2['f'][0],  c='#ae017e', s=150, zorder=6)  # 2MASS_H
ax1.scatter(df2['w'][1], df2['f'][1],  c='#ae017e', s=150, zorder=6)  # 2MASS_J
ax1.scatter(df2['w'][2], df2['f'][2],  c='#ae017e', s=150, zorder=6)  # 2MASS_K
ax1.scatter(df2['w'][3], df2['f'][3],  c='#dd3497', s=150, zorder=6)  # PS_g
ax1.scatter(df2['w'][4], df2['f'][4],  c='#dd3497', s=150, zorder=6)  # PS_i
ax1.scatter(df2['w'][5], df2['f'][5],  c='#dd3497', s=150, zorder=6)  # PS_r
ax1.scatter(df2['w'][6], df2['f'][6],  c='#dd3497', s=150, zorder=6)  # PS_y
ax1.scatter(df2['w'][7], df2['f'][7],  c='#dd3497', s=150, zorder=6)  # PS_z
#ax1.scatter(df2['w'][5], df2['f'][5],  c='#f768a1', s=150, zorder=6)  # Johnson_V
ax1.scatter(df2['w'][8], df2['f'][8],  c='#7a0177', s=150, zorder=6)  # WISE_W1
ax1.scatter(df2['w'][9], df2['f'][9],  c='#7a0177', s=150, zorder=6)  # WISE_W2
ax1.scatter(df2['w'][10], df2['f'][10],  c='#7a0177', s=150, zorder=6)  # WISE_W3

# ----- Set axes limits, reformat ticks -----------
plt.xlim([0.45, 12.5])
plt.ylim([10**(-17), 2.5*10**(-14)])
ax1.xaxis.set_major_formatter(ScalarFormatter())
ax1.xaxis.set_minor_formatter(ScalarFormatter())
ax1.xaxis.set_minor_locator(plt.FixedLocator([0.5, 0.7, 2, 3, 4]))
ax1.tick_params(axis='both', which='major', labelsize=20, length=8, width=1.1)
ax1.tick_params(axis='both', which='minor', labelsize=20, length=4, width=1.1)

# ------ Axes Labels --------
plt.xlabel('Wavelength ($\mu m$)', fontsize=25)
plt.ylabel('Flux  ($erg\ s^{-1} cm^{-2} A^{-1}$)', fontsize=25)

# ------ Labeling Spectra and Photometric points --------
ax1.annotate('R-C Spec', xy=(0.78, 0.2*10**(-15)), color='#0179FF', fontsize=15)
ax1.annotate('FIRE', xy=(1.7, 0.2*10**(-14)), color='#009B45', fontsize=15)
# ax1.annotate('V', xy=(0.53, 0.2*10**(-15)), color='#f768a1', fontsize=15)
ax1.annotate('PS g', xy=(0.46, 2*10**(-16)), color='#dd3497', fontsize=15)
ax1.annotate('PS r', xy=(0.52, 4*10**(-16)), color='#dd3497', fontsize=15)
ax1.annotate('PS i', xy=(0.6, 2.5*10**(-15)), color='#dd3497', fontsize=15)
ax1.annotate('PS z', xy=(0.7, 8*10**(-15)), color='#dd3497', fontsize=15)
ax1.annotate('PS y', xy=(0.8, 1.67*10**(-14)), color='#dd3497', fontsize=15)
ax1.annotate('2MASS J', xy=(1.3, 0.18*10**(-13)), color='#ae017e', fontsize=15)
ax1.annotate('2MASS H', xy=(1.78, 1*10**(-14)), color='#ae017e', fontsize=15)
ax1.annotate('2MASS K', xy=(2.25, 0.65*10**(-14)), color='#ae017e', fontsize=15)
ax1.annotate('WISE W1', xy=(2.75, 0.7*10**(-15)), color='#7a0177', fontsize=15)
ax1.annotate('WISE W2', xy=(3.75, 0.27*10**(-15)), color='#7a0177', fontsize=15)
ax1.annotate('WISE W3', xy=(8.25, 0.2*10**(-16)), color='#7a0177', fontsize=15)

# ---------- Add Bandpasses for the photometry: From utilities file -------------
# Johnson_V = pd.DataFrame()
# Johnson_V['x'] = [0.473333, 0.687500]
# Johnson_V['y'] = [1.2*10**(-17), 1.2*10**(-17)]
# plt.plot(Johnson_V['x'], Johnson_V['y'], color='#f768a1', linestyle='solid')

# Cousins_R = pd.DataFrame()
# Cousins_R['x'] = [0.550435, 0.883333]
# Cousins_R['y'] = [1.5*10**(-17), 1.5*10**(-17)]
# plt.plot(Cousins_R['x'], Cousins_R['y'], color='#dd3497', linestyle='solid')
#
# Cousins_I = pd.DataFrame()
# Cousins_I['x'] = [0.704167, 0.916667]
# Cousins_I['y'] = [1.9*10**(-17), 1.9*10**(-17)]
# plt.plot(Cousins_I['x'], Cousins_I['y'], color='#dd3497', linestyle='solid')

PS_g = pd.DataFrame()
PS_g['x'] = [0.394340, 0.559327]
PS_g['y'] = [1.2*10**(-17), 1.2*10**(-17)]
plt.plot(PS_g['x'], PS_g['y'], color='#dd3497', linestyle='solid')

PS_r = pd.DataFrame()
PS_r['x'] = [0.538623, 0.703565]
PS_r['y'] = [1.5*10**(-17), 1.5*10**(-17)]
plt.plot(PS_r['x'], PS_r['y'], color='#dd3497', linestyle='solid')

PS_i = pd.DataFrame()
PS_i['x'] = [0.677845, 0.830437	]
PS_i['y'] = [1.2*10**(-17), 1.2*10**(-17)]
plt.plot(PS_i['x'], PS_i['y'], color='#dd3497', linestyle='solid')

PS_z = pd.DataFrame()
PS_z['x'] = [0.802800, 0.934600]
PS_z['y'] = [1.5*10**(-17), 1.5*10**(-17)]
plt.plot(PS_z['x'], PS_z['y'], color='#dd3497', linestyle='solid')

PS_y = pd.DataFrame()
PS_y['x'] = [0.910050, 1.083850]
PS_y['y'] = [1.2*10**(-17), 1.2*10**(-17)]
plt.plot(PS_y['x'], PS_y['y'], color='#dd3497', linestyle='solid')

twomass_j = pd.DataFrame()
twomass_j['x'] = [1.080647, 1.406797]
twomass_j['y'] = [1.5*10**(-17), 1.5*10**(-17)]
plt.plot(twomass_j['x'], twomass_j['y'], color='#ae017e', linestyle='solid')

twomass_h = pd.DataFrame()
twomass_h['x'] = [1.478738, 1.823102]
twomass_h['y'] = [1.2*10**(-17), 1.2*10**(-17)]
plt.plot(twomass_h['x'], twomass_h['y'], color='#ae017e', linestyle='solid')

twomass_k = pd.DataFrame()
twomass_k['x'] = [1.954369, 2.355240]
twomass_k['y'] = [1.5*10**(-17), 1.5*10**(-17)]
plt.plot(twomass_k['x'], twomass_k['y'], color='#ae017e', linestyle='solid')

W1 = pd.DataFrame()
W1['x'] = [2.754097, 3.872388]
W1['y'] = [1.2*10**(-17), 1.2*10**(-17)]
plt.plot(W1['x'], W1['y'], color='#7a0177', linestyle='solid')

W2 = pd.DataFrame()
W2['x'] = [3.963326, 5.341360]
W2['y'] = [1.5*10**(-17), 1.5*10**(-17)]
plt.plot(W2['x'], W2['y'], color='#7a0177', linestyle='solid')

W3 = pd.DataFrame()
W3['x'] = [7.443044, 17.26134]
W3['y'] = [1.2*10**(-17), 1.2*10**(-17)]
plt.plot(W3['x'], W3['y'], color='#7a0177', linestyle='solid')

plt.tight_layout()
plt.savefig('Figures/TrappistFullSED.pdf', dpi=150)
