FROM ubuntu:24.04

ENV LANG=en_US.utf8
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y locales && rm -rf /var/lib/apt/lists/* \
    && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8

RUN apt update && apt install -y \
    dbus-x11 \
    rtkit \
    xvfb \
    pipewire \
    pipewire-pulse \
    wireplumber \
    pulseaudio-utils \
    libportaudio2 \
    pipewire-audio-client-libraries \
    alsa-utils


ENV DISABLE_RTKIT=y
ENV XDG_RUNTIME_DIR=/tmp
ENV PIPEWIRE_RUNTIME_DIR=/tmp
ENV PULSE_RUNTIME_DIR=/tmp
ENV DISPLAY=:0.0
    

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

CMD ["/entrypoint.sh"]
