from .behaviors import IMetaFromFile


def update_meta_from_docfile(obj, evt):
   "update content object metadata from primary (document) file field"

   try:
      meta = IMetaFromFile(obj)
   except:
      return
   else:
      meta.update_all()

