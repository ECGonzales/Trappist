import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------------
# ------------------- Read in Indices and polynomials ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas dataframes
df = pd.read_csv('Data/Indices/indices.tsv', sep="\t", comment='#', header=0)
# names=[Shortname, Spectra, Lit. OPT SPT,	opt grav, Lit NIR SpT, nir grav, Final Gravity low,	FInal gravity Med.,	FEH_Z,
# E_FEH_Z, VO_Z, E_VO_Z, FEH_J,	E_FEH_J, KI_J, E_KI_J, HCONT, E_HCONT, NAI,	E_NAI, KI_169, E_KI_169, KI_177, E_KI_177,
# KI_244, E_KI_244, KI_253,	E_KI_253]

# Separate the data into field, gamma, and beta, and medium res.
df_gamma = df[(df['nir grav'] == 'g') & (df['Spectra'] != 'prism')]
df_beta = df[(df['nir grav'] == 'b') & (df['Spectra'] != 'prism')]
df_field = df[(df['nir grav'] == 'f') & (df['Spectra'] != 'prism')]
df_field2 = df[(df['opt grav'] == 'f') & (df['nir grav'].isnull()) & (df['Spectra'] != 'prism')]
df_subd = df[(df['opt grav'] == 'sd') & (df['Spectra'] != 'prism')]

# --------------------------------------------------------------------------------------
# -----------------------------Plot up the indices NAI-----------------------------------
# --------------------------------------------------------------------------------------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)

# ------Tick size and Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.ylabel('Na I EW ($\AA$)', fontsize=25)
plt.xlabel('NIR Spectral Type', fontsize=25)
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xticks([6,7, 8, 9, 10,11, 12], ['M6', "M7", 'M8','M9', 'L0','L1', 'L2'], fontsize=20)
plt.xlim([5.8, 12])
plt.ylim([0, 16])


# plot data
gamma = plt.scatter(df_gamma['SpT_used'], df_gamma['NAI'], color='#9B0132', s=70, zorder=4)
ax1.errorbar(df_gamma['SpT_used'], df_gamma['NAI'], yerr=df_gamma['E_NAI'], c='#9B0132', fmt='o', zorder=3)

beta = plt.scatter(df_beta['SpT_used'], df_beta['NAI'], color='#D01810', s=70, zorder=4)
ax1.errorbar(df_beta['SpT_used'], df_beta['NAI'], yerr=df_beta['E_NAI'], c='#D01810', fmt='o', zorder=3)

fld = plt.scatter(df_field['SpT_used'], df_field['NAI'], color='#7C7D70', s=70, zorder=4)
ax1.errorbar(df_field['SpT_used'], df_field['NAI'], yerr=df_field['E_NAI'], c='#7C7D70', fmt='o', zorder=3)

fld_opt = plt.scatter(df_field2['SpT_used'], df_field2['NAI'], color='#ABBDC4', s=70, zorder=4)
ax1.errorbar(df_field2['SpT_used'], df_field2['NAI'], yerr=df_field2['E_NAI'], c='#ABBDC4', fmt='o', zorder=3)

# sd = plt.scatter(df_subd['SpT_used'], df_subd['FEH_Z'], color='blue', s=70)
# ax1.errorbar(df_subd['SpT_used'], df_subd['FEH_Z'], yerr=df_subd['E_FEH_Z'], c='blue', fmt='o')

# --- Designate Trappist-1 -----
# FIRE
trap_f = plt.scatter(df_field2['SpT_used'][26], df_field2['NAI'][26], color='k', s=200, zorder=2, marker="s")
ax1.errorbar(df_field2['SpT_used'][26], df_field2['NAI'][26], yerr=df_field2['E_NAI'][26], c='k', zorder=2, fmt='o')
# SXD
trap_s = plt.scatter(df_field2['SpT_used'][27], df_field2['NAI'][27], color='k', s=200, zorder=2, marker="o")
ax1.errorbar(df_field2['SpT_used'][27], df_field2['NAI'][27], yerr=df_field2['E_NAI'][27], c='k', zorder=2, fmt='o')

# ---- Add Legend ----
plt.legend([fld, fld_opt, gamma, beta, trap_f], ["Field", "Field (opt Spt)", "$\gamma$", '$\\beta$', 'TRAPPIST-1'],
           frameon=False, fontsize=12)

