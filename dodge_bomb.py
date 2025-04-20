import os
import sys
import pygame as pg


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
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        screen.blit(bg_img, [0, 0]) #背景画像の表示

        key_lst = pg.key.get_pressed() #押キー取得
        sum_mv = [0, 0]
        if key_lst[pg.K_UP]:
            sum_mv[1] -= 5
        if key_lst[pg.K_DOWN]:
            sum_mv[1] += 5
        if key_lst[pg.K_LEFT]:
            sum_mv[0] -= 5
        if key_lst[pg.K_RIGHT]:
            sum_mv[0] += 5
        kk_rct.move_ip(sum_mv)
        screen.blit(kk_img, kk_rct)
        pg.display.update() #画面の更新
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
