vagrant-hbase
=============

Vagrantfile for quick-and-dirty HBase setup.

System
------

Ubuntu 12.04 LTS (precise)

Provisioning
------------

This vagrant setup uses [Ansible](http://www.ansibleworks.com/) for VM
provisioning.

Getting started
---------------

1. install Ansible on your host machine
2. `git clone https://github.com/zsiciarz/vagrant-hbase.git && cd vagrant-hbase && vagrant up`
3. ????
4. PROFIT!

What's in the box?
------------------

This Vagrantfile sets up a single HBase node in standalone mode (using local file system, not HDFS).
Master web UI is available at http://127.0.0.1:60110, RegionServer web UI at http://127.0.0.1:60130.
