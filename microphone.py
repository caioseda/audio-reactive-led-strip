import time
import numpy as np
import pyaudio
import config
import visualization

def start_stream(callback):
    print("stream iniciada")
    p = pyaudio.PyAudio()
    frames_per_buffer = int(config.MIC_RATE / config.FPS)
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=config.MIC_RATE,
                    input=True,
                    frames_per_buffer=frames_per_buffer)
    overflows = 0
    prev_ovf_time = time.time()
    visualization_need = True
    
    # effect = visualization.visualization_effect.__name__
    while visualization_need:
        try:
            y = np.fromstring(stream.read(frames_per_buffer, exception_on_overflow=False), dtype=np.int16)
            y = y.astype(np.float32)
            stream.read(stream.get_read_available(), exception_on_overflow=False)
            visualization_need = callback(y)
        except IOError:
            overflows += 1
            if time.time() > prev_ovf_time + 1:
                prev_ovf_time = time.time()
                print('Audio buffer has overflowed {} times'.format(overflows))
    stream.stop_stream()
    stream.close()
    p.terminate()
    print("stream fechada")