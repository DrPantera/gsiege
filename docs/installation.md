# Installation instructions #

Follow these steps to install Gades Siege in a Debian-based GNU/Linux system. Other systems will require similar steps.

## Download the source code ##

Using [Git](https://git-scm.com), open a terminal and run this:
```
git clone https://github.com/DrPantera/gsiege.git
```

This will create a `gsiege` folder with the Gades Siege source code.


## Download Python-Clips ##

First, check your version of Python with:

```
python --version
```

Depending on the version of Python, the steps will slightly change: see below.

### Python 2.6 and earlier ###

First, download the appropriate package for PyClips from the [official website](http://sourceforge.net/projects/pyclips/files/debian%20packages/), according to your CPU architecture (amd64 for a 64-bits system, i386 for a 32-bits one). Once the download has completed, you can install it as usual for your distribution. From the terminal, you could run a command like this:

```
sudo dpkg -i nombre_paquete.deb
```

### Python 2.7 and later ###

PyClips has not been packaged for newer Python releases, so you will have to install it from the sources. First, install the build dependencies:
```
sudo apt-get install libclips-dev python-dev build-essential
```

Next, download the [PyClips source code](http://sourceforge.net/projects/pyclips/files/pyclips/pyclips-1.0/pyclips-1.0.7.348.tar.gz/download). Unpack the archive, and run these commands from the resulting folder:
```
cd pyclips
sudo python setup.py install
```

After this, PyClips will be ready to use in our systems.

## Install the other dependencies ##

Gades Siege requires **pycha** to draw charts and **pygame** to draw 2D graphics during games. Both libraries are usually in the default package repositories, so installing them is as simple as running:
```
sudo apt-get install python-pycha python-pygame
```

## Launch ##

Gades Siege can be launched from the main script in the base folder of the project:
```
./gsiege.py
```
