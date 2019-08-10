# Code to determine the fake Photometry for the TRAPPIST-1 paper to fluff up the uncertainties.
import pandas as pd
from astrodbkit import astrodb
import numpy as np

# Load up the database ( a real and fake version)
db = astrodb.Database('/Users/eileengonzales/Dropbox/BDNYC/BDNYCdb_copy/BDNYCdevdb/bdnycdev.db')
db_fake = astrodb.Database('/Users/eileengonzales/Dropbox/BDNYC/BDNYCdb_copy/Fake_database/bdnycdev_fake.db')

# For the real database add the PS photometry for the objects of intrest Cross matching comes from Best+18
data = list()
data.append(['bibcode','shortname', 'DOI', 'description'])
data.append(['2018ApJS..234....1B','Best18', '10.3847/1538-4365/aa9982', 'Photometry and Proper Motions of M, L, and T Dwarfs from the Pan-STARRS1 3pi Survey'])
db.add_data(data, 'publications')

data = list()
data.append(['source_id', 'band', 'magnitude', 'magnitude_unc', 'publication_shortname', 'comments'])
# vb8
data.append([1371,'PS_g',17.4262, 0.0042,'Cham16'])    #17.43 0.01
data.append([1371,'PS_r',16.0220,	0.0071,'Cham16'])  #16.02 0.01
#data.append([1371,'PS_i',13.2570,	0.0049,'Cham16'])
#data.append([1371,'PS_z',12.0603,	0.0100,'Cham16'])
#data.append([1371,'PS_y',11.7421,	0.0847,'Cham16'])
# vb10
#data.append([300,'PS_g',18.2231, 0.0114,'Cham16'])
data.append([300,'PS_r',16.5893,0.0030,'Cham16']) #16.59 0.01
#data.append([300,'PS_i',13.9473,0.0011,'Cham16'])
#data.append([300,'PS_z',12.6794,0.0648,'Cham16'])
#data.append([300,'PS_y',11.7284,0.0164,'Cham16'])
#0320
data.append([320,'PS_g',19.7975,0.0292,'Cham16']) #19.80 0.03
data.append([320,'PS_r',18.2044,0.0100,'Cham16']) #18.20 0.01
data.append([320,'PS_i',15.6026,0.0073,'Cham16']) #15.60 0.01
data.append([320,'PS_z',14.2388,0.0040,'Cham16']) # 14.24 0.01
data.append([320,'PS_y',13.4329,0.0056,'Cham16']) #13.43 0.01
#LHS 3003
#Will doesn't have these at all. He has g and r 17.65	0.01	16.21	0.01
# data.append([126,'PS_i',13.4577,0.0134,'Cham16'])
# data.append([126,'PS_z',12.2627,0.0010,'Cham16'])
# data.append([126,'PS_y',11.5639,0.0010,'Cham16'])
# --- NEW ----- 2MASS J18353790+3259545
data.append([82,'PS_g',	19.0248,	0.0121,'Cham16']) #19.02 0.01
data.append([82,'PS_r',17.1756,	0.0094,'Cham16']) #17.18 0.01
# data.append([82,'PS_i',14.4478,	0.0006,'Cham16'])
# data.append([82,'PS_z',12.9888,	0.0014,'Cham16'])
# data.append([82,'PS_y',12.0515,	0.0038,'Cham16'])
# None 1048-39
# --- NEW ----- 2MASS J08533619-0329321
data.append([355,'PS_g',19.7983,	0.0418,'Cham16']) #19.80 0.04
data.append([355,'PS_r',17.8464,	0.0084,'Cham16']) #17.85 0.01
data.append([355,'PS_i',15.5047,	0.0014,'Cham16']) #15.50 0.01
data.append([355,'PS_z',14.0634,	0.0047,'Cham16']) #14.06 0.01
data.append([355,'PS_y',13.1045,	0.0018,'Cham16']) #13.10 0.01
#SSSPM J1013-1356
data.append([1333,'PS_g',20.9931, 0.0730,'Cham16']) #20.99 0.07
data.append([1333,'PS_r',19.2511,0.0095,'Cham16'])  #19.25 0.01
data.append([1333,'PS_i',17.1840,0.0005,'Cham16'])  #17.18 0.01
data.append([1333,'PS_z',16.2469,0.0018,'Cham16']) #16.25 0.01
data.append([1333,'PS_y',15.9044,0.0027,'Cham16']) #15.90 0.01
# GJ660.1b
data.append([1476,'PS_y',14.40,0.018,'Best18'])
#1256
data.append([1357,'PS_r',21.7783,0.1857,'Cham16'])
data.append([1357,'PS_i',19.4728,0.0448,'Cham16']) #19.47 0.04
data.append([1357,'PS_z',18.0028,0.0264,'Cham16']) #18.00 0.03
data.append([1357,'PS_y',17.5395,0.0120,'Cham16']) #17.54 0.01
#1444
data.append([1454,'PS_r',19.31,0.03,'Best18'])
data.append([1454,'PS_i',16.09,0.05,'Best18'])
data.append([1454,'PS_y',14.06,0.02,'Best18'])
# Non 1247-38
#0608
data.append([413,'PS_r',20.9394,0.0241,'Cham16']) #20.94 0.02
data.append([413,'PS_i',18.1406,0.0037,'Cham16']) #18.14 0.01
data.append([413,'PS_z',16.5489,0.0055,'Cham16']) #16.55 0.01
data.append([413,'PS_y',15.5418,0.0067,'Cham16']) #15.54 0.01
# none 2000-75
#none 1207-39
#0443+0002 -- ADDED         #WILL: 21.51	0.07	19.66	0.02	16.96	0.01	15.38	0.01	14.40	0.01
# 0518
#data.append([91,'PS_r',21.8871,	0.1550,'Cham16'])
data.append([91,'PS_i',19.9933,	0.0232,'Cham16']) #19.99	0.02	18.49	0.01	17.50	0.01
data.append(['source_id', 'band', 'magnitude', 'magnitude_unc', 'publication_shortname', 'comments'])
data.append([91,'PS_z',18.49,	0.01,'Cham16', 'Best18 unc'])
data.append([91,'PS_y',17.50,	0.01,'Cham16', 'Best18 unc'])
#None 2235-59
#0714
data.append([849,'PS_g',20.1524,	0.0257,'Cham16']) #20.15	0.03	18.61	0.01	15.86	0.01	14.48	0.01	13.66	0.01
data.append([849,'PS_r',18.6059,	0.0085,'Cham16'])
data.append([849,'PS_i',15.8585,	0.0021,'Cham16'])
data.append([849,'PS_z',14.4771,	0.0049,'Cham16'])
data.append([849,'PS_y',13.6642,	0.0027,'Cham16'])
#0953
data.append([415,'PS_r',20.4710,	0.0282,'Cham16']) #20.47	0.03	18.00	0.01	16.47	0.01	15.44	0.01
data.append([415,'PS_i',17.9995,	0.0044,'Cham16'])
data.append([415,'PS_z',16.4657,	0.0028,'Cham16'])
data.append([415,'PS_y',15.4396,	0.0048,'Cham16'])
#2352
data.append([146,'PS_g',20.5741,	0.0248,'Cham16']) #20.57	0.02	19.18	0.01	16.49	0.01	15.23	0.01	14.49	0.01
data.append([146,'PS_r',19.1830,	0.0142,'Cham16'])
data.append([146,'PS_i',16.4937,	0.0019,'Cham16'])
data.append([146,'PS_z',15.2285,	0.0019,'Cham16'])
data.append([146,'PS_y',14.4897,	0.0022,'Cham16'])
#2341
data.append([669,'PS_g',21.1287,	0.0323,'Cham16'])  # These are not in Will's paper at all. Keep???? I kept and updated uncs
data.append([669,'PS_r',19.8407,	0.0181,'Cham16'])
data.append([669,'PS_i',17.1363,	0.0025,'Cham16'])
data.append([669,'PS_z',15.8644,	0.0024,'Cham16'])
data.append([669,'PS_y',15.1312,	0.0049,'Cham16'])
#None ---LHS 132
#0532
data.append([1304,'PS_z',18.0747,	0.0096,'Cham16']) # 18.07	0.01	16.92	0.03
data.append([1304,'PS_y',16.9173,	0.0260,'Cham16'])
# LHS 377
data.append([1452,'PS_g',18.9919, 0.0124,'Cham16']) #18.99	0.02	17.69	0.01	15.68	0.01	14.84	0.01	14.48	0.01
data.append([1452,'PS_r',17.6872,0.0116,'Cham16'])
data.append([1452,'PS_i',15.5951,0.0140,'Cham16'])
data.append([1452,'PS_z',14.8256,0.0027,'Cham16'])
data.append([1452,'PS_y',14.4663,0.0129,'Cham16'])
#1610
data.append([1591,'PS_g',20.1155,	0.0963,'Cham16']) #20.12	0.10	18.08	0.01	15.90	0.01	14.86	0.01	14.41	0.02
data.append([1591,'PS_r',18.0825,	0.0037,'Cham16'])
data.append([1591,'PS_i',15.8974,	0.0007,'Cham16'])
data.append([1591,'PS_z',14.8636,	0.0058,'Cham16'])
data.append([1591,'PS_y',14.4070,	0.0154,'Cham16'])
data.append([1592,'PS_g',20.1155,	0.0963,'Cham16'])
data.append([1592,'PS_r',18.0825,	0.0037,'Cham16'])
data.append([1592,'PS_i',15.8974,	0.0007,'Cham16'])
data.append([1592,'PS_z',14.8636,	0.0058,'Cham16'])
data.append([1592,'PS_y',14.4070,	0.0154,'Cham16'])
#2036
data.append([1490,'PS_g',19.6098,	0.0150,'Cham16']) #19.61	0.02	18.14	0.01	16.13	0.01	15.24	0.01	14.89	0.01
data.append([1490,'PS_r',18.1371,	0.0092,'Cham16'])
data.append([1490,'PS_i',16.1318,	0.0012,'Cham16'])
data.append([1490,'PS_z',15.2421,	0.0040,'Cham16'])
data.append([1490,'PS_y',14.8904,	0.0074,'Cham16'])

db.add_data(data, 'photometry')
db.add_changelog('Eileen Gonzales', 'Photometry', 'Added PS photometry for TRAPPIST-1 Referee report')
# ---------Save and pr before moving on. Move tabledata over. ----------
 # ---------- HERE IS Where I need to pick up for new values -----
# Then query the real db to create individual dataframes of the photometry for each source
x_1371 = db.query("Select source_id, band, magnitude, magnitude_unc from photometry where source_id=1371", fmt='pandas')
x_300 = db.query("Select source_id, band, magnitude, magnitude_unc from photometry where source_id=300", fmt='pandas')
#x_300 = x_300.drop(x_300['magnitude_unc']=="None")
x_320 = db.query("Select source_id, band, magnitude, magnitude_unc from photometry where source_id=320", fmt='pandas')
#x_320 = x_320.drop(16) # drop by index
x_126 = db.query("Select source_id, band, magnitude, magnitude_unc from photometry where source_id=126", fmt='pandas')
x_82 = db.query("Select source_id, band, magnitude, magnitude_unc from photometry where source_id=82", fmt='pandas')
x_130 = db.query("Select source_id, band, magnitude, magnitude_unc from photometry where source_id=130", fmt='pandas')
#x_130 = x_130.drop([3,4,5])
x_355 = db.query("Select source_id, band, magnitude, magnitude_unc from photometry where source_id=355", fmt='pandas')
#x_355 = x_355.drop(14)
x_1333 = db.query("Select source_id, band, magnitude, magnitude_unc from photometry where source_id=1333", fmt='pandas')
#x_1333 = x_1333.drop(6)
x_1476 = db.query("Select source_id, band, magnitude, magnitude_unc from photometry where source_id=1476", fmt='pandas')
x_1357 = db.query("Select source_id, band, magnitude, magnitude_unc from photometry where source_id=1357", fmt='pandas')
#x_1357 = x_1357.drop([5,8,9])
x_1454 = db.query("Select source_id, band, magnitude, magnitude_unc from photometry where source_id=1454", fmt='pandas')
#x_1454 = x_1454.drop(6)
x_1940 = db.query("Select source_id, band, magnitude, magnitude_unc from photometry where source_id=1940", fmt='pandas')
x_413 = db.query("Select source_id, band, magnitude, magnitude_unc from photometry where source_id=413", fmt='pandas')
#x_413 = x_413.drop(6)
x_759 = db.query("Select source_id, band, magnitude, magnitude_unc from photometry where source_id=759", fmt='pandas')
x_475 = db.query("Select source_id, band, magnitude, magnitude_unc from photometry where source_id=475", fmt='pandas')
x_1928 = db.query("Select source_id, band, magnitude, magnitude_unc from photometry where source_id=1928", fmt='pandas')
x_751 = db.query("Select source_id, band, magnitude, magnitude_unc from photometry where source_id=751", fmt='pandas')
#x_751= x_751.drop(0)
x_91 = db.query("Select source_id, band, magnitude, magnitude_unc from photometry where source_id=91", fmt='pandas')
x_2107 = db.query("Select source_id, band, magnitude, magnitude_unc from photometry where source_id=2107", fmt='pandas')
x_849 = db.query("Select source_id, band, magnitude, magnitude_unc from photometry where source_id=849", fmt='pandas')
x_415 = db.query("Select source_id, band, magnitude, magnitude_unc from photometry where source_id=415", fmt='pandas')
x_146 = db.query("Select source_id, band, magnitude, magnitude_unc from photometry where source_id=146", fmt='pandas')
#x_146=x_146.drop(0)
x_669 = db.query("Select source_id, band, magnitude, magnitude_unc from photometry where source_id=669", fmt='pandas')
x_107 = db.query("Select source_id, band, magnitude, magnitude_unc from photometry where source_id=107", fmt='pandas')
x_1304 = db.query("Select source_id, band, magnitude, magnitude_unc from photometry where source_id=1304", fmt='pandas')
x_1452 = db.query("Select source_id, band, magnitude, magnitude_unc from photometry where source_id=1452", fmt='pandas')
#x_1452 = x_1452.drop(16)
x_1591 = db.query("Select source_id, band, magnitude, magnitude_unc from photometry where source_id=1591", fmt='pandas')
#x_1591 = x_1591.drop(9)
x_1490 = db.query("Select source_id, band, magnitude, magnitude_unc from photometry where source_id=1490", fmt='pandas')

# Concatenate queries into one dataframe
df = pd.concat([x_1371, x_300, x_320, x_126, x_82, x_130, x_355, x_1333, x_1476, x_1357, x_1454, x_1940, x_413, x_759,
               x_475, x_1928, x_751, x_91, x_2107, x_849, x_415, x_146, x_669, x_107, x_1304, x_1452, x_1591, x_1490],
               ignore_index=True)
# Drop the upper limits
df = df.dropna()

# Add columns for upper and lower limits and uncertainites, make sure all are floats and round to 4 decimals
df['Upper'] = df['magnitude'] + df['magnitude_unc']
df['Upper_unc'] = df['magnitude_unc']
df['Lower'] = df['magnitude'] - df['magnitude_unc']
df['Lower_unc'] = df['magnitude_unc']
df['pub'] = 'Missing'
df['comments'] = 'Fake Upper'
df['comments1'] = 'Fake lower'

df.Upper.astype(float)
df.Upper_unc.astype(float)
df.Lower.astype(float)
df.Lower_unc.astype(float)

decimals = 4
df['Upper'] = df['Upper'].apply(lambda x: round(x, decimals))
df['Upper_unc'] = df['Upper_unc'].apply(lambda x: round(x, decimals))
df['Lower'] = df['Lower'].apply(lambda x: round(x, decimals))
df['Lower_unc'] = df['Lower_unc'].apply(lambda x: round(x, decimals))


