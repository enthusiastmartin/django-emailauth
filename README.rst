django-emailauth
============

Django - custom user model with email authentication.

Note : still in development - although ready to use.

Documentation
------------

To do ...

Installation
------------

To get the latest commit from GitHub

.. code-block:: bash

    pip install -e git+git://github.com/enthusiastmartin/django-emailauth.git#egg=djangoemailauth

[Optional] Add ``djangoemailauth`` to your ``INSTALLED_APPS``. This is necessary only if built-in ``EmailUser`` is used ( see Usage below for details )

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'djangoemailauth',
    )


Usage
-----

``EmailUser``

Make sure to add djangoemailauth to installed apps.

Update ``settings.py`` to tell Django to use MyUser

.. code-block:: python

     AUTH_USER_MODEL = 'djangoemailauth.EmailUser'

``AbstractEmailUser``

.. code-block:: python

    from djangoemailauth.models import AbstractEmailUser

    class MyUser(AbstractEmailUser):
         ** extend User model with your attributes **

Update ``settings.py`` to tell Django to use MyUser

.. code-block:: python

     AUTH_USER_MODEL = '<your module>.MyUser'

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
