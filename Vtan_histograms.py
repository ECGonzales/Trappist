import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


# ------------------------------------------------------------------------------------
# ------------------- Read in Data ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas dataframes
df = pd.read_csv('Data/Young Objects with Kinematics - Sheet1.tsv', sep="\t", comment='#', header=0)
# make smaller df of only needed info
df_vtan= df[['NAME', 'BEST-PI','SPT_use', 'Vtan','Best_Group', 'Total_Group_P']].copy()
df_vtan['In_group']= np.where(df_vtan['Total_Group_P']>= 90, 'in','no')

# Create gropus
df_beta_in= df_vtan[(df_vtan['SPT_use']== 'beta') & (df_vtan['In_group'] == 'in') & (df_vtan['BEST-PI'] != -100)]
df_beta_out= df_vtan[(df_vtan['SPT_use']== 'beta') & (df_vtan['In_group'] == 'no') & (df_vtan['BEST-PI'] != -100)]
df_gamma_in= df_vtan[(df_vtan['SPT_use']== 'gamma') & (df_vtan['In_group'] == 'in') & (df_vtan['BEST-PI'] != -100)]
df_gamma_out= df_vtan[(df_vtan['SPT_use']== 'gamma') & (df_vtan['In_group'] == 'no') & (df_vtan['BEST-PI'] != -100)]


# ------------------------------------------------------------------------------------
# ------------------- Plots: Beta, IN/OUT ---------------------------
# ------------------------------------------------------------------------------------
bins = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]

fig1 = plt.figure()

# First plot
ax1 = fig1.add_subplot(121)
fig1.set_size_inches(10, 6.45)
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)

# ------Tick size and Axes Labels --------
plt.ylabel('Number', fontsize=25)
plt.xlabel('V$_\mathrm{tan}$ (km/s)', fontsize=25)
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xlim([0, 100])
plt.ylim(0,8)

# bins = np.linspace(0, 40, 50)
plt.hist(df_beta_in['Vtan'], bins=bins, color='#FF6B03', edgecolor='k', alpha=0.75, label="$\\beta$ in Group")

# Create the second plot
ax2 = fig1.add_subplot(122)
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax2.spines[axis].set_linewidth(1.1)

plt.ylabel('Number', fontsize=25)
plt.xlabel('V$_\mathrm{tan}$ (km/s)', fontsize=25)
ax2.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xlim([0, 100])
plt.ylim([0, 10.5])

plt.hist(df_beta_out['Vtan'], bins=bins, color='#FC1301', edgecolor='k', alpha=0.75, label="$\\beta$ not in Group")

ax1.legend(fontsize=15)
ax2.legend(fontsize=15)
plt.tight_layout()
plt.savefig('Figures/Vtan_beta.pdf', dpi=150)

# ------------------------------------------------------------------------------------
# ------------------- Plots: Gamma, IN/OUT ---------------------------
# ------------------------------------------------------------------------------------
fig2 = plt.figure()

# ------- Create the first plot --------
ax1 = fig2.add_subplot(121)
fig2.set_size_inches(10, 6.45)
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)

# ------Tick size and Axes Labels --------
plt.ylabel('Number', fontsize=25)
plt.xlabel('V$_\mathrm{tan}$ (km/s)', fontsize=25)
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
ax1.yaxis.set_major_locator(MaxNLocator(integer=True))
plt.xlim([0, 40])
plt.ylim([0, 20])

plt.hist(df_gamma_in['Vtan'], bins=bins, color='#9B0132', edgecolor='k', alpha=0.75, label="$\gamma$ in Group")

# ---------- Create the second plot --------
ax2 = fig2.add_subplot(122)
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax2.spines[axis].set_linewidth(1.1)

plt.ylabel('Number', fontsize=25)
plt.xlabel('V$_\mathrm{tan}$ (km/s)', fontsize=25)
ax2.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xlim([0, 40])
plt.ylim([0, 8.5])

plt.hist(df_gamma_out['Vtan'], bins=bins, color='#BD250E', edgecolor='k', alpha=0.75, label="$\gamma$ not \n in Group")

# legends and such
ax1.legend(loc=2,fontsize=14)
ax2.legend(loc=2,fontsize=14)
plt.tight_layout()
plt.savefig('Figures/Vtan_gamma.pdf', dpi=150)
