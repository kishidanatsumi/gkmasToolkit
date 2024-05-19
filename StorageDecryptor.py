import hashlib
import json
import octodb_pb2
import sqlite3
import sys
import re
from rich.console import Console
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from pathlib import Path
from google.protobuf.json_format import MessageToJson

fileName = "fd922587c134ae44339676a8a22a0dec"
KEY = "b9d8b4d1bfb2240b2a96efbdca519474"
IV = "1b07142724cd64ea7a583374ba889667"
filePath = "./ipr/Assets"

def decryptStorageFile(key: str, iv: str):

    key = bytes(key, "utf-8")
    iv = bytes(iv, "utf-8")

    # key = hashlib.md5(key).digest()
    # iv = hashlib.md5(iv).digest()
    cipher = AES.new(key, AES.MODE_CBC, iv)

    encryptData = Path(filePath + fileName).read_bytes()
    decryptedBytes = cipher.decrypt(encryptData)
    decryptedBytes = unpad(decryptedBytes, block_size=16, style="pkcs7")

    outputPath = Path(filePath + fileName + "_decrypt")
    outputPath.write_bytes(decryptedBytes)

decryptStorageFile(IV, KEY[9:25])
