import requests
import os
dic = {"compress": "https://i.ibb.co/HXfHfHr/compress-new.jpg", "decompress": "https://i.ibb.co/N6hwjWs/decompress-new.jpg", "decrypt":"https://i.ibb.co/3cTCSF7/appstore1024.jpg", "encrypt":"https://i.ibb.co/kqfKMv2/encrypt.jpg", "logo": "https://i.ibb.co/ZgPWNdb/final-One-Filelogo.jpg"}
keys = list(dic.keys())
for i in keys:
    url = dic[i]
    file_name = i + ".png"
    if os.path.exists(file_name):
        pass
    else:
        response = requests.get(url)
        if response.status_code:
            fp = open(file_name, 'wb')
            fp.write(response.content)
            fp.close()