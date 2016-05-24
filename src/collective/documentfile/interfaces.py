# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.interface import Interface, Attribute
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IDocumentFileLayer(IDefaultBrowserLayer):
   """Marker interface that defines a browser layer."""


class IDocumentInfo(Interface):
   "document metadata"

   title = Attribute("dc title")
   description = Attribute("dc description")
   language = Attribute("dc language")
   keywords = Attribute("a.k.a dc subject")
   pagecount = Attribute("number of pages document has")
   image = Attribute("representative (cover) image for document")


class IDocumentFile(Interface):
   "document file marker interface"
