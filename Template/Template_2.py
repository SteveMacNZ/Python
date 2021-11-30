#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Short description of this Python module.

Longer description of this module.


This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

# Standard Fields
__author__ = "Steve McIntyre"
__authors__ = ["One developer", "And another one", "etc"]
__contact__ = "mail@example.com"
__copyright__ = "Copyright 2021, Fujitsu New Zealand"
__credits__ = ["One developer", "And another one", "etc"]
__deprecated__ = False
__email__ =  "steve.mcintyre@fujitsu.com"
__license__ = "GPLv3"
__maintainer__ = "developer"
__status__ = "Production"
__version__ = "0.0.1"
__path__ = ''

# Custom Fields
__date__ = "2021/11/26"
__description__ = 'Template Example'
__ScriptName__ = 'Template_2.py'

# ------------------------------------[Imports]--------------------------------

import os
import sys
import datetime 

# ----------------------------------[Declarations]-----------------------------
now = ''                                # Define now for get_now function


# ------------------------------------[Functions]-------------------------------
# Now Function - gets current timestamp for logging
def get_now():
    global now
    from datetime import datetime
    now = datetime.now().strftime("%Y-%m-%d: %H:%M:%S:%f")

# Another function

# ------------------------------------[Execution]-------------------------------
#? -------------------------------------[NOTES:]--------------------------------
#& Best veiwed and edited with MS VS Code with colorful comments extension
#^ logging messages using get_now function now variable
#  print (f'{now} [INFORMATION] Information Message')
#  print (f'{now} [WARNING] Warning Message')
#  print (f'{now} [ERROR] Error Message')
#? ------------------------------------------------------------------------------

# Print Header informaiton when script is run
print('# ' + '=' * 78)
print('# ' + 'ScriptName: ' + __ScriptName__)
print('# ' + 'Description: ' + __description__)
print('# ' + 'Status: ' + __status__)
print('# ' + 'Version: ' + __version__)
print('# ' + 'Date: ' + __date__)
#print('# ' + 'Maintainer: ' + __maintainer__)
print('# ' + '-' * 78)
print('# ' + 'Author: ' + __author__)
#print('# ' + 'Authors: ' + __authors__)
print('# ' + 'Email: ' + __email__)
print('# ' + '-' * 78)
print('# ' + 'Copyright: ' + __copyright__)
#print('# ' + 'Credits: ' + ', '.join(__credits__))
print('# ' + 'License: ' + __license__)
print('# ' + '=' * 78)
print ('')
print ('')

get_now()
print (f'{now} [INFORMATION] Script {__ScriptName__} Starting')

print ('')

print ('doing stuff here')

print ('')
print ('')


get_now()
print (f'{now} [INFORMATION] Script {__ScriptName__} completed')
#---------------------------------------------------------[Execution Completed]----------------------------------------------------------
