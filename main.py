# import required libraries
from vidgear.gears import CamGear
from vidgear.gears import WriteGear
import cv2

# Open live webcam video stream on first index(i.e. 0) device
stream = CamGear(source=0, logging=True).start()

# define required FFmpeg optimizing parameters for your writer
output_params = {
    "-preset:v": "veryfast",
    "-g": 60,
    "-keyint_min": 60,
    "-sc_threshold": 0,
    "-bufsize": "2500k",
    "-f": "flv",

}

# [WARNING] Change your Twitch Stream Key here:
TWITCH_KEY = "live_XXXXXXXXXX~XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

# Define writer with defined parameters and
writer = WriteGear(
    output_filename="rtmp://live.twitch.tv/app/{}".format(TWITCH_KEY),
    logging=True,
    **output_params
)

# loop over
while True:

    # read frames from stream
    frame = stream.read()

    # check for frame if Nonetype
    if frame is None:
        break

    # {do something with the frame here}

    # write frame to writer
    writer.write(frame)

    # Show output window
    cv2.imshow("Output Frame", frame)

    # check for 'q' key if pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# close output window
cv2.destroyAllWindows()

# safely close video stream
stream.stop()

# safely close writer
writer.close()
# import required libraries
from vidgear.gears import VideoGear
from vidgear.gears import WriteGear
import cv2

# Open live video stream on webcam at first index(i.e. 0) device
stream = VideoGear(source=0).start()

# change with your webcam soundcard, plus add additional required FFmpeg parameters for your writer
output_params = {
    "-input_framerate": stream.framerate,
    "-thread_queue_size": "512",
    "-ac": "2",
    "-ar": "48000",
    "-f": "alsa", # !!! warning: always keep this line above "-i" parameter !!!
    "-i": "hw:1",
}

# Define writer with defined parameters and suitable output filename for e.g. `Output.mp4
writer = WriteGear(output_filename="Output.mp4", logging=True, **output_params)

# loop over
while True:

    # read frames from stream
    frame = stream.read()

    # check for frame if Nonetype
    if frame is None:
        break

    # {do something with the frame here}

    # write frame to writer
    writer.write(frame)

    # Show output window
    cv2.imshow("Output Frame", frame)

    # check for 'q' key if pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# close output window
cv2.destroyAllWindows()

# safely close video stream
stream.stop()

# safely close writer
writer.close()
# import required libraries
from vidgear.gears import CamGear
from vidgear.gears import StreamGear
import cv2

# open any valid video stream(for e.g `foo1.mp4` file)
stream = CamGear(source="foo1.mp4").start()

# add various streams, along with custom audio
stream_params = {
    "-streams": [
        {
            "-resolution": "1280x720",
            "-video_bitrate": "4000k",
        },  # Stream1: 1280x720 at 4000kbs bitrate
        {"-resolution": "640x360", "-framerate": 30.0},  # Stream2: 640x360 at 30fps
    ],
    "-input_framerate": stream.framerate,  # controlled framerate for audio-video sync !!! don't forget this line !!!
    "-audio": [
        "-f",
        "dshow",
        "-i",
        "audio=Microphone (USB2.0 Camera)",
    ],  # assign appropriate input audio-source device and demuxer
}

# describe a suitable manifest-file location/name and assign params
streamer = StreamGear(output="dash_out.mpd", **stream_params)

# loop over
while True:

    # read frames from stream
    frame = stream.read()

    # check for frame if Nonetype
    if frame is None:
        break

    # {do something with the frame here}

    # send frame to streamer
    streamer.stream(frame)

    # Show output window
    cv2.imshow("Output Frame", frame)

    # check for 'q' key if pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# close output window
cv2.destroyAllWindows()

# safely close video stream
stream.stop()

# safely close streamer
streamer.terminate()
