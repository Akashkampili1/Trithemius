from PIL import Image
from stegano import lsb
from os.path import isfile,join
import pyaes
import codecs
import wave
import time    
import cv2
import numpy as np
import math
import os
import shutil
from subprocess import call,STDOUT

banner = """\u001b[36m

████████╗██████╗░██╗████████╗██╗░░██╗███████╗███╗░░░███╗██╗██╗░░░██╗░██████╗
╚══██╔══╝██╔══██╗██║╚══██╔══╝██║░░██║██╔════╝████╗░████║██║██║░░░██║██╔════╝
░░░██║░░░██████╔╝██║░░░██║░░░███████║█████╗░░██╔████╔██║██║██║░░░██║╚█████╗░
░░░██║░░░██╔══██╗██║░░░██║░░░██╔══██║██╔══╝░░██║╚██╔╝██║██║██║░░░██║░╚═══██╗
░░░██║░░░██║░░██║██║░░░██║░░░██║░░██║███████╗██║░╚═╝░██║██║╚██████╔╝██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝╚═╝░╚═════╝░╚═════╝░        \u001b[0m
                            \u001b[32m - \u001b[0m
            """
print(banner)
print(f'[>] Created By   :Team Phoenix\n')
print(f'[>] The Worlds first complete Steganographic Framework with AES-256 Encryption \n\n')

key = b'\xf9\t\x8d,\x87s\x13\xd6\xe3q\x83"\x88j\x10G\x93\xa7\\\xaf\xb6D\xee\xd1\xa2\x01c\n|\xf9\x8b\x13'
iv = 67626443437380293210426335676717161172391347866016768051113432018942163049741
# Text-Module


def text_encode(plaintext):
    aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
    ciphertext = aes.encrypt(plaintext)
    fa = codecs.encode(ciphertext, 'hex')
    print("Encrypted Text ==>", fa)


def text_decode(ciphertext):
    fa = codecs.decode(ciphertext, 'hex')
    aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
    decrypted = aes.decrypt(fa)
    print("Decrypted Text ==>", decrypted)


# Image-Module


def genData(data):

		
		newd = []

		for i in data:
			newd.append(format(ord(i), '08b'))
		return newd


def modPix(pix, data):

	datalist = genData(data)
	lendata = len(datalist)
	imdata = iter(pix)

	for i in range(lendata):

		
		pix = [value for value in imdata.__next__()[:3] +
								imdata.__next__()[:3] +
								imdata.__next__()[:3]]

		
		for j in range(0, 8):
			if (datalist[i][j] == '0' and pix[j]% 2 != 0):
				pix[j] -= 1

			elif (datalist[i][j] == '1' and pix[j] % 2 == 0):
				if(pix[j] != 0):
					pix[j] -= 1
				else:
					pix[j] += 1
				

		
		if (i == lendata - 1):
			if (pix[-1] % 2 == 0):
				if(pix[-1] != 0):
					pix[-1] -= 1
				else:
					pix[-1] += 1

		else:
			if (pix[-1] % 2 != 0):
				pix[-1] -= 1

		pix = tuple(pix)
		yield pix[0:3]
		yield pix[3:6]
		yield pix[6:9]

def encode_enc(newimg, data):
	w = newimg.size[0]
	(x, y) = (0, 0)

	for pixel in modPix(newimg.getdata(), data):

		
		newimg.putpixel((x, y), pixel)
		if (x == w - 1):
			x = 0
			y += 1
		else:
			x += 1

def image_encode():
	img = input("Enter image name(with extension) : ")
	image = Image.open(img, 'r')

	data = input("Enter data to be encoded : ")
	if (len(data) == 0):
		raise ValueError('Data is empty')

	newimg = image.copy()
	encode_enc(newimg, data)

	new_img_name = input("Enter the name of new image(with extension) : ")
	newimg.save(new_img_name, str(new_img_name.split(".")[1].upper()))


def image_decode():
	img = input("Enter image name(with extension) : ")
	image = Image.open(img, 'r')

	data = ''
	imgdata = iter(image.getdata())

	while (True):
		pixels = [value for value in imgdata.__next__()[:3] +
								imgdata.__next__()[:3] +
								imgdata.__next__()[:3]]

		
		binstr = ''

		for i in pixels[:8]:
			if (i % 2 == 0):
				binstr += '0'
			else:
				binstr += '1'

		data += chr(int(binstr, 2))
		if (pixels[-1] % 2 != 0):
			return data


