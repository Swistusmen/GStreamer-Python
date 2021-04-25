from threading import Thread
import gi #binding for gstreamer library

gi.require_version("Gst","1.0")

from gi.repository import Gst, GLib

Gst.init()

main_loop=GLib.MainLoop() 
main_loop_thread=Thread(target=main_loop.run)
main_loop_thread.start()

src_demux = "filesrc location=/home/michal/Documents/MyPrograms/PlayingWithGstreamer/beza.mp4! qtdemux name=demux" 
h264_transcode = "demux.video_0"

#Gst.parse_launch("v4l2src ! decodebin ! videoconvert ! autovideosink")
pipeline1="{0} {1} ! queue ! rtph264pay name=pay0 config-interval=1 pt=96".format(src_demux, h264_transcode)
pipeline=Gst.parse_launch(pipeline1)
pipeline.set_state(Gst.State.PLAYING)


try:
    while True:
        sleep(0.1)
except KeyboardInterrupt:
    pass

pipeline.set_state(Gst.State.NULL)
main_loop.quit()
main_loop_thread.join()





