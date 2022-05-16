import pvporcupine
import pyaudio
import struct

class Porcupine: 

    def __init__(self):
        self.porcupine = pvporcupine.create(
            access_key={ACCES_KEY},
            keywords=['picovoice', 'bumblebee','hey siri','Charlie']
        )

        self.pa = pyaudio.PyAudio()

        self.audioStream = self.pa.open(
            rate=self.porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=self.porcupine.frame_length
        )

    def activate(self):
        try:
            

            while True:
                pcm = self.audioStream.read(self.porcupine.frame_length)
                pcm = struct.unpack_from("h" * self.porcupine.frame_length, pcm)

                keyword_index = self.porcupine.process(pcm)

                if keyword_index >= 0:
                    print("hotword detected")
                    self.audioStream.close()
                    break
        
        
        except KeyboardInterrupt:
            if self.porcupine is not None:
                self.porcupine.delete()
                print("deleting porc")

            if self.audioStream is not None:
                self.audioStream.close()
                print("closing stream")

            if self.pa is not None:
                self.pa.terminate()
                print("terminating pa")
            
                exit(0)
                    
        finally:
            if self.porcupine is not None:
                self.porcupine.delete()
                print("deleting porc")

            if self.audioStream is not None:
                self.audioStream.close()
                print("closing stream")

            if self.pa is not None:
                self.pa.terminate()
                print("terminating pa")