# write to two files for easy adding to the FAKE database to make the uppers and lowers one at a time
df.to_csv('/Users/eileengonzales/Dropbox/BDNYC/BDNYCdb_copy/Fake_database/Fake_phot_upper.txt',columns=['source_id', 'band', 'Upper', 'Upper_unc', 'pub', 'comments'], index=False)
df.to_csv('/Users/eileengonzales/Dropbox/BDNYC/BDNYCdb_copy/Fake_database/Fake_phot_lower.txt',columns=['source_id', 'band', 'Lower', 'Lower_unc', 'pub', 'comments1'], index=False)

# Now remove orginial photometry from the FAKE db and add upper/lower to FAKE database
db_fake.modify("Delete from photometry where source_id in (1371, 300, 320, 126, 82, 130, 355, 1476, 1357, 1454, 1940, \
413, 759, 475, 1928, 751, 91, 2107, 849, 415, 146, 669, 107, 1304, 1452, 1591, 1490)")

# Renmae header info to match db input and add
db_fake.add_data('Fake_database/Fake_phot_upper.txt','photometry', delimiter=',')

# Add for Trappist list of fake Upper limits
# Code to calculate upper and lower limits.
up=14.1     +    0.01
down = 14.1  -       0.01
print up, down

data  =list()
data.append(['source_id', 'band', 'magnitude', 'magnitude_unc', 'publication_shortname', 'comments'])
data.append([137, '2MASS_H', 10.739,0.021, 'Missing', 'Fake Upper'])
data.append([137, '2MASS_J', 11.376,0.022, 'Missing', 'Fake Upper'])
data.append([137, '2MASS_Ks', 10.319,0.023, 'Missing', 'Fake Upper'])
data.append([137, 'Gaia_BP', 19.046,0.048, 'Missing', 'Fake Upper'])
data.append([137, 'Gaia_RP', 14.11,0.01, 'Missing', 'Fake Upper'])
data.append([137, 'PS_g', 19.35,0.01, 'Missing', 'Fake Upper'])
data.append([137, 'PS_r', 17.8864,0.0061, 'Missing', 'Fake Upper'])
data.append([137, 'PS_i', 15.1139,0.0017, 'Missing', 'Fake Upper'])
data.append([137, 'PS_z', 13.7777,0.0126, 'Missing', 'Fake Upper'])
data.append([137, 'PS_y', 12.9933,0.0067, 'Missing', 'Fake Upper'])
data.append([137, 'WISE_W1', 10.065,0.023, 'Missing', 'Fake Upper'])
data.append([137, 'WISE_W2', 9.819,0.02, 'Missing', 'Fake Upper'])
data.append([137, 'WISE_W3', 9.569,0.041, 'Missing', 'Fake Upper'])
db_fake.add_data(data, 'photometry')

