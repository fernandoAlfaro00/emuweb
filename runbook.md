## Pulse audio

crear interface de audio 
pw-cli create-node adapter '{ factory.name=support.null-audio-sink node.name=my-sink media.class=Audio/Sink object.linger=true audio.position=[FL FR FC LFE RL RR] monitor.channel-volumes=true monitor.passthrough=true }'



docker run -it --rm   -v /run/user/1000:/run/user/1000   -e PIPEWIRE_REMOTE=pipewire-0  ubuntu bash 

root
docker run -it --rm   -v /run/user/1000/pipewire-0:/tmp/pipewire-0   -e PIPEWIRE_REMOTE=pipewire-0 -e PIPEWIRE_RUNTIME_DIR=/tmp -e XDG_RUNTIME_DIR=/tmp/runtime ubuntu bash 


instalar en docker emisor
apt update && apt install -y \
    pipewire \
    pulseaudio \
    ffmpeg

parecord --device=my-sink output.wav


