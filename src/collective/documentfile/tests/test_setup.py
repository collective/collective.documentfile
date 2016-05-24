# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.documentfile.testing import COLLECTIVE_DOCUMENTFILE_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.documentfile is properly installed."""

    layer = COLLECTIVE_DOCUMENTFILE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.documentfile is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.documentfile'))

    def test_browserlayer(self):
        """Test that IDocumentFileLayer is registered."""
        from collective.documentfile.interfaces import (
            IDocumentFileLayer)
        from plone.browserlayer import utils
        self.assertIn(IDocumentFileLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_DOCUMENTFILE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['collective.documentfile'])

    def test_product_uninstalled(self):
        """Test if collective.documentfile is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.documentfile'))

    def test_browserlayer_removed(self):
        """Test that IDocumentFileLayer is removed."""
        from collective.documentfile.interfaces import IDocumentFileLayer
        from plone.browserlayer import utils
        self.assertNotIn(IDocumentFileLayer, utils.registered_layers())
