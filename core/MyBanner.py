from manim import *

class MyBanner(Scene):
    def construct(self):
        logo_bk_color = "#2C3E50"
        self.set_camera_bk_color(logo_bk_color);
        self.banner(logo_bk_color)
        
    def set_camera_bk_color(self, color):
        self.camera.background_color = color

    def create_logo(self, bk_color):
        logo_black = bk_color
        circle = Circle().shift(LEFT)
        circle1 = circle.copy()
        circle1.next_to(circle)
        top = Triangle().scale(1.5)
        top.set_stroke(color=GREEN, width=20)
        top.set_fill(RED, opacity=0.5)
        top.shift(UP * 2)
        triangle = Triangle().scale(0.3)
        triangle1 = Triangle().scale(0.3)
        eye_group = VGroup(triangle , triangle1)
        circle.set_stroke(color=GREEN, width=20)
        circle1.set_stroke(color=GREEN, width=20)
        triangle.set_fill(RED, opacity=0.5)
        triangle1.set_fill(RED, opacity=0.5)
        triangle.move_to(circle.get_center_of_mass())
        triangle1.move_to(circle1.get_center_of_mass())
        logo_grp = VGroup(top ,circle , circle1 , eye_group)
        logo_grp.add_background_rectangle(color=logo_black)
        return logo_grp    

    def banner(self,bk_color):
        sym_grp = self.create_logo(bk_color)
        ds_m = Tex(r'$Welcome\;to\;\mathbb{M}ath$\;tutorial\;!').scale(3)
        for letter in ds_m[0]:
            letter.set_color(random_bright_color())
        ds_m.shift(DOWN * 2)
        logo = VGroup(sym_grp, ds_m)   # order matters
        logo.scale(0.5)
        logo.move_to(ORIGIN)
        self.play(FadeIn(sym_grp),Flash(sym_grp[0]),Flash(sym_grp[1]),Write(ds_m))
        self.wait()

   