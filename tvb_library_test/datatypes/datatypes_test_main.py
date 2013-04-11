# -*- coding: utf-8 -*-
#
#
# TheVirtualBrain-Framework Package. This package holds all Data Management, and 
# Web-UI helpful to run brain-simulations. To use it, you also need do download
# TheVirtualBrain-Scientific Package (for simulators). See content of the
# documentation-folder for more details. See also http://www.thevirtualbrain.org
#
# (c) 2012-2013, Baycrest Centre for Geriatric Care ("Baycrest")
#
# This program is free software; you can redistribute it and/or modify it under 
# the terms of the GNU General Public License version 2 as published by the Free
# Software Foundation. This program is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public
# License for more details. You should have received a copy of the GNU General 
# Public License along with this program; if not, you can download it here
# http://www.gnu.org/licenses/old-licenses/gpl-2.0
#
#
"""
Created on Mar 20, 2013

.. moduleauthor:: Bogdan Neacsa <bogdan.neacsa@codemart.ro>
"""
if __name__ == "__main__":
    from tvb_library_test import setup_test_console_env
    setup_test_console_env()
    
import unittest

# Import just to test for any runtime/syntax erros
import tvb.datatypes.api_datatypes

from tvb_library_test.datatypes import arrays_test
from tvb_library_test.datatypes import connectivity_test
from tvb_library_test.datatypes import coupling_test
from tvb_library_test.datatypes import equations_test
from tvb_library_test.datatypes import graph_test
from tvb_library_test.datatypes import lookup_tables_test
from tvb_library_test.datatypes import mode_decompositions_test
from tvb_library_test.datatypes import patterns_test
from tvb_library_test.datatypes import projections_test
from tvb_library_test.datatypes import sensors_test
from tvb_library_test.datatypes import spectral_test
from tvb_library_test.datatypes import surfaces_test
from tvb_library_test.datatypes import temporal_correlations_test
from tvb_library_test.datatypes import timeseries_test
from tvb_library_test.datatypes import volumes_test


def suite():
    """
    Gather all the tests in a test suite.
    """
    test_suite = unittest.TestSuite()
    test_suite.addTest(arrays_test.suite())
    test_suite.addTest(connectivity_test.suite())
    test_suite.addTest(coupling_test.suite())
    test_suite.addTest(equations_test.suite())
    test_suite.addTest(graph_test.suite())
    test_suite.addTest(lookup_tables_test.suite())
    test_suite.addTest(mode_decompositions_test.suite())
    test_suite.addTest(patterns_test.suite())
    test_suite.addTest(projections_test.suite())
    test_suite.addTest(sensors_test.suite())
    test_suite.addTest(spectral_test.suite())
    test_suite.addTest(surfaces_test.suite())
    test_suite.addTest(temporal_correlations_test.suite())
    test_suite.addTest(timeseries_test.suite())
    test_suite.addTest(volumes_test.suite())
    return test_suite


if __name__ == "__main__":
    #So you can run tests from this package individually.
    TEST_RUNNER = unittest.TextTestRunner()
    TEST_SUITE = suite()
    TEST_RUNNER.run(TEST_SUITE)