import os
import tkinter as tk
import codecs

# Uebergreifende Variablen
errorCodeText = "Ready"
errorCodeColor = "orange"

# Definieren Command
def CreateBTN():
    SSIDText = SSIDTextbox.get()
    PSKText = PSKTextbox.get()

    if not SSIDText:
        text = errorCode["text"]
        fg = errorCode["fg"]
        errorCode["text"] = "Insert SSID!"
        errorCode["fg"] = "red"

    else:
        SSIDText = SSIDTextbox.get()
        SSIDNum = bytes(SSIDText, 'utf-8')
        SSIDNum = SSIDText.encode('utf-8')
        SSIDHex = codecs.encode(SSIDNum, "hex")
        SSIDHexS = str(SSIDHex)[2:-1]

        if not PSKText:
            text = errorCode["text"]
            fg = errorCode["fg"]
            errorCode["text"] = "Insert PSK!"
            errorCode["fg"] = "red"

        else:
            text = errorCode["text"]
            fg = errorCode["fg"]
            errorCode["text"] = "Success"
            errorCode["fg"] = "green"

            wlnxml = open("wln.xml", 'w')
            wlnxml.write('<?xml version="1.0"?>\r<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">\r\t<name>' + SSIDText + '</name>\r\t<SSIDConfig>\r\t\t<SSID>\r\t\t\t<hex>' + SSIDHexS + '</hex>\r\t\t\t<name>' + SSIDText + '</name>\r\t\t</SSID>\r\t</SSIDConfig>\r\t<connectionType>ESS</connectionType>\r\t<connectionMode>auto</connectionMode>\r\t<MSM>\r\t\t<security>\r\t\t\t<authEncryption>\r\t\t\t\t<authentication>WPA2PSK</authentication>\r\t\t\t\t<encryption>AES</encryption>\r\t\t\t\t<useOneX>false</useOneX>\r\t\t\t</authEncryption>\r\t\t\t<sharedKey>\r\t\t\t\t<keyType>passPhrase</keyType>\r\t\t\t\t<protected>false</protected>\r\t\t\t\t<keyMaterial>' + PSKText + '</keyMaterial>\r\t\t\t</sharedKey>\r\t\t</security>\r\t</MSM>\r\t<MacRandomization xmlns="http://www.microsoft.com/networking/WLAN/profile/v3">\r\t\t<enableRandomization>false</enableRandomization>\r\t\t<randomizationSeed>1141186600</randomizationSeed>\r\t</MacRandomization>\r</WLANProfile>')
            os.startfile("wln.xml")

# Grundaufbau GUI
window = tk.Tk()
window.title("Wlan Profile Creator")
window.geometry('200x180')

SSID = tk.Label(text="SSID:")
SSID.pack()
SSIDTextbox = tk.Entry()
SSIDTextbox.pack()

PSK = tk.Label(text = "Preshared Key:")
PSK.pack()
PSKTextbox = tk.Entry()
PSKTextbox.pack()

blanc1 =tk.Label(text = " ")
blanc1.pack()

create = tk.Button(
    master = window,
    text = "Create",
    command = lambda index = 1: CreateBTN()
)
create.pack()

blanc2 =tk.Label(text = " ")
blanc2.pack()

errorCode = tk.Label(
    bg="white",
    fg=errorCodeColor,
    width=20,
    text=errorCodeText
)
errorCode.pack()

window.mainloop()
