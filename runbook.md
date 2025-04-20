## Pulse audio

crear interface de audio 
pw-cli create-node adapter '{ factory.name=support.null-audio-sink node.name=my-sink media.class=Audio/Sink object.linger=true audio.position=[FL FR FC LFE RL RR] monitor.channel-volumes=true monitor.passthrough=true }'


user
docker run -it --rm \
  -v /run/user/1000/pipewire-0:/run/user/1000/pipewire-0 \
  -e PIPEWIRE_REMOTE=pipewire-0 \
  --user $(id -u):$(id -g) \
  ubuntu bash

root
docker run -it --rm   -v /run/user/1000/pipewire-0:/tmp/pipewire-0   -e PIPEWIRE_REMOTE=pipewire-0 -e PIPEWIRE_RUNTIME_DIR=/tmp -e XDG_RUNTIME_DIR=/tmp/runtime ubuntu bash 


instalar en docker emisor
apt update && apt install -y \
    pipewire \
    pulseaudio \
    ffmpeg


  

parecord --device=my-sink output.wav


pacmd list-sources  | grep name:


ffmpeg \
  -f x11grab -video_size 1280x720 -i :99 \
  -f pulse -i default \
  -c:v rawvideo -c:a aac \
  -f v4l2 /dev/video1