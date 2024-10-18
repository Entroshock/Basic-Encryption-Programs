
alphabet = 26

def encrypt(text,shift):
    text=text.lower()
    encrypted_text = ""
    for char in text:
        if char.islower():
            #convert text to number with ord() method and shift, change back to string with chr
            encrypted_text += chr((ord(char) + shift - 97) % alphabet + 97)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    text = text.lower()
    decrypted_text = ""
    for char in text:
        if char.islower():
            decrypted_text += chr((ord(char) - shift - 97) % alphabet + 97)
        else:
            decrypted_text += char
    return decrypted_text



# textInput = input('Please Enter your text: ')
# shiftInput = int(input('Please enter the shift key: '))
# cipher_text = encrypt(textInput, shiftInput)

cipher_text = ("RQH YDULDWLRQ WR WKH VWDQGDUG FDHVDU FLSKHU LV ZKHQ WKH DOSKDEHW LV "
               "\"NHBHG\" EB XVLQJ D ZRUG. LQ WKH WUDGLWLRQDO YDULHWB, RQH FRXOG ZULWH WKH "
               "DOSKDEHW RQ WZR VWULSV DQG MXVW PDWFK XS WKH VWULSV DIWHU VOLGLQJ WKH "
               "ERWWRP VWULS WR WKH OHIW RU ULJKW. WR HQFRGH, BRX ZRXOG ILQG D OHWWHU "
               "LQ WKHWRS URZ DQG VXEVWLWXWH LW IRU WKH OHWWHU LQ WKH ERWWRP URZ.IRU "
               "D NHBHG YHUVLRQ, RQH ZRXOG QRW XVH D VWDQGDUG DOSKDEHW,EXW ZRXOG "
               "ILUVW ZULWH D ZRUG (RPLWWLQJ GXSOLFDWHG OHWWHUV)DQG WKHQ ZULWH WKH "
               "UHPDLQLQJ OHWWHUV RI WKH DOSKDEHW. IRUWKH HADPSOH EHORZ, L XVHG "
               "D NHB RI \"UXPNLQ.FRP\" DQG BRX ZLOO VHHWKDW WKH SHULRG LV UHPRYHG "
               "EHFDXVH LW LV QRW D OHWWHU. BRX ZLOO DOVR QRWLFH WKH VHFRQG \"P\" "
               "LV QRW LQFOXGHG EHFDXVHWKHUH ZDV DQ P DOUHDGB DQG BRX FDQ'W KDYH "
               "GXSOLFDWHV.")

# print("Your encoded text is: ", cipher_text)
# print("" * 10)

print(f"{'Shift':<6} {'Decrypted Text'}")
print("=" * 70)

for shift in range(alphabet):
    decrypted_text = decrypt(cipher_text, shift)
    print(f"Shift {shift}:\n{decrypted_text}\n")
    print("-" * 70)


