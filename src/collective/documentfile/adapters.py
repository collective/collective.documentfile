from zope.interface import implementer
from .interfaces import IDocumentInfo


@implementer(IDocumentInfo)
class EmptyDocumentInfo(object):
   "base document file adapter that just provides default empty values"

   title = u""
   description = u""
   keywords = ()
   language = u""
   pagecount = None
   image = None

   def __init__(self, context):
      self.context = context


