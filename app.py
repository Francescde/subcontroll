import lgtv
from flask import Flask

app = Flask(__name__)


# Choose the serial port which is connected to the RS232 port of your TV
# This may be of the form /dev/ttyUSBx for USB dongles
device = '/dev/ttyS0'

lg = lgtv.LGTV(device)

# Set the input source to HDMI1
lg.setsource(lgtv.LG_SOURCE_HDMI1)

# Set the sound to 20%
lg.setsound(20)


@app.route('/openTv')
def hello_world():
    # Power ON the television
    lg.on()
    return '{"status":"open"}'


@app.route('/closeTv')
def end_world():
    lg.off()
    return '{"status":"close"}'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
