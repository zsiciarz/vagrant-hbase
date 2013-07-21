vagrant-hbase
=============

Vagrantfile for quick-and-dirty HBase setup.

Overview
--------

This Vagrant project sets up a Ubuntu 12.04 (precise) virtual machine and
provisions it for HBase development. [Ansible](http://www.ansibleworks.com/)
is used for VM provisioning.

After running `vagrant up`, a single HBase node is set up in standalone mode
(using local file system, not HDFS). A Thrift server is also running,
allowing access from languages outside of the JVM.

Getting started
---------------

1. install Ansible on your host machine
2. `git clone https://github.com/zsiciarz/vagrant-hbase.git && cd vagrant-hbase && vagrant up`
3. ????
4. PROFIT!

**Note:** Ansible < 1.2 may not work due to some bugs in parsing Jinja2 syntax
in playbooks. Ubuntu 13.04 has only Ansible 1.1 in repositories, therefore
it's best to use `sudo pip install ansible` to get a more recent version.

Network and ports
-----------------

The guest machine has a private IP address 192.168.15.166. HBase-related
ports are forwarded according to the following rule:

    hostPortNumber = guestPortNumber + 100

For example, HBase web UIs are available from the host machine at
http://127.0.0.1:60110 (Master) and http://127.0.0.1:60130 (RegionServer).

Initial data
------------

The `create_test_table.rb` file can be loaded into HBase shell to define
a dead simple test table with one column family `cf`. The table looks like this:

    +--------+-----------+
    | rowkey |  cf:col1  |
    +--------+-----------+
    |  row1  |   value1  |
    +--------+-----------+

To load the data, execute:

    vagrant ssh
    cd hbase-0.94.9/
    ./bin/hbase shell /vagrant/data/create_test_table.rb

Jython
------

A Jython interpreter is also installed in the VM. To access Java HBase API
from Jython, you need to set the CLASSPATH environment variable correctly.
HBase CLI tool can help in that matter.

    vagrant ssh
    cd hbase-0.94.9/
    export CLASSPATH=`./bin/hbase classpath`
    jython

This should drop you into Jython REPL where you can import Java classes
and use them in a more Pythonic way. An example script that reads the data
loaded with `create_test_table.rb` is at `/vagrant/test.py`.