# Remove and add fake lowers
db_fake.modify("Delete from photometry where comments='Fake Upper'")

db_fake.add_data('Fake_database/Fake_phot_lower.txt','photometry', delimiter=',')
# Trapist fake lowers
data=list()
data.append(['source_id', 'band', 'magnitude', 'magnitude_unc', 'publication_shortname', 'comments'])
data.append([137, '2MASS_H', 10.697,0.021, 'Missing', 'Fake lower'])
data.append([137, '2MASS_J', 11.332,0.022, 'Missing', 'Fake lower'])
data.append([137, '2MASS_Ks', 10.273,0.023, 'Missing', 'Fake lower'])
data.append([137, 'Gaia_BP', 18.95,0.048, 'Missing', 'Fake lower'])
data.append([137, 'Gaia_RP', 14.09,0.01, 'Missing', 'Fake lower'])
data.append([137, 'PS_g', 19.3145,0.0189, 'Missing', 'Fake lower'])
data.append([137, 'PS_r', 17.8742,0.0061, 'Missing', 'Fake lower'])
data.append([137, 'PS_i', 15.1105,0.0017, 'Missing', 'Fake lower'])
data.append([137, 'PS_z', 13.7525,0.0126, 'Missing', 'Fake lower'])
data.append([137, 'PS_y', 12.9799,0.0067, 'Missing', 'Fake lower'])
data.append([137, 'WISE_W1', 10.019,0.023, 'Missing', 'Fake lower'])
data.append([137, 'WISE_W2', 9.779,0.02, 'Missing', 'Fake lower'])
data.append([137, 'WISE_W3', 9.487,0.041, 'Missing', 'Fake lower'])
db_fake.add_data(data, 'photometry')

db_fake.modify("Delete from photometry where comments='Fake lower' and source_id=137")
