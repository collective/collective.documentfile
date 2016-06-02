# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.interface import Interface, Attribute
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IFileMetaProvided(Interface):
   "marker interface for custom types for which file metadata should be processed"


# browser layers for each profile

class IFileMetaLayer(IDefaultBrowserLayer):
   """Marker interface set when collective.filemeta package is installed"""

class ICustomTypeLayer(IDefaultBrowserLayer):
   """Additionally set when the custom type profile is installed"""

class IExtendedFileLayer(IDefaultBrowserLayer):
   """Additionally set when the extended File profile is installed"""


# metadata update utility interfaces

class IFileMetaProvider(Interface):
   "provide metadata as a dict grouped (nested) by standard, ie. dc, exif, iptc, xmp..."

   def get_metadata(self, obj):
      "return metadata"


class IContentMetaUpdater(Interface):
   "update a particular set of metadata, or just single metadata item"

   def update_content(self, obj, metadata):
      "update the content with metadata that can be "


class IFileMetaUpdater(Interface):
   "updater that provides round-tripping, ie. copying metadata back to the file"

   # note: this is an advanced use case for which there are no known implementations

   def update_file(self, filedata, metadata):
      "update the source file with metadata"

