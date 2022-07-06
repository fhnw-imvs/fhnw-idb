# Data Transport

1. [Overview](#overview)
2. [Resources](#resources)
3. [Connecting nRF52840 and Pi using BLE](#connecting-nrf52840-and-pi-using-ble)
3. [Connecting to Wi-Fi](#connecting-to-wi-fi)
4. [Using the ThingSpeak IoT platform](#using-the-thingspeak-iot-platform)
5. [Sending data to the ThingSpeak REST API](#sending-data-to-the-thingspeak-rest-api)
6. [Sending data to the ThingSpeak MQTT API](#sending-data-to-the-thingspeak-mqtt-api)
7. [Sending data to ThingSpeak with LoRaWAN](sending-data-to-thingspeak-with-lorawan)
8. [CircuitPython examples](#circuitpython-examples)
9. [Python examples](#python-examples)

## Overview
<table><tr><td><img width="600" src="overview-data-transport.png"></td></tr></table>

>Data transport (data transmission, also data communication or digital communications) is the transfer of data (a digital bitstream or a digitized analog signal) over a point-to-point or point-to-multipoint communication channel. 

--- from Wikipedia

To transfer the data, a communication channel must be established between the "Connected device" and a "Cloud Backend".

We will use examples of data transport technologies to find out:

* how to establish a communication channel between two communication parties?
* how the sensor values can be transfered to the backend?
* how transfer protocols of the internet can be used to enable the transfer?
* how these transfer protocols differ?

## Resources

- Slides on [Sending Sensor Data to IoT Platforms](IdbSensorDataPlatforms.pdf).
- Slides on [Internet Protocols and HTTP](IdbInternetProtocols.pdf).
- Slides on [Messaging Protocols and Data Formats](IdbMessagingProtocols.pdf).
- Slides on [Long Range Connectivity with LoRaWAN](IdbLoRaWANConnectivity.pdf).

## Connecting nRF52840 and Pi using BLE
Bluetooth Low Energy (BLE) is well suited to connect a microcontroller like the nRF5280 to a dedicated computer like a Raspberry Pi. In such a scenario, the Pi can act as a hub to collect data from multiple sensors all connected to one microcontroller. The Pi, which is more powerful than any microcontroller, can perform initial data processing before forwarding the processed data to a central cloud service or database.

Adafruit provides corresponding libraries and tutorials for BLE communiation:
- [Getting Started with CircuitPython and Bluetooth Low Energy](https://learn.adafruit.com/circuitpython-nrf52840): Tutorial to introduce BLE on the nRF52480.
- [CircuitPython BLE Libraries on Any Computer](https://learn.adafruit.com/circuitpython-ble-libraries-on-any-computer/ble-uart-example): Tutorial to run BLE on a Pi and to communicate to a nRF52480 microcontroller.

**Remark**: Use BLE libraries from the same provider to easily build a BLE connection between the communication partners.

## Connecting to Wi-Fi
Wi-Fi is well known. It can provide high-throughput data transfer for both enterprise and home environments. However, in the IoT space, its major limitations in coverage, scalability and power consumption make the technology much less prevalent.

Since IoT is widely diverse and multifaceted, their is no one-size-fits-all communication solution. Figure 1 shows the most important technologies in comparison with their _Data Rate & Power Consumption_ and _Range_.

<img width="600" src="iot-wireless-tech.jpg">

Figure 1: Visualization from [Behr Technologies](https://behrtech.com/blog/6-leading-types-of-iot-wireless-tech-and-their-best-use-cases/)

However, Wi-Fi can be used well in prototyping. Our two hardware platforms are or can be equipped with Wi-Fi.

- The [Raspberry Pi Zero W](https://github.com/fhnw-imvs/fhnw-idb/wiki/Raspberry-Pi-Zero-W) has Wi-Fi on board.
- The [Feather nRF52840 Express](https://github.com/fhnw-imvs/fhnw-idb/wiki/Feather-nRF52840-Express) needs the [FeatherWing ESP32 AirLift](https://github.com/fhnw-imvs/fhnw-idb/wiki/FeatherWing-ESP32-AirLift) as Wi-Fi co-processor.

## Using the ThingSpeak IoT platform
We will use [ThingSpeak](https://thingspeak.com/) as our *cloud backend*. ThingSpeak is an IoT analytics platform that allows you to aggregate, visualize, and analyze live data streams in the cloud. 

For an introduction look at this tutorial:

* [Introduction to ThingSpeak](https://ch.mathworks.com/de/support/search.html/videos/introduction-to-thingspeak-107749.html?q=&fq=asset_type_name:video%20category:matlab/data-import-and-export&page=1)

Your steps to get started with ThingSpeak are:

1. **Create a free account**
    
    ThingSpeak does provide free access, but with [limited resources and functionality](https://thingspeak.com/prices/thingspeak_student). To use [ThingSpeak](https://thingspeak.com/), start creating a free account with your **FHNW email address** by clicking the button as shown in figure 1.

    <img width="640" src="thingspeak-get-started.png"></td></tr></table>

    Figure 1: Get started on ThingSpeak with a free, limited account

2. **Create a channel**
    
    To be able to collect data on ThingSpeak, you have to provide a so-called **Channel**. Use the information in [Collect Data in a New Channel](https://ch.mathworks.com/help/thingspeak/collect-data-in-a-new-channel.html) to setup your first channel with 3 fields: *Temperature, Humidity, Dew Point*

    Save the channel.

3. **Get your access keys**

    API keys enable you to write data to a channel or read data from a private channel. API keys are auto-generated when you create a new channel.

    You can access your API key icon your channel page in tab **API Keys** (see Figure 2). You will need the **Write API Key**

4. **Test your channel**

    You can test your channel by sending test data manually using the HTTP protocol.

    Use `curl` to send a HTTP POST request to ThingSpeak:

    ```
    $ curl -v https://api.thingspeak.com/update -d "api_key=MY_WRITE_API_KEY&field1=5&field2=10&field3=20"
    ```
    
    or use your browser to send a HTTP GET request, what is also supported:
    
    ```
    https://api.thingspeak.com/update?api_key=MY_WRITE_API_KEY&field1=0&field2=10&field3=20
    ```

    You should see on each chart one red point, which corresponds to your test values as shown in figure 2.

    <img width="640" src="thingspeak-charts.png"></td></tr></table>

    Figure 2: Charts with first test data

5. **Create idb channel**

    For your [CircuitPython](#circuitpython-examples) and [Python examples](#python-examples) we need a new channel with the two fields `temperature` and `humidity`. 

    Create this channel and get the API Keys.

6. **Done**

    Your ThingSpeak channel is now ready to collect your sensor data.

## Sending data to the ThingSpeak REST API
The Hypertext Transfer Protocol [(HTTP)](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) is an application layer protocol for distributed, collaborative, hypermedia information systems. HTTP is the foundation of data communication for the World Wide Web, where hypertext documents include hyperlinks to other resources that the user can easily access.

Representational state transfer [(REST)](https://en.wikipedia.org/wiki/Representational_state_transfer) is an architectural style designed as a *request-response model* that communicates over HTTP. The ThingSpeak IoT platform uses the REST API calls GET, POST, PUT, and DELETE to create and delete channels, *read and write channel data*, and clear the data in a channel. A web browser or client sends a request to the server, which responds with data in the requested format.

* To get started with the ThingSpeak REST API, see [REST API](https://ch.mathworks.com/help/thingspeak/rest-api.html?s_tid=CRUX_lftnav)

## Sending data to the ThingSpeak MQTT API
MQTT is a *publish/subscribe communication protocol* that uses TCP/IP sockets or WebSockets. The ThingSpeak IoT platform enables clients to update and receive updates from channel feeds via the *ThingSpeak MQTT broker*. A client device connects to the MQTT broker and can publish to a channel or subscribe to updates from that channel.

* To get started with the ThingSpeak MQTT API, see [MQTT Basics](https://ch.mathworks.com/help/thingspeak/mqtt-basics.html).
* For a curated list of MQTT libraries, see [MQTT libraries](https://github.com/mqtt/mqtt.github.io/wiki/libraries).

## Sending data to Thingspeak with LoRaWAN
[LoRaWAN](https://lora-alliance.org/about-lorawan) is a high capacity, Long Range, open, Low Power Wide Area Network (LPWAN) standard designed for LoRa Powered IoT Solutions by the LoRa Alliance. It is a bi-directional protocol which takes full advantage of all the features of the LoRa technology to deliver services including reliable message delivery, end to end security, location and multicast capabilities. The standard ensures the interoperability of the various LoRaWAN networks world-wide.

TheThingsNetwork [(TTN)](https://www.thethingsnetwork.org/) is a community-based initiative to build a LoRaWAN for the Internet of Things.

The integration for ThingSpeak to external platforms like [AWS IoT](https://aws.amazon.com/de/iot/) or [ThingSpeak](https://thingspeak.com/) can be found on their [integrations](https://www.thethingsnetwork.org/docs/applications/integrations.html) webpage.

## CircuitPython examples
Try these examples with CircuitPython on the nRF52840.

### Wi-Fi
Consider to setup a hotspot on your smartphone and to access and use a WLAN anywhere.
* [Reading the Wi-Fi module MAC address](CircuitPython/wifi_address)
* [Scanning Wi-Fi networks](CircuitPython/wifi_scan)
* [Connecting to a Wi-Fi network](CircuitPython/wifi_connect)

### HTTP
These examples use generic HTTP servers.
* [Getting data from a Web server](CircuitPython/http_get_client)
* [Posting data to a Web server](CircuitPython/http_get_client)

These examples use the ThingSpeak REST API.
* [Getting data from the ThingSpeak REST API](CircuitPython/thingspeak_http_get_client)
* [Posting data to the ThingSpeak REST API](CircuitPython/thingspeak_http_post_client)

### MQTT
These examples use a generic MQTT broker.
* [Publishing to a MQTT topic](CircuitPython/mqtt_pub_client)
* [Subscribing to a MQTT topic](CircuitPython/mqtt_sub_client)

These examples use the ThingSpeak MQTT API.
* [Publishing data to the ThingSpeak MQTT API](CircuitPython/thingspeak_mqtt_pub_client)

### LoRaWAN
* [Sending data to TheThingsNetwork with LoRaWAN (ABP)](CircuitPython/lorawan_abp)

## Python examples

Try these examples with Python on the Raspberry Pi Zero W.

### Wi-Fi

Use the information [Configure Wi-Fi](https://github.com/fhnw-imvs/fhnw-idb/wiki/Raspberry-Pi-Zero-W#configure-wi-fi) on the Wiki to add your Pi to your WLAN.

Note that you can add to the configuration file `wpa_supplicant.conf` more than one network. Consider to setup a hotspot on your smartphone and to access and use a WLAN anywhere.

Try these examples with Python on the Raspberry Pi and with Wi-Fi enabled:

* [Posting data to the ThingSpeak REST API](Python/wifi/http)
* [Publishing data to the ThingSpeak MQTT API](Python/wifi/mqtt)


