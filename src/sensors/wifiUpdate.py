def update_wifi(file,ssid,password): 
    raw = open(file, "r+")
    contents = raw.read().split("\n")
    raw.seek(0)                        # <- This is the missing piece
    raw.truncate()
    raw.write('country=CZ\nctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev\n update_config=1\n network={\n ssid="{ssid}"\npsk="{password}"\n}')
    raw.close()