import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1600, 900
VX, VY = 5, 5
delta = {
    pg.K_UP: (0, -5),
    pg.K_DOWN: (0, +5),
    pg.K_LEFT: (-5, 0),
    pg.K_RIGHT: (+5, 0)
}



def check_bound(rct: pg.Rect) -> tuple[bool, bool]:
    """
    オブジェクトが画面内or画面外を判定し、真理値タプルを返す関数
    引数 rct:効果とんor爆弾surfaceのrect
    戻り値：横方向、縦方向判定結果（画面内:True/画面外:False)
    """
    yoko, tate = True, True
    if rct.left < 0 or rct.right > WIDTH:  
        yoko = False
    if rct.top < 0 or rct.bottom > HEIGHT:
        tate = False
    return yoko, tate

def main():
    global VX, VY
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("/Users/patrickdharma/Desktop/プロエン/ProjExD2023/ex02-20231128/fig/pg_bg.jpg")
    # コウカトン作成
    kk_img = pg.image.load("/Users/patrickdharma/Desktop/プロエン/ProjExD2023/ex02-20231128/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 900, 400

    # 爆弾作成
    ball = pg.Surface((20, 20))
    pg.draw.circle(ball, (255, 0, 0), (10, 10), 10)
    ball.set_colorkey((0, 0, 0))
    ball_rct = ball.get_rect()  # 練習２：爆弾surface設定
    ball_rct.centerx = random.randint(0, WIDTH)
    ball_rct.centery = random.randint(0, HEIGHT)
    # クロック作成
    clock = pg.time.Clock()
    tmr = 0

    flipped_kk = pg.transform.flip(kk_img, True, False)
    rotozoom_dict = {
    (-5, 0): pg.transform.rotozoom(kk_img, 0, 1),
    (-5, -5): pg.transform.rotozoom(kk_img, -45, 1),
    (-5, +5): pg.transform.rotozoom(kk_img, 45, 1),
    (0, -5): pg.transform.rotozoom(flipped_kk, 90, 1),
    (0, +5): pg.transform.rotozoom(flipped_kk, -90, 1),
    (+5, -5): pg.transform.rotozoom(flipped_kk, 45, 1),
    (+5, +5): pg.transform.rotozoom(flipped_kk, -45, 1),
    (+5, 0): pg.transform.rotozoom(flipped_kk, 0, 1)
}
    
    while True:
        # イベントハンドラー
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        # 衝突処理
        if kk_rct.colliderect(ball_rct):
            print("Game Over")
            return
        # コウカトンの動き
        key_lst = pg.key.get_pressed()
        tot_travel = [0, 0]
        for k, tpl in delta.items():
            if key_lst[k]:
                tot_travel[0] += tpl[0]
                tot_travel[1] += tpl[1]

        # 飛ぶ方向に従ってコウカトン画像を切り替わる
        if tuple(tot_travel) in rotozoom_dict.keys():
            kk_img = rotozoom_dict[tuple(tot_travel)]
        
        kk_rct.move_ip(tot_travel[0], tot_travel[1])
        # check bound
        if check_bound(kk_rct) != (True, True):
            kk_rct.move_ip(-tot_travel[0], -tot_travel[1])
        # 背景ブリット
        screen.blit(bg_img, [0, 0])
        # コウカトンブリット
        screen.blit(kk_img, kk_rct)
        # 爆弾ブリット
        screen.blit(ball, ball_rct)
        ball_rct.move_ip(VX, VY)  
        yoko, tate = check_bound(ball_rct)
        if not yoko:  # 横方向にはみ出たら
            VX *= -1
        if not tate:  # 横方向にはみ出たら
            VY *= -1
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()