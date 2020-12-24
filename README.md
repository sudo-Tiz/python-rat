# My first virus in python
## Disclaimer :
**This application is for educational purposes. I cannot be held responsible for any abusive use of my code.**

# This virus can do :
* reverse shell
* keylogger
* wifis password stealer
* screen sharing
* camera sharing

## Requirements :
* python3 
* mss for screen streaming
* pynput for keylogger
* opencv-python (know as cv2) for camera streaming
* numpy for camera streaming

## How to install :

``pip3 install requirements.txt``

watch out requirements are differents for attacker and victim
## How to run :

on the victim computer :
``python3 victim.py``

on windows you can just launch run.bat which download the requirements and run the virus

on the attacker computer:
``python3 attacker.py``


## Options :

Victim side:
```py
usage: victim.py [-h] [--host HOST] [--port PORT] [--keylog KEYLOG] [--wifi WIFI] [--shell SHELL]
                [--camera CAMERA] [--screen SCREEN]

Tiz Virus Victim

optional arguments:
  -h, --help       show this help message and exit
  --host HOST      listening ip, default is '0.0.0.0', no need to change
  --port PORT      default port is 5000, revershell = port, camera stream = port+1, screen stream =port+2
  --keylog KEYLOG  keylog=t create a keylogger file / keylog=f don't create the file
  --wifi WIFI      wifi=t create a file with all wifis password / wifi=f don't create the file
  --shell SHELL    shell=t revershell on port (default = 5000) / shell=f don't revershell
  --camera CAMERA  camera=t stream camera on port+1 (default = 5001) / camera=f don't stream
  --screen SCREEN  screen=t stream screen on port+2 (default = 5002) / screen=f don't stream
  ```

  ---

  Attacker side:
  ```py
usage: attacker.py [-h] [--host HOST] [--port PORT] [--shell SHELL] [--camera CAMERA] [--screen SCREEN]

Tiz Virus attacker

optional arguments:
  -h, --help       show this help message and exit
  --host HOST      connecting ip, default is localhost'
  --port PORT      default port is 5000, revershell = port, camera stream = port+1, screen stream = port+2
  --shell SHELL    shell=t revershell on port (default = 5000) / shell=f don't revershell
  --camera CAMERA  camera=t stream camera on port+1 (default = 5001) / camera=f don't stream
  --screen SCREEN  screen=t stream screen on port+2 (default = 5002) / screen=f don't stream
  ```


  ## Futur improvements :
  * concat every attacker files in one file
  * any idea ?

  # TIZ
