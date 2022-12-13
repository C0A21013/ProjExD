import pygame as pg
import random
import sys
import time


def check_bound(obj_rct, scr_rct):
    # 第1引数：こうかとんrectまたは爆弾rect
    # 第2引数：スクリーンrect
    # 範囲内：+1／範囲外：-1
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate

def check_bound2(obj_rct, scr_rct):
    yoko2, tate2 = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko2 = -1.5
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate2 = -1.5
    return yoko2, tate2

def gameover(scrn_sfc):
    font1 = pg.font.SysFont("hg正楷書体pro", 150)
    text1 = font1.render("ゲームオーバー", True, (255,0,0))
                        
    scrn_sfc.fill((0,0,0))  #画面を黒で塗りつぶす
    scrn_sfc.blit(text1, (350,300))

    pg.display.update() #描画処理を実行
    time.sleep(3)


def main():
    clock =pg.time.Clock()
    
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))
    scrn_rct = scrn_sfc.get_rect()
    pgbg_sfc = pg.image.load("fig/pg_bg.jpg")
    pgbg_rct = pgbg_sfc.get_rect()

    
    tori_sfc = pg.image.load("fig/mychr2.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 1.5)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400
    # scrn_sfcにtori_rctに従って，tori_sfcを貼り付ける
    scrn_sfc.blit(tori_sfc, tori_rct) 

    bomb_sfc = pg.Surface((20, 20)) # 正方形の空のSurface
    bomb_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = random.randint(0, scrn_rct.width)
    bomb_rct.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(bomb_sfc, bomb_rct) 
    vx, vy = +1, +1

    bomb2_sfc = pg.Surface((20, 20)) # 正方形の空のSurface
    bomb2_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb2_sfc, (50, 205, 50), (10, 10), 10)
    bomb2_rct = bomb2_sfc.get_rect()
    bomb2_rct.centerx = random.randint(0, scrn_rct.width)
    bomb2_rct.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(bomb2_sfc, bomb2_rct) 
    vx2, vy2 = +1, +1

    while True:
        scrn_sfc.blit(pgbg_sfc, pgbg_rct) 

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        key_dct = pg.key.get_pressed() # 辞書型
        if key_dct[pg.K_UP]:
            tori_rct.centery -= 1
        if key_dct[pg.K_DOWN]:
            tori_rct.centery += 1
        if key_dct[pg.K_LEFT]:
            tori_rct.centerx -= 1
        if key_dct[pg.K_RIGHT]:
            tori_rct.centerx += 1

        if check_bound(tori_rct, scrn_rct) != (+1, +1):
            # どこかしらはみ出ていたら
            if key_dct[pg.K_UP]:
                tori_rct.centery += 1
            if key_dct[pg.K_DOWN]:
                tori_rct.centery -= 1
            if key_dct[pg.K_LEFT]:
                tori_rct.centerx += 1
            if key_dct[pg.K_RIGHT]:
                tori_rct.centerx -= 1            
        scrn_sfc.blit(tori_sfc, tori_rct) 

        bomb_rct.move_ip(vx, vy)
        scrn_sfc.blit(bomb_sfc, bomb_rct) 
        yoko, tate = check_bound(bomb_rct, scrn_rct)
        vx *= yoko
        vy *= tate

        if tori_rct.colliderect(bomb_rct):
            gameover(scrn_sfc)
            return

        bomb2_rct.move_ip(vx2, vy2)
        scrn_sfc.blit(bomb2_sfc, bomb2_rct) 
        yoko2, tate2 = check_bound2(bomb2_rct, scrn_rct)        
        vx2 *= yoko2
        vy2 *= tate2
        
        if tori_rct.colliderect(bomb2_rct):
            gameover(scrn_sfc)
            return
        
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()