Aquarium
========

Aquarium is a cookiecuter_ template for hassle-free
`Docker Compose`_ + Splash_ setup. Think of it as a Splash instance
with extra features and without common pitfalls.

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

Then use http://<host>:8050 as a regular Splash_ instance. On Linux
http://0.0.0.0:8050 should work; on OS X and Windows IP address depends on
boot2docker or docker-machine.

Options
-------

When generating a config, cookiecutter will ask a bunch of questions.

* ``folder_name (default is "aquarium")`` - a name of the target folder.
* ``num_splashes (default is "3")`` - a number of Splash instances to create.
  To utilize full server capacity it makes sense to create slightly more Splash
  instances than CPU cores - e.g. on 2-core machine 3 instances often
  work best.
* ``splash_version (default is "master")`` - a version of scrapighub/splash
  Docker image.
* ``splash_verbosity (default is "1")`` - Splash log verbosity, from 0 to 5.
* ``max_timeout (default is "3600")`` - maximum allowed timeout.
* ``maxrss_mb (default is "3000")`` - a soft memory limit, in MB. Splash
  container will be restarted after some time if it starts to use more memory
  then this value.
* ``stats_enabled (default is "1")`` - whether to enable HAProxy stats.
  If stats are enabled visit http://<host>:8036 to see stats page.
* ``stats_auth (default is "admin:adminpass")`` - HTTP Basic Auth credentials
  for HAProxy stats.
* ``tor (default is "1")`` - enter 0 to disable Tor_ support. When Tor support
  is enabled, all .onion links are opened using Tor. In addition to
  that, there is ``tor`` `Splash proxy profile`_ which you can use to render
  any page using Tor.
* ``adblock (default is "1")`` - FIXME: this option is not working yet.
   Enter 0 to disable AdBlock Plus `request filters`_. By default,
   the following filters are available:

  * `easylist`: default set of EasyList_ filters for English;
  * `easyprivacy`: EasyPrivacy filters remove tracking scripts;
  * `easylist_noadult`: EasyList variant without filters for adult domains;
  * `fanboy-social`: removes social media content such as the Facebook like
    buttons and other widgets.
  * `fanboy-annoyance`: blocks Social Media content, in-page pop-ups
    and other annoyances; use it to decrease loading times and uncluttering
    pages. `fanboy-social` is already included in this filter.

.. _Tor: http://torproject.org
.. _Splash proxy profile: http://splash.readthedocs.org/en/latest/api.html#proxy-profiles
.. _request filters: http://splash.readthedocs.org/en/latest/api.html#request-filters
.. _EasyList: https://easylist.adblockplus.org/en/

Contributing
------------

* Source code: https://github.com/TeamHG-Memex/aquarium
* Bug tracker: https://github.com/TeamHG-Memex/aquarium/issues

License is MIT.
