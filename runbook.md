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




ejemplo conectar audio de un sistema a otro pipewire 

export SERVER_AUDIO=debian

receptor 
pactl load-module module-native-protocol-tcp port=4656 listen=0.0.0.0 auth-anonymous=true

emite 
pactl load-module module-tunnel-sink server=tcp:$SERVER_AUDIO:4656


# RUN wget -q --show-progress -P /tmp https://buildbot.libretro.com/assets/frontend/autoconfig.zip && unzip -q /tmp/autoconfig.zip -d  /root/.config/retroarch/autoconfig && rm /tmp/autoconfig.zip
