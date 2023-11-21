

#7-12 matplotlibでリストのデータを可視化する

# %matplotlib inline
# import matplotlib.pyploy as plt
# weight = [68.4,68.0,69.5,68.4,68.6,70.2,71.4,70.8,68.5,68.6,68.3,68.4]

# plt.plot(weight)


print("--------------------------------------------------------------------------------")
#7-13 requestsでpythonの公式サイトを取得
import requests
response = requests.get("https://www.python.org/downloads/")
text = response.text
print(text)


print("--------------------------------------------------------------------------------")


#7-14 標準ライブラリを利用したwebページの取得
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET","/downloads/")
response = conn.getresponse()
text = response.read().decode("UTF-8")
print(text)
conn.close()



print("--------------------------------------------------------------------------------")







