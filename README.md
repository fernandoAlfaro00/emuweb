https://buildbot.libretro.com/nightly/linux/x86_64/latest/


Xvfb :99 -screen 0 1280x720x24 &

XDG_RUNTIME_DIR=/tmp/runtime DISPLAY=:99 retroarch -L /home/retro/config/nestopia_libretro.so /home/retro/roms/roms/contra.nes &

ffmpeg -video_size 1280x720 -framerate 30 -f x11grab -i :99 -t 10 -preset ultrafast -c:v libx264 salida2.mp4



ffmpeg -f x11grab -video_size 1280x720 -i :99 -f v4l2 salida2.mp4





docker run --rm -p 8000:8000 \
    -e DISPLAY=:99 \
    --link retroarch-container \
    mpromonet/webrtc-streamer:latest \
    "ffmpeg -f x11grab -video_size 1280x720 -i :99 -f v4l2 /dev/video0"




XDG_RUNTIME_DIR=/tmp/runtime DISPLAY=:99 retroarch -L /usr/lib/x86_64-linux-gnu/libretro/nestopia_libretro.so /app/roms/contra.nes &


sudo apt install v4l2loopback-dkms

sudo modprobe v4l2loopback video_nr=1

sudo modprobe uinput
