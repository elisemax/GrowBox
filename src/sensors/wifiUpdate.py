def update_wifi(file,ssid,password): 
    raw = open(file, "r+")
    contents = raw.read().split("\n")
    raw.seek(0)                        # <- This is the missing piece
    raw.truncate()
    str ='country=CZ\nctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev\nupdate_config=1\nnetwork={\n ssid="'+ssid+'"\n psk="'+password+'"\n}'
    raw.write(str)
    raw.close()