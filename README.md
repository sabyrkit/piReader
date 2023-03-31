# piReader
Use the GPIO of a Raspberry Pi to send wiegand data to a physical access control system (PACS).

## Supported card formats

* Standard 26-bit
* HID H10302 37-bit (no facility code)
* HID H10304 37-bit (with facility code)
* More to come
  * Raw 32-bit
  * HID Corporate 1000 35-bit
  * HID Corporate 1000 48-bit

## You will need:

1. Raspberry Pi Zero W, 1A+, 1B+, 2B, 3A+, 3B, 3B+, 4B (wired ethernet prefered)
2. Jumper wires to connect the GPIO

## Todo

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
