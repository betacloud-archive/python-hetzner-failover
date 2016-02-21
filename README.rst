Script to work with Hetzner failover IP addresses
=================================================

Installation
------------

tbd

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

tbd


API Rate Limits
---------------

Hetzner robot webservice is rate limited at 100 queries per 1 hour window.


Documentation
-------------

* http://wiki.hetzner.de/index.php/Failover
* http://wiki.hetzner.de/index.php/Robot_Webservice#Failover
