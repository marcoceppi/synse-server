#!/usr/bin/env python
""" OpenDCRE Southbound Redfish Endpoint Tests

    Author: Morgan Morley Mills, based off IPMI tests by Erick Daniszewski
    Date:   02/06/2017

    \\//
     \/apor IO
"""

import unittest

from opendcre_southbound.tests.test_config import PREFIX
from vapor_common import http
from vapor_common.errors import VaporHTTPError


class RedfishScanAllTestCase(unittest.TestCase):
    """ Test scan all with the Redfish emulator running
    """
    def test_01_scan_all(self):
        """ Test the OpenDCRE scan all endpoint.
        """
        r = http.get(PREFIX + '/scan')
        self.assertTrue(http.request_ok(r.status_code))

        response = r.json()
        self.assertIsInstance(response, dict)
        self.assertIn('racks', response)

        racks = response['racks']
        self.assertIsInstance(racks, list)
        self.assertEqual(len(racks), 1)

        rack = racks[0]
        self.assertIsInstance(rack, dict)
        self.assertIn('rack_id', rack)
        self.assertEqual(rack['rack_id'], 'rack_1')
        self.assertIn('boards', rack)

        boards = rack['boards']
        self.assertIsInstance(boards, list)
        self.assertEqual(len(boards), 1)

        board = boards[0]
        self.assertIsInstance(board, dict)
        self.assertIn('board_id', board)
        self.assertEqual(board['board_id'], '70000000')
        self.assertIn('ip_addresses', board)
        self.assertEqual(board['ip_addresses'], ['redfish-emulator'])
        self.assertIn('hostnames', board)
        self.assertEqual(board['hostnames'], ['redfish-emulator'])
        self.assertIn('devices', board)

        devices = board['devices']
        self.assertIsInstance(devices, list)
        self.assertEqual(len(devices), 11)

        device_types = [
            'power', 'system', 'led', 'voltage', 'fan_speed', 'temperature', 'power_supply'
        ]

        for device in devices:
            self.assertIsInstance(device, dict)
            self.assertIn('device_type', device)
            self.assertIn('device_id', device)

            dev_type = device['device_type']
            self.assertIn(dev_type.lower(), device_types)

    def test_02_scan_all(self):
        """ Test the OpenDCRE force scan endpoint.
        """
        r = http.get(PREFIX + '/scan/force')
        self.assertTrue(http.request_ok(r.status_code))

        response = r.json()
        self.assertIsInstance(response, dict)
        self.assertIn('racks', response)

        racks = response['racks']
        self.assertIsInstance(racks, list)
        self.assertEqual(len(racks), 1)

        rack = racks[0]
        self.assertIsInstance(rack, dict)
        self.assertIn('rack_id', rack)
        self.assertEqual(rack['rack_id'], 'rack_1')
        self.assertIn('boards', rack)

        boards = rack['boards']
        self.assertIsInstance(boards, list)
        self.assertEqual(len(boards), 1)

        board = boards[0]
        self.assertIsInstance(board, dict)
        self.assertIn('board_id', board)
        self.assertEqual(board['board_id'], '70000000')
        self.assertIn('ip_addresses', board)
        self.assertEqual(board['ip_addresses'], ['redfish-emulator'])
        self.assertIn('hostnames', board)
        self.assertEqual(board['hostnames'], ['redfish-emulator'])
        self.assertIn('devices', board)

        devices = board['devices']
        self.assertIsInstance(devices, list)
        self.assertEqual(len(devices), 11)

        device_types = [
            'power', 'system', 'led', 'voltage', 'fan_speed', 'temperature', 'power_supply'
        ]

        for device in devices:
            self.assertIsInstance(device, dict)
            self.assertIn('device_type', device)
            self.assertIn('device_id', device)

            dev_type = device['device_type']
            self.assertIn(dev_type.lower(), device_types)