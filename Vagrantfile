Vagrant.configure("2") do |config|
    config.vm.provider "virtualbox" do |vb|
      vb.memory = 2048
      vb.cpus = 2
    end
    config.vm.box_check_update = false
  
    config.vm.define "nasa", primary: true do |nasa|
    nasa.vm.box = "ubuntu/jammy64"
      nasa.vm.hostname = "nasa.local"
      nasa.vm.network "private_network", ip: "192.168.56.101"
      nasa.vm.synced_folder "shares", "/vagrant", disabled: false
      nasa.vm.provision "file", source: "key_gen.sh", destination: "/home/vagrant/"
      nasa.vm.provision "shell", path: "configs/pre_nasa_config.sh"
    end
  end