plt.tight_layout()
plt.savefig('Figures/NAI_vs_NIRSpt.pdf', dpi=150)


# --------------------------------------------------------------------------------------
# -----------------------------Plot up the indices KI 1.169-----------------------------------
# --------------------------------------------------------------------------------------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)

# ------Tick size and Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.ylabel('K I 1.169 EW ($\AA$)', fontsize=25)
plt.xlabel('NIR Spectral Type', fontsize=25)
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xticks([6,7, 8, 9, 10,11, 12], ['M6', "M7", 'M8','M9', 'L0','L1', 'L2'], fontsize=20)
plt.xlim([5.8, 12])
plt.ylim([1, 6.1])


# plot data
gamma = plt.scatter(df_gamma['SpT_used'], df_gamma['KI_169'], color='#9B0132', s=70, zorder=4)
ax1.errorbar(df_gamma['SpT_used'], df_gamma['KI_169'], yerr=df_gamma['E_KI_169'], c='#9B0132', fmt='o', zorder=3)

beta = plt.scatter(df_beta['SpT_used'], df_beta['KI_169'], color='#D01810', s=70, zorder=4)
ax1.errorbar(df_beta['SpT_used'], df_beta['KI_169'], yerr=df_beta['E_KI_169'], c='#D01810', fmt='o', zorder=3)

fld = plt.scatter(df_field['SpT_used'], df_field['KI_169'], color='#7C7D70', s=70, zorder=4)
ax1.errorbar(df_field['SpT_used'], df_field['KI_169'], yerr=df_field['E_KI_169'], c='#7C7D70', fmt='o', zorder=3)

fld_opt = plt.scatter(df_field2['SpT_used'], df_field2['KI_169'], color='#ABBDC4', s=70, zorder=4)
ax1.errorbar(df_field2['SpT_used'], df_field2['KI_169'], yerr=df_field2['E_KI_169'], c='#ABBDC4', fmt='o', zorder=3)

# sd = plt.scatter(df_subd['SpT_used'], df_subd['FEH_Z'], color='blue', s=70)
# ax1.errorbar(df_subd['SpT_used'], df_subd['FEH_Z'], yerr=df_subd['E_FEH_Z'], c='blue', fmt='o')

# --- Designate Trappist-1 -----
# FIRE
trap_f = plt.scatter(df_field2['SpT_used'][26], df_field2['KI_169'][26], color='k', s=200, zorder=2, marker="s")
ax1.errorbar(df_field2['SpT_used'][26], df_field2['KI_169'][26], yerr=df_field2['E_KI_169'][26], c='k', zorder=2, fmt='o')
# SXD
trap_s = plt.scatter(df_field2['SpT_used'][27], df_field2['KI_169'][27], color='k', s=200, zorder=2, marker="o")
ax1.errorbar(df_field2['SpT_used'][27], df_field2['KI_169'][27], yerr=df_field2['E_KI_169'][27], c='k', zorder=2, fmt='o')

# ---- Add Legend ----
plt.legend([fld, fld_opt, gamma, beta, trap_f], ["Field", "Field (opt Spt)", "$\gamma$", '$\\beta$', 'TRAPPIST-1'],
           frameon=False, fontsize=12)

plt.tight_layout()
plt.savefig('Figures/KI_169_vs_NIRSpt.pdf', dpi=150)

# --------------------------------------------------------------------------------------
# -----------------------------Plot up the indices KI 1.177-----------------------------
# --------------------------------------------------------------------------------------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)

# ------Tick size and Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.ylabel('K I 1.177 EW ($\AA$)', fontsize=25)
plt.xlabel('NIR Spectral Type', fontsize=25)
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xticks([6,7, 8, 9, 10,11, 12], ['M6', "M7", 'M8','M9', 'L0','L1', 'L2'], fontsize=20)
plt.xlim([5.8, 12])
plt.ylim([0.75, 9])

# plot data
gamma = plt.scatter(df_gamma['SpT_used'], df_gamma['KI_177'], color='#9B0132', s=70, zorder=4)
ax1.errorbar(df_gamma['SpT_used'], df_gamma['KI_177'], yerr=df_gamma['E_KI_177'], c='#9B0132', fmt='o', zorder=3)

