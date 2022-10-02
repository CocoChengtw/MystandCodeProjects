"""
File: my_drawing.py
Name: Coco
----------------------
This project is to draw a picture with campy.
"""

from campy.graphics.gobjects import GOval, GRect, GArc, GPolygon, GLine
from campy.graphics.gwindow import GWindow

window = GWindow(width=500, height=600, title='MyFace')


def main():
    """
    Title: Ice Critten

    To be (an ice cream), or not to be (an ice cream).
    That is a cat, anyway.
    """
    bk = GRect(500, 600)
    bk.filled = True
    bk.fill_color = 'cadetblue'
    bk.color = 'cadetblue'
    window.add(bk)

    cat = GOval(250, 250, x=125, y=125)
    cat.filled = True
    cat.fill_color = 'antiquewhite'
    cat.color = 'antiquewhite'
    window.add(cat)

    bk_d = GRect(500, 350, x=0, y=270)
    bk_d.filled = True
    bk_d.fill_color = 'cadetblue'
    bk_d.color = 'cadetblue'
    window.add(bk_d)

    tail_t = GOval(10, 120, x=124, y=250)
    tail_t.filled = True
    tail_t.fill_color = 'antiquewhite'
    tail_t.color = 'antiquewhite'
    window.add(tail_t)

    corn = GPolygon()
    corn.add_vertex((125, 250))
    corn.add_vertex((375, 250))
    corn.add_vertex((250, 550))
    corn.filled = True
    corn.fill_color = 'sandybrown'
    corn.color = 'sandybrown'
    window.add(corn, x=0, y=20)

    corn_l1 = GLine(180, 275, 140, 305)
    corn_l1.color = 'sienna'
    window.add(corn_l1)

    corn_l2 = GLine(265, 275, 160, 355)
    corn_l2.color = 'sienna'
    window.add(corn_l2)

    corn_l3 = GLine(350, 275, 180, 405)
    corn_l3.color = 'sienna'
    window.add(corn_l3)

    corn_l4 = GLine(340, 355, 205, 460)
    corn_l4.color = 'sienna'
    window.add(corn_l4)

    corn_l5 = GLine(290, 470, 230, 520)
    corn_l5.color = 'sienna'
    window.add(corn_l5)

    corn_l6 = GLine(315, 275, 350, 310)
    corn_l6.color = 'sienna'
    window.add(corn_l6)

    corn_l7 = GLine(250, 275, 335, 365)
    corn_l7.color = 'sienna'
    window.add(corn_l7)

    corn_l8 = GLine(180, 275, 310, 420)
    corn_l8.color = 'sienna'
    window.add(corn_l8)

    corn_l9 = GLine(150, 320, 285, 485)
    corn_l9.color = 'sienna'
    window.add(corn_l9)

    corn_l10 = GLine(220, 498, 258, 550)
    corn_l10.color = 'sienna'
    window.add(corn_l10)

    foot1 = GOval(20, 55, x=180, y=240)
    foot1.filled = True
    foot1.fill_color = 'antiquewhite'
    foot1.color = 'antiquewhite'
    window.add(foot1)

    foot2 = GOval(18, 45, x=275, y=240)
    foot2.filled = True
    foot2.fill_color = 'antiquewhite'
    foot2.color = 'antiquewhite'
    window.add(foot2)

    foot3 = GOval(18, 45, x=330, y=240)
    foot3.filled = True
    foot3.fill_color = 'antiquewhite'
    foot3.color = 'antiquewhite'
    window.add(foot3)

    eye_l = GOval(15, 15, x=280, y=220)
    eye_l.filled = True
    eye_l.fill_color = 'white'
    eye_l.color = 'white'
    window.add(eye_l)

    eye_lb = GOval(8, 8, x=284, y=224)
    eye_lb.filled = True
    eye_lb.fill_color = 'black'
    eye_lb.color = 'black'
    window.add(eye_lb)

    eye_r = GOval(15, 15, x=325, y=220)
    eye_r.filled = True
    eye_r.fill_color = 'white'
    eye_r.color = 'white'
    window.add(eye_r)

    eye_rb = GOval(8, 8, x=329, y=224)
    eye_rb.filled = True
    eye_rb.fill_color = 'black'
    eye_rb.color = 'black'
    window.add(eye_rb)

    mouth_l = GArc(25, 25, 0, -90)
    mouth_l.color = 'sienna'
    window.add(mouth_l, x=297, y=225)

    mouth_r = GArc(25, 25, 180, 90)
    mouth_r.color = 'sienna'
    window.add(mouth_r, x=310, y=225)

    ear_ll = GLine(284, 190, 272, 205)
    ear_ll.color = 'sienna'
    window.add(ear_ll)

    ear_lr = GLine(284, 190, 296, 203)
    ear_lr.color = 'sienna'
    window.add(ear_lr)

    ear_rl = GLine(335, 190, 320, 203)
    ear_rl.color = 'sienna'
    window.add(ear_rl)

    ear_rr = GLine(335, 190, 345, 205)
    ear_rr.color = 'sienna'
    window.add(ear_rr)

    candy1 = GLine(180, 155, 202, 150)
    candy1.color = 'darksage'
    window.add(candy1)
    candy11 = GLine(181, 156, 203, 151)
    candy11.color = 'darksage'
    window.add(candy11)
    candy111 = GLine(182, 157, 204, 152)
    candy111.color = 'darksage'
    window.add(candy111)
    candy1111 = GLine(183, 158, 205, 153)
    candy1111.color = 'darksage'
    window.add(candy1111)

    candy2 = GLine(160, 180, 170, 160)
    candy2.color = 'indianred'
    window.add(candy2)
    candy22 = GLine(161, 181, 171, 161)
    candy22.color = 'indianred'
    window.add(candy22)
    candy222 = GLine(162, 182, 172, 162)
    candy222.color = 'indianred'
    window.add(candy222)
    candy2222 = GLine(163, 183, 173, 163)
    candy2222.color = 'indianred'
    window.add(candy2222)

    candy3 = GLine(188, 170, 212, 170)
    candy3.color = 'orange'
    window.add(candy3)
    candy33 = GLine(188, 171, 212, 171)
    candy33.color = 'orange'
    window.add(candy33)
    candy333 = GLine(188, 172, 212, 172)
    candy333.color = 'orange'
    window.add(candy333)
    candy3333 = GLine(188, 173, 212, 173)
    candy3333.color = 'orange'
    window.add(candy3333)
    candy33333 = GLine(188, 174, 212, 174)
    candy33333.color = 'orange'
    window.add(candy33333)

    candy4 = GLine(220, 140, 230, 160)
    candy4.color = 'darkslateblue'
    window.add(candy4)
    candy44 = GLine(221, 140, 231, 160)
    candy44.color = 'darkslateblue'
    window.add(candy44)
    candy444 = GLine(222, 140, 232, 160)
    candy444.color = 'darkslateblue'
    window.add(candy444)
    candy4444 = GLine(223, 140, 233, 160)
    candy4444.color = 'darkslateblue'
    window.add(candy4444)
    candy44444 = GLine(224, 140, 234, 160)
    candy44444.color = 'darkslateblue'
    window.add(candy44444)

    candy5 = GLine(247, 137, 270, 135)
    candy5.color = 'darksage'
    window.add(candy5)
    candy55 = GLine(248, 138, 271, 136)
    candy55.color = 'darksage'
    window.add(candy55)
    candy555 = GLine(249, 139, 272, 137)
    candy555.color = 'darksage'
    window.add(candy555)
    candy5555 = GLine(250, 140, 273, 138)
    candy5555.color = 'darksage'
    window.add(candy5555)

    candy6 = GLine(240, 169, 255, 149)
    candy6.color = 'indianred'
    window.add(candy6)
    candy66 = GLine(241, 170, 256, 150)
    candy66.color = 'indianred'
    window.add(candy66)
    candy666 = GLine(242, 171, 257, 151)
    candy666.color = 'indianred'
    window.add(candy666)
    candy6666 = GLine(243, 172, 258, 152)
    candy6666.color = 'indianred'
    window.add(candy6666)

    candy7 = GLine(265, 155, 290, 158)
    candy7.color = 'darkslateblue'
    window.add(candy7)
    candy77 = GLine(265, 156, 290, 159)
    candy77.color = 'darkslateblue'
    window.add(candy77)
    candy777 = GLine(265, 157, 290, 160)
    candy777.color = 'darkslateblue'
    window.add(candy777)
    candy7777 = GLine(265, 158, 290, 161)
    candy7777.color = 'darkslateblue'
    window.add(candy7777)

    candy8 = GLine(288, 143, 312, 150)
    candy8.color = 'orange'
    window.add(candy8)
    candy88 = GLine(288, 144, 312, 151)
    candy88.color = 'orange'
    window.add(candy88)
    candy888 = GLine(288, 145, 312, 152)
    candy888.color = 'orange'
    window.add(candy888)
    candy8888 = GLine(288, 146, 312, 153)
    candy8888.color = 'orange'
    window.add(candy8888)

    candy9 = GLine(300, 168, 325, 170)
    candy9.color = 'cadetblue'
    window.add(candy9)
    candy99 = GLine(300, 169, 325, 171)
    candy99.color = 'cadetblue'
    window.add(candy99)
    candy999 = GLine(300, 170, 325, 172)
    candy999.color = 'cadetblue'
    window.add(candy999)
    candy9999 = GLine(300, 171, 325, 173)
    candy9999.color = 'cadetblue'
    window.add(candy9999)

    candy10 = GLine(210, 188, 234, 185)
    candy10.color = 'cadetblue'
    window.add(candy10)
    candy1010 = GLine(210, 189, 234, 186)
    candy1010.color = 'cadetblue'
    window.add(candy1010)
    candy101010 = GLine(210, 190, 234, 187)
    candy101010.color = 'cadetblue'
    window.add(candy101010)
    candy10101010 = GLine(210, 191, 234, 188)
    candy10101010.color = 'cadetblue'
    window.add(candy10101010)


if __name__ == '__main__':
    main()
