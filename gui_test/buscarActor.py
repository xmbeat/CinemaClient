
#! /usr/bin/python

from xpresser import Xpresser
import time

def main():
    xp = Xpresser()
    xp.load_images('/home/jxsxs/Escritorio/Final-Project-Alex-master/Xpresser/Images')
    time.sleep(3)
    xp.click('name-actor')
    xp.type('michael j fox')
    xp.click(1321,100)
    time.sleep(3)
    xp.click(703,135)
    xp.click(703,135)
    xp.click(1323,135)
    #xp.click('btn-seleccionar-actor')
       
if __name__ == "__main__":
     main()
