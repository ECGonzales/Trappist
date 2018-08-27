import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------------
# ------------------- Read in Data ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas dataframes
df = pd.read_csv('Data/Young Objects with Kinematics - Sheet1.tsv', sep="\t", comment='#', header=0)
# make smaller df of only needed info
df_vtan= df[['NAME','SPT_use', 'Vtan','Best_Group', 'Total_Group_P']].copy()
df_vtan['In_group']= np.where(df_vtan['Total_Group_P']>= 90, 'in','no')

# Create gropus
df_beta_in= df_vtan[(df_vtan['SPT_use']== 'beta') & (df_vtan['In_group'] == 'in')]
df_beta_out= df_vtan[(df_vtan['SPT_use']== 'beta') & (df_vtan['In_group'] == 'no')]
df_gamma_in= df_vtan[(df_vtan['SPT_use']== 'gamma') & (df_vtan['In_group'] == 'in')]
df_gamma_out= df_vtan[(df_vtan['SPT_use']== 'gamma') & (df_vtan['In_group'] == 'no')]


# ------------------------------------------------------------------------------------
# ------------------- Plots: Beta, IN/OUT ---------------------------
# ------------------------------------------------------------------------------------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)

# ------Tick size and Axes Labels --------
plt.ylabel('Number', fontsize=25)
plt.xlabel('V$_\mathrm{tan}$ (km/s)', fontsize=25)
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xlim([-10,40])
bins = [-10,-5,0,5,10,15,20,25,30,35,40]
# bins = np.linspace(0, 40, 50)
plt.hist(df_beta_in['Vtan'], bins=bins, color='#FF6B03', edgecolor='k', alpha=0.75, label="$\\beta$ in Group")
plt.hist(df_beta_out['Vtan'], bins=bins, color='#FC1301', alpha=0.5, label="$\\beta$ not in Group")

plt.legend()
plt.tight_layout()
plt.savefig('Figures/Vtan_beta.pdf', dpi=150)

# ------------------------------------------------------------------------------------
# ------------------- Plots: Gamma, IN/OUT ---------------------------
# ------------------------------------------------------------------------------------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)

# ------Tick size and Axes Labels --------
plt.ylabel('Number', fontsize=25)
plt.xlabel('V$_\mathrm{tan}$ (km/s)', fontsize=25)
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xlim([-10,40])

plt.hist(df_gamma_in['Vtan'], bins=bins, color='#9B0132', edgecolor='k', alpha=0.75, label="$\gamma$ in Group")
plt.hist(df_gamma_out['Vtan'], bins=bins, color='#BD250E', edgecolor='k', alpha=0.5, label="$\gamma$ not in Group")

plt.legend()
plt.tight_layout()
plt.savefig('Figures/Vtan_gamma.pdf', dpi=150)
