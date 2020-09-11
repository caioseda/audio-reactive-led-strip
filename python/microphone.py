import time
import numpy as np
import pyaudio
import config

stereoId = ""
def getInputDevices():
    global stereoId 
    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')
    stereoId = p.get_default_input_device_info().get("index")
    devices = []
    for i in range(0, numdevices):
        if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
            name = p.get_device_info_by_host_api_device_index(0, i).get('name')
            devices.append(name)
            if name.split(" ")[0] == "Stereo":
                stereoId = p.get_device_info_by_host_api_device_index(0, i).get('index')
    return devices
getInputDevices()

def start_stream(callback):
    print("stream iniciada")
    p = pyaudio.PyAudio()
    frames_per_buffer = int(config.MIC_RATE / config.FPS)
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=config.MIC_RATE,
                    input=True,
                    input_device_index = stereoId ,
                    frames_per_buffer=frames_per_buffer)
    overflows = 0
    prev_ovf_time = time.time()

    visualization_need = True
    
    # effect = visualization.visualization_effect.__name__
    it = 0
    print(visualization_need)
    while visualization_need:
        try:
            y = np.fromstring(stream.read(frames_per_buffer, exception_on_overflow=False), dtype=np.int16)
            y = y.astype(np.float32)
            stream.read(stream.get_read_available(), exception_on_overflow=False)
            visualization_need = callback(y)
            print(it, visualization_need)
            it += 1
        except IOError:
            overflows += 1
            if time.time() > prev_ovf_time + 1:
                prev_ovf_time = time.time()
                print('Audio buffer has overflowed {} times'.format(overflows))
    stream.stop_stream()
    stream.close()
    p.terminate()
    print("stream fechada")
if __name__ == "__main__":
    devices = getInputDevices()
    print(devices)