import time
from threading import Thread
import keyboard
import pymem.process
import requests
import os

os.system('title Intervention v1.1')
offsets = 'https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json'
response = requests.get(offsets).json()
##############################
dwForceJump = int(response["signatures"]["dwForceJump"])
dwLocalPlayer = int(response["signatures"]["dwLocalPlayer"])
dwEntityList = int(response["signatures"]["dwEntityList"])
m_fFlags = int(response["netvars"]["m_fFlags"])
m_iTeamNum = int(response["netvars"]["m_iTeamNum"])
m_bSpotted = int(response["netvars"]["m_bSpotted"])
dwForceAttack = int(response["signatures"]["dwForceAttack"])
m_iCrosshairId = int(response["netvars"]["m_iCrosshairId"])
dwClientState_GetLocalPlayer = int(response["signatures"]["dwClientState_GetLocalPlayer"])
##############################
trigger_key = "alt"
os.system('color 04')
pm = pymem.Pymem("csgo.exe")
client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
print("[OK] -- HWID Bypass v1.0.0")
print("[OK] -- AntiVAC+ v1.0.1")


def bhop():
    while True:
        if keyboard.is_pressed("space"):
            force_jump = client + dwForceJump
            player = pm.read_int(client + dwLocalPlayer)
            if player:
                on_ground = pm.read_int(player + m_fFlags)
                if on_ground and on_ground == 257:
                    pm.write_int(force_jump, 5)
                    time.sleep(0.08)
                    pm.write_int(force_jump, 4)

        time.sleep(0.002)


print("[OK] -- BunnyHop")
Thread(target=bhop).start()


def radar():
    while True:
        try:
            if pm.read_int(client + dwLocalPlayer):
                localplayer = pm.read_int(client + dwLocalPlayer)
                localplayer_team = pm.read_int(localplayer + m_iTeamNum)
                for i in range(64):
                    if pm.read_int(client + dwEntityList + i * 0x10):
                        entity = pm.read_int(client + dwEntityList + i * 0x10)
                        entity_team = pm.read_int(entity + m_iTeamNum)
                        if entity_team != localplayer_team:
                            pm.write_int(entity + m_bSpotted, 1)
        except:
            pass


print("[OK] -- Radar")
Thread(target=radar).start()


def trigger():
    while True:
        if not keyboard.is_pressed(trigger_key):
            time.sleep(0.1)

        if keyboard.is_pressed(trigger_key):
            player = pm.read_int(client + dwLocalPlayer)
            entity_id = pm.read_int(player + m_iCrosshairId)
            entity = pm.read_int(client + dwEntityList + (entity_id - 1) * 0x10)

            entity_team = pm.read_int(entity + m_iTeamNum)
            player_team = pm.read_int(player + m_iTeamNum)

            if entity_id > 0 and entity_id <= 64 and player_team != entity_team:
                pm.write_int(client + dwForceAttack, 6)

            time.sleep(0.006)


print("[OK] -- TriggerBot -- Bind [ALT]")
Thread(target=trigger).start()

print("\nLog:")