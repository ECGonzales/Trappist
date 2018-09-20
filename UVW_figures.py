import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------------
# ------------------- Read in Data ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas dataframes
df_UVW = pd.read_csv('Data/Table11_UVW.txt', sep="\t", comment='#', header=0)

# calculate sqrt(u^2+v^+w^2) and err
a = np.sqrt(df_UVW['U']**2 + df_UVW['V']**2 + df_UVW['W']**2)
b = df_UVW['U']**2 + df_UVW['V']**2 + df_UVW['W']**2
db = 2*(df_UVW['dU']/abs(df_UVW['U'])) + 2*(df_UVW['dV']/abs(df_UVW['V'])) + 2*(df_UVW['dW']/abs(df_UVW['W']))

df_UVW['Total'] = np.sqrt(df_UVW['U']**2 + df_UVW['V']**2 + df_UVW['W']**2)
df_UVW['Total_err'] = (1/2)*(db/abs(b))

# Separate the to g/b, in/out
df_gamma_group = df_UVW[(df_UVW['Grav_use'] == 'gamma') & (df_UVW['Group'].notnull())]
df_gamma_nogroup = df_UVW[(df_UVW['Grav_use'] == 'gamma') & (df_UVW['Group'].isnull())]
# df_beta_group = df_UVW[(df_UVW['Grav_use'] == 'beta') & (df_UVW['Group'].notnull())]  # Non in groups
df_beta_nogroup = df_UVW[(df_UVW['Grav_use'] == 'beta') & (df_UVW['Group'].isnull())]

# Trappist UVW
trap_U = -44.147
trap_dU = 0.086
trap_V = -67.192
trap_dV = 0.095
trap_W = 11.66
trap_dW = 0.14

trap_total_UVW = np.sqrt(trap_U**2 + trap_V**2 + trap_W**2)

# intermediate steps
c = trap_U**2 + trap_V**2 + trap_W**2
dc = 2*(trap_dU/abs(trap_U)) + 2*(trap_dV/abs(trap_V)) + 2*(trap_dW/abs(trap_W))
trap_total_UVW_err = (1/2)*(dc/abs(c))

# ------------------------------------------------------------------------------------
# -------------------------------- Plots: U vs V -------------------------------------
# ------------------------------------------------------------------------------------
fig = plt.figure()
ax1 = fig.add_subplot(111)
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)
fig.set_size_inches(10, 6.45)
plt.xlim([-73, 45])
plt.ylim([-75, 0])

# ------Tick size and Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.ylabel('$U$ (km/s)', fontsize=25)
plt.xlabel('$V$ (km/s)', fontsize=25)
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)

#  ---------- add data -------------
# gamma group
gamma_in = plt.scatter(df_gamma_group['U'], df_gamma_group['V'], color='white', edgecolors='#9B0132', s=70)
ax1.errorbar(df_gamma_group['U'], df_gamma_group['V'], xerr=df_gamma_group['dU'],yerr=df_gamma_group['dV'], c='#9B0132',
             fmt='o', mfc='white')
# gamma non
gamma_out = plt.scatter(df_gamma_nogroup['U'], df_gamma_nogroup['V'], color='#9B0132', s=70,
                        marker="o")
ax1.errorbar(df_gamma_nogroup['U'], df_gamma_nogroup['V'], xerr=df_gamma_nogroup['dU'], yerr=df_gamma_nogroup['dV'],
             c='#9B0132', fmt='o')
# beta non
beta_out = plt.scatter(df_beta_nogroup['U'], df_beta_nogroup['V'], color='#FF6B03', s=70)
ax1.errorbar(df_beta_nogroup['U'], df_beta_nogroup['V'], xerr=df_beta_nogroup['dU'],yerr=df_beta_nogroup['dV'],
             c='#FF6B03', fmt='o')
# TRAPPIST-1
trappist = plt.scatter(trap_U, trap_V, color='k', s=700, marker='*')
ax1.errorbar(trap_U, trap_V, xerr=trap_dU,yerr=trap_dV, c='k', fmt='o')

# Add eagan good box line
plt.hlines(-50, -30, 0, linestyles='dashed', linewidth=1)
plt.hlines(20, -30, 0, linestyles='dashed', linewidth=1)
plt.vlines(-30, -50, 20, linestyles='dashed', linewidth=1)
plt.vlines(0, -50, 20, linestyles='dashed', linewidth=1)

plt.legend([gamma_in, gamma_out, beta_out, trappist], ['$\gamma$ in group', '$\gamma$ not in group',
                                                       '$\\beta$ not in group', 'TRAPPIST-1'], frameon=False, fontsize=12)
plt.tight_layout()
plt.savefig('Figures/U_vs_V.pdf')

# ------------------------------------------------------------------------------------
# -------------------------------- Plots: U vs W -------------------------------------
# ------------------------------------------------------------------------------------
fig = plt.figure()
ax1 = fig.add_subplot(111)
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)
fig.set_size_inches(10, 6.45)
plt.xlim([-75, 45])
plt.ylim([-75, 16])

# ------Tick size and Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.ylabel('$U$ (km/s)', fontsize=25)
plt.xlabel('$W$ (km/s)', fontsize=25)
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)

#  ---------- add data -------------
# gamma group
gamma_in = plt.scatter(df_gamma_group['U'], df_gamma_group['W'], color='white', edgecolors='#9B0132', s=70)
ax1.errorbar(df_gamma_group['U'], df_gamma_group['W'], xerr=df_gamma_group['dU'],yerr=df_gamma_group['dW'], c='#9B0132',
             fmt='o', mfc='white')
