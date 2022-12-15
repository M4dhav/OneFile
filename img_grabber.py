import requests
import os
dic = {"compress": "https://i.ibb.co/frgGFBP/compress-icon.jpg", "decompress": "https://i.ibb.co/1ZnGpjQ/decompress-icon.jpg", "decrypt":"https://i.ibb.co/hL9qZMj/decrypt-icon.jpg", "encrypt":"https://i.ibb.co/prwryRc/encrpyt-icon.jpg", "logo": "https://i.ibb.co/ZgPWNdb/final-One-Filelogo.jpg"}
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