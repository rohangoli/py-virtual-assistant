For running wxpython GUI apps in WSL2:

In Windows,

1. Install VcXsrv https://sourceforge.net/projects/vcxsrv/
2. Start VcXsrv with server number '0' on the first screen with Public Access
3. Disable Firewall for Guest/Public Network

In WSL,
    sudo apt install ubuntu-desktop mesa-utils
    sudo apt install x11-apps ubuntu-restricted-extras
export DISPLAY=$(grep -m 1 nameserver /etc/resolv.conf | awk '{print $2}'):0.0
export LIBGL_ALWAYS_INDIRECT=0
export LIBGL_ALWAYS_SOFTWARE=0
    
    For testing GUI,
        run 'xeyes'/'glxgears'

For more details:
https://discourse.ubuntu.com/t/getting-graphical-applications-to-work-on-wsl2/11868
https://github.com/Adriankhl/wsl2-xwin-audio
https://elecming.medium.com/the-ultimate-emacs-hacking-tutorial-in-windows-10-wsl-2-2fc4e9a899b0
https://carette.xyz/posts/setup_sound_video_wsl2/
https://www.linuxuprising.com/2021/03/how-to-get-sound-pulseaudio-to-work-on.html

For Pulse Audio,
In Windows,
    1. Download and extract Pulse on C:\
    2. create config.pa configuration file to serve tcp audio
    3. Download and Install NSSM on windows for service creation
    4. Create Windows Serive
    5. Start windows service

In WSL2,
    1. Export env variable
export HOST_IP="$(ip route |awk '/^default/{print $3}')"
export PULSE_SERVER="tcp:$HOST_IP"

Test WXPython GUI in WSL2
```
import wx

app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "Hello World")
frame.Show(True)
app.MainLoop()
```

Test PulseAudio in Windows
```
paplay /usr/share/sounds/freedesktop/stereo/bell.oga
```

Test Espeak
```
import pyttsx
engine = pyttsx.init()
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()
```

export LD_LIBRARY_PATH=/usr/local/lib
export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig

Pulse Audio v7.1 -> config.pa
```
load-module module-native-protocol-tcp auth-ip-acl=127.0.0.1;172.16.0.0/12
load-module module-esound-protocol-tcp auth-ip-acl=127.0.0.1;172.16.0.0/12
load-module module-waveout sink_name=output source_name=input record=1
```

speaker-test -c6 -twav
aplay --list-devices

https://community.rhasspy.org/t/how-to-use-rhasspy-with-windows-subsystem-for-linux-wsl/984
aplay & arecord configured with pulse with this

Need to try: RTC Mix for WSL2 http://sites.music.columbia.edu/brad/osx-windows-new-RTcmixes/wsl2-RTcmix.html

Change Speech Recognition Microphone Device for recording
https://www.programcreek.com/python/example/107719/speech_recognition.Microphone