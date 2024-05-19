from ManifestDecryptor import doDecrypt
from MaskedHeaderStream import unObfuscate, rename
from Downloader import download
from eDiffMode import DiffMode
from eWorkingMode import WorkingMode

global output_dir
output_dir="./gkmas"

download_asset = 0
download_resource = 0

diffMode = DiffMode.Diff
jDict = doDecrypt(diffMode)

download(jDict, output_dir,download_asset,download_resource)

unObfuscate(jDict)
rename(jDict)
