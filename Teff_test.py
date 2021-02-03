import numpy as np
import astropy.units as q, astropy.constants as ac
import pandas as pd

def get_teff(Lbol, sig_Lbol, r, sig_r):
    """
  Returns the effective temperature in Kelvin given the bolometric luminosity, radius, and uncertanties.

  Parameters
  ----------
  Lbol: astropy.quantity
    The bolometric luminosity in solar units
  sig_Lbol: astropy.quantity
    The uncertainty in the bolometric luminosity
  r: astropy.quantity
    The radius of the source in units of R_Jup
  sig_r: astropy.quantity
    The uncertainty in the radius

  Returns
  -------
  The effective temperature and uncertainty in Kelvin

  """
    # Lbol, r = (ac.L_sun*10**Lbol).to(q.W) if solar_units else Lbol, ac.R_jup*r
    # sig_Lbol, sig_r = (ac.L_sun*sig_Lbol/(Lbol*np.log(10))).to(q.W) if solar_units else sig_Lbol, ac.R_jup*sig_r
    # Convert R_jup to meters
    r, sig_r = ac.R_jup * r, ac.R_jup * sig_r
    # Get Lbol into watts: take out of log and convert to Watts
    Lbol_watt=10**(Lbol)*ac.L_sun
    sig_Lbol_watt = Lbol_watt*np.log(10)*sig_Lbol
    T = np.sqrt(np.sqrt(((Lbol_watt)/ (4 * np.pi * ac.sigma_sb * r ** 2)).to(q.K ** 4)))
    sig_T = T * np.sqrt((sig_Lbol_watt / Lbol_watt).value** 2 + (2 * sig_r / r).value ** 2) / 4. # This uses the ratio in as what comes out in SEDkit for Lbol and sig_Lbol
    return T.round(0), sig_T.round(0)


df=pd.read_csv('Data/forTeffCalc.csv', header=0, comment='#')
# Run this for all objects in TRAPPIST-1 paper
df['Teff'],df['sig_Teff']=get_teff(df['Lbol'].values, df['sig_Lbol'].values, df['r'].values, df['sig_r'].values)
df['Teff_sigma']=abs(df['Teff'][0]-df['Teff'])/(df['sig_Teff'][0]+ df['sig_Teff'])
df['Lbol_sigma']=abs(df['Lbol'][0]-df['Lbol'])/(df['sig_Lbol'][0]+ df['sig_Lbol'])
df

df.to_csv("Data/Trappist-paper_proper_Teffs.txt",columns=['Name', 'Lbol', 'sig_Lbol', 'r', 'sig_r', 'Teff', 'sig_Teff',
                                                          'Teff_sigma', 'Lbol_sigma'], index=False)

# Double checking the math so that it is correct
# u'Lbol_W': < Quantity 2.0591196911096768e+30 erg / s >,
# u'Lbol_W_unc': < Quantity 1.9369713898590036e+29 erg / s >,
# u'fbol': < Quantity 5.132081041976383e-12erg / (cm2 s) >,
# u'fbol_unc': < Quantity 5.787548446132412e-14erg / (cm2 s) >,
# u'd': < Quantity 57.908 pc >,  1.78704088e+20 cm
# u'd_unc': < Quantity 2.704 pc >, 8.344544000000001e+18
#
# <Quantity 2.0592509731978307e+23 W>
# <Quantity 8.422336480379127e+21 W>
#
# L_Sun= 3.846e+26 W
# 1 ergs/second = 1.0E-7 watts
# 1pc = 3.086e+18 cm