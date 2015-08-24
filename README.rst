Aquarium
========

Aquarium is a cookiecuter_ template for production-ready
`Docker Compose`_ + Splash_ setup.

.. _cookiecuter: http://cookiecutter.rtfd.org
.. _Splash: https://github.com/scrapinghub/splash
.. _Docker Compose: https://docs.docker.com/compose/

Usage
-----

First, make sure Docker and Docker Compose are installed.

Then install cookiecutter::

    pip install cookiecutter

or (on OS X + homebrew)::

    brew install cookiecutter

Then generate a folder with config files::

    cookiecutter gh:TeamHG-Memex/aquarium

With all default options it'll create an ``aquarium`` folder in the current
path. Go to this folder and start the Splash cluster::

    cd ./aquarium
    docker-compose up

Contributing
------------

* Source code: https://github.com/TeamHG-Memex/aquarium
* Bug tracker: https://github.com/TeamHG-Memex/aquarium/issues

License is MIT.
