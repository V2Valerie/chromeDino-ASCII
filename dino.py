import time, os

banner1 = """
            ▄█▀▀▀▀▀▀▀▀▀█▄ 
            █  ▄        █
            █           █
            █           █
  ▄         █     ▀▀▀█▀▀▀
 █ █      ▄▄▀    █▀▀▀▀
 █  ▀▄▄▄▀▀       ▀▀█
 █              █▄▄█
 █              █
 ▀▄           ▄▀ 
   ▀▄   ▄█▄ ▄▀  
    █  ▀▄ █▄▄█
    █▄▄▄█ 
"""

banner2 = """
            ▄█▀▀▀▀▀▀▀▀▀█▄ 
            █  ▄        █
            █           █
            █           █
  ▄         █     ▀▀▀█▀▀▀
 █ █      ▄▄▀    █▀▀▀▀
 █  ▀▄▄▄▀▀       ▀▀█
 █              █▄▄█
 █              █
 ▀▄           ▄▀ 
   ▀▄   ▄█▄ ▄▀  
    █▄▄▄█ █ ▀▄
          █▄▄█
"""

crnt = 2
while 1:
    os.system("clear")
    if crnt == 1:
        print(banner2)
        crnt = 2

    elif crnt == 2:
        print(banner1)
        crnt = 1

    time.sleep(0.5)
    