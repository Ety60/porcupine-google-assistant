# Google assistant with Porcupine hotword detection
This script integrates Picovoice porcupine with Google Assistant SDK on the Raspberry Pi. With this script you can activate your Google Assistant with a costum hotword.

## Requirements

- The Google Assistant SDK should be installed and the `googlesamples-assistant-pushtotalk` command should work on your Raspberry Pi.
- Internet connection

## Installation

#### Install porcupine
In the terminal type:
```sh
pip install pvporcupine
```

#### Clone the current directory into your Downloads folder
```sh
cd ~/Downloads && gh repo clone Ety60/porcupine-google-assistant
```

#### Create an account on picovoice.ai
Go to [Picovoice.ai](https://console.picovoice.ai/signup) and follow the signup instructions.

#### Fill in your Acces Key
Go to your [Picovoice Console](https://console.picovoice.ai/), click on "Show AccesKey" and copy the key.
In the porcupine.py file, change YOUR_ACCES_KEY with the acces key you just copied. You can also add or remove costum wakewords by editing the keywords variable.
```sh
nano ~/Downloads/porcupine-google-assistant/porcupine.py
```

#### Replace the pushtotalk.py file
In order to integrate porcupine in Google Assistant, replace the pushtotalk.py file form Google with the costum one from this directory.
```sh
rm ~/env/lib/python3.7/site-packages/googlesamples/assistant/grpc/pushtotalk.py && cp ~/Downloads/porcupine-google-assistant/pushtotalk.py ~/env/lib/python3.7/site-packages/googlesamples/assistant/grpc/
```
Copy the porcupine.py file to the googlesamples directory.
```sh
cp ~/Downloads/porcupine-google-assistant/porcupine.py ~/env/lib/python3.7/site-packages/googlesamples/assistant/grpc/
```

#### Run the assistant
You are done! To activate the assistant with hotword detection, run the following command:
```sh
googlesamples-assistant-pushtotalk
```



