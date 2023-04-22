from manim import *

class MyBannerScene(Scene):
    def construct(self):
        logo_bk_color = "#2C3E50"
        self.set_camera_bk_color(logo_bk_color);
        self.banner(logo_bk_color, '$Welcome\;to\;\mathbb{M}ath$\;tutorial\;!')
        
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
        logo_grp = VGroup(top ,circle , circle1, eye_group)
        logo_grp.add_background_rectangle(color=logo_black)
        print(logo_grp.submobjects)
        return logo_grp

    def create_text(self, tex_string):
        ds_m = Tex(tex_string).scale(3)
        for letter in ds_m[0]:
            letter.set_color(random_bright_color()) 
        return ds_m      

    def banner(self,bk_color,banner_text):
        sym_grp = self.create_logo(bk_color)
        ds_m = self.create_text(banner_text)
        ds_m.shift(DOWN * 2)
        logo = VGroup(sym_grp, ds_m)   # order matters
        logo.scale(0.5)
        logo.move_to(ORIGIN)
        #self.add(logo)
        eye_grp=sym_grp.submobjects[4]
        self.play(FadeIn(sym_grp),Flash(eye_grp[0]),Flash(eye_grp[1]),Write(ds_m))
        self.wait()
        self.add(logo)