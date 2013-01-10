#!/usr/bin/env python

#--------------------------------------------------------------------------------------
## pythonFlu - Python wrapping for OpenFOAM C++ API
## Copyright (C) 2010- Alexey Petrov
## Copyright (C) 2009-2010 Pebble Bed Modular Reactor (Pty) Limited (PBMR)

## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
## 
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.

## See http://sourceforge.net/projects/pythonflu
##
## Author : Alexey Petrov
##


#--------------------------------------------------------------------------------------
def choose_proper_pythonflu( requires ):
    import pkg_resources
    for req in requires:
       try:
           pkg_resources.require( req )
           return [ req ]
       except pkg_resources.DistributionNotFound :
           pass
       pass
    print "There are no proper pythonFlu installation available"
    print "To use this solver one of the following pythonFlu versions have to be installed - %s" %requires
    import os; os._exit( os.EX_OK )
    pass


#--------------------------------------------------------------------------------------
from setuptools import setup, find_packages

setup( name = "rhoPorousSimpleFlux",
       description = 'Python front-end of the rhoPorousSimpleFoam',
       author = 'Alexey Petrov',
       author_email = 'alexey.petrov.nnov@gmail.com', 
       license = 'GPL',
       url = 'http://sourceforge.net/projects/pythonFlu',
       install_requires = choose_proper_pythonflu( [ "pythonflu==9.1-SWIG-1.6-ext-dev", "Foam >=8.2-hybrid" ] ),
       platforms = [ 'linux' ],
       version = "1.3",
       classifiers = [ 'Development Status :: 3 - Alpha',
                       'Environment :: Console',
                       'Intended Audience :: Science/Research',
                       'License :: OSI Approved :: GNU General Public License (GPL)',
                       'Operating System :: POSIX',
                       'Programming Language :: Python',
                       'Topic :: Scientific/Engineering'],
       packages = find_packages(),
       entry_points = { 'console_scripts': [
           'rhoPorousSimpleFlux = rhoPorousSimpleFlux:entry_point'] },
       zip_safe = True )


#--------------------------------------------------------------------------------------

