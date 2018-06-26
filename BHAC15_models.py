import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

df = pd.read_csv('BHAC15.txt', sep='\s+', comment='!', header=None, names=['mass', 'Teff', 'Lbol', 'gravity', 'radius',
                                                                           'Li', 'My', 'Mz', 'Mj','Mh', 'Mk', 'age'])

# break into mass dataframes so I can plot lines of equal mass
df_10 = df[df['mass'] == 0.010]
df_15 = df[df['mass'] == 0.015]
df_20 = df[df['mass'] == 0.020]
df_30 = df[df['mass'] == 0.030]
df_40 = df[df['mass'] == 0.040]
df_50 = df[df['mass'] == 0.050]
df_60 = df[df['mass'] == 0.060]
df_70 = df[df['mass'] == 0.070]
df_72 = df[df['mass'] == 0.072]
df_75 = df[df['mass'] == 0.075]
df_80 = df[df['mass'] == 0.080]
df_90 = df[df['mass'] == 0.090]
df_100 = df[df['mass'] == 0.100]
df_200 = df[df['mass'] == 0.200]
df_300 = df[df['mass'] == 0.300]
df_400 = df[df['mass'] == 0.400]
df_500 = df[df['mass'] == 0.500]
df_600 = df[df['mass'] == 0.600]
df_700 = df[df['mass'] == 0.700]
df_800 = df[df['mass'] == 0.800]
df_900 = df[df['mass'] == 0.900]

# Figure layout
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)  # This makes sure that the labels aren't cut off
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)
ax1.xaxis.set_minor_formatter(ScalarFormatter())
ax1.xaxis.set_minor_locator(plt.FixedLocator([0.5]))


plt.plot(df_10['age'], df_10['Lbol'], label='10')
plt.plot(df_15['age'], df_15['Lbol'], label='15')
plt.plot(df_20['age'], df_20['Lbol'], label='20')
plt.plot(df_30['age'], df_30['Lbol'], label='30')
plt.plot(df_40['age'], df_40['Lbol'], label='40')
plt.plot(df_50['age'], df_50['Lbol'], label='50')
plt.plot(df_60['age'], df_60['Lbol'], label='60')
plt.plot(df_70['age'], df_70['Lbol'], label='70')
plt.plot(df_72['age'], df_72['Lbol'], label='72')
plt.plot(df_75['age'], df_75['Lbol'], label='75')
plt.plot(df_80['age'], df_80['Lbol'], label='80')
plt.plot(df_90['age'], df_90['Lbol'], label='90')
plt.plot(df_100['age'], df_100['Lbol'], label='100')
plt.plot(df_200['age'], df_200['Lbol'], label='200')

# line for Lbol of Trappist
x = pd.DataFrame()
x['x'] = [0, 10]
x['y'] = [-3.255, -3.255]
plt.plot(x['x'], x['y'], c='k', linewidth=2)

# labels and such
plt.xlim([0,10])
plt.ylim([-3.5,-3.0])
plt.xlabel('Age (Gyr)', fontsize=20)
plt.ylabel('$L_\mathrm{bol}$', fontsize=20)
plt.legend()
plt.tight_layout()


plt.savefig('Trappist_BHAC15models.png')
