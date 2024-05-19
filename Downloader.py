import requests
import json
import os

def download(jdic: dict, download_dir:str, download_asset:int, download_resource:int):
    assetBundleList: list = jdic['assetBundleList']
    resourceList: list = jdic['resourceList']
    assetnum=assetBundleList.__len__()
    resourcenum=resourceList.__len__()
    assetpath=f"{download_dir}/Assets"
    resourcepath=f"{download_dir}/Resource"
    print("Total asset number is:",assetnum)
    print("Total resource number is:",resourcenum)   
    # 创建保存下载文件的目录
    os.makedirs(download_dir, exist_ok=True)
    
    if (download_asset):
        print("Start downloading asset files...")
        if not os.path.exists(assetpath):
            os.mkdir(assetpath)
        count=1
        for asset in assetBundleList:
            ab_name = asset['name']
            object_name = asset['objectName']
            md5_name = asset['md5']
            url = f'https://object.asset.game-gakuen-idolmaster.jp/{object_name}'
            file_path = os.path.join(assetpath, md5_name)
            if os.path.exists(file_path):
                    print(f">>> [Skipped] ({count}/{assetnum}) Assetbundle '{ab_name}.unity3d' saved as {md5_name} has existed.")
            else:
                # 下载文件
                response = requests.get(url)
                if (response.status_code == 200):
                    with open(file_path, 'wb') as f:
                        f.write(response.content)
                    print(f">>> [Succeed] ({count}/{assetnum}) Assetbundle '{ab_name}.unity3d' has been saved as {md5_name}.")
                else:
                    print(f">>> [Failed] ({count}/{assetnum}) Assetbundle '{ab_name}.unity3d' saved as {md5_name} failed.")
            count=count+1
    
    
    if (download_resource):
        print("Start downloading resource files...")
        if not os.path.exists(resourcepath):
            os.mkdir(resourcepath)
        count=1
        for res in resourceList:
            res_name = res['name']
            object_name = res['objectName']
            md5_name = res['md5']
            url = f"https://object.asset.game-gakuen-idolmaster.jp/{object_name}"
            file_path = os.path.join(resourcepath, res_name)
            if os.path.exists(file_path):
                    print(f">>> [Skipped] ({count}/{resourcenum}) ResourceBundle '{res_name}' has existed.")
            else:
                # 下载文件
                response = requests.get(url)
                if (response.status_code == 200):
                    with open(file_path, 'wb') as f:
                        f.write(response.content)
                    print(f">>> [Succeed] ({count}/{resourcenum}) ResourceBundle '{res_name}' has been saved.")
                else:
                    print(f">>> [Failed] ({count}/{resourcenum}) ResourceBundle '{res_name}' saving failed.")
            count=count+1
    
    print("All files downloaded.")
