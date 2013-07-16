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

**Note:** Ansible < 1.2 may not work due to some bugs in parsing Jinja2 syntax
in playbooks. Ubuntu 13.04 has only Ansible 1.1 in repositories, therefore
it's best to use `sudo pip install ansible` to get a more recent version.

What's in the box?
------------------

This Vagrantfile sets up a single HBase node in standalone mode (using local file system, not HDFS).
Master web UI is available from the host machine at http://127.0.0.1:60110,
RegionServer web UI at http://127.0.0.1:60130.
