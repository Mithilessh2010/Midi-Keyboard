import time
import board
import keypad
import rotaryio
import displayio
import busio
import terminalio
import audiobusio
import audiocore
import usb_midi
import adafruit_midi

from fourwire import FourWire
from adafruit_display_text import label
from adafruit_st7735r import ST7735R
from adafruit_midi.note_on import NoteOn
from adafruit_midi.note_off import NoteOff

rows = [board.GP0, board.GP1, board.GP2]
cols = [board.GP3, board.GP4, board.GP5]

matrix = keypad.KeyMatrix(
    row_pins=rows,
    column_pins=cols,
    columns_to_anodes=True
)

encoder = rotaryio.IncrementalEncoder(board.GP6, board.GP7)
last_enc_pos = encoder.position

displayio.release_displays()

spi = busio.SPI(clock=board.GP10, MOSI=board.GP11)
display_bus = FourWire(
    spi,
    command=board.GP12,
    chip_select=board.GP13,
    reset=board.GP14
)

display = ST7735R(
    display_bus,
    width=128,
    height=160,
    rotation=90
)

splash = displayio.Group()
display.root_group = splash

text_label = label.Label(
    terminalio.FONT,
    text="Mini MIDI Magic",
    color=0xFFFFFF,
    x=10,
    y=20
)

splash.append(text_label)

dac = audiobusio.I2SOut(
    bit_clock=board.GP18,
    word_select=board.GP19,
    data=board.GP20
)

try:
    wav_file = open("sound.wav", "rb")
    wav = audiocore.WaveFile(wav_file)
    dac.play(wav)
    while dac.playing:
        pass
except OSError:
    pass

midi = adafruit_midi.MIDI(
    midi_in=usb_midi.ports[0],
    midi_out=usb_midi.ports[1],
    in_channel=0,
    out_channel=0
)

while True:
    event = matrix.events.get()
    if event:
        note = 60 + event.key_number
        if event.pressed:
            midi.send(NoteOn(note, 127))
        else:
            midi.send(NoteOff(note, 0))

    pos = encoder.position
    if pos != last_enc_pos:
        last_enc_pos = pos

    time.sleep(0.01)
