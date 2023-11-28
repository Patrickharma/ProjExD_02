import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1600, 900
VX, VY = 5, 5

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("/Users/patrickdharma/Desktop/プロエン/ProjExD2023/ex02-20231128/fig/pg_bg.jpg")
    kk_img = pg.image.load("/Users/patrickdharma/Desktop/プロエン/ProjExD2023/ex02-20231128/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    # 爆弾の作成
    ball = pg.Surface((20, 20))
    pg.draw.circle(ball, (255, 0, 0), (10, 10), 10)
    ball.set_colorkey((0, 0, 0))
    ball_rct = ball.get_rect()  # 練習２：爆弾surface設定
    ball_rct.centerx = random.randint(0, WIDTH)
    ball_rct.centery = random.randint(0, HEIGHT)
    #create clock
    clock = pg.time.Clock()
    tmr = 0
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        #background blit
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])

        #ball blit
        screen.blit(ball, ball_rct)
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()