.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
collective.documentfile
==============================================================================

Background information
-----------------------

When Document files, such as MS Office or PDF documents are stored in Plone as
File content, utilizing document metadata embedded in the documents is not possible.
Nor does Plone provide a screenshot or cover page thumbnail of the document.

This packages aims to provide those missing features.

Note that in addition to this package, you need additional packages that do the actual
document-specific metadata extraction:

- Products.OpenXml for MS Office document support
- collective.pdfdocument for PDF support

Features provided
------------------

- Generic means to update content metadata from information extracted from a document file
  stored in the primary file field of content schema. This is achieved using a subscriber
  that attempts to adapt the primary file field contents (NamedFile) to IDocumentInfo.
  The adapter lookup can be switched on by assigning the 'Meta from document file'
  behavior.

- A basic (optional) 'Document File' Dexterity content type with the behavior assigned, that
  gets its metadata and cover image automatically copied over from the uploaded document.
  The type has a 'file' field for storing documents, 'image' field for cover image and a nice
  default view ('docfileview').

Note that the 'Meta from document file' behavior does not provide a cover image field. So
in your own content type, a image field named 'image' must be assigned separately, for
example by also assigning the lead image behavior to the content type.

To add support for an additional document type, a named adapter is needed that adapts
plone.namedfile.interfaces.INamedFile to collective.documentfile.interfaces.IDocumentFile,
named according to the mime type of the document type. See adapters.py for a base adapter
that provides default empty values, useful for partial IDocumentInfo implementations, ie.
when you only want some metadata updated from file rather than all of what IDocumentInfo
specifies.

Not provided
-------------

- viewing the document contents
- indexing of documents (would be a good fit though)
- asynchronous conversion

A note on metadata and cover images
------------------------------------

Usually people don't bother with document metadata so prior to uploading, you should check the
document properties.

For MS Office docs, make sure that the "store preview" option is selected,
before saving the document. PDFs have no embedded cover image; for them, collective.pdfdocument
converts the first page of the PDF into a PNG cover image.


Installation
------------

Install collective.documentfile by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.documentfile


and then running ``bin/buildout``. Remember that you will also need some additional packages that
provide the file type -specific extraction of document file metadata.


Contribute
----------

- Issue Tracker: https://github.com/collective/collective.documentfile/issues
- Source Code: https://github.com/collective/collective.documentfile


Support
-------

If you are having issues, please submit them to tracker or contact the author.

License
-------

The project is licensed under the GPLv2.
