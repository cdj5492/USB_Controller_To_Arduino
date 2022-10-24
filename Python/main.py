import pygame
import time
from pySerialTransfer import pySerialTransfer as txfer

pygame.init()

joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
print(joysticks)

if(len(joysticks) == 0):
    print("No joysticks found")
    exit()
    
# read from joystick in loop
if __name__ == '__main__':
    link = txfer.SerialTransfer('COM6')
    
    time.sleep(2) # allow some time for the Arduino to completely reset
    link.open()
    
    while True:
        try:
            pygame.event.pump()
            joysticksAxes = [joysticks[0].get_axis(x) for x in range(joysticks[0].get_numaxes())]
            # remap all from -1 to 1 to 0 to 255
            joysticksAxesScaled = [((x + 1) * 511.5)/4 for x in joysticksAxes]
            print(joysticksAxesScaled)
            
            send_size = 0
            send_size = link.tx_obj(joysticksAxesScaled, start_pos=send_size)
            
            link.send(send_size)
            
        except KeyboardInterrupt:
            try:
                link.close()
                exit()
            except:
                exit()
        except:
            import traceback
            traceback.print_exc()
            
            try:
                link.close()
                time.sleep(2)
                link.open()
            except:
                break