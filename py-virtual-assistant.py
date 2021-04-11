import wx
import wikipedia
import wolframalpha
import espeak
import speech_recognition as sr

espeak.init()
speaker = espeak.Espeak()
speaker.say("Welcome to PyVirtualAssistant!")
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(450,100),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
            wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="PyVirtualAssistant")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl =wx.StaticText(panel,
            label="Hello! I'm PyVirtualAssistant. How can I help you?")
        my_sizer.Add(lbl,0,wx.ALL,5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER, size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0 , wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()
    
    def OnEnter(self, event):
        input = self.txt.GetValue()
        input = input.lower()
        app_id = "H4K399-TUE2PT76GV"
        client = wolframalpha.Client(app_id)
        if input == '':
            record = sr.Recognizer()
            with sr.Microphone() as source:
                audio = record.listen(source)
            try:
                self.txt.SetValue(record.recognize_google(audio).lower())
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio!")
            except sr.RequestError as e:
                print("Could not request results from Google Speech recognition service; {0}".format(e))
        else:
            try:
                # Wolfralpha API
                res = client.query(input)
                answer = next(res.results).text
                print(answer)
                speaker.say("The answer is "+answer)
            except:
                # Wikipedia API
                input = input.split(' ')
                input = " ".join(input[2:])
                speaker.say("Searched for "+input)
                print(wikipedia.summary(input,sentences=2))

if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()