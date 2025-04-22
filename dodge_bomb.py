import os
import sys
import pygame as pg
import random

WIDTH, HEIGHT = 1100, 650
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("逃げろ！こうかとん") #ウィンドウタイトル
    screen = pg.display.set_mode((WIDTH, HEIGHT)) #スクリーン
    bg_img = pg.image.load("fig/pg_bg.jpg")   #背景画像のロード
    kk_img = pg.transform.rotozoom(pg.image.load("fig/3.png"), 0, 0.9) #0.9倍画像
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200 #Rect取得、画像の初期位置を300, 200 に設定
    clock = pg.time.Clock()
    tmr = 0
    DELTA = {"K_UP" : (0,-5) , "K_DOWN" : (0,5), "K_LEFT" : (-5,0), "K_RIGHT" : (5,0) } #辞書生成　練習1
    bb_img = pg.Surface((20, 20)) #円の生成　練習2
    pg.draw.circle(bb_img, (255, 0, 0), (10, 10), 10)
    bb_img.set_colorkey((0, 0, 0))
    bb_rct = bb_img.get_rect()
    rx = random.randint(0,1100)
    ry = random.randint(0,650)
    bb_rct.center = (rx, ry)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        screen.blit(bg_img, [0, 0]) #背景画像の表示
        key_lst = pg.key.get_pressed() #押キー取得
        sum_mv = [0, 0]
        if key_lst[pg.K_UP]:
            sum_mv = DELTA["K_UP"]
        if key_lst[pg.K_DOWN]:
            sum_mv = DELTA["K_DOWN"]
        if key_lst[pg.K_LEFT]:
            sum_mv = DELTA["K_LEFT"]
        if key_lst[pg.K_RIGHT]:
            sum_mv = DELTA["K_RIGHT"]
        kk_rct.move_ip(sum_mv)
        screen.blit(kk_img, kk_rct)
        screen.blit(bb_img, bb_rct) #ばくだんのblit
        pg.display.update() #画面の更新
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
