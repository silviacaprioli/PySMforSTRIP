import pysm
from pysm.nominal import models
import healpy as hp
from astropy.io import fits


#Sky configuration

nside = 256

sky_config = {
    'synchrotron': models('s1', nside),
    'dust': models('d1', nside),
    'cmb': models('c1', nside),
    #'freefree': models('f1', nside), #not polarized
    #'ame': models('a1', nside),  #not polarized 
}

#initialize sky
sky = pysm.Sky(sky_config)
signal = sky.signal()

#choose the frequency
sky_map_g = signal(nu=43)

#change units from u_K to K
sky_map_g = sky_map_g*1e-06

#rotate map from Galactic to Equatorial Coordinates
r = hp.Rotator(coord=["G", "E"])
sky_map_eq = r.rotate_map(sky_map_g)

#Save map to .fits 
hp.fitsfunc.write_map("PySM_map_nside256.fits", sky_map_eq, coord="Equatorial", column_names = ("T", "Q", "U"), column_units="K_RJ")                      