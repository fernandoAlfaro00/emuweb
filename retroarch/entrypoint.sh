#!/bin/bash
set -e

rm -f /tmp/.X99-lock
Xvfb :99 -screen 0 1280x720x24 &
DBUS_FATAL_WARNINGS=0 DISPLAY=:99 XDG_RUNTIME_DIR=/tmp/runtime retroarch --verbose -L /usr/lib/x86_64-linux-gnu/libretro/nestopia_libretro.so /app/roms/Mario.nes &
pipewire-pulse &
sleep 2
ffmpeg -f x11grab -video_size 1280x720 -i :99 -f v4l2 /dev/video1

ffmpeg \
  -f x11grab -video_size 1280x720 -i :99 \
  -f pulse -i default \
  -c:v rawvideo -c:a aac \
  -f v4l2 /dev/video1