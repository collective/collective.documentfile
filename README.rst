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



Examples
--------

Add this package and a recent version of Products.OpenXml, grab a PowerPoint presentation, add a Document File and upload the presentation into it.


Documentation
-------------

Full documentation for end users can be found in the "docs" folder, and is also available online at http://docs.plone.org/foo/bar


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