beta = plt.scatter(df_beta['SpT_used'], df_beta['KI_177'], color='#D01810', s=70, zorder=4)
ax1.errorbar(df_beta['SpT_used'], df_beta['KI_177'], yerr=df_beta['E_KI_177'], c='#D01810', fmt='o', zorder=3)

fld = plt.scatter(df_field['SpT_used'], df_field['KI_177'], color='#7C7D70', s=70, zorder=4)
ax1.errorbar(df_field['SpT_used'], df_field['KI_177'], yerr=df_field['E_KI_177'], c='#7C7D70', fmt='o', zorder=3)

fld_opt = plt.scatter(df_field2['SpT_used'], df_field2['KI_177'], color='#ABBDC4', s=70, zorder=4)
ax1.errorbar(df_field2['SpT_used'], df_field2['KI_177'], yerr=df_field2['E_KI_177'], c='#ABBDC4', fmt='o', zorder=3)

# sd = plt.scatter(df_subd['SpT_used'], df_subd['FEH_Z'], color='blue', s=70)
# ax1.errorbar(df_subd['SpT_used'], df_subd['FEH_Z'], yerr=df_subd['E_FEH_Z'], c='blue', fmt='o')

# --- Designate Trappist-1 -----
# FIRE
trap_f = plt.scatter(df_field2['SpT_used'][26], df_field2['KI_177'][26], color='k', s=200, zorder=2, marker="s")
ax1.errorbar(df_field2['SpT_used'][26], df_field2['KI_177'][26], yerr=df_field2['E_KI_177'][26], c='k', zorder=2, fmt='o')
# SXD
trap_s = plt.scatter(df_field2['SpT_used'][27], df_field2['KI_177'][27], color='k', s=200, zorder=2, marker="o")
ax1.errorbar(df_field2['SpT_used'][27], df_field2['KI_177'][27], yerr=df_field2['E_KI_177'][27], c='k', zorder=2, fmt='o')

# ---- Add Legend ----
plt.legend([fld, fld_opt, gamma, beta, trap_f], ["Field", "Field (opt Spt)", "$\gamma$", '$\\beta$', 'TRAPPIST-1'],
           frameon=False, fontsize=12)

plt.tight_layout()
plt.savefig('Figures/KI_177_vs_NIRSpt.pdf', dpi=150)

# --------------------------------------------------------------------------------------
# -----------------------------Plot up the indices KI 1.244-----------------------------
# --------------------------------------------------------------------------------------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)

# ------Tick size and Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.ylabel('K I 1.244 EW ($\AA$)', fontsize=25)
plt.xlabel('NIR Spectral Type', fontsize=25)
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xticks([6,7, 8, 9, 10,11, 12], ['M6', "M7", 'M8','M9', 'L0','L1', 'L2'], fontsize=20)
plt.xlim([5.8, 12])
plt.ylim([-17, 6])


# plot data
gamma = plt.scatter(df_gamma['SpT_used'], df_gamma['KI_244'], color='#9B0132', s=70, zorder=4)
ax1.errorbar(df_gamma['SpT_used'], df_gamma['KI_244'], yerr=df_gamma['E_KI_244'], c='#9B0132', fmt='o', zorder=3)

beta = plt.scatter(df_beta['SpT_used'], df_beta['KI_244'], color='#D01810', s=70, zorder=4)
ax1.errorbar(df_beta['SpT_used'], df_beta['KI_244'], yerr=df_beta['E_KI_244'], c='#D01810', fmt='o', zorder=3)

fld = plt.scatter(df_field['SpT_used'], df_field['KI_244'], color='#7C7D70', s=70, zorder=4)
ax1.errorbar(df_field['SpT_used'], df_field['KI_244'], yerr=df_field['E_KI_244'], c='#7C7D70', fmt='o', zorder=3)

fld_opt = plt.scatter(df_field2['SpT_used'], df_field2['KI_244'], color='#ABBDC4', s=70, zorder=4)
ax1.errorbar(df_field2['SpT_used'], df_field2['KI_244'], yerr=df_field2['E_KI_244'], c='#ABBDC4', fmt='o', zorder=3)

# sd = plt.scatter(df_subd['SpT_used'], df_subd['FEH_Z'], color='blue', s=70)
# ax1.errorbar(df_subd['SpT_used'], df_subd['FEH_Z'], yerr=df_subd['E_FEH_Z'], c='blue', fmt='o')

# --- Designate Trappist-1 -----
# FIRE
trap_f = plt.scatter(df_field2['SpT_used'][26], df_field2['KI_244'][26], color='k', s=200, zorder=2, marker="s")
ax1.errorbar(df_field2['SpT_used'][26], df_field2['KI_244'][26], yerr=df_field2['E_KI_244'][26], c='k', zorder=2, fmt='o')
# SXD
trap_s = plt.scatter(df_field2['SpT_used'][27], df_field2['KI_244'][27], color='k', s=200, zorder=2, marker="o")
ax1.errorbar(df_field2['SpT_used'][27], df_field2['KI_244'][27], yerr=df_field2['E_KI_244'][27], c='k', zorder=2, fmt='o')

# ---- Add Legend ----
plt.legend([fld, fld_opt, gamma, beta, trap_f], ["Field", "Field (opt Spt)", "$\gamma$", '$\\beta$', 'TRAPPIST-1'],
           frameon=False, fontsize=12)

plt.tight_layout()
plt.savefig('Figures/KI_244_vs_NIRSpt.pdf', dpi=150)

# --------------------------------------------------------------------------------------
# -----------------------------Plot up the indices KI 1.253-----------------------------
# --------------------------------------------------------------------------------------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)

# ------Tick size and Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.ylabel('K I 1.169 EW ($\AA$)', fontsize=25)
plt.xlabel('NIR Spectral Type', fontsize=25)
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xticks([6,7, 8, 9, 10,11, 12], ['M6', "M7", 'M8','M9', 'L0','L1', 'L2'], fontsize=20)
plt.xlim([5.8, 12])
plt.ylim([1, 10])


# plot data
gamma = plt.scatter(df_gamma['SpT_used'], df_gamma['KI_253'], color='#9B0132', s=70, zorder=4)
ax1.errorbar(df_gamma['SpT_used'], df_gamma['KI_253'], yerr=df_gamma['E_KI_253'], c='#9B0132', fmt='o', zorder=3)

beta = plt.scatter(df_beta['SpT_used'], df_beta['KI_253'], color='#D01810', s=70, zorder=4)
ax1.errorbar(df_beta['SpT_used'], df_beta['KI_253'], yerr=df_beta['E_KI_253'], c='#D01810', fmt='o', zorder=3)

fld = plt.scatter(df_field['SpT_used'], df_field['KI_253'], color='#7C7D70', s=70, zorder=4)
ax1.errorbar(df_field['SpT_used'], df_field['KI_253'], yerr=df_field['E_KI_253'], c='#7C7D70', fmt='o', zorder=3)

fld_opt = plt.scatter(df_field2['SpT_used'], df_field2['KI_253'], color='#ABBDC4', s=70, zorder=4)
ax1.errorbar(df_field2['SpT_used'], df_field2['KI_253'], yerr=df_field2['E_KI_253'], c='#ABBDC4', fmt='o', zorder=3)

# sd = plt.scatter(df_subd['SpT_used'], df_subd['FEH_Z'], color='blue', s=70)
# ax1.errorbar(df_subd['SpT_used'], df_subd['FEH_Z'], yerr=df_subd['E_FEH_Z'], c='blue', fmt='o')

# --- Designate Trappist-1 -----
# FIRE
trap_f = plt.scatter(df_field2['SpT_used'][26], df_field2['KI_253'][26], color='k', s=200, zorder=2, marker="s")
ax1.errorbar(df_field2['SpT_used'][26], df_field2['KI_253'][26], yerr=df_field2['E_KI_169'][26], c='k', zorder=2, fmt='o')
# SXD
trap_s = plt.scatter(df_field2['SpT_used'][27], df_field2['KI_253'][27], color='k', s=200, zorder=2, marker="o")
ax1.errorbar(df_field2['SpT_used'][27], df_field2['KI_253'][27], yerr=df_field2['E_KI_253'][27], c='k', zorder=2, fmt='o')

# ---- Add Legend ----
plt.legend([fld, fld_opt, gamma, beta, trap_f], ["Field", "Field (opt Spt)", "$\gamma$", '$\\beta$', 'TRAPPIST-1'],
           frameon=False, fontsize=12)

plt.tight_layout()
plt.savefig('Figures/KI_253_vs_NIRSpt.pdf', dpi=150)
