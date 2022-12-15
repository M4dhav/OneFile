import requests
dic = {"compress": "https://ibb.co/bN0Rmq8", "decompress": "https://ibb.co/F6W4fC3", "decrypt":"https://github.com/M4dhav/open-file-winrar-alternative/blob/main/decrypt_icon.jpg", "encrypt":"https://github.com/M4dhav/open-file-winrar-alternative/blob/main/encrpyt_icon.jpg"}
keys = list(dic.keys())
for i in keys:
    url = dic[i]
    file_name = i + ".png"
    response = requests.get(url)
    if response.status_code:
        fp = open(file_name, 'wb')
        fp.write(response.content)
        fp.close()