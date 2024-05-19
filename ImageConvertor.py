from os import path
from PIL import Image
from pathlib import Path
from rich import console
from rich.console import Console

# input = r"F:\UnityExtract\Texture2D"
input = r"F:\UnityExtract\new"
output = r"F:\UnityExtract\Converted"

# The raw size is 2048 x 1024 
innerSize = (1820, 1024)
outterSize = (2048, 1152)

console = Console()
paths = Path(input).glob("**/*.png")
count = 0
countAll = paths.__sizeof__() - 5
for p in paths:
    count += 1
    im = Image.open(p)
    nim = im.resize(innerSize, resample=Image.LANCZOS, reducing_gap=3)
    # Convert to webp or png
    nim.save(fp=Path(output).joinpath(p.stem + ".webp"), format="webp", lossless=True, method=6)
    # nim.save(fp=Path(output).joinpath("png").joinpath(p.name), format="png")
    console.print(f"[bold green]>>> [Succeed][/bold green] ({count}/{countAll}) '{p.name}' has been successfully converted.")
