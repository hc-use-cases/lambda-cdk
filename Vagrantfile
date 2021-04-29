# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "apopa/bionic64"
  config.vm.hostname = "lambda-cdk"
  config.vm.network "public_network", ip: "192.168.178.25", bridge: "en7: Dell Universal Dock D6000"
  config.vm.provision "shell", path: "bootstrap/bootstrap.sh"
end
