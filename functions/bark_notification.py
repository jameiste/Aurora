from BarkNotificator import BarkNotificator

from environment.variables import BARK_KEY

def send_bark_notification(title: str, text:str):
    bark = BarkNotificator(device_token=BARK_KEY)
    bark.send(title=title, 
        content=text,
        target_url="https://aurorareach.com/sightings/2025/10/29/ddd9ecb2c1594fbf853ba108d51054a4",
        icon_url="https://cdn-icons-png.flaticon.com/128/2912/2912019.png"
    )