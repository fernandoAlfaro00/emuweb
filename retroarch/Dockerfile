FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Instalar dependencias básicas
RUN apt update && apt install -y \
    software-properties-common \
    wget \
    curl \
    git \
    x11vnc \
    xvfb \
    retroarch \
    ffmpeg \
    libgl1 \
    libxv1 \
    libxrandr2 \
    libxi6 \
    libxss1 \
    libxcursor1 \
    libxcomposite1 \
    libasound2 \
    libpulse0 \
    libudev1 \
    libxdamage1 \
    libxinerama1 \
    libgtk-3-0 \
    libdbus-glib-1-2 \
    ca-certificates \
    unzip \
    && apt clean

RUN wget -O /tmp/nestopia_libretro.so.zip  https://buildbot.libretro.com/nightly/linux/x86_64/latest/nestopia_libretro.so.zip && unzip /tmp/nestopia_libretro.so.zip -d /usr/lib/x86_64-linux-gnu/libretro



# Crear un usuario no root
RUN useradd -m retro && usermod -a -G video retro
USER retro
WORKDIR /home/retro

# Carpeta para las ROMs y configuración
RUN mkdir -p /home/retro/roms /home/retro/config /home/retro/.config/retroarch
COPY ./retroarch.cfg /home/retro/.config/retroarch/retroarch.cfg

# ENTRYPOINT ["retroarch"]
# CMD ["-L", "/usr/lib/x86_64-linux-gnu/libretro/nestopia_libretro.so", "/home/retro/roms/mario.nes"]
