# ecef_to_eci.py
#
# Usage: python3 ecef_to_eci.py year month day hour minute second ecef_x_km ecef_y_km ecef_z_km
#  Text explaining script usage
# Parameters:
# year
# month
# day
# hour
# minute
# second
# ecef_x_km
# ecef_y_km
# ecef_x_km
# Output:
#  ECI coordinates
#
# Written by Sean Rockett
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys # argv
import math

# "constants"
# e.g., R_E_KM = 6378.137
w = 7.292115*10**(-5)

# helper functions

## function description
# def calc_something(param1, param2):
#   pass

# initialize script arguments
year = 'nan' # description of argument 1
month = 'nan' # description of argument 2
day = 'nan'
hour = 'nan'
minute = 'nan'
second = 'nan'
ecef_x_km = 'nan'
ecef_y_km = 'nan'
ecef_z_km = 'nan'

# parse script arguments
if len(sys.argv)==10:
    year = float(sys.argv[1])
    month = float(sys.argv[2])
    day = float(sys.argv[3])
    hour = float(sys.argv[4])
    minute = float(sys.argv[5])
    second = float(sys.argv[6])
    ecef_x_km = float(sys.argv[7])
    ecef_y_km = float(sys.argv[8])
    ecef_z_km = float(sys.argv[9])
else:
    print(\
    'Usage: '\
    'python3 eci_to_ecef.py year month day hour minute second ecef_x_km ecef_y_km ecef_z_km'\
    )
    exit()

# write script below this line

JD = day-32075+1461*(year+4800+(month-14)/12)/4+367*(month-2-(month-14)/12*12)/12-3*((year+4900+(month-14)/12)/100)/4
JD_mid = JD-0.5
D_frac = (second + 60*(minute + 60*hour))/86400
jd_frac = JD + D_frac

# calculating GMST
tut1 = (jd_frac-2451545.0)/36525
GMST_sec = 67310.54841+(876600*60*60+8640184.812866)*tut1 + 0.093104*tut1**2 - 6.2*10**(-6)*tut1**3 # seconds
GMST_rad = ((GMST_sec/86400)+2*math.pi) % 2*math.pi

# calculating ECI coordinates
eci_x_km = ecef_x_km*math.cos(GMST_rad) - ecef_y_km*math.sin(GMST_rad)
eci_y_km = ecef_x_km*math.sin(GMST_rad) + ecef_y_km*math.cos(GMST_rad)
eci_z_km = ecef_z_km

# print results
print(eci_x_km)
print(eci_y_km)
print(eci_z_km)
