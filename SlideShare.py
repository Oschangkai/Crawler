try:
    from urllib import urlretrieve
except ImportError:
    from urllib.request import urlretrieve
for i in range(1,54,1):
    print ("取得<檔案名>第",i,"張中....")
    url = "http://image.slidesharecdn.com/" + "" + str(i) + "-1024.jpg"
    filename = "<檔案名>-" + str(i) + ".jpg"
    urlretrieve(url, filename)
