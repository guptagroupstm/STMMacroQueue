import SXMRemote
import numpy as np
import time

MySXM = None
Cancel = False
def Initialize():
    global MySXM
    MySXM= SXMRemote.DDEClient("SXM","Remote")


def OnClose():
    if MySXM is not None:
        pass


# Bias=The bias voltage in V
def Set_Bias(Bias= 0):
    pass

# Setpoint=The current setpoint in Amps
def Set_Setpoint(Setpoint=1e-9):
    pass


# XOffset=The X center of the image in nm
# YOffset=The Y center of the image in nm
def Set_Scan_Window_Position(XOffset=0,YOffset=0):
    pass
    
# ImageSize=The length of a row and column in nm
def Set_Scan_Image_Size(ImageSize=1e-9):
    pass

# Angle=The angle on the scan in degrees
def Set_Scan_Window_Angle(Angle=0):
    MySXM.SendWait(f"ScanPara('Angle',{Angle});")

# NPixels=The number of pixels in each row and each column
def Set_NPixels(NPixels=512):
    pass

# LineSpeed=The speed the tip moves in nm/s
def Set_Scan_Speed(LineSpeed=2e-9):
    pass

def Scan():
    pass