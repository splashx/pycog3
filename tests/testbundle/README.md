testbundle 
=======================================

# Overview

This is a dummy cog bundle used to test pycog3 python module
 
# Installing

Create a virtual env and:

```bash
pip3 install --upgrade .
```


# Configuring

There is one dynamic configuration file which should be set in the environmental variables:

```bash
export dyn_config_var1
 
```

# Executing

```bash
/usb/bin/cog-command
```

# Building

To build the Docker image, simply run:

    $ make docker

Requires Python 3.6.x, pip, make, and Docker.
