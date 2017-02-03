# -*- coding: utf-8 -*-
import os
from unittest import TestCase

from nose.tools import assert_equal
from nose.tools import assert_greater
from nose.tools import assert_is_instance

from networkapiclient.ClientFactory import ClientFactory

NETWORKAPI_URL = os.getenv('NETWORKAPI_URL', 'http://10.0.0.2:8000/')
NETWORKAPI_USER = os.getenv('NETWORKAPI_USER', 'networkapi')
NETWORKAPI_PWD = os.getenv('NETWORKAPI_PWD', 'networkapi')


class TestNetworkIPv6(TestCase):

    """ Class that tests IPv6 networks creation """

    def setUp(self):
        self.client = ClientFactory(NETWORKAPI_URL, NETWORKAPI_USER,
                                    NETWORKAPI_PWD)
        self.api_net_ipv6 = self.client.create_api_network_ipv6()

    def test_list_networks(self):
        """ List all IPv6 networks """

        networks = self.api_net_ipv6.list()

        assert_is_instance(networks, list)
        assert_greater(len(networks), 1)

    def test_create_new_ipv6_network(self):
        """ Create a new IPv6 network """
        data = {
            'vlan': 9,
            'network_type': 2,
            'environmentvip': None,
        }

        network_id = self.api_net_ipv6.create([data])[0]['id']
        network = self.api_net_ipv6.get([network_id])['networks'][0]

        assert_is_instance(network, dict)
        assert_equal(network['vlan'], data['vlan'])

        self.api_net_ipv6.delete([network_id])

    def test_create_new_ipv6_network_by_prefix(self):
        """ Creates a new IPv6 network """

        data = {
            'vlan': 9,
            'network_type': 2,
            'environmentvip': None,
            'prefix': 62,
        }

        network_id = self.api_net_ipv6.create([data])[0]['id']
        network = self.api_net_ipv6.get([network_id])['networks'][0]

        assert_equal(network['prefix'], data['prefix'])

        self.api_net_ipv6.delete([network_id])
