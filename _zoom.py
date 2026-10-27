from PIL import Image
import os
base = r"C:\Users\chnbamboo\AppData\Local\Doubao\User Data\ClipboardTemp"
out = r"C:\Users\chnbamboo\AppData\Local\Doubao\User Data\ClipboardTemp\_zoom"
os.makedirs(out, exist_ok=True)
jobs = [
    ("bbeea14a-5a9e-43d9-9850-1570e3d453d3.png", "z9.png", (30, 90, 445, 700)),
    ("f459b585-db95-4f31-81a7-5bc7339d0f17.png", "z4.png", (30, 70, 445, 660)),
]
for fn, on, box in jobs:
    p = os.path.join(base, fn)
    im = Image.open(p).convert("RGB")
    w, h = im.size
    print(fn, im.size)
    crop = im.crop(box)
    crop = crop.resize((crop.width*4, crop.height*4), Image.LANCZOS)
    crop.save(os.path.join(out, on))
print("done")