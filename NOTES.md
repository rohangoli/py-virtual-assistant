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


Test WXPython GUI in WSL2
```
import wx

app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "Hello World")
frame.Show(True)
app.MainLoop()
```