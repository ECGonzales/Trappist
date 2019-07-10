import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------------
# ------------------- Read in Data ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas dataframes
df_UVW = pd.read_csv('Data/Table11_UVW.txt', sep="\t", comment='#', header=0)


# calculate sqrt(u^2+ w^2) and err
df_UVW['UW'] = np.sqrt(df_UVW['U']**2 +  df_UVW['W']**2)
uncertainty_U2 = 2*(df_UVW['dU']/abs(df_UVW['U']))
uncertainty_W2 = 2*(df_UVW['dW']/abs(df_UVW['W']))
unc_U2_plus_W2 = np.sqrt(uncertainty_U2**2 + uncertainty_W2**2)
final_unc_toom = (1./2.)*(unc_U2_plus_W2/abs(df_UVW['UW']))
df_UVW['UW_err'] = final_unc_toom

# Separate the to g/b, in/out
df_gamma_group = df_UVW[(df_UVW['Grav_use'] == 'gamma') & (df_UVW['Group'].notnull())]
df_gamma_nogroup = df_UVW[(df_UVW['Grav_use'] == 'gamma') & (df_UVW['Group'].isnull())]
# df_beta_group = df_UVW[(df_UVW['Grav_use'] == 'beta') & (df_UVW['Group'].notnull())]  # Non in groups
df_beta_nogroup = df_UVW[(df_UVW['Grav_use'] == 'beta') & (df_UVW['Group'].isnull())]

# Trappist UVW
trap_U = -44.1
trap_dU = 0.1
trap_V = -67.2
trap_dV = 0.3
trap_W = 11.7
trap_dW = 0.4

trap_UW = np.sqrt(trap_U**2 + trap_W**2)
unc_trap_U2 = 2*(trap_dU/abs(trap_U))
unc_trap_W2 = 2*(trap_dW/abs(trap_W))
unc_U2_plus_W2_trap = np.sqrt(unc_trap_U2**2+unc_trap_W2**2)
final_unc_toom_trap = (1./2.)*(unc_U2_plus_W2_trap/abs(trap_UW))

#Teegarden UVW
# U [km/s] −69.46 ± 0.31 Cor16
# V [km/s] −71.17 ± 0.15 Cor16
# W [km/s] −58.68 ± 0.25 Cor16
tee_U = -69.46
tee_dU = 0.31
tee_V = -71.17
tee_dV = 0.15
tee_W = -58.68
tee_dW = 0.25

tee_UW = np.sqrt(tee_U**2 + tee_W**2)
unc_tee_U2 = 2*(tee_dU/abs(tee_U))
unc_tee_W2 = 2*(tee_dW/abs(tee_W))
unc_U2_plus_W2_tee = np.sqrt(unc_tee_U2**2+unc_tee_W2**2)
final_unc_toom_tee = (1./2.)*(unc_U2_plus_W2_tee/abs(tee_UW))

#LHS 132 U,V,W, dU,dV,dW
# -22.363629       37.042244      -68.081299       1.2497961       1.2475648      0.94968432
LHS_U = -22.4
LHS_dU = 1.2
LHS_V = 37.
LHS_dV = 1.2
LHS_W = -68.08
LHS_dW = 0.95

LHS_UW = np.sqrt(LHS_U**2 + LHS_W**2)
unc_LHS_U2 = 2*(LHS_dU/abs(LHS_U))
unc_LHS_W2 = 2*(LHS_dW/abs(LHS_W))
unc_U2_plus_W2_LHS = np.sqrt(unc_LHS_U2**2+unc_LHS_W2**2)
final_unc_toom_LHS = (1./2.)*(unc_U2_plus_W2_LHS/abs(LHS_UW))

# ------------------------------------------------------------------------------------
# -------------------------------- Plot: Toomre -------------------------------------
# ------------------------------------------------------------------------------------
fig = plt.figure()
ax1 = fig.add_subplot(111)
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)
fig.set_size_inches(10, 6.45)
plt.xlim([-80, 40])
plt.ylim([0, 100])

# ------Tick size and Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.ylabel('$(U^2 + W^2)^{(1/2)}$ (km/s)', fontsize=25)
plt.xlabel('$V$ (km/s)', fontsize=25)
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)

#  ---------- add data -------------
# gamma group
gamma_in = plt.scatter(df_gamma_group['V'], df_gamma_group['UW'],  color='white', edgecolors='#9B0132', s=70)
ax1.errorbar( df_gamma_group['V'], df_gamma_group['UW'], xerr=df_gamma_group['dV'],yerr=df_gamma_group['UW_err'], c='#9B0132',
             fmt='o', mfc='white')
# gamma non
gamma_out = plt.scatter(df_gamma_nogroup['V'], df_gamma_nogroup['UW'], color='#9B0132', s=70, marker="o")
ax1.errorbar( df_gamma_nogroup['V'], df_gamma_nogroup['UW'], xerr=df_gamma_nogroup['dV'], yerr=df_gamma_nogroup['UW_err'],
             c='#9B0132', fmt='o')
# beta non
beta_out = plt.scatter(df_beta_nogroup['V'], df_beta_nogroup['UW'],  color='#FF6B03', s=70)
ax1.errorbar( df_beta_nogroup['V'], df_beta_nogroup['UW'], xerr=df_beta_nogroup['dV'],yerr=df_beta_nogroup['UW_err'],
             c='#FF6B03', fmt='o')
# TRAPPIST-1
trappist = plt.scatter(trap_V, trap_UW, color='k', s=600, marker='*')
ax1.errorbar(trap_V, trap_UW, xerr=trap_dV,yerr=final_unc_toom_trap, c='k', fmt='o')

# Teegarden's Star
teegarden = plt.scatter(tee_V, tee_UW, color='k', s=150, marker='s')
ax1.errorbar(tee_V, tee_UW, xerr=tee_dV,yerr=final_unc_toom_tee, c='k', fmt='o')

# LHS132
LHS_132 = plt.scatter(LHS_V, LHS_UW, color='k', s=150, marker='o')
ax1.errorbar(LHS_V, LHS_UW, xerr=LHS_dV,yerr=final_unc_toom_LHS, c='k', fmt='o')

circle=plt.Circle((0,0),50, color='k', fill=False, linestyle='--')
circle2=plt.Circle((0,0),70, color='k', fill=False, linestyle='--')
ax1.add_artist(circle)
ax1.add_artist(circle2)

plt.legend([gamma_in, gamma_out, beta_out, trappist, teegarden, LHS_132], ['$\gamma$ in group', '$\gamma$ not in group',
                                                       '$\\beta$ not in group', 'TRAPPIST-1', "Teegarden's Star",
                                                        "LHS 132"],
           frameon=False,fontsize=12, loc=4)
plt.tight_layout()
plt.savefig('Figures/UW_vs_V.pdf')
