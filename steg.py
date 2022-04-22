from PIL import Image
import numpy as np

def encode(imgPath,txtPath,dest):
    #initialize vars
    try:
        im = Image.open(imgPath).convert('RGB')
    except FileNotFoundError:
        print("✖ Image file not found!")
        return False
    
    px = list(im.getdata())
    w, h = im.size
    k = 0

    #convert intensities to 8bit bin
    for i in range(0,len(px)):
        px[i] = ['{0:08b}'.format(px[i][0]),
                 '{0:08b}'.format(px[i][1]),
                 '{0:08b}'.format(px[i][2])]
   
    #convert message to 8bit bin
    try:
        with open(txtPath, 'r') as file:
            txt = file.read()
    except FileNotFoundError:
        print("✖ Text file not found!")
        return False
    
    txtbin = ''.join(format(ord(i), '08b') for i in txt)
    #append end delimiter
    txtbin = txtbin + "00100100001001010010010000100101"

    #Check encoding feasibility
    if (3*w*h) <= len(txtbin):
        print("✖ Message is too long to encode in image!")
        print("Use a shorter messsage (currently: " + str(len(txtbin))
              + " bits)  or larger image (currently: " + str(w) + "x" + str(h) + ").")
        return False;
    elif (3*w*h) - len(txtbin) < (w*h):
        print("Message length may significantly degrade image quality!" +
        "Consider using a shorter message or larger image.")
 
    #encoding process
    for i in range(0,len(px)): 
        for j in range(0,3): 
            if k < len(txtbin):
                #change LSB, convert to int
                px[i][j] = (px[i][j][:-1] + txtbin[k]) 
                px[i][j] = int(px[i][j],2)
                k += 1
            else:
                #keep bit constant
                px[i][j] = int(px[i][j],2)

    #reconvert to img
    encodearr = np.array(px).reshape(h, w, 3)
    enc_img = Image.fromarray(encodearr.astype('uint8'), mode="RGB").save(dest)
    return True;
    
def decode(imgPath):
    #initialize vars
    try:
        im = Image.open(imgPath)
    except FileNotFoundError:
        print("✖ File not found!")
        return("")
    
    px = list(im.getdata())
    txtbin = ""
    txt = ""

    #convert all px to bin
    for i in range(0,len(px)):
        for j in range(0,3):
            txtbin += format(px[i][j],"b")[-1]

    #convert bin to unicode
    for i in range(8,len(txtbin),8):
        txt += chr(int(txtbin[i-8:i], 2))
        if i >= 24 and txt[-3:] == "$%$":
            return (txt[:-3])

    return("No message found.")

def main():
    print("\nWelcome to:\n" +
    " _    _ _     _      _____       \n" +
    "| |  | (_)   | |    |  __ \      \n" +
    "| |__| |_  __| | ___| |__) |   _ \n" +
    "|  __  | |/ _` |/ _ \  ___/ | | |\n" +
    "| |  | | | (_| |  __/ |   | |_| |\n" +
    "|_|  |_|_|\__,_|\___|_|    \__, |\n" +
    "                            __/ |\n" +
    "                           |___/ \n" +
    "\nA steganography tool written in Python!\n")

    cmd = ""
    while cmd != 'q':
        cmd = input("\nSelect an option:\ne: encode image\nd: decode image\nq: quit\n\nuser@hidepy $  ")

        if cmd == 'e':
            imgPath = input("Please enter a path to your image file\nuser@hidepy $ ")
            txtPath = input("PLease enter a path to your message file\nuser@hidepy $ ")
            dest = input("Please enter a name for your encrypted image (with file extension!)\nuser@hidepy $ ")
            if(encode(imgPath,txtPath,dest)):
                print("✓ Message successfully encoded.")
        elif cmd == 'd':
            imgPath = input("Please enter a path to your image file\nuser@hidepy $ ")
            if(decode(imgPath) != ""):
                print("\n✓ Secret Message: " + decode(imgPath))
        elif cmd != 'q':
            print("Input not recognized!\n")

    print("\nGoodbye!\n")
                
main()
