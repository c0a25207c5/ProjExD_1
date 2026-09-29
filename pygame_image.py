import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg2_img = pg.transform.flip(bg_img,True,False)#練習8背景（bg_img）を左右反転
    kk_img = pg.image.load("fig/3.png")#練習３　こうかとんsurface作成
    kk_img = pg.transform.flip(kk_img,True,False)#練習３こうかとん（kk_img）を左右反転
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x=tmr
        x=tmr%3200#練習9背景のループ
        screen.blit(bg_img, [-x, 0])#練習５背景画像を右から左
        screen.blit(bg2_img,[-x+1600,0]) #練習7背景画像surface貼り付け
        screen.blit(bg_img,[-x+3200,0]) #練習9背景画像surface貼り付け
        screen.blit(kk_img,[300,200]) #練習４こうかとんsurface貼り付け
        pg.display.update()
        tmr += 1        
        clock.tick(2000)#練習6FPSを変更


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()