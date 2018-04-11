from PIL import Image
from sys import argv

def convertBinaryToMessage(array_bin_msg):
	s = ''.join(str(i) for i in array_bin_msg)
	return chr(int(s,base=2))

def decryptImage(img):
	byte = bytearray(img)  
	decrypted_message = ""
	decrypted_char = ""
	header_offset = 0
	if "BM" in byte[:20]:
		header_offset = 54
	else:
		print ("Can't decrypt not BMP file")
		return None
	temp_byte = [ ]
	while True:
		temp_byte.append(byte[header_offset]%2)
		header_offset+=1
		if len(temp_byte) == 8:
			#temp_byte[0]=0
			decrypted_char = convertBinaryToMessage(temp_byte)
			temp_byte = [ ]
		if decrypted_char is not "\x00":
			decrypted_message += decrypted_char
			decrypted_char = ""
		else:
			break
	return decrypted_message
    
    
if __name__ == "__main__":
	data = open(argv[1], 'rb').read()
	decrypted_message = decryptImage(data)
	if decrypted_message is not None:
		print ("Hidden Message: " + decrypted_message) 
	else:
		print ("Failed to decrypt")