# gamma non
gamma_out = plt.scatter(df_gamma_nogroup['U'], df_gamma_nogroup['W'], color='#9B0132', s=70,
                        marker="o")
ax1.errorbar(df_gamma_nogroup['U'], df_gamma_nogroup['W'], xerr=df_gamma_nogroup['dU'], yerr=df_gamma_nogroup['dW'],
             c='#9B0132', fmt='o')
# beta non
beta_out = plt.scatter(df_beta_nogroup['U'], df_beta_nogroup['W'], color='#FF6B03', s=70)
ax1.errorbar(df_beta_nogroup['U'], df_beta_nogroup['W'], xerr=df_beta_nogroup['dU'],yerr=df_beta_nogroup['dV'],
             c='#FF6B03', fmt='o')
# TRAPPIST-1
trappist = plt.scatter(trap_U, trap_W, color='k', s=700, marker='*')
ax1.errorbar(trap_U, trap_W, xerr=trap_dU,yerr=trap_dW, c='k', fmt='o')

plt.legend([gamma_in, gamma_out, beta_out, trappist], ['$\gamma$ in group', '$\gamma$ not in group',
                                                       '$\\beta$ not in group', 'TRAPPIST-1'], frameon=False, fontsize=12)
plt.tight_layout()
plt.savefig('Figures/U_vs_W.pdf')

# ------------------------------------------------------------------------------------
# -------------------------------- Plots: V vs W -------------------------------------
# ------------------------------------------------------------------------------------
fig = plt.figure()
ax1 = fig.add_subplot(111)
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)
fig.set_size_inches(10, 6.45)
plt.xlim([-75, 0])
plt.ylim([-65, 20])

# ------Tick size and Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.ylabel('$V$ (km/s)', fontsize=25)
plt.xlabel('$W$ (km/s)', fontsize=25)
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)

#  ---------- add data -------------
# gamma group
gamma_in = plt.scatter(df_gamma_group['V'], df_gamma_group['W'], color='white', edgecolors='#9B0132', s=70)
ax1.errorbar(df_gamma_group['V'], df_gamma_group['W'], xerr=df_gamma_group['dV'],yerr=df_gamma_group['dW'], c='#9B0132',
             fmt='o', mfc='white')
# gamma non
gamma_out = plt.scatter(df_gamma_nogroup['V'], df_gamma_nogroup['W'], color='#9B0132', s=70,
                        marker="o")
ax1.errorbar(df_gamma_nogroup['V'], df_gamma_nogroup['W'], xerr=df_gamma_nogroup['dV'], yerr=df_gamma_nogroup['dW'],
             c='#9B0132', fmt='o')
# beta non
beta_out = plt.scatter(df_beta_nogroup['V'], df_beta_nogroup['W'], color='#FF6B03', s=70)
ax1.errorbar(df_beta_nogroup['V'], df_beta_nogroup['W'], xerr=df_beta_nogroup['dV'],yerr=df_beta_nogroup['dW'],
             c='#FF6B03', fmt='o')
# TRAPPIST-1
trappist = plt.scatter(trap_V, trap_W, color='k', s=700, marker='*')
ax1.errorbar(trap_V, trap_W, xerr=trap_dV,yerr=trap_dW, c='k', fmt='o')

plt.legend([gamma_in, gamma_out, beta_out, trappist], ['$\gamma$ in group', '$\gamma$ not in group',
                                                       '$\\beta$ not in group', 'TRAPPIST-1'], loc=4,
           frameon=False, fontsize=12)
plt.tight_layout()
plt.savefig('Figures/V_vs_W.pdf')

# ------------------------------------------------------------------------------------
# -------------------------------- Plots: Total Velocity -----------------------------
# ------------------------------------------------------------------------------------
# ---------Gamma in----------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)

# ------Tick size and Axes Labels --------
plt.ylabel('Number', fontsize=25)
plt.xlabel('Total velocity (km/s)', fontsize=25)
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
bins=np.linspace(10,100,10)

plt.hist(df_gamma_group['Total'], bins=bins, color='#9B0132', edgecolor='k', label="$\gamma$ in Group")
plt.legend(fontsize=15)
plt.tight_layout()
plt.savefig('Figures/Total_UVW_velocity_hist_gammaIn.pdf', dpi=150)

# ----------------Gamma out--------------------------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)

# ------Tick size and Axes Labels --------
plt.ylabel('Number', fontsize=25)
plt.xlabel('Total velocity (km/s)', fontsize=25)
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
bins=np.linspace(10,100,10)


plt.hist(df_gamma_nogroup['Total'], bins=bins, color='#BD250E', edgecolor='k', label="$\gamma$ not in Group")
plt.legend(fontsize=15)
plt.tight_layout()
plt.savefig('Figures/Total_UVW_velocity_hist_gammaOut.pdf', dpi=150)

# ---------------------beta out----------------------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)

# ------Tick size and Axes Labels --------
plt.ylabel('Number', fontsize=25)
plt.xlabel('Total velocity (km/s)', fontsize=25)
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
bins=np.linspace(10,100,10)

plt.hist(df_beta_nogroup['Total'], bins=bins, color='#FF6B03', edgecolor='k', alpha=0.75, label="$\\beta$ not in Group")
plt.legend(fontsize=15)
plt.tight_layout()
plt.savefig('Figures/Total_UVW_velocity_hist_betaOut.pdf', dpi=150)
