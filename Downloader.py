import requests
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

def download_file(url, file_path, name, count, total, is_asset):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, 'wb') as f:
            f.write(response.content)
        type_desc = "Assetbundle" if is_asset else "ResourceBundle"
        print(f">>> [Succeed] ({count}/{total}) {type_desc} '{name}' has been saved as {file_path}.")
    else:
        type_desc = "Assetbundle" if is_asset else "ResourceBundle"
        print(f">>> [Failed] ({count}/{total}) {type_desc} '{name}' saving failed.")

def download(jdic: dict, download_dir: str, download_asset: int, download_resource: int, num_worker: int):
    assetBundleList: list = jdic['assetBundleList']
    resourceList: list = jdic['resourceList']
    assetnum = len(assetBundleList)
    resourcenum = len(resourceList)
    assetpath = f"{download_dir}/Assets"
    resourcepath = f"{download_dir}/Resource"
    
    print("Total asset number is:", assetnum)
    print("Total resource number is:", resourcenum)
    
    os.makedirs(download_dir, exist_ok=True)
    
    executor = ThreadPoolExecutor(max_workers=num_worker)

    if download_asset:
        print("Start downloading asset files...")
        if not os.path.exists(assetpath):
            os.mkdir(assetpath)
        futures = []
        for count, asset in enumerate(assetBundleList, start=1):
            ab_name = asset['name']
            object_name = asset['objectName']
            md5_name = asset['md5']
            url = f'https://object.asset.game-gakuen-idolmaster.jp/{object_name}'
            file_path = os.path.join(assetpath, md5_name)
            if os.path.exists(file_path):
                print(f">>> [Skipped] ({count}/{assetnum}) Assetbundle '{ab_name}.unity3d' saved as {md5_name} has existed.")
            else:
                futures.append(executor.submit(download_file, url, file_path, ab_name, count, assetnum, True))
        
        for future in as_completed(futures):
            future.result()

    if download_resource:
        print("Start downloading resource files...")
        if not os.path.exists(resourcepath):
            os.mkdir(resourcepath)
        futures = []
        for count, res in enumerate(resourceList, start=1):
            res_name = res['name']
            object_name = res['objectName']
            md5_name = res['md5']
            url = f"https://object.asset.game-gakuen-idolmaster.jp/{object_name}"
            file_path = os.path.join(resourcepath, res_name)
            if os.path.exists(file_path):
                print(f">>> [Skipped] ({count}/{resourcenum}) ResourceBundle '{res_name}' has existed.")
            else:
                futures.append(executor.submit(download_file, url, file_path, res_name, count, resourcenum, False))
        
        for future in as_completed(futures):
            future.result()

    executor.shutdown()
    print("All files downloaded.")
