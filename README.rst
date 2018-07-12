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

