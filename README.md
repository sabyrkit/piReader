# piReader
Use the GPIO of a Raspberry Pi to send [wiegand](https://en.wikipedia.org/wiki/Wiegand_interface) data to a physical access control system (PACS).

![alt text](https://github.com/sabyrkit/piReader/blob/main/assets/piReader.gif?raw=true)

## Supported card formats

* Standard 26-bit
* HID H10302 37-bit (no facility code)
* HID H10304 37-bit (with facility code)
* More to come

## You will need:

1. Raspberry Pi with the 40-pin GPIO header. e.g. Zero W, 1A+, 1B+, 2B, 3A+, 3B, 3B+, 4B (wired ethernet prefered)
2. Jumper wires to connect the GPIO
3. Physical access control system controller

## Installation

1. Install [flask](https://flask.palletsprojects.com/en/2.2.x/) with [pip](https://docs.python.org/3/installing/index.html)
```bash
$ pip install flask
```
2. Clone the repository
```bash
$ git clone https://github.com/sabyrkit/piReader.git
```

## Usage

You can use the flask developmental server
```bash
$ flask --app ~/piReader/app run
```

Or you can use a production WSGI server such as [gunicorn](https://gunicorn.org/)
```bash
$ pip install gunicorn
$ gunicorn -w 2 -b 0.0.0.0:5000 --chdir ~/piReader app:app
```

Now you can wire up the Pi to your access control system
* Reader 1:
  * D0/DATA/Green = GPIO 16
  * D1/CLOCK/White = GPIO 20
  * GND = Any ground pin
* Reader 2:
  * D0/DATA/Green = GPIO 19
  * D1/CLOCK/White = GPIO 26
  * GND = Any ground pin
* The wiegand data signals are typically 5VDC. May need a level shifter to bring up the Pi's 3V3 signals to 5V. It's working fine with a Pi 3B wired directly to a Mercury EP1501. You're results may vary.
* [Pi Pinout](https://pinout.xyz/)

Now head over to http://localhost:5000/ or http://your-pi-ip:5000/

Select either Reader 1 or 2. The first section you can manually enter credential data for Standard 26-bit, HID H10302 37-bit, or HID H10304 37-bit. The next two sections are hard coded credentals.

## ToDo:

* Additional card formats
  * HID PINs
  * Raw 32-bit (partialy implemented)
  * HID Corporate 1000 35-bit
  * HID Corporate 1000 48-bit
* Support for multiple virtual readers
* Support for other access control I/O
  * Door Contact
  * Request to Exit (REX)
  * Lock status
* OSDP Support
* Develope a Pi HAT
  * Simplify connections to the Pi
  * 12-24VDC power
  * PoE support????
