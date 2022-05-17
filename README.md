# Google assistant with porcupine hotword detection


This script integrates Picovoice porcupine with Google Assistant SDK on the Raspberry Pi. With this script you can activate your Google Assistant with a costum hotword.

## Requirements

- The Google Assistant SDK should be installed and the `googlesamples-assistant-pushtotalk` command should work on your device.
- Internet connection

## Installation

#### First install porcupine
In the terminal type:
`
pip install pvporcupine
`

#### Clone the current directory into your Downloads folder
`cd ~/Downloads && gh repo clone Ety60/porcupine-google-assistant`


#### Create an account on picovoice.ai
Go to [Picovoice.ai](https://console.picovoice.ai/signup) and follow the signup instructions.

#### Fill in your Acces Key
Go to your [Picovoice Console](https://console.picovoice.ai/), click on "Show AccesKey" and copy the key.
Then edit the porcupine.py file (`nano ~/Downloads/porcupine-google-assistant/porcupine.py`) and change YOUR_ACCES_KEY with the acces key you just copied. You can also add or remove costum wakewords by editing the keywords variable.

#### Replace the pushtotalk.py file
In order to integrate 

