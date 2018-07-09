django-emailauth
============

Django - custom user model with email authentication.

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    pip install djangoemailauth

To get the latest commit from GitHub

.. code-block:: bash

    pip install -e git+git://github.com/enthusiastmartin/django-emailauth.git#egg=django-emailauth

TODO: Describe further installation steps (edit / remove the examples below):

Add ``djangoemailauth`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'djangoemailauth',
    )

Add the ``djangoemailauth`` URLs to your ``urls.py``

.. code-block:: python

    urlpatterns = [
        url(r'^app-url/', include('djangoemailauth.urls')),
    ]

Before your tags/filters are available in your templates, load them by using

.. code-block:: html

	{% load django-emailauth_tags %}


Don't forget to migrate your database

.. code-block:: bash

    ./manage.py migrate django-emailauth


Usage
-----

TODO: Describe usage or point to docs. Also describe available settings and
templatetags.


Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    mkvirtualenv -p python2.7 django-emailauth
    make develop

    git co -b feature_branch master
    # Implement your feature and tests
    git add . && git commit
    git push -u origin feature_branch
    # Send us a pull request for your feature branch

In order to run the tests, simply execute ``tox``. This will install two new
environments (for Django 1.8 and Django 1.9) and run the tests against both
environments.
