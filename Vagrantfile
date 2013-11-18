# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.box = "precise32"
  config.vm.box_url = "http://files.vagrantup.com/precise32.box"

  config.vm.hostname = "vagrant-hbase"

  config.vm.network :private_network, ip: "192.168.15.166"
  # Hadoop web UI ports
  config.vm.network :forwarded_port, guest: 50070, host: 50170
  config.vm.network :forwarded_port, guest: 50075, host: 50175
  config.vm.network :forwarded_port, guest: 50090, host: 50190
  # HBase web UI ports
  config.vm.network :forwarded_port, guest: 60010, host: 60110
  config.vm.network :forwarded_port, guest: 60030, host: 60130
  # Thrift
  config.vm.network :forwarded_port, guest: 9090, host: 9190

  config.ssh.forward_agent = true

  # increase available memory
  config.vm.provider :virtualbox do |vb|
     vb.customize ["modifyvm", :id, "--memory", "768"]
  end

  config.vm.provision :ansible do |ansible|
    ansible.playbook = "ansible/playbook.yml"
    ansible.inventory_path = "ansible/ansible_hosts"
    ansible.verbose = true
  end
end
