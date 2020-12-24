# My first virus in python
this virus can do :
* reverse shell
* keylogger
* wifis password stealer
* screen sharing
* camera sharing

## requirement
* python3
use pip3 to install 
* mss
for screen streaming
* pynput
for keylogger
* cv2
for camera streaming

## How to install :
on windows you can run virus.bat to install the requirement and run the virus


## options :
```py
usage: virus.py [-h] [--host HOST] [--port PORT] [--keylog KEYLOG] [--wifi WIFI] [--camera CAMERA]
                [--screen SCREEN] [--shell SHELL]

Tiz Virus

optional arguments:
  -h, --help       show this help message and exit
  --host HOST      listening ip, no need to change
  --port PORT      stream port, reverse shell port = stream port +1
  --keylog KEYLOG  keylog=t create a keylogger file / keylog=f don't create the file
  --wifi WIFI      wifi=t create a file with all wifis password / wifi=f don't create the file
  --camera CAMERA  camera=t stream camera on port+1 (default = 5001) / camera=f don't stream
  --screen SCREEN  screen=t stream screen on port+2 (default = 5002)/ screen=f don't stream
  --shell SHELL    shell=t revershell on port (default = 5000)/ shell=f don't revershell
  ```

  ## Futur improvement:
  * create an installer in bash
  * create a requirement.txt file
  * concat every attacker files in one file
  * any idea ?

--- 
  # TIZ
---