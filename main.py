from network import LoRa
import binascii
import socket
import time

# Initialize LoRa in LORAWAN mode.
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.AU915, adr=False, tx_retries=0, device_class=LoRa.CLASS_A)

# credentials
APP_EUI = 'XXX'
APP_KEY = 'YYY'

# remove default channels
for i in range(16, 65):
    lora.remove_channel(i)

for i in range(66, 72):
    lora.remove_channel(i)

# create an OTA authentication params
app_eui = binascii.unhexlify(APP_EUI.replace(' ',''))
app_key = binascii.unhexlify(APP_KEY.replace(' ',''))

print("Joining")
# join a network using OTAA if not previously done
lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

# wait until the module has joined the network
while not lora.has_joined():
    print("attempt...")
    time.sleep(2.5)
