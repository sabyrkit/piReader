
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Reader:
    def __init__(self, pin0, pin1):
        """
        Pins used to send Wiegand data
        pin0 - The GPIO pin goes LOW when sending a zero
        pin1 - The GPIO pin goes LOW when sending a one
        led = GPIO pin used for the LED from the ACS
        buz = GPIO pin used for the buzzer from the ACS
        """
        self.pin0 = pin0
        GPIO.setup(self.pin0, GPIO.OUT)
        GPIO.output(pin0, GPIO.HIGH)
        self.pin1 = pin1
        GPIO.setup(self.pin1, GPIO.OUT)
        GPIO.output(pin1, GPIO.HIGH)

def _sum(arr):              # Funtion used to sum parity bits
    sum = 0
    for i in arr:
        if i == 1:
            sum = sum + 1
    return(sum)

def sendData(binArrayb, readerPort):
    pulseTime = .00005      # Set the pulse time, typical 100 micro seconds
    if binArrayb == "":
        return
    else:
        for i in binArrayb:
            if i == 0:
                GPIO.output(readerPort.pin0, GPIO.LOW)
                time.sleep(pulseTime)
                GPIO.output(readerPort.pin0, GPIO.HIGH)
            elif i == 1:
                GPIO.output(readerPort.pin1, GPIO.LOW)
                time.sleep(pulseTime)
                GPIO.output(readerPort.pin1, GPIO.HIGH)
            else:
                return
        return

def sendH10301(facilityCode, cardNumber):
    """
    PFFFFFFFFCCCCCCCCCCCCCCCCP
    EXXXXXXXXXXXX.............
    .............XXXXXXXXXXXXO
    Facility Code: 8 bits, 0 to 255
    Card Number: 16 bits, 0 to 65,535
    """

    # Check if the input is an integer
    try:
        isinstance(int(facilityCode), int)
        isinstance(int(cardNumber), int)
        facilityCode = int(facilityCode)
        cardNumber = int(cardNumber)
    except:
        print(f"Not an integer")
        return
    
    # Check if card number is outside of range
    if (facilityCode > 255) or (cardNumber > 65535):
        print(f"Card Number too large")
        return
    else:
        # Convert the card number to a binary array
        binArray = [int(d) for d in str(bin(facilityCode))[2:].zfill(8)]
        
        binArray = binArray + ([int(d) for d in str(bin(cardNumber))[2:].zfill(16)])

        # Calculate the EVEN parity bit
        # if first 12 bits are EVEN, parit is 0; if ODD, parity is 1
        if (_sum(binArray[:12]) % 2) == 0:
            evenParityBit = 0
        else:
            evenParityBit = 1
        
        # Calculate the ODD parity bit
        # if last 12 bits are ODD, parity is 0; if EVEN, parity is 1
        if (_sum(binArray[13:]) % 2) == 0:
            oddParityBit = 1
        else:
            oddParityBit = 0
        # Add parity bits to the array
        binArray.insert(0, evenParityBit)
        binArray.append(oddParityBit)
        
    return(binArray)

def sendH10302(cardNumber):
    """
    PCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCP
    EXXXXXXXXXXXXXXXXXX.................. First 18 bits
    p01011001011101000010010011000100010p   = 12006270498
    ..................XXXXXXXXXXXXXXXXXXO Last 18 bits
    Card Number: 25 bits, 0 to 34,359,738,367
    """
    
    # Check if the input is an integer
    try:
        isinstance(int(cardNumber), int)
        cardNumber = int(cardNumber)
    except:
        print(f"Not an integer")
        return
    
    # Check if card number is outside of range
    if cardNumber > 34359738367:
        print(f"Card Number too large")
        return
    else:
        # Convert the card number to a binary array
        binArray = [int(d) for d in str(bin(cardNumber))[2:].zfill(35)]

        # Calculate the EVEN parity bit
        # if first 18 bits are EVEN, parit is 0; if ODD, parity is 1
        if (_sum(binArray[:18]) % 2) == 0:
            evenParityBit = 0
        else:
            evenParityBit = 1
        
        # Calculate the ODD parity bit
        # if last 18 bits are ODD, parity is 0; if EVEN, parity is 1
        if (_sum(binArray[17:]) % 2) == 0:
            oddParityBit = 1
        else:
            oddParityBit = 0
        # Add parity bits to the array
        binArray.insert(0, evenParityBit)
        binArray.append(oddParityBit)

    return(binArray)

def sendH10304(facilityCode, cardNumber):
    """
    PFFFFFFFFFFFFFFFFCCCCCCCCCCCCCCCCCCCP
    EXXXXXXXXXXXXXXXXXX..................
    ..................XXXXXXXXXXXXXXXXXXO
    Facility Code: 16 bits, 0 to 65,535
    Card Number: 19 bits, 0 to 524,287
    """
    # Check if the input is an integer
    try:
        isinstance(int(facilityCode), int)
        isinstance(int(cardNumber), int)
        facilityCode = int(facilityCode)
        cardNumber = int(cardNumber)
    except:
        print(f"Not an integer")
        return
    
    # Check if card number is outside of range
    if (facilityCode > 65535) or (cardNumber > 524287):
        print(f"Card Number too large")
    else:
        # Convert the card number to a binary array
        binArray = [int(d) for d in str(bin(facilityCode))[2:].zfill(16)]
        
        binArray = binArray + ([int(d) for d in str(bin(cardNumber))[2:].zfill(19)])
        # print(binArray)

        # Calculate the EVEN parity bit
        # if first 18 bits are EVEN, parit is 0; if ODD, parity is 1
        if (_sum(binArray[:18]) % 2) == 0:
            evenParityBit = 0
        else:
            evenParityBit = 1
        
        # Calculate the ODD parity bit
        # if last 18 bits are ODD, parity is 0; if EVEN, parity is 1
        if (_sum(binArray[17:]) % 2) == 0:
            oddParityBit = 1
        else:
            oddParityBit = 0
        # Add parity bits to the array
        binArray.insert(0, evenParityBit)
        binArray.append(oddParityBit)
        
    return(binArray)

def sendRaw(cardNumber):
    """
    Send raw data
    No parity
    """
    try:
        isinstance(int(cardNumber), int)
        cardNumber = int(cardNumber)
    except:
        print(f"Not an integer")
        return
    
    
    binArray = [int(d) for d in str(bin(cardNumber))[2:].zfill(32)]
    print(binArray)
    return(binArray)

Reader1 = Reader(16, 20)
Reader2 = Reader(19, 26)
# Reader3 = Reader(16, 20)
# Reader4 = Reader(16, 20)
