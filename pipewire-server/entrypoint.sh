#!/bin/bash
set -e

mkdir -p /run/dbus
dbus-daemon --system --fork

Xvfb -screen $DISPLAY 1920x1080x24 &

mkdir -p /dev/snd

echo "Starting PipeWire..."
pipewire &
echo "Starting wireplumber..."
wireplumber &
echo "Starting pulse..."
pipewire-pulse &

sleep 5
pactl load-module module-virtual-sink sink_name=v1
pactl set-default-sink input.v1
pactl set-default-source input.v1.monitor

tail -f /dev/null