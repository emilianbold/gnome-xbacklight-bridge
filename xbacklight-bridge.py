from pydbus import SessionBus
from gi.repository import GLib
from pydbus import Variant
from os import system

loop = GLib.MainLoop()

bus = SessionBus()
power = bus.get("org.gnome.SettingsDaemon.Power", "/org/gnome/SettingsDaemon/Power")
props = power['org.freedesktop.DBus.Properties']

#props.Set("org.gnome.SettingsDaemon.Power.Screen", "Brightness", Variant("i", 20))

def xbacklight(name, changeDict, someArr):
    if "org.gnome.SettingsDaemon.Power.Screen" == name:
        brightness = changeDict["Brightness"]
        system("xbacklight -set " + str(brightness))

props.PropertiesChanged.connect(xbacklight)

loop.run()
