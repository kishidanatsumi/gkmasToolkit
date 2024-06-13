from ManifestDecryptor import doDecrypt
from MaskedHeaderStream import unObfuscate, rename
from Downloader import download
from eDiffMode import DiffMode
from eWorkingMode import WorkingMode

global output_dir
output_dir="./gkmas"

download_asset = 1
download_resource = 0
download_worker_num = 16

#diffMode = DiffMode.Diff
jDict = doDecrypt()

download(jDict, output_dir, download_asset, download_resource, download_worker_num)

unObfuscate(jDict)
rename(jDict)
