import os
import random
import sys
import pygame as pg
import time


WIDTH, HEIGHT = 1100, 650
DELTA = {pg.K_UP : (0,-5) , pg.K_DOWN : (0,+5), pg.K_LEFT : (-5,0), pg.K_RIGHT : (5,0) }  #辞書生成　練習1

os.chdir(os.path.dirname(os.path.abspath(__file__)))
bb_accs = [a for a in range(1,11)]
def check_bound(rct: pg.Rect) -> tuple[bool, bool]:
    """
    引数：こうかとんRectかばくだんRect
    戻り値：判定結果のタプル（たてよこ）
    画面内：True 画面外：False
    """
    yoko, tate = True, True
    if rct.left < 0 or WIDTH < rct.right:  #画面内(横方向)の判定
        yoko = False
    if rct.top < 0 or HEIGHT < rct.bottom:  #画面内(縦方向)の判定
        tate = False
    return yoko, tate

def gameover(screen: pg.Surface) -> None:
    """
    演習1
    gameoverになった際の判定
    引数：Screen
    画面を暗くする、こうかとん、GameOverの表示
    5秒停止
    """
    blackout = pg.Surface((WIDTH, HEIGHT))
    fonto  = pg.font.Font(None, 80)
    text = fonto.render("Game Over", True, (255,255,255))
    cry_img = pg.image.load("../Lecture02/fig/8.png")

    pg.draw.rect(blackout, (0,0,0), (0, 0, WIDTH, HEIGHT))
    blackout.set_alpha(200)

    screen.blit(blackout, (0,0))
    screen.blit(text, [400, 300])
    screen.blit(cry_img, (350, 300))
    screen.blit(cry_img, (730, 300))

    pg.display.update()
    time.sleep(5)

def acc(bb_imgs: list):
    """
    演習2
    時間とともに爆弾を大きくしていく
    引数：りすと
    戻り値：円の大きさの段階を指し示す
    """
    for r in range(1, 11):
        bb_img = pg.Surface((20*r, 20*r))
        pg.draw.circle(bb_img, (255, 0, 0), (10*r, 10*r), 10*r)
        bb_imgs.append(bb_img)
    return bb_imgs

def get_kk_img(sum_mv: tuple, [int, int]) -> pg.Surface:
    if sum_mv[0] == 0 and sum_mv[1] == -5:
        pg.transform.rotate(kk_img, )


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("fig/pg_bg.jpg")    
    kk_img = pg.transform.rotozoom(pg.image.load("fig/3.png"), 0, 0.9)
    #kk_img = get_kk_img((0, 0))
    #kk_img = get_kk_img(tuple(sum_mv))
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200
    tmr = 0
    bb_accs = [a for a in range(1,11)]  #加速度のリスト 10段階
    vx, vy = +5, -5

    bb_img = pg.Surface((20, 20))  #円の生成　練習2
    pg.draw.circle(bb_img, (255, 0, 0), (10, 10), 10)
    bb_rct = bb_img.get_rect()
    bb_rct.center = random.randint(0, WIDTH), random.randint(0, HEIGHT)
    clock = pg.time.Clock()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        screen.blit(bg_img, [0, 0]) 


        #if kk_rct.colliderect(bb_rct):  #こうかとんRectと爆弾Rectの衝突の判定
            #print("GAMEOVER")
            #return
        
        if kk_rct.colliderect(bb_rct):
            print("GAMEOVER")
            gameover(screen)
            return
        
        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
        for key, mv in DELTA.items():
            if key_lst[key]:
                sum_mv[0] += mv[0]
                sum_mv[1] += mv[1]
        kk_rct.move_ip(sum_mv)

        if check_bound(kk_rct) != (True, True):
            kk_rct.move_ip(-sum_mv[0], -sum_mv[1])
        screen.blit(kk_img, kk_rct)

        avx = vx*bb_accs[min(tmr//500, 9)]  #ばくだんの速度(x方向)
        avy = vy*bb_accs[min(tmr//500, 9)]  #ばくだんの速度(y方向)
        bb_rct.move_ip(avx, avy)

        yoko, tate = check_bound(bb_rct)
        if not yoko: #左右のはみ出し
            vx *= -1
        if not tate:
            vy *= -1

        bb_imgs = []
        acc(bb_imgs)
        bb_img = bb_imgs[min(tmr//500, 9)]
        bb_img.set_colorkey((0, 0, 0))
        screen.blit(bb_img, bb_rct)
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
