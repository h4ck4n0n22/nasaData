# nasaData

Vagrant environment to stand up the NASA API data programme in Ubuntu VM.

Sets up the main vm **`nasa`**, installs all required tools and dependencies.

## Prerequisites

* [Git](\\US-SEATTLE\Software\Developer\Git) installed!
* [Vagrant](\\US-SEATTLE\Software\Developer\Vagrant) installed!
* [Virtualbox](\\US-SEATTLE\Software\Freeware\Virtualbox) installed!
* [Vagrant](\\US-SEATTLE\Software\Developer\Vagrant\Windows) installed!

Once you have Vagrant installed, you will need to install the reload plugin

```bash
vagrant plugin install vagrant-reload
```

## NASA VM

### Set up and access to VM

```bash
# Set up the VM
vagrant up nasa

# SSH to the machine
vagrant ssh nasa
```

### Set up the virtual environment

```bash
# Make a new directory in the users home folder called nasadata
vagrant@nasa:~$ mkdir ~/nasadata
# Copy over the contents from /vagrant into the new directory
vagrant@nasa:~$ cp -r /vagrant/* ~/nasadata
# Change into the new directory
vagrant@nasa:~$ cd ~/nasadata
# Use python to set up the virtual environment to work in
vagrant@nasa:~/nasadata$ python3 -m venv .
# Activate the virtual environment
vagrant@nasa:~/nasadata$ source ./bin/activate
# Now we are in it, we can install the required python libraries we need
(nasadata) vagrant@nasa:~/nasadata$ pip install -r ./requirements.txt
```

### Setting up the jupyter server

```bash
# We have what we need now, so we can start up the jupyter notebook server
# Don't forget to replace the beginning of the URL with 192.168.56.101
(nasadata) vagrant@nasa:~/nasadata$ jupyter notebook --port 8888 --ip 0.0.0.0

# Should end up with an output that look like the following

[I 13:59:32.656 NotebookApp] Serving notebooks from local directory: /home/vagrant/nasadata
[I 13:59:32.656 NotebookApp] Jupyter Notebook 6.5.4 is running at:
[I 13:59:32.656 NotebookApp] http://nasa:8888/?token=[random_token_hash_value]
[I 13:59:32.656 NotebookApp]  or http://127.0.0.1:8888/?token=[random_token_hash_value]
[I 13:59:32.656 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[W 13:59:32.662 NotebookApp] No web browser found: could not locate runnable browser.
[C 13:59:32.662 NotebookApp]

    To access the notebook, open this file in a browser:
        file:///home/vagrant/.local/share/jupyter/runtime/nbserver-22304-open.html
    Or copy and paste one of these URLs:
        http://nasa:8888/?token=[random_token_hash_value]
     or http://127.0.0.1:8888/?token=[random_token_hash_value]
```

## Working terminal

Now we need to open a new terminal, leaving the one above alone as that is serving out jupyter server for us.

```bash
# SSH to the machine
vagrant ssh nasa
# Change into the working directory
vagrant@nasa:~$ cd ~/nasadata
# Activate the virtual environment
vagrant@nasa:~/nasadata$ source ./bin/activate
# Terminal should look like this
(nasadata) vagrant@nasa:~/nasadata$
```

### Running the programme

```bash
# Run the python programme without any options
(nasadata) vagrant@nasa:~/nasadata$ python3 ./main.py
# Should see the help output
    main.py -d <datatype> -o <out_file> [optional args]

    datatype can be one of:
    * fireball
    * asteroid_neo
    * potd
    * donki
        [optional args: --start_date --end_date]
        [must include donki_type (-k)] one of:
        - cme
        - cmea
        - gst
        - ips
        - flr
        - sep
        - mpc
        - rbe
        - hss
        - wsa
        - notifications
    * exoplanet [must include exo_data_type (-e)] one of:
        - kooi
        - tce
        - kst
        - k2t
        - maes
        - cpm
```