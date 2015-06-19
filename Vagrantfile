# -*- mode: ruby -*-
# vi: set ft=ruby :

require 'rbconfig'

Vagrant.configure("2") do |config|

  config.vm.box = "trusty64"
  config.vm.box_url = "http://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"

  config.vm.hostname = "vagrant-hbase"

  config.vm.network :private_network, ip: "192.168.15.166"
  # Hadoop web UI ports
  config.vm.network :forwarded_port, guest: 50070, host: 50170
  config.vm.network :forwarded_port, guest: 50075, host: 50175
  config.vm.network :forwarded_port, guest: 50090, host: 50190
  # Job History
  config.vm.network :forwarded_port, guest: 10020, host: 10120
  # HBase web UI ports
  config.vm.network :forwarded_port, guest: 60010, host: 60110
  config.vm.network :forwarded_port, guest: 60030, host: 60130
  # Thrift
  config.vm.network :forwarded_port, guest: 9090, host: 9190
  #ZooKeeper
  config.vm.network :forwarded_port, guest: 2181, host: 2281

  config.ssh.forward_agent = true

  # increase available memory
  config.vm.provider :virtualbox do |vb|
     vb.customize ["modifyvm", :id, "--memory", "1024"]
  end
  is_windows = (RbConfig::CONFIG['host_os'] =~ /mswin|mingw|cygwin/)
  if is_windows
    # Provisioning configuration for shell script.
    config.vm.provision "shell" do |sh|
      sh.privileged = false
      sh.path = "windows/windows.sh"
      sh.args = "ansible/playbook.yml ansible/ansible_hosts"
    end
  else
    config.vm.provision :ansible do |ansible|
      ansible.playbook = "ansible/playbook.yml"
      ansible.inventory_path = "ansible/ansible_hosts"
      ansible.limit = "all"
      ansible.verbose = "vv"
    end
  end
end