#audio file
def audio_encode():
    print("\nEncoding Starts..")
    audio_file = input("Enter the name of the audio file (with extension): ")
    audio = wave.open(audio_file, mode="rb")
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
    string = Text
    print(string)
    string = string + int((len(frame_bytes)-(len(string)*8*8))/8) * '#'
    bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8, '0') for i in string])))
    for i, bit in enumerate(bits):
        frame_bytes[i] = (frame_bytes[i] & 254) | bit
    frame_modified = bytes(frame_bytes)
    for i in range(0, 10):
        print(frame_bytes[i])
    newAudio = wave.open(audio_file, 'wb')
    newAudio.setparams(audio.getparams())
    newAudio.writeframes(frame_modified)
    newAudio.close()
    audio.close()
    print(" |---->succesfully encoded inside {audio_file} ")


def audio_decode():
    print("\nDecoding Starts..")
    audio_file = input("Enter the name of the audio file (with extension): ")
    audio = wave.open(audio_file, mode='rb')
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
    extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
    string = "".join(chr(int("".join(map(str, extracted[i:i+8])), 2)) for i in range(0, len(extracted), 8))
    decoded = string.split("###")[0]
    print("Successfully decoded: " + decoded)
    audio.close()

#video module
def split_string(split_str,count=10):
    per_c=math.ceil(len(split_str)/count)
    c_cout=0
    out_str=''
    split_list=[]
    for s in split_str:
        out_str+=s
        c_cout+=1
        if c_cout == per_c:
            split_list.append(out_str) 
            out_str=''
            c_cout=0
    if c_cout!=0:
        split_list.append(out_str)
    return split_list

def frame_extraction(video):
    if not os.path.exists("./temp"):
        os.makedirs("temp")
    temp_folder="./temp"
    print("[INFO] temp directory is created")
    vidcap = cv2.VideoCapture(video)
    count = 0
    while True:
        success, image = vidcap.read()
        if not success:
            break
        cv2.imwrite(os.path.join(temp_folder, "{:d}.png".format(count)), image)
        count += 1

def encode_string(input_string,root="./temp/"):
    split_string_list=split_string(input_string)   
    for i in range(0,len(split_string_list)):
        f_name="{}{}.png".format(root,i)                   
        secret_enc=lsb.hide(f_name,split_string_list[i])   
        secret_enc.save(f_name)                            
        print("[INFO] frame {} holds {}".format(f_name,lsb.reveal(f_name)))
    print("The message is stored in the Embedded_Video.mp4 file")


def video_decode(video):
    frame_extraction(video)        
    secret=[]
    root="./temp/"
    for i in range(len(os.listdir(root))):
        f_name="{}{}.png".format(root,i)
        secret_dec=lsb.reveal(f_name)         
        if secret_dec == None:
            break
        secret.append(secret_dec)
    print(''.join([i for i in secret]))
    clean_temp()

def clean_temp(path="./temp"):
    if os.path.exists(path):
        shutil.rmtree(path)
        print("[INFO] temp files are cleaned up")


def video_encode(f_name):
    input_string = input("Enter the message :")   
    frame_extraction(f_name)
    
    call(["ffmpeg", "-i",f_name, "-q:a", "0", "-map", "a", "temp/audio.mp3", "-y"],stdout=open(os.devnull, "w"), stderr=STDOUT)
    encode_string(input_string)
    call(["ffmpeg", "-i", "temp/%d.png" , "-vcodec", "png", "temp/Embedded_Video.mp4", "-y"],stdout=open(os.devnull, "w"), stderr=STDOUT)
    call(["ffmpeg", "-i", "temp/Embedded_Video.mp4", "-i", "temp/audio.mp3", "-codec", "copy", "Embedded_Video.mp4", "-y"],stdout=open(os.devnull, "w"), stderr=STDOUT)
    clean_temp()

while True:
    print("\nMAIN MENU")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    choice1 = int(input("Enter the Choice:"))

    if choice1 == 1:
        Text = input("Enter Text to encrypt:")
        main_text=text_encode(Text)

        print("\Choose PARAMETER")
        print("1. Image")
        print("2. Audio")
        print("3. Video")
        print("4. Exit")
        choice2 = int(input("Enter the Choice:"))

        if choice2 == 1:
            image_encode()

        elif choice2 == 2:
            audio_encode()

        elif choice2 == 3:
            f_name=input("Enter the name of video file with extension:")
            video_encode(f_name)
        elif choice2 == 3:
            break

        else:
            print("Oops! Incorrect Choice.")

    elif choice1 == 2:
        print("\nCALCULATE AREA")
        print("1. Text")
        print("2. image")
        print("3. audio")
        print("4. video")
        print("4. Exit")
        choice3 = int(input("Enter the Choice:"))

        if choice3 == 1:
            text_q = eval(input("Enter Radius of Circle:"))
            text_decode(text_q)

        elif choice3 == 2:
            print("Decoded Word :" + image_decode())

        elif choice3 == 3:
            audio_decode()
        
        elif choice3 == 4:
            video_decode()

        elif choice3 == 5:
            break

        else:
            print("Oops! Incorrect Choice.")

    elif choice1 == 3:
        break

    else:
        print("Oops! Incorrect Choice.")
