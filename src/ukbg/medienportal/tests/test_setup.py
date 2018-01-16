# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from ukbg.medienportal.testing import UKBG_MEDIENPORTAL_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that ukbg.medienportal is properly installed."""

    layer = UKBG_MEDIENPORTAL_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if ukbg.medienportal is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'ukbg.medienportal'))

    def test_browserlayer(self):
        """Test that IUkbgMedienportalLayer is registered."""
        from ukbg.medienportal.interfaces import (
            IUkbgMedienportalLayer)
        from plone.browserlayer import utils
        self.assertIn(IUkbgMedienportalLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = UKBG_MEDIENPORTAL_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['ukbg.medienportal'])

    def test_product_uninstalled(self):
        """Test if ukbg.medienportal is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'ukbg.medienportal'))

    def test_browserlayer_removed(self):
        """Test that IUkbgMedienportalLayer is removed."""
        from ukbg.medienportal.interfaces import \
            IUkbgMedienportalLayer
        from plone.browserlayer import utils
        self.assertNotIn(IUkbgMedienportalLayer, utils.registered_layers())
