import pygame
import cv2
import numpy as np


# Initialize
pygame.init()

# Create Window/Display
width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sign Language Recognition")

# Initialize Clock for FPS
fps = 30
clock = pygame.time.Clock()

#webcam
cap=cv2.VideoCapture(0)


# Colors
c = {"lightGreen": (189, 209, 197),
"Lightorange": (238, 204, 140),
"LightPink": (232, 178, 152),
"darkPink": (211, 162, 157),
"darkGreen": (158, 171, 162),
"darkGray": (128, 126, 126),
"LightGray": (204, 204, 204),
"darkBrown": (89, 61, 61),
"white": (255, 255, 255),
"black": (0, 0, 1) ,
"Yellow":(160,99,156)
}


imgBackground = pygame.image.load('2.Resources/images/bg.jpeg').convert()
imgBackground = pygame.transform.scale(imgBackground, (width, height))
imgDesg = pygame.image.load('2.Resources/images/design.png').convert_alpha()
imgDesg = pygame.transform.scale(imgDesg, (width, height))
imgIcon1 = pygame.image.load ('2.Resources/images/icon.png').convert_alpha()
imgIcon2 = pygame.image.load ('2.Resources/images/icon.png').convert_alpha()
imgIcon3 = pygame.image.load ('2.Resources/images/icon.png').convert_alpha()
imgIcon4 = pygame.image.load ('2.Resources/images/icon.png').convert_alpha()
imgIcon5 = pygame.image.load ('2.Resources/images/icon.png').convert_alpha()
imgIcon6 = pygame.image.load ('2.Resources/images/icon.png').convert_alpha()
imgToggleOn = pygame.image.load ('2.Resources/images/tog_on.png').convert_alpha()
imgToggle0ff = pygame.image.load ('2.Resources/images/tog_off.png').convert_alpha()


# List of WindowPads
pads =[{"no": 1, "color": c['lightGreen'], "text": "Original", "icon": imgIcon2},
       {"no": 2, "color": c['Lightorange'], "text": "DIP_tech_1", "icon": imgIcon3},
       {"no": 3, "color": c['LightPink'], "text": "DIP_tech_2", "icon": imgIcon4},
        {"no": 4, "color": c['darkPink'], "text": "DIP_tech_3","icon": imgIcon5},
        {"no": 5, "color": c['Yellow'], "text": "DIP_tech_4","icon": imgIcon6}
        ]
def drawWindowPad (pos, color, text, icon):
    Xo,Yo,w,h = pos
    pygame.draw.rect (window, color, (Xo,Yo, w, 64),
                    border_top_left_radius=10, border_top_right_radius=10)
    pygame.draw.rect(window, c['white'], (Xo,Yo+64, w, h-87),
                    border_bottom_left_radius=10, border_bottom_right_radius=10)
    window.blit(icon,(Xo+20,Yo+12))
    font = pygame.font.Font ('2.Resources/Marcellus-Regular.ttf',20)
    text = font. render (text, True, c['darkBrown' ])
    window.blit(text, (Xo+82, Yo+20))


def drawFilterPad():
    drawWindowPad((75, 57, 312, 301), c["darkGreen"], "Filter", imgIcon1)
    font=pygame.font.Font ('2.Resources/Marcellus-Regular.ttf',16)
    #1
    textDisp1 = font.render ("DIP tech 1", True, c["darkBrown"])
    window.blit(textDisp1, (106, 83+43)) 
    window.blit(imgToggleOn, (280, 77+45))
    # 2
    textDisp2 = font.render ("DIP tech 2", True, c["darkBrown"])
    window.blit(textDisp2, (106, 83+43*2)) 
    window.blit (imgToggleOn, (280, 77+45*2))
    # 3
    textDisp3 = font.render ("DIP tech 3", True, c["darkBrown"])
    window.blit(textDisp3, (106, 87+43*3)) 
    window.blit (imgToggleOn, (280, 77+45*3))
    # 4
    textDisp4 = font.render ("DIP tech 4", True, c["darkBrown"])
    window.blit(textDisp4, (106, 90+43*4)) 
    window.blit (imgToggleOn, (280, 77+45*4))
    # 5
    textDisp4 = font.render ("DIP tech 5", True, c["darkBrown"])
    window.blit(textDisp4, (106, 92+43*5)) 
    window.blit (imgToggleOn, (280, 77+45*5))
    # SLiders
    '''font = pygame. font. Font ('2.Resources/Marcellus-Regular.ttf', 25)
    for y in range (0, 3):
        h = 447 + y * 55
        sliderPos = 105 + 50 * y + 30
        pygame.draw.line(window, c["LightGray"], (105, h), (105 + 155, h), 5) 
        pygame.draw.line (window, c["darkGray"], (105, h), (sliderPos, h), 5) 
        pygame.draw.rect(window, c["darkGray"], (sliderPos, h - 15, 12, 30))
        textDisp = font.render (str(y * 50 + 30), True, c["darkBrown"])
        window.blit(textDisp, (286, h - 18))'''

def drawall():
    w, h = 312, 301
    gapW,gapH=72,25
    drawWindowPad ((484, 57, w, h), pads [0]['color'], pads [0]['text'], pads[0]['icon']) 
    drawWindowPad ((484+w+gapW, 57, w, h), pads [1]['color'], pads [1]['text'], pads[1]['icon']) 
    drawWindowPad ((484, 57+h+gapH, w, h), pads [2]['color'], pads [2]['text'], pads[2]['icon']) 
    drawWindowPad ((484+w+gapW, 57+gapH+h, w, h), pads [3]['color'], pads [3]['text'], pads[3]['icon']) 
    drawWindowPad ((75, 57+gapH+h, w, h), pads [4]['color'], pads [4]['text'], pads[4]['icon']) 

    #window.blit(imgIcon1, (100, 100))
    drawFilterPad()
 



# Main Loop
start = True
while start:
    # Get Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    # Apply Logic
    window.blit(imgBackground,(0,0))
    imgDesg.set_alpha(0)
    window.blit(imgDesg,(0,0))    


    drawall()
    # OpencV
    
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    imgRGB = np.rot90(imgRGB)
    webcam_surface = pygame.surfarray.make_surface(imgRGB)

    # Adjust the position and size of the webcam feed surface to fit the designated area
    webcam_surface = pygame.transform.scale(webcam_surface, (310, 200))  # Adjust dimensions as needed

    # Blit the webcam feed onto the designated area
    window.blit(webcam_surface, (484, 121))  # Adjust coordinates as

    # Update Display
    pygame.display.update()

    # Set FPS
    clock.tick(fps)
