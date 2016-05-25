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

Features provided
------------------

- generic means to update content metadata from information extracted from a document file
  stored in the primary file field of content schema, implemented as a behavior and a
  specification for adding support for a particular document type

- a basic content type implementation for storing documents, that gets its metadata and
  cover image automatically copied over from the original document file

To support various types of documents, install:

- Products.OpenXml for MS Office document support
- collective.pdfdocument for PDF support

Adding support for other document types only requires registering a named adapter of
plone.namedfile.interfaces.INamedFile to collective.documentfile.interfaces.IDocumentFile,
named according to the mime type of the document.

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
