import os
import urllib.request

def download(txt):
    # 创建一个保存图片的文件夹
    if not os.path.exists('images'):
        os.makedirs('images')

    # 从 URLs.txt 文件中读取 URL 地址
    with open(f'{txt}.txt', 'r') as f:
        urls = f.readlines()

    # 遍历 URL 地址
    for url in urls:
        url = url.strip() # 删除 URL 地址两端的空白字符
        label = url[-1]
        url = url[:-2]
        if url.endswith('.jpg') or url.endswith('.png'):
            try:
                # 发送 GET 请求并保存图片文件
                filename = url.split('/')[-1]
                filepath = os.path.join('images',txt,label)
                if not os.path.exists(f"{filepath}"):
                    os.makedirs(f"{filepath}", exist_ok=True)
                savename = os.path.join(filepath,filename)
                urllib.request.urlretrieve(url=url, filename=savename)
                print(f'{url} downloaded successfully and saved as {filename}')
            except:
                print(f'{url} failed to download')

    print('All images downloaded successfully!')
if __name__=='__main__':
    txt1,txt2 = 'test25','train25'
    # download(txt1)
    download(txt2)
