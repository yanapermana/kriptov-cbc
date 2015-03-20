import Tkconstants, tkFileDialog
from Tkinter import *

# AES CBC
import os, random, struct
from Crypto.Cipher import AES

# Toolbar
from PIL import Image, ImageTk

# Tooltip
from tooltips2 import ToolTip

def encrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):
    """ Encrypts a file using AES (CBC mode) with the
        given key.

        key:
            The encryption key - a string that must be
            either 16, 24 or 32 bytes long. Longer keys
            are more secure.

        in_filename:
            Name of the input file

        out_filename:
            If None, '<in_filename>.enc' will be used.

        chunksize:
            Sets the size of the chunk which the function
            uses to read and encrypt the file. Larger chunk
            sizes can be faster for some files and machines.
            chunksize must be divisible by 16.
    """
    if not out_filename:
        out_filename = in_filename + '.enc'

    iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(in_filename)

    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16)

                outfile.write(encryptor.encrypt(chunk))

def decrypt_file(key, in_filename, out_filename=None, chunksize=24*1024):
    """ Decrypts a file using AES (CBC mode) with the
        given key. Parameters are similar to encrypt_file,
        with one difference: out_filename, if not supplied
        will be in_filename without its last extension
        (i.e. if in_filename is 'aaa.zip.enc' then
        out_filename will be 'aaa.zip')
    """
    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0]

    with open(in_filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)

        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(origsize)

# Close Menu
def close_menu():
	T.delete("1.0",END)


# TopLevel
def about():
	top3 = Toplevel(padx=64,pady=64)
	top3.title("About")

	# Label
	var = StringVar()
	var2 = StringVar()
	var3 = StringVar()
	var4 = StringVar()
	var5 = StringVar()
	var6 = StringVar()
	label = Label( top3, textvariable=var, relief=FLAT, anchor=W, font=("Ubuntu", 24))
	label2 = Label( top3, textvariable=var2, relief=FLAT, anchor=W, font=("Ubuntu", 12))
	label3 = Label( top3, textvariable=var3, relief=FLAT, anchor=W, font=("Ubuntu", 12))
	label4 = Label( top3, textvariable=var4, relief=FLAT, anchor=W, font=("Ubuntu", 12))
	label5 = Label( top3, textvariable=var5, relief=FLAT, anchor=W, font=("Ubuntu", 12))
	label6 = Label( top3, textvariable=var6, relief=FLAT, anchor=W, font=("Ubuntu", 12))
	var.set("Kriptov CBC")
	var2.set("1.0")
	var3.set("Kriptov CBC for Linux")
	var4.set("Kriptov CBC is designed by Yana Permana, Crypto Enthusiast.")
	var5.set(" ")
	var6.set("Sound interesting? Contact me on twitter @yansen1204")
	label.pack(fill=BOTH, expand="yes")
	label2.pack(fill=BOTH, expand="yes")
	label3.pack(fill=BOTH, expand="yes")
	label4.pack(fill=BOTH, expand="yes")
	label5.pack(fill=BOTH, expand="yes")
	label6.pack(fill=BOTH, expand="yes")

	top3.mainloop()

def help():
    top3 = Toplevel(padx=64,pady=64)
    top3.title("Guide")

    # Label
    var = StringVar()
    var2 = StringVar()
    var3 = StringVar()
    var4 = StringVar()
    var5 = StringVar()
    var6 = StringVar()
    var7 = StringVar()
    var8 = StringVar()
    var9 = StringVar()
    var10 = StringVar()
    var11 = StringVar()
    var12 = StringVar()
    var13 = StringVar()

    label = Label( top3, textvariable=var, relief=FLAT, anchor=W, font=("Ubuntu", 24))
    label2 = Label( top3, textvariable=var2, relief=FLAT, anchor=W, font=("Ubuntu", 12))
    label3 = Label( top3, textvariable=var3, relief=FLAT, anchor=W, font=("Ubuntu", 12))
    label4 = Label( top3, textvariable=var4, relief=FLAT, anchor=W, font=("Ubuntu", 12))
    label5 = Label( top3, textvariable=var5, relief=FLAT, anchor=W, font=("Ubuntu", 12))
    label6 = Label( top3, textvariable=var6, relief=FLAT, anchor=W, font=("Ubuntu", 12))
    label7 = Label( top3, textvariable=var7, relief=FLAT, anchor=W, font=("Ubuntu", 12))
    label8 = Label( top3, textvariable=var8, relief=FLAT, anchor=W, font=("Ubuntu", 12))
    label9 = Label( top3, textvariable=var9, relief=FLAT, anchor=W, font=("Ubuntu", 12))
    label10 = Label( top3, textvariable=var10, relief=FLAT, anchor=W, font=("Ubuntu", 12))
    label11 = Label( top3, textvariable=var11, relief=FLAT, anchor=W, font=("Ubuntu", 12))
    label12 = Label( top3, textvariable=var12, relief=FLAT, anchor=W, font=("Ubuntu", 12))
    label13 = Label( top3, textvariable=var13, relief=FLAT, anchor=W, font=("Ubuntu", 12))
    
    var.set("Petunjuk Penggunaan")
    var2.set(" ")
    var3.set("Encrypt")
    var4.set("1. Klik pada icon enkripsi atau pada menu > enkripsi")
    var5.set("2. Masukkan key, panjang key harus 16, 24 dan 64 karakter; Contoh: 0123456789abcdef")
    var6.set("3. Pilih file yang ingin anda enkripsi")
    var7.set("4. Hasil akan muncul dengan format .enc")
    var8.set(" ")
    var9.set("Decrypt")
    var10.set("1. Klik pada icon dekripsi atau pada menu > dekripsi")
    var11.set("2. Masukkan key, panjang key harus 16, 24 dan 64 karakter; Contoh: 0123456789abcdef")
    var12.set("3. Pilih file yang ingin anda dekripsi; Harus mempunyai format .enc")
    var13.set("4. Hasil akan muncul dengan format asli")
    
    label.pack(fill=BOTH, expand="yes")
    label2.pack(fill=BOTH, expand="yes")
    label3.pack(fill=BOTH, expand="yes")
    label4.pack(fill=BOTH, expand="yes")
    label5.pack(fill=BOTH, expand="yes")
    label6.pack(fill=BOTH, expand="yes")
    label7.pack(fill=BOTH, expand="yes")
    label8.pack(fill=BOTH, expand="yes")
    label9.pack(fill=BOTH, expand="yes")
    label10.pack(fill=BOTH, expand="yes")
    label11.pack(fill=BOTH, expand="yes")
    label12.pack(fill=BOTH, expand="yes")
    label13.pack(fill=BOTH, expand="yes")

    top3.mainloop()

# Menu
def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

def on_hide():
    top.withdraw()

def on_show():
    top.deiconify()
    
def on_show2():
    top2.deiconify()
    
def on_hide2():
    top2.withdraw()

def askopenfile():
    on_show()    
    
def askopenfile_dec():
    on_show2()    

def open_enc():

    # Set IV dan Key
    # txt_IV = entry_IV.get()
    txt_Key = entry_Key.get()
    # print txt_IV, txt_Key
    on_hide()

    # Dialog File
    path_filename = tkFileDialog.askopenfilename(parent=root,title='Choose a file')

    # Clear Textarea
    T.delete("1.0",END)
    
    # Read File
    fo = open(path_filename, "r")
    line = fo.read()
    T.insert(END, line)
    var.set(path_filename)
    
    key = txt_Key
    in_filename = path_filename
    encrypt_file(key, in_filename, out_filename=None, chunksize=64*1024)

    # Clear Textarea
    T2.delete("1.0",END)
    path_filename = path_filename + '.enc'

    # Read File
    fo2 = open(path_filename, "r")
    line2 = fo2.read()
    T2.insert(END, line2)
    var2.set(path_filename)

def open_dec():
	# Set IV dan Key
    # txt_IV2 = entry_IV2.get()
    txt_Key2 = entry_Key2.get()
    # print txt_IV2, txt_Key2
    on_hide2()
    
    # Dialog File
    path_filename = tkFileDialog.askopenfilename(parent=root,title='Choose a file')

    # Clear Textarea
    T.delete("1.0",END)
    
    # Read File
    fo = open(path_filename, "r")
    line = fo.read()
    T.insert(END, line)
    var.set(path_filename)

    key = txt_Key2
    in_filename_enc = path_filename
    path_filename = os.path.splitext(in_filename_enc)[0]
    decrypt_file(key, in_filename_enc, out_filename=None, chunksize=24*1024)

    # Clear Textarea
    T2.delete("1.0",END)

    # Read File
    fo2 = open(path_filename, "r")
    line2 = fo2.read()
    T2.insert(END, line2)
    var2.set(path_filename)

def createToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)


# Main
root = Tk()
root.title("Kriptov CBC")

line = []
path_file = ''

menubar = Menu(root, font=("Ubuntu", 10))
filemenu = Menu(menubar, tearoff=0, font=("Ubuntu", 10))
filemenu.add_command(label="Encrypt", command=askopenfile)
filemenu.add_command(label="Decrypt", command=askopenfile_dec)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0, font=("Ubuntu", 10))

helpmenu.add_command(label="Guide", command=help)
helpmenu.add_separator()
helpmenu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)
root.config(menu=menubar)

# Toolbar 1

toolbar = Frame(root, bd=1, relief=RAISED)

# Encrypt Button

img2 = Image.open("image/encrypt.png")
eimg2 = ImageTk.PhotoImage(img2)  

encryptButton = Button(toolbar, image=eimg2, relief=FLAT, command=askopenfile)
encryptButton.image = eimg2
encryptButton.pack(side=LEFT, padx=2, pady=2)

# Decrypt Button
img3 = Image.open("image/decrypt.png")
eimg3 = ImageTk.PhotoImage(img3)  

decryptButton = Button(toolbar, image=eimg3, relief=FLAT, command=askopenfile_dec)
decryptButton.image = eimg3
decryptButton.pack(side=LEFT, padx=2, pady=2)

# Help Button

img4 = Image.open("image/help.png")
eimg4 = ImageTk.PhotoImage(img4)  

helpButton = Button(toolbar, image=eimg4, relief=FLAT, command=help)
helpButton.image = eimg4
helpButton.pack(side=LEFT, padx=2, pady=2)

# About Button

img5 = Image.open("image/about.png")
eimg5 = ImageTk.PhotoImage(img5)  

aboutButton = Button(toolbar, image=eimg5, relief=FLAT, command=about)
aboutButton.image = eimg5
aboutButton.pack(side=LEFT, padx=2, pady=2)

# Exit Button

img = Image.open("image/exit.png")
eimg = ImageTk.PhotoImage(img)  

exitButton = Button(toolbar, image=eimg, relief=FLAT, command=root.quit)
exitButton.image = eimg
exitButton.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

# Label Frame
labelframe = LabelFrame(root, text="Opened File", font=("Ubuntu", 10))
labelframe.pack()

# Label
var = StringVar()
label = Label( labelframe, textvariable=var, relief=RIDGE, width = 48 , font=("Ubuntu", 10))
var.set("/path/input/file")
label.pack(side=BOTTOM,fill=BOTH)

# Scrolled Text
S = Scrollbar(labelframe)
T = Text(labelframe, height=16, width=64, font=("Ubuntu", 10))
S.pack(side=RIGHT, fill=BOTH)
T.pack(side=RIGHT, fill=BOTH)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
quote = ""
T.insert(END, quote)

# Label Frame 2
labelframe2 = LabelFrame(root, text="Result File", font=("Ubuntu", 10))
labelframe2.pack()

# Label 2
var2 = StringVar()
label2 = Label( labelframe2, textvariable=var2, relief=RIDGE, width = 48 , font=("Ubuntu", 10))
var2.set("/path/output/file")
label2.pack(side=BOTTOM,fill=BOTH)

# Scrolled Text 2
S2 = Scrollbar(labelframe2)
T2 = Text(labelframe2, height=16, width=64, font=("Ubuntu", 10))
S2.pack(side=RIGHT, fill=Y)
T2.pack(side=RIGHT, fill=Y)
S2.config(command=T2.yview)
T2.config(yscrollcommand=S2.set)
quote2 = ""
T2.insert(END, quote2)

# Top Level
top = Toplevel()
top2 = Toplevel()

# Top 1
txt_Key = ''

'''
txt_IV = ''

L1 = Label(top, text="IV", font=("Ubuntu", 10))
L1.pack(side=LEFT)

var_entry_IV = StringVar()
entry_IV = Entry(top, textvariable=var_entry_IV)
var_entry_IV.set("Random")
entry_IV.pack(side=LEFT)
'''

L2 = Label(top, text="Key", font=("Ubuntu", 10))
L2.pack(side=LEFT)

entry_Key = Entry(top)
entry_Key.pack(side=LEFT)

submit = Button(top,text="Submit",command=open_enc, font=("Ubuntu", 10))
submit.pack(side=LEFT)

cancel = Button(top,text="Cancel",command=on_hide, font=("Ubuntu", 10))
cancel.pack(side=LEFT)

# Top 2
txt_Key2 = ''

'''
txt_IV2 = ''

L12 = Label(top2, text="IV", font=("Ubuntu", 10))
L12.pack(side=LEFT)

entry_IV2 = Entry(top2)
entry_IV2.pack(side=LEFT)
'''

L22 = Label(top2, text="Key", font=("Ubuntu", 10))
L22.pack(side=LEFT)

entry_Key2 = Entry(top2)
entry_Key2.pack(side=LEFT)

submit2 = Button(top2,text="Submit",command=open_dec, font=("Ubuntu", 10))
submit2.pack(side=LEFT)

cancel2 = Button(top2,text="Cancel",command=on_hide2, font=("Ubuntu", 10))
cancel2.pack(side=LEFT)

# Tooltip
createToolTip(encryptButton, "Encrypt")
createToolTip(decryptButton, "Decrypt")
createToolTip(aboutButton, "About")
createToolTip(helpButton, "Help")
createToolTip(exitButton, "Exit")

# Main
top.withdraw()
top2.withdraw()
root.mainloop()

#0123456789abcdef