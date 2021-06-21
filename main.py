from requests import post
from time import strftime
# Script by poggersbutnot. Github: poggersbutnot
print("Welcome! Script Start[:"+ strftime("%H:%M:%S") + ":]")

print('<' + '=' * 20 + "[Settings Area]" + '=' * 20 + '>')

device = str(input("Enter A Device OS: (Default: 101)(IOS: 0)(Android: 1)(MetroPlayerX64: 2)(Amazon: 3) "))
if not device:
    device = '101'
    print("Device Automatically set to Default(" + device + ")")
elif device:
    print("Device remotley set to ", device)

id = str(input('Player ID to search: '))
if not id:
    id = '192819483'
    print("ID auto set to a banned ID ("+ id + ')')
elif id:
    print("ID set to ("+ id + ")")

ver = str(input("Version: "))
if not ver:
    ver = '21.4.1'
    print("Version has been automatically set to: "+ ver)
elif ver is ver:
    print("Version Remotley set by user to "+ ver)

url = 'https://secure.pixelgunserver.com/pixelgun3d-config/getBanList.php'
if url is None:
    url = 'https://secure.pixelgunserver.com/pixelgun3d-config/getBanList.php'
    print("Auto applied url "+ url + " as the main url.")
elif url != 'https://secure.pixelgunserver.com/pixelgun3d-config/getBanList.php':
    url = 'https://secure.pixelgunserver.com/pixelgun3d-config/getBanList.php'
    print("You may have edited the url, therefore, the main url was set to ", url)
else:
    print(" Connected ✅")
data = {
    'app_version': device + ":" + ver,
    'id': id
}
r = post(url, data=data)
r = r.text
while data['id'] is None:
    break
if(r == '1'):
    print("User "+ data['id'] + " is banned!")
elif(r == '0'):
    print("User "+ data['id'] + " Not Banned!")
elif(r == '-1'):
    print("This usually happens if you are a developer.")
elif(r == "File not found."):
    print("PHP File was deleted.")  
else:
    print("pixelgun-config may have been deleted (or the servers were swapped.)")
