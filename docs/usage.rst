=====
Usage
=====

To use Test Project in a project, add it to your `INSTALLED_APPS`:

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
