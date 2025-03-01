import socket
import pyaudio

# Socket
HOST = socket.gethostname()
PORT = 5000

# Audio
CHUNK = 1024 * 4
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 3
WAVE_OUTPUT_FILENAME = "output.wav"
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("Recording")

with socket.socket() as client_socket:
    client_socket.connect((HOST, PORT))
    while True:
        data = stream.read(CHUNK)
        print(type(data))
        client_socket.send(data)