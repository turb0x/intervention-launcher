import time
import ctypes
import pymem
import requests
import keyboard
import os

os.system('title Intervention Skin Changer v1.0')
os.system('color 04')
offsets = 'https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json'
response = requests.get( offsets ).json()

dwClientState = int( response["signatures"]["dwClientState"] )
dwLocalPlayer = int(response['signatures']['dwLocalPlayer'])
m_hMyWeapons = int(response['netvars']['m_hMyWeapons'])
dwEntityList = int(response["signatures"]["dwEntityList"])
m_iItemDefinitionIndex = int(response["netvars"]["m_iItemDefinitionIndex"])
m_OriginalOwnerXuidLow = int(response["netvars"]["m_OriginalOwnerXuidLow"])
m_iItemIDHigh = int(response["netvars"]["m_iItemIDHigh"])
m_nFallbackPaintKit = int(response["netvars"]["m_nFallbackPaintKit"])
m_iAccountID = int(response["netvars"]["m_iAccountID"])
m_nFallbackStatTrak = int(response["netvars"]["m_nFallbackStatTrak"])
m_nFallbackSeed = int(response["netvars"]["m_nFallbackSeed"])
m_flFallbackWear = int(response["netvars"]["m_flFallbackWear"])

user32 = ctypes.windll.user32

pm = pymem.Pymem( "csgo.exe" )
client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
engine = pymem.process.module_from_name(pm.process_handle, "engine.dll").lpBaseOfDll

def GetWindowText(handle, length=100):

    window_text = ctypes.create_string_buffer(length)
    user32.GetWindowTextA(
        handle,
        ctypes.byref(window_text),
        length
    )

    return window_text.value.decode('cp1252')


def GetForegroundWindow():

    return user32.GetForegroundWindow()

def change_skin():
    akpaint = 639
    awppaint = 736
    usppaint = 653
    deaglepaint = 962
    glockpaint = 957
    fivepaint = 837
    ppaint = 678
    tecpaint = 889
    mapaint = 309
    mspaint = 946
    galilpaint = 661
    famaspaint = 919
    augpaint = 455
    sgpaint = 897
    scoutpaint = 624
    macpaint = 947
    mpsevpaint = 696
    mpninpaint = 609
    pppaint = 542
    pneunpaint = 359
    umppaint = 802
    magpaint = 948
    novpaint = 537
    sawpaint = 256
    xmpaint = 850
    revolverpaint = 38
    czpaint = 643
    dualiespaint = 658
    p2000paint = 389
    mp5paint = 810
    negevpaint = 763
    m249paint = 469
    g3sg1paint = 438
    scarpaint = 954
    engine_state = pm.read_int(engine + dwClientState)
    while True:
        if not GetWindowText( GetForegroundWindow() ) == "Counter-Strike: Global Offensive":
            time.sleep( 1 )
            continue
        local_player = pm.read_int(client + dwLocalPlayer)
        if local_player == 0:
            continue
        for i in range(0, 8):
            my_weapons = pm.read_int(local_player + m_hMyWeapons + (i - 1) * 0x4) & 0xFFF
            weapon_address = pm.read_int(client + dwEntityList + (my_weapons - 1) * 0x10)
            if weapon_address:
                weapon_id = pm.read_short(weapon_address + m_iItemDefinitionIndex)

                weapon_owner = pm.read_int(weapon_address + m_OriginalOwnerXuidLow)
                seed = 420
                if weapon_id == 7:
                    fallbackpaint = akpaint
                    seed = 661
                elif weapon_id == 9:
                    fallbackpaint = awppaint
                    seed = 420
                elif weapon_id == 61:
                    fallbackpaint = usppaint
                    seed = 420
                elif weapon_id == 1:
                    fallbackpaint = deaglepaint
                    seed = 420
                elif weapon_id == 4:
                    fallbackpaint = glockpaint
                    seed = 420
                elif weapon_id == 3:
                    fallbackpaint = fivepaint
                    seed = 420
                elif weapon_id == 36:
                    fallbackpaint = ppaint
                    seed = 420
                elif weapon_id == 30:
                    fallbackpaint = tecpaint
                    seed = 420
                elif weapon_id == 16:
                    fallbackpaint = mapaint
                elif weapon_id == 60:
                    fallbackpaint = mspaint
                elif weapon_id == 13:
                    fallbackpaint = galilpaint
                elif weapon_id == 10:
                    fallbackpaint = famaspaint
                elif weapon_id == 8:
                    fallbackpaint = augpaint
                elif weapon_id == 39:
                    fallbackpaint = sgpaint
                elif weapon_id == 40:
                    fallbackpaint = scoutpaint
                elif weapon_id == 17:
                    fallbackpaint = macpaint
                elif weapon_id == 33:
                    fallbackpaint = mpsevpaint
                elif weapon_id == 34:
                    fallbackpaint = mpninpaint
                elif weapon_id == 26:
                    fallbackpaint = pppaint
                elif weapon_id == 19:
                    fallbackpaint = pneunpaint
                elif weapon_id == 24:
                    fallbackpaint = umppaint
                elif weapon_id == 27:
                    fallbackpaint = magpaint
                elif weapon_id == 35:
                    fallbackpaint = novpaint
                elif weapon_id == 29:
                    fallbackpaint = sawpaint
                elif weapon_id == 25:
                    fallbackpaint = xmpaint
                elif weapon_id == 64:
                    fallbackpaint = revolverpaint
                elif weapon_id == 63:
                    fallbackpaint = czpaint
                elif weapon_id == 2:
                    fallbackpaint = dualiespaint
                elif weapon_id == 32:
                    fallbackpaint = p2000paint
                elif weapon_id == 23:
                    fallbackpaint = mp5paint
                elif weapon_id == 28:
                    fallbackpaint = negevpaint
                elif weapon_id == 14:
                    fallbackpaint = m249paint
                elif weapon_id == 11:
                    fallbackpaint = g3sg1paint
                elif weapon_id == 38:
                    fallbackpaint = scarpaint
                else:
                    continue
                pm.write_int(weapon_address + m_iItemIDHigh, -1)
                pm.write_int(weapon_address + m_nFallbackPaintKit, fallbackpaint)
                pm.write_int(weapon_address + m_iAccountID, weapon_owner)
                pm.write_int(weapon_address + m_nFallbackSeed, seed)
                pm.write_float(weapon_address + m_flFallbackWear, float(0.000001))

        # time.sleep(20)
        if keyboard.is_pressed("f6"):
            pm.write_int(engine_state + 0x174, -1)
print("[OK] -- Skin Changer -- Bind [F6]")

if __name__ == "__main__":
    change_skin()
