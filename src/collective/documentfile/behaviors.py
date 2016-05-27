# -*- coding: utf-8 -*-

from persistent.dict import PersistentDict

from zope.annotation import IAnnotations
from zope.component import getAdapter
from zope.interface import Interface
from zope.interface import implementer

from plone.namedfile.file import NamedBlobImage
from plone.rfc822.interfaces import IPrimaryFieldInfo

from .interfaces import IDocumentInfo
from .adapters import EmptyDocumentInfo

class IMetaFromFile(Interface):
    """Marker interface to enable metadata from file behavior"""


@implementer(IMetaFromFile)
class MetaFromFile(object):

    def __init__(self, context):
        self.context = context
        info = IPrimaryFieldInfo(context, None)
        if info is None or info.value is None:
            self.docfile = EmptyDocumentInfo(context)
            return None

        src_file = info.value

        # need to let ComponentLookupError propagate if not found
        self.docfile = getAdapter(src_file, IDocumentInfo, name=src_file.contentType)


    def update_title(self):
        if self.docfile.title:
            self.context.setTitle(self.docfile.title)

    def update_description(self):
        if self.docfile.description:
            self.context.setDescription(self.docfile.description)

    def update_subject(self):
        if self.docfile.keywords:
            self.context.setSubject(self.docfile.keywords)

    def update_language(self):
        if self.docfile.language:
            self.context.setLanguage(self.docfile.language)

    def update_pagecount(self):
        try:
            annotations = IAnnotations(self.context)
        except:
            return
        else:
            if "document_meta" not in annotations:
                annotations["document_meta"] = PersistentDict()
            annotations["document_meta"]["pagecount"] = self.docfile.pagecount

    def update_image(self):
        if self.docfile.image and hasattr(self.context, "image"):
            isuffix, idata = self.docfile.image
            itype = isuffix.lower().strip()
            imime = "image/" + isuffix
            ifilename = u"cover" + isuffix
            # if proper image exists, just (re)set the data and file name
            if self.context.image:
                self.context.image._setData(idata)
                self.context.image.filename = ifilename
            # otherwise add a blob image; TODO are there cases when should not use blob?
            else:
                self.context.image=NamedBlobImage(data=idata, contentType=imime, filename=ifilename)

    def update_all(self):
        self.update_title()
        self.update_description()
        self.update_subject()
        self.update_language()
        self.update_pagecount()
        self.update_image()
