import astropy.constants as ac
import astropy.units as q
import numpy as np
from SEDkit import SEDs
from astrodbkit import astrodb
import matplotlib.pyplot as plt

# ----- Load up the databases -------
db = astrodb.Database('/Users/eileengonzales/Dropbox/BDNYC/BDNYCdb_copy/BDNYCdevdb/bdnycdev.db')
db_fake = astrodb.Database('/Users/eileengonzales/Dropbox/BDNYC/BDNYCdb_copy/Fake_database/bdnycdev_fake.db')

# ------- Create Real SED -------
a_true = SEDs.MakeSED(137, db, spec_ids=[396, 1015],trim=[(396, 1.34, 1.48), (396,1.8,2.0),(1015,0,0.63),(1015,0.95,3)],
                      est_mags=False, pi=(80.4512,0.1211), SNR_trim=5, pop=['Johnson_V', 'Cousins_R', "Cousins_I"])


#------- Create Upper and Lower SEDs for the Uncertainties to be estimated------
# For Adding fake photometry. Text file saved from before. To make a new test file see Caluate_fake.py
db_fake.add_data('/Users/eileengonzales/Dropbox/BDNYC/BDNYCdb_copy/Fake_database/Fake_phot_upper_T.txt','photometry', delimiter=',')
# Run SED for Upper
a_up = SEDs.MakeSED(137, db_fake, spec_ids=[396, 1015],trim=[(396, 1.34, 1.48), (396,1.8,2.0),(1015,0,0.63),(1015,0.95,3)],
                    est_mags=False, pi=(80.4512,0.1211), SNR_trim=5, pop=['Johnson_V', 'Cousins_R', "Cousins_I", 'PS_y'])

#delete uppers and add lowers
db_fake.modify("Delete from photometry where comments='Fake Upper' and source_id=137")
db_fake.add_data('/Users/eileengonzales/Dropbox/BDNYC/BDNYCdb_copy/Fake_database/Fake_phot_lower_T.txt','photometry', delimiter=',')

# Run SED for Lower
a_low = SEDs.MakeSED(137, db_fake, spec_ids=[396, 1015],trim=[(396, 1.34, 1.48), (396,1.8,2.0),(1015,0,0.63),(1015,0.95,3)],
                    est_mags=False, pi=(80.4512,0.1211), SNR_trim=5, pop=['Johnson_V', 'Cousins_R', "Cousins_I", 'PS_y'])


# ------ Get the Fbol and Lbol Values in erg / (cm2 s) from the SED dictionary ----
# b.data lists all things Joe calcuates
fbol_trap= a_true.data['fbol']
fbol_lower= a_low.data['fbol']
fbol_upper= a_up.data['fbol']

Lbol_trap=a_true.data['Lbol_W']  # <Quantity 2.3396526008789738e+30 erg / s>, to get the unitless numbers np.log10(Lbol_trap/ac.L_sun)=-3.2159
Lbol_upper=a_up.data['Lbol_W']  # <Quantity 2.2063850518713438e+30 erg / s>, np.log10(Lbol_upper/ac.L_sun)=-3.2413
Lbol_lower=a_low.data['Lbol_W']  # <Quantity 2.2884199414469557e+30 erg / s>, np.log10(Lbol_lower/ac.L_sun)=-3.2255


# Get the new uncertainty in erg/s from my Lbol difference hack (unc Lbol= Lbol_upper-Lbol_lower)
Lbol_trap_unc=abs(Lbol_upper-Lbol_lower) #<Quantity 8.20348895756119e+28 erg / s>

# get the distance to use in inverting the Lbol equation
# pi2pc converts the parallax into a distance (found in utilities)
def pi2pc(parallax, parallax_unc=0, pc2pi=False):
    if parallax:
        if pc2pi:
            return ((1 * q.pc * q.arcsec) / parallax).to(q.mas), (parallax_unc * q.pc * q.arcsec / parallax ** 2).to(
                q.mas)
        else:
            pi, sig_pi = parallax * q.arcsec / 1000., parallax_unc * q.arcsec / 1000.
            d, sig_d = (1 * q.pc * q.arcsec) / pi, sig_pi * q.pc * q.arcsec / pi ** 2
            return (d.round(2), sig_d.round(2))
    else:
        return ['', '']

d, sig_d = pi2pc(80.4512,0.1211)


# Invert Lbol to get fbol
fbol_trap_der=Lbol_trap/((4*np.pi*(d.to(q.cm))**2))
# matches value from appended pickle.
# <Quantity 1.2656049507551483e-10 erg / (cm2 s)>
# fbol_trap
# Out[124]:
# <Quantity 1.265604950755148e-10 erg / (cm2 s)>

# therefore should work for unc as well
fbol_trap_unc_der=Lbol_trap_unc/((4*np.pi*(d.to(q.cm))**2))
# <Quantity 4.437571729347392e-12 erg / (cm2 s)>




