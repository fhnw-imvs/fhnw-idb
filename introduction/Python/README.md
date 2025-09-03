# Getting Started with Python on Raspberry Pi

1. [Prerequisites](#prerequisites)
2. [Update Raspian](#update-raspian)
3. [Install Python 3](#install-python-3)
4. [Install Blinka](#install-blinka) or [Install Grove](#install-grove)
5. [Run your first program](#run-your-first-program)

## Prerequisites

The following steps require a Raspberry Pi Zero W with Raspberry Pi OS Lite, a Linux operating system. To install it, see [Raspberry Pi Zero W Setup](https://github.com/fhnw-imvs/fhnw-idb/wiki/Raspberry-Pi-Zero-W#setup). Make sure to [configure Wi-Fi](https://github.com/fhnw-imvs/fhnw-idb/wiki/Raspberry-Pi-Zero-W#1-flash-raspberry-pi-os-bookworm-onto-an-sd-card) and [enable SSH access](https://github.com/fhnw-imvs/fhnw-idb/wiki/Raspberry-Pi-Zero-W#1-flash-raspberry-pi-os-bookworm-onto-an-sd-card) so you can [find your Pi](https://github.com/fhnw-imvs/fhnw-idb/wiki/Raspberry-Pi-Zero-W#2-boot-the-raspberry-pi-and-connect-via-ssh), if your computer is in the same local Wi-Fi network.

## Update Raspian

Update Raspberry Pi OS Lite to the latest version (this process may take some time):

```shell
sudo apt update
sudo apt upgrade
```

## Check Python Version

A fresh installation of the Raspberry Pi OS Lite has **Python 3 preinstalled**. Check this with:

```shell
$ python --version
Python 3.11.2
```

You need to install `pip3` to be able to download python packages to your project. Install `pip3` as follows:

```shell
$ sudo apt-get install python3-pip
$ pip --version
pip 23.0.1 from /usr/lib/python3/dist-packages/pip (python 3.11)
```

**Optional:** If you don't have Python3 installed, install it with:

```shell
sudo apt update
sudo apt install python3
````

The [python documentation](https://www.raspberrypi.org/documentation/usage/python/) includes chapters on [installing libraries](https://www.raspberrypi.com/documentation/computers/os.html#installing-python-libraries) and using [GPIO in Python](https://www.raspberrypi.org/documentation/usage/gpio/python/README.md).

## Raspberry Pi OS Bookworm

**Note:**  
If you are using *Raspberry Pi OS Bookworm*, check [this information](https://www.raspberrypi.com/documentation/computers/os.html#python-on-raspberry-pi).

## Install Blinka

**Note:** The advantage of this approach is that you can use the same CircuitPython code on the Raspberry Pi as on the microcontroller.

Install the [Blinka Python package](https://github.com/adafruit/Adafruit_Blinka) with the following steps, based on [this tutorial](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi) by Adafruit:

Frist create a [Virtual Environment](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi#setup-virtual-environment-3157129))

```bash
sudo apt install python3-venv
python -m venv env --system-site-packages
```

Activate the virtual environment (every time the Pi is rebooted):

```bash
source env/bin/activate
```

Install the Adafruit packages with:

```bash
cd ~
pip install --upgrade adafruit-python-shell
wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
sudo -E env PATH=$PATH python3 raspi-blinka.py
```

and test it using the [Blinka Test](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi#blinka-test-3030038) after a restart and activation of the virtual environment:

```bash
source env/bin/activate
```

## Install Grove

**Note:** If you want to work with pure Python programming, you must install the corresponding Python package in order to access the hardware.

To access the GPIOs on the Pi and work with Grove sensors and actuators we use the [Grove Python package](https://github.com/Seeed-Studio/grove.py).

Install the Grove Python package with:

```shell
sudo pip install grove.py
```

Here are some [code examples](https://github.com/Seeed-Studio/grove.py/blob/master/doc/README.md#gui-graphical-user-interface) by Seeed Studio.

## Run your first program

Now, [run your first program](blink_grove/README.md) and install it permanently on your microcontroller.
