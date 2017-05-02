#!/usr/bin/env python
""" Test suite for Vapor Core Southbound SNMP emulator tests

    \\//
     \/apor IO
"""
import logging
import time
import unittest

from snmp_device_kills.test_snmp_device_kills import SnmpDeviceKillsTestCase
from vapor_common.test_utils import run_suite, exit_suite


def get_suite():
    """ Create an instance of the test suite for SNMP emulator tests
    """
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(SnmpDeviceKillsTestCase))
    return suite


if __name__ == '__main__':
    time.sleep(30)  # Wait for emulators to die.
    result = run_suite('test-snmp-device-kills', get_suite(), loglevel=logging.INFO)
    exit_suite(result)