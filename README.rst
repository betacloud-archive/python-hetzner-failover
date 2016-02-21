Script to work with Hetzner failover IP addresses
=================================================

Requirements
------------

* oslo.conf <https://github.com/openstack/oslo.conf>
* oslo.log <https://github.com/openstack/oslo.log>
* Requests <http://docs.python-requests.org/en/master/>
* tabulate <https://pypi.python.org/pypi/tabulate>


Implemented commands
--------------------


list
~~~~

* http://wiki.hetzner.de/index.php/Robot_Webservice#GET_.2Ffailover

.. code::

   $ ./hetzner-failover.py --config-file hetzner-failover.conf list
   +------------------+---------+-----------------+---------------+-----------+
   | active_server_ip | ip      | netmask         | server_number | server_ip |
   +==================+=========+=================+===============+===========+
   | a.b.c.d          | e.f.g.h | 255.255.255.255 |        123456 | a.b.c.d   |
   | ...              | ...     | ...             |           ... | ...       |
   | ...              | ...     | ...             |           ... | ...       |
   +------------------+---------+-----------------+---------------+-----------+


show
~~~~

* http://wiki.hetzner.de/index.php/Robot_Webservice#GET_.2Ffailover.2F.3Cfailover-ip.3E

.. code::

   $ ./hetzner-failover.py --config-file hetzner-failover.conf show e.f.g.h
   +------------------+---------+-----------------+---------------+-----------+
   | active_server_ip | ip      | netmask         | server_number | server_ip |
   +==================+=========+=================+===============+===========+
   | a.b.c.d          | e.f.g.h | 255.255.255.255 |        123456 | a.b.c.d   |
   +------------------+---------+-----------------+---------------+-----------+

route
~~~~~

* http://wiki.hetzner.de/index.php/Robot_Webservice#POST_.2Ffailover.2F.3Cfailover-ip.3E

.. code::

   $ ./hetzner-failover.py --config-file hetzner-failover.conf route e.f.g.h i.j.k.l
   elapsed time for failover: 28.0130250454 seconds
   +------------------+---------+-----------------+---------------+-----------+
   | active_server_ip | ip      | netmask         | server_number | server_ip |
   +==================+=========+=================+===============+===========+
   | i.j.k.l          | e.f.g.h | 255.255.255.255 |        123456 | a.b.c.d   |
   +------------------+---------+-----------------+---------------+-----------+


API Rate Limits
---------------

Hetzner robot webservice is rate limited.

* 100 queries per 1 hour window for ``GET /failover`` (``list`` command)
* 100 queries per 1 hour window for ``GET /failover/<failover-address>`` (``show`` command)
* 50 queries per 1 hour window for ``POST /failover/<failover-address>`` (``route`` command)


Documentation
-------------

* http://wiki.hetzner.de/index.php/Failover
* http://wiki.hetzner.de/index.php/Robot_Webservice#Failover

Development
-----------

.. code::

   $ virtualenv .venv
   $ source .venv/bin/activate
   $ pip install -r requirements.txt
