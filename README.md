# Plataforma emulacion desde el navegador
![](https://github.com/fernandoAlfaro00/emuweb/blob/main/images/ejemplo.png)

## Componenetes
![](https://github.com/fernandoAlfaro00/emuweb/blob/main/images/comunicacion.png)
## Requisitos
- v4l2loopback-dkms (sudo apt install v4l2loopback-dkms)
- uinput


## Pasos Manuales 

### Habilitar modulos

#### v4l2loopback - permite crear dispositivo de video virtuales

```bash
 sudo modprobe  v4l2loopback video_nr=1

 sudo modprobe v4l2loopback video_nr=10 card_label="virtualcam" exclusive_caps=1
```

#### uinput - crear dispositivo de entrada virtuales(mouse, teclado , gamepad)

```bash
 sudo modprobe uinput
```


## Referencias

- https://buildbot.libretro.com/nightly/linux/x86_64/latest/
- https://stackoverflow.com/questions/28985714/run-apps-using-audio-in-a-docker-container/75775875#75775875



## Notas
Crear screen virtual
```bash
Xvfb :99 -screen 0 1280x720x24 &
```
Ejecutar Retroarch
```bash
XDG_RUNTIME_DIR=/tmp/runtime DISPLAY=:99 retroarch -L /home/retro/config/nestopia_libretro.so /home/retro/roms/roms/contra.nes &
```

Test video 
```bash
 ffmpeg -f x11grab -video_size 1280x720 -i :99 -f v4l2 salida2.mp4

 ffmpeg -video_size 1280x720 -framerate 30 -f x11grab -i :99 -t 10 -preset ultrafast -c:v libx264 salida2.mp4

 ffmpeg \
  -f x11grab -video_size 1280x720 -i :99 \
  -f pulse -i default \
  -c:v rawvideo -c:a aac \
  -f v4l2 /dev/video1

```

Test mando virtual
```bash
sudo apt install evtest
sudo chmod 666 /dev/uinput
evtest
```

Test audio

```bash
speaker-test -Dpipewire -c2

```