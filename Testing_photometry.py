import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas dataframes  NOTE: These files use PS unc of 0.03!!!!!!
df_trap_PS = pd.read_csv('Data/Test_smooth_output/untitled_folder/PS_2306-0502 (M7.5) SED_spexified.txt', sep=" ",
                      comment='#', header=None, names=["w", "f", "err"])
df_trap_og= pd.read_csv('Data/Test_smooth_output/untitled_folder/Gaia2306-0502 (M7.5) SED_spexified.txt', sep=" ",
                      comment='#', header=None, names=["w", "f", "err"])
df_trap_all= pd.read_csv('Data/Test_smooth_output/untitled_folder/Gaia_PS_JC2306-0502 (M7.5) SED_spexified.txt', sep=" ",
                      comment='#', header=None, names=["w", "f", "err"])

df_trap_phot = pd.read_csv('Data/Gaia_PS_JC2306-0502 (M7.5) phot.txt', sep=" ", comment='#', header=None,
                           names=["w", "f", "err"])


# -------------------------------------------------------------------------------------
# ------------------- Plotting: Field Comparison of similar Lbol ----------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)  # to make sure proper size run entire code at once and change 8 to 6.45 to
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)  # match other plots on github (the size will change if done in pieces
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)

# -------- Add data -----------
ax1.loglog(df_trap_all['w'], df_trap_all['f'], c='m', zorder=3, label='PS, Gaia, J-C')
ax1.loglog(df_trap_PS['w'], df_trap_PS['f'], c='k', zorder=3, label='PS')
ax1.loglog(df_trap_og['w'], df_trap_og['f'], c='b', zorder=3, label='Johnson-Cousins')
ax1.scatter(df_trap_phot['w'], df_trap_phot['f'], c='k', s=70, zorder=6)

# ----- Set axes limits, reformat ticks -----------
plt.xlim([0.5, 2.7])
plt.ylim([1*10**(-16), 3*10**(-14)])
ax1.xaxis.set_major_formatter(ScalarFormatter())
ax1.xaxis.set_minor_formatter(ScalarFormatter())
ax1.xaxis.set_minor_locator(plt.FixedLocator([0.5, 0.7, 2, 3, 4]))
ax1.tick_params(axis='both', which='major', labelsize=20, length=8, width=1.1)
ax1.tick_params(axis='both', which='minor', labelsize=20, length=4, width=1.1)
plt.yticks(fontsize=20)

# ------ Axes Labels --------
plt.xlabel('Wavelength ($\mu m$)', fontsize=25)
plt.ylabel('Flux  ($erg\ s^{-1} cm^{-2} A^{-1}$)', fontsize=25)

plt.legend()
plt.tight_layout()
plt.savefig('Figures/Various_photometry_scaling.pdf')


# ======================================================================================================================
# -------------------------------------------------------------------------------------
# ------------------- Plotting: Will's CMDs ----------------------
# -------------------------------------------------------------------------------------
# read in the csv
df= pd.read_csv('Data/Best18_sample.tsv', header=0, sep='\t')

#Create the colors
df['g-y'] = df['PS1_g']-df['PS1_y']
df['r-i'] = df['PS1_r']-df['PS1_i']
df['r-z'] = df['PS1_r']-df['PS1_z']
df['r-y'] = df['PS1_r']-df['PS1_y']
df['i-z'] =df['PS1_i']-df['PS1_z']
df['i-y'] =df['PS1_i']-df['PS1_y']
df['i-J'] =df['PS1_i']-df['J']
df['z-y'] =df['PS1_z']-df['PS1_y']
df['z-J'] =df['PS1_z']-df['J']
df['y-J'] =df['PS1_y']-df['J']
df['y-W1'] =df['PS1_y']-df['W1']

df=df[df['Binary']== 'null']
df1 =df[(df['e_PS1gmag'] <= 0.2) & (df['e_PS1ymag'] <= 0.2)]
df2 =df[(df['e_PS1rmag'] <= 0.2) & (df['e_PS1imag'] <= 0.2)]
df3 =df[(df['e_PS1rmag'] <= 0.2) & (df['e_PS1zmag'] <= 0.2)]
df4 =df[(df['e_PS1rmag'] <= 0.2) & (df['e_PS1ymag'] <= 0.2)]
df5 =df[(df['e_PS1imag'] <= 0.2) & (df['e_PS1zmag'] <= 0.2)]
df6 =df[(df['e_PS1imag'] <= 0.2) & (df['e_PS1ymag'] <= 0.2)]
df7 =df[(df['e_PS1imag'] <= 0.2) & (df['J_err'] <= 0.2)]
df8 =df[(df['e_PS1zmag'] <= 0.2) & (df['e_PS1ymag'] <= 0.2)]
df9 =df[(df['e_PS1zmag'] <= 0.2) & (df['J_err'] <= 0.2)]
df10 =df[(df['e_PS1ymag'] <= 0.2) & (df['J_err'] <= 0.2)]
df11 =df[(df['e_PS1ymag'] <= 0.2) & (df['W1_err'] <= 0.2)]

# Split off Trappist and SPTs
trap=df[df['name']=='2MASS_J23062928-0502285']
df_0608 = df[df['name']=='2MASS_J06085283-2753583']
df_0518 = df[df['name']=='2MASS_J05184616-2756457']
M7 = df[(df['SpT-n']>= 6) & (df['SpT-n'] <= 7.9)]
M8 = df[(df['SpT-n']>= 8) & (df['SpT-n'] <= 9.9)]


# G-y
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)  # to make sure proper size run entire code at once and change 8 to 6.45 to
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)  # match other plots on github (the size will change if done in pieces
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)

# ------ Axes Labels --------
plt.xlabel('SpT', fontsize=25)
plt.ylabel('g-y', fontsize=25)

plt.scatter(df1['SpT-n'], df1['g-y'])
plt.scatter(trap['SpT-n'], trap['g-y'], marker='*', s=300)

# r-i
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)  # to make sure proper size run entire code at once and change 8 to 6.45 to
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)  # match other plots on github (the size will change if done in pieces
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)

# ------ Axes Labels --------
plt.xlabel('SpT', fontsize=25)
plt.ylabel('r-i', fontsize=25)

plt.scatter(df2['SpT-n'], df2['r-i'])
plt.scatter(trap['SpT-n'], trap['r-i'], marker='*', s=300)
plt.scatter(df_0608['SpT-n'], df_0608['r-i'], marker='s', s=100)


# r-z
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)  # to make sure proper size run entire code at once and change 8 to 6.45 to
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)  # match other plots on github (the size will change if done in pieces
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)

# ------ Axes Labels --------
plt.xlabel('SpT', fontsize=25)
plt.ylabel('r-z', fontsize=25)

plt.scatter(df3['SpT-n'], df3['r-z'])
plt.scatter(trap['SpT-n'], trap['r-z'], marker='*', s=300)
plt.scatter(df_0608['SpT-n'], df_0608['r-z'], marker='s', s=100)

# r-y
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)  # to make sure proper size run entire code at once and change 8 to 6.45 to
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)  # match other plots on github (the size will change if done in pieces
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)

# ------ Axes Labels --------
plt.xlabel('SpT', fontsize=25)
plt.ylabel('r-y', fontsize=25)

plt.scatter(df4['SpT-n'], df4['r-y'])
plt.scatter(trap['SpT-n'], trap['r-y'], marker='*', s=300)
plt.scatter(df_0608['SpT-n'], df_0608['r-y'], marker='s', s=100)


# i-z
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)  # to make sure proper size run entire code at once and change 8 to 6.45 to
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)  # match other plots on github (the size will change if done in pieces
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)

# ------ Axes Labels --------
plt.xlabel('SpT', fontsize=25)
plt.ylabel('i-z', fontsize=25)

plt.scatter(df5['SpT-n'], df5['i-z'])
plt.scatter(trap['SpT-n'], trap['i-z'], marker='*', s=300)
plt.scatter(df_0608['SpT-n'], df_0608['i-z'], marker='s', s=100)
plt.scatter(df_0518['SpT-n'], df_0518['i-z'], marker='^', s=100)

# i-y
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)  # to make sure proper size run entire code at once and change 8 to 6.45 to
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)  # match other plots on github (the size will change if done in pieces
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)

# ------ Axes Labels --------
plt.xlabel('SpT', fontsize=25)
plt.ylabel('i-y', fontsize=25)

plt.scatter(df6['SpT-n'], df6['i-y'])
plt.scatter(trap['SpT-n'], trap['i-y'], marker='*', s=300)
plt.scatter(df_0608['SpT-n'], df_0608['i-y'], marker='s', s=100)
plt.scatter(df_0518['SpT-n'], df_0518['i-y'], marker='^', s=100)

# i-J
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)  # to make sure proper size run entire code at once and change 8 to 6.45 to
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)  # match other plots on github (the size will change if done in pieces
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)

# ------ Axes Labels --------
plt.xlabel('SpT', fontsize=25)
plt.ylabel('i-J', fontsize=25)

plt.scatter(df7['SpT-n'], df7['i-J'])
plt.scatter(trap['SpT-n'], trap['i-J'], marker='*', s=300)
plt.scatter(df_0608['SpT-n'], df_0608['i-J'], marker='s', s=100)
plt.scatter(df_0518['SpT-n'], df_0518['i-J'], marker='^', s=100)

# z-y
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)  # to make sure proper size run entire code at once and change 8 to 6.45 to
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)  # match other plots on github (the size will change if done in pieces
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)

# ------ Axes Labels --------
plt.xlabel('SpT', fontsize=25)
plt.ylabel('z-y', fontsize=25)

plt.scatter(df8['SpT-n'], df8['z-y'])
plt.scatter(trap['SpT-n'], trap['z-y'], marker='*', s=300)
plt.scatter(df_0608['SpT-n'], df_0608['z-y'], marker='s', s=100)
plt.scatter(df_0518['SpT-n'], df_0518['z-y'], marker='^', s=100)

# z-J
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)  # to make sure proper size run entire code at once and change 8 to 6.45 to
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)  # match other plots on github (the size will change if done in pieces
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)

# ------ Axes Labels --------
plt.xlabel('SpT', fontsize=25)
plt.ylabel('z-J', fontsize=25)

plt.scatter(df9['SpT-n'], df9['z-J'])
plt.scatter(trap['SpT-n'], trap['z-J'], marker='*', s=300)
plt.scatter(df_0608['SpT-n'], df_0608['z-J'], marker='s', s=100)
plt.scatter(df_0518['SpT-n'], df_0518['z-J'], marker='^', s=100)

# y-J
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)  # to make sure proper size run entire code at once and change 8 to 6.45 to
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)  # match other plots on github (the size will change if done in pieces
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)

# ------ Axes Labels --------
plt.xlabel('SpT', fontsize=25)
plt.ylabel('y-J', fontsize=25)

plt.scatter(df10['SpT-n'], df10['y-J'])
plt.scatter(trap['SpT-n'], trap['y-J'], marker='*', s=300)
plt.scatter(df_0608['SpT-n'], df_0608['y-J'], marker='s', s=100)
plt.scatter(df_0518['SpT-n'], df_0518['y-J'], marker='^', s=100)

# y-W1
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)  # to make sure proper size run entire code at once and change 8 to 6.45 to
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)  # match other plots on github (the size will change if done in pieces
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)

# ------ Axes Labels --------
plt.xlabel('SpT', fontsize=25)
plt.ylabel('y-W1', fontsize=25)

plt.scatter(df11['SpT-n'], df11['y-W1'])
plt.scatter(trap['SpT-n'], trap['y-W1'], marker='*', s=300)
plt.scatter(df_0608['SpT-n'], df_0608['y-W1'], marker='s', s=100)
plt.scatter(df_0518['SpT-n'], df_0518['y-W1'], marker='^', s=100)

# -----------------------------------------------------------------------
# ----------------------- Color-color plots -----------------------------
# -----------------------------------------------------------------------

# z-y vs r-i
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)  # to make sure proper size run entire code at once and change 8 to 6.45 to
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)  # match other plots on github (the size will change if done in pieces
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)

# ------ Axes Labels --------
plt.xlabel('r-i', fontsize=25)
plt.ylabel('z-y', fontsize=25)

plt.scatter(df['r-i'], df['z-y'])
plt.scatter(M7['r-i'], M7['z-y'])
plt.scatter(M8['r-i'], M8['z-y'])
plt.scatter(trap['r-i'], trap['z-y'])

# Get medians for large symbols
medM8_ri = M8['r-i'].median()
medM7_ri = M7['r-i'].median()
medM8_zy = M8['z-y'].median()
medM7_zy = M7['z-y'].median()

plt.scatter(medM8_ri, medM8_zy, s=100,marker='s')
plt.scatter(medM7_ri, medM7_zy, s=100, marker='s')

# z-J vs i-z
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)  # to make sure proper size run entire code at once and change 8 to 6.45 to
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)  # match other plots on github (the size will change if done in pieces
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)

# ------ Axes Labels --------
plt.xlabel('i-z', fontsize=25)
plt.ylabel('z-J', fontsize=25)

plt.scatter(df['i-z'], df['z-J'])
plt.scatter(M7['i-z'], M7['z-J'])
plt.scatter(M8['i-z'], M8['z-J'])
plt.scatter(trap['i-z'], trap['z-J'])

# Get medians for large symbols
medM8_iz = M8['i-z'].median()
medM7_iz = M7['i-z'].median()
medM8_zJ = M8['z-J'].median()
medM7_zJ = M7['z-J'].median()

plt.scatter(medM8_iz, medM8_zJ, s=100,marker='s')
plt.scatter(medM7_iz, medM7_zJ, s=100, marker='s')

# z-y vs i-z
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)  # to make sure proper size run entire code at once and change 8 to 6.45 to
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)  # match other plots on github (the size will change if done in pieces
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)

# ------ Axes Labels --------
plt.xlabel('i-z', fontsize=25)
plt.ylabel('z-y', fontsize=25)

plt.scatter(df['i-z'], df['z-y'])
plt.scatter(M7['i-z'], M7['z-y'])
plt.scatter(M8['i-z'], M8['z-y'])
plt.scatter(trap['i-z'], trap['z-y'])

# Get medians for large symbols
medM8_iz = M8['i-z'].median()
medM7_iz = M7['i-z'].median()
medM8_zy = M8['z-y'].median()
medM7_zy = M7['z-y'].median()

plt.scatter(medM8_iz, medM8_zy, s=100,marker='s')
plt.scatter(medM7_iz, medM7_zy, s=100, marker='s')