=============================
Test Project
=============================

.. image:: https://badge.fury.io/py/test-project.svg
    :target: https://badge.fury.io/py/test-project

.. image:: https://travis-ci.org/hugobessa/test-project.svg?branch=master
    :target: https://travis-ci.org/hugobessa/test-project

.. image:: https://codecov.io/gh/hugobessa/test-project/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/hugobessa/test-project

aloalo

Documentation
-------------

The full documentation is at https://test-project.readthedocs.io.

Quickstart
----------

Install Test Project::

    pip install test-project

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'test_project.apps.TestProjectConfig',
        ...
    )

Add Test Project's URL patterns:

.. code-block:: python

    from test_project import urls as test_project_urls


    urlpatterns = [
        ...
        url(r'^', include(test_project_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
