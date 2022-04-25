<h1 align="center"><b>HidePy</b></h1>
<p align="center"><b>A minimal LSB steganography tool written in python for single bit encoding/decoding.</b></p>
</br>

**Setup/Install:**

`HidePy` can be installed via `https` with git:

```console
sudhan@osx:~ $ git clone https://github.com/sudhanchitgopkar/hidePy.git
sudhan@osx:~ $ cd hidePy
```

and requires Python3+ to run. Check your version of python using `python --version` or `python3 --version`.

`HidePy` also depends on [Pillow](https://pillow.readthedocs.io/en/stable/) and [NumPy](https://numpy.org/). Both can be installed using `pip`
```console
sudhan@osx:~ $ python3 -m pip install --upgrade pip
sudhan@osx:~ $ python3 -m pip install --upgrade Pillow
sudhan@osx:~ $ pip install numpy
```
---
**Run with Python3 as default**:
```console
sudhan@osx:~ $ python steg.py
```
**Or with Python3 explicitly**
```console
sudhan@osx:~ $ python3 steg.py
```
---
**Usage:**
Upon opening, users will be prompted with the following CLI:

```console

Welcome to:
 _    _ _     _      _____
| |  | (_)   | |    |  __ \
| |__| |_  __| | ___| |__) |   _
|  __  | |/ _` |/ _ \  ___/ | | |
| |  | | | (_| |  __/ |   | |_| |
|_|  |_|_|\__,_|\___|_|    \__, |
                            __/ |
                           |___/

A steganography tool written in Python!


Select an option:
e: encode image
d: decode image
q: quit

user@hidepy $
```

`e` allows users to encode some image with some text to produce some encoded output image. For optimal use, place both the image and message to encode in the same directory as `HidePy`. Output files should retain the same file type as the input files. **While HidePy works with RGB + RGBa file types, JPEG/JPG files will not encode properly due to their compression.**

`d` allows users to decode some image to produce the encoded message. Output messages will be displayed to screen and written to `decoded.txt`. **This file will be overwritten during each decode.**

`q` allows users to quit the `HidePy`

