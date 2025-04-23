FROM ubuntu:24.04
RUN apt-get update && apt-get install -y locales && rm -rf /var/lib/apt/lists/* \
	&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG=en_US.utf8
ENV DEBIAN_FRONTEND=noninteractivev

ARG src=".config/autoconfig/NES Virtual Gamepad.cfg"
ARG target="/root/.config/retroarch/autoconfig/udev/NES Virtual Gamepad.cfg"

# Instalar dependencias básicas
RUN apt update && apt install -y \
    software-properties-common \
    wget \
    unzip \
    retroarch \
    xvfb \
    ffmpeg \
    evtest \
    x11vnc 
    # dbus-x11 \
    # ca-certificates 



#depedencias de pipewire
RUN apt update && apt install -y \
    pipewire-alsa \
    pipewire \
    alsa-utils 

RUN wget -O /tmp/nestopia_libretro.so.zip \
  https://buildbot.libretro.com/nightly/linux/x86_64/latest/nestopia_libretro.so.zip \
   && unzip /tmp/nestopia_libretro.so.zip -d /usr/lib/x86_64-linux-gnu/libretro


# Crear un usuario no root
# RUN useradd -m retro && usermod -a -G video retro
# USER retro
# WORKDIR /home/retro

# Carpeta para las ROMs y configuración
RUN mkdir -p /root/roms /root/config /root/.config/retroarch
COPY ./.config/retroarch.cfg /root/.config/retroarch/retroarch.cfg

RUN mkdir -p /root/.config/retroarch/autoconfig/udev
COPY ${src} ${target}

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]