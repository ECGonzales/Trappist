import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter


# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# -------------------------------------------------------------------------------------

# ------------ 1256-0224 (Poster in SED)----------------
# Read in as pandas dataframe
df = pd.read_csv('Data/2306-0502 (M7.5) SED.txt', sep=" ", comment='#', header=None,
                 names=["w", "f", "err"])
df2 = pd.read_csv('Data/2306-0502 (M7.5) phot.txt', sep=" ", comment='#', names=["w", "f", "err"])

# -------------------------------------------------------------------------------------
# ------------------------- Plotting --------------------------------------------------
# -------------------------------------------------------------------------------------

# -------- Generate spectral regime SED plot ---------------------------
# Make subarrays for color coding
opt = df[(df['w'] <= 0.8)]
overlap = df[(df['w'] >= 0.733791) & (df['w'] <= 0.8)]
nir = df[(df['w'] >= .733791)]

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
ax1.scatter(df2['w'][3], df2['f'][3],  c='#dd3497', s=150, zorder=6)  # Cousins_I
ax1.scatter(df2['w'][4], df2['f'][4],  c='#dd3497', s=150, zorder=6)  # Cousins_R
ax1.scatter(df2['w'][5], df2['f'][5],  c='#f768a1', s=150, zorder=6)  # Johnson_V
ax1.scatter(df2['w'][6], df2['f'][6],  c='#7a0177', s=150, zorder=6)  # WISE_W1
ax1.scatter(df2['w'][7], df2['f'][7],  c='#7a0177', s=150, zorder=6)  # WISE_W2
ax1.scatter(df2['w'][8], df2['f'][8],  c='#7a0177', s=150, zorder=6)  # WISE_W3

# ----- Set axes limits, reformat ticks -----------
plt.xlim([0.5, 12.5])
plt.ylim([10**(-17), 2*10**(-14)])
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
ax1.annotate('SpeX', xy=(1.7, 0.2*10**(-14)), color='#009B45', fontsize=15)
ax1.annotate('V', xy=(0.53, 0.2*10**(-15)), color='#f768a1', fontsize=15)
ax1.annotate('R', xy=(0.62, 0.97*10**(-15)), color='#dd3497', fontsize=15)
ax1.annotate('I', xy=(0.785, 0.55*10**(-14)), color='#dd3497', fontsize=15)
ax1.annotate('2MASS J', xy=(1.3, 0.15*10**(-13)), color='#ae017e', fontsize=15)
ax1.annotate('2MASS H', xy=(1.75, 0.95*10**(-14)), color='#ae017e', fontsize=15)
ax1.annotate('2MASS K', xy=(2.25, 0.55*10**(-14)), color='#ae017e', fontsize=15)
ax1.annotate('WISE W1', xy=(2.75, 0.7*10**(-15)), color='#7a0177', fontsize=15)
ax1.annotate('WISE W2', xy=(3.75, 0.27*10**(-15)), color='#7a0177', fontsize=15)
ax1.annotate('WISE W3', xy=(8.25, 0.2*10**(-16)), color='#7a0177', fontsize=15)

plt.tight_layout()
plt.savefig('Figures/TrappistFullSED.png')
