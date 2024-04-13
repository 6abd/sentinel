import sys # System stuff.
import os # Operating System functions.
from colorama import Fore # For text colour.
import argparse # For adding arguments.


import etc.init.banner as banner
import sentinel.main as main

# Modules
import sentinel.apicon as apicon
# # SECURITY.
# ENUMERATION.
# OSINT.
import sentinel.modules.shodan as shodan
import sentinel.modules.numlook as numlook
import sentinel.modules.geolock as geolock
# CASE-GEN.
# SDB.
# Loki.
# FORENSICS.

# Clears screen
os.system("clear")

parser = argparse.ArgumentParser()
ap = parser.add_mutually_exclusive_group()

ap.add_argument('-apicon', help='Configure the API settings for Sentinel\n', action="store_true")
# SECURITY.
#ap.add_argument('-Torshell', help='\n', action="store_true")
#ap.add_argument('-Pvpn', help='\n', action="store_true")
#ap.add_argument('-Ovpn', help='\n', action="store_true")
# ENUMERATION.
#ap.add_argument('-Fallenflare', help='\n', action="store_true")
#ap.add_argument('-Recpull', help='\n', action="store_true")
#ap.add_argument('-Anonfile', help='\n', action="store_true")
#ap.add_argument('-Onionshare', help='\n', action="store_true")
# OSINT.
ap.add_argument('-shodan', help='Call on Loki to encrypt the home directory and pull the encryption key.\n', action="store_true")
#ap.add_argument('-wiggle', help='Use an API for SSID/BSSIDs stat, locations, & Bluetooth data.\n', action="store_true")
ap.add_argument('-numlook', help='Look up validity, carriers, names of phone numbers globally.\n', action="store_true")
ap.add_argument('-geolock', help='Shodan & auxiliary API based IP tracing & tracking.\n', action="store_true")
#ap.add_argument('-bankindex', help='Search up BIN/IIN, Sort Codes, Cheque details, etc.\n', action="store_true")
#ap.add_argument('-Mactrace', help='\n', action="store_true")
#ap.add_argument('-Flightinfo', help='\n', action="store_true")
#ap.add_argument('-Licenseinfo', help='\n', action="store_true")
#ap.add_argument('-Cryptotrace', help='\n', action="store_true")
#ap.add_argument('-Dischook', help='\n', action="store_true")
#ap.add_argument('-Ytd', help='\n', action="store_true")
#ap.add_argument('-Leverage', help='\n', action="store_true")
# CASE-GEN.
#ap.add_argument('-Casegenerate', help='\n', action="store_true")
#ap.add_argument('-Casesecure', help='\n', action="store_true")
#ap.add_argument('-Casedelete', help='\n', action="store_true")
# SDB.
#ap.add_argument('-sdb', help='Create or search through your custom sentinel database built in SQL.\n', action="store_true")
args = vars(parser.parse_args())


from io import StringIO 
import sys

class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout

if args['numlook']: # Runs the numlook program.
    while True:
        try:
                numlook.numlook()
                os._exit(0)
        except:
            print(f">_ {Fore.RED}FAILURE{Fore.WHITE}: ensare failed to run here!\n")
            os._exit(0)

if __name__ == '__main__':
    try:
        banner.banner()
        main.main_script()
    except KeyboardInterrupt:
        print(f'\n{Fore.YELLOW}You interrupted the program.{Fore.WHITE}')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
