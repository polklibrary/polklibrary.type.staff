# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from polklibrary.type.staff.testing import POLKLIBRARY_TYPE_STAFF_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that polklibrary.type.staff is properly installed."""

    layer = POLKLIBRARY_TYPE_STAFF_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if polklibrary.type.staff is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('polklibrary.type.staff'))

    def test_browserlayer(self):
        """Test that IPolklibraryTypeStaffLayer is registered."""
        from polklibrary.type.staff.interfaces import IPolklibraryTypeStaffLayer
        from plone.browserlayer import utils
        self.assertIn(IPolklibraryTypeStaffLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = POLKLIBRARY_TYPE_STAFF_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['polklibrary.type.staff'])

    def test_product_uninstalled(self):
        """Test if polklibrary.type.staff is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled('polklibrary.type.staff'))

    def test_browserlayer_removed(self):
        """Test that IPolklibraryTypeStaffLayer is removed."""
        from polklibrary.type.staff.interfaces import IPolklibraryTypeStaffLayer
        from plone.browserlayer import utils
        self.assertNotIn(IPolklibraryTypeStaffLayer, utils.registered_layers())
