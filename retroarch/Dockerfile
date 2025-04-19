FROM ubuntu:24.04
RUN apt-get update && apt-get install -y locales && rm -rf /var/lib/apt/lists/* \
	&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG=en_US.utf8
ENV DEBIAN_FRONTEND=noninteractivev


# Instalar dependencias básicas
RUN apt update && apt install -y \
    software-properties-common \
    wget \
    curl \
    git \
    unzip \
    retroarch \
    xvfb \
    ffmpeg \
    evtest \
    x11vnc \
    # libgl1 \
    # libxv1 \
    # libxrandr2 \
    # libxi6 \
    # libxss1 \
    # libxcursor1 \
    # libxcomposite1 \
    # libpulse0 \
    # libudev1 \
    # libxdamage1 \
    # libxinerama1 \
    # libgtk-3-0 \
    # libdbus-glib-1-2 \
    # dbus-x11 \
    ca-certificates 



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
COPY ./retroarch.cfg /root/.config/retroarch/retroarch.cfg

# RUN mkdir -p /root/.config/retroarch/autoconfig/udev
# COPY ./gamepad.cfg /root/.config/retroarch/autoconfig/gamepad.cfg

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]