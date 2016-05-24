.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
collective.documentfile
==============================================================================


Features
--------

- basic framework to support copying and updating of various metadata from content primary file field
- base adapter for adding support for more file types
- a 'MetaFromFile' behavior for types that want to have their metadata updated from the primary file field
- a basic 'Document File' implementation that provides a nice default view
- PDF support by installing collective.pdfdocument package (search github)

Soon:

- MS Office document support by installing Products.OpenXml and openxmllib packages (search github)

For best experience, install plone.app.contenttypes on your Plone site; that will provide a nice folder
summary view with preview images of all documents.

Examples
--------

Install the package in Plone, add a Document File and upload a document file. Enjoy the nice Plone content
representation.

Note that usually people don't bother with document metadata so check the source document file to make sure
it has some metadata. For MS Office docs, make sure that "generate preview" is selected prior to saving the document.

Translations
------------

Will soon be translated to Finnish.


Installation
------------

Install collective.documentfile by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.documentfile


and then running ``bin/buildout``. Note that you will need some additional packages that provide the actual, file type -specific extraction of document file metadata.


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
