from __future__ import annotations

__all__ = ["MyBanner"]

from manim import *

class MyBanner(VGroup):
    def __init__(self ):
        super().__init__()

        logo_bk_color = "#2C3E50"
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
        return logo_grp

    def create_text(self, tex_string):
        ds_m = Tex(tex_string).scale(3)
        for letter in ds_m[0]:
            letter.set_color(random_bright_color()) 
        return ds_m      

    def banner(self,bk_color,banner_text):
        self.sym_grp = self.create_logo(bk_color)
        self.ds_m = self.create_text(banner_text)
        self.ds_m.shift(DOWN * 2)
        logo = VGroup(self.sym_grp, self.ds_m)
        logo.scale(0.5)
        logo.move_to(ORIGIN)
        self.add(logo)
        self.eye_grp=self.sym_grp.submobjects[3]
        self.add(logo)

    @override_animation(Create)
    def create(self, run_time: float = 2) -> AnimationGroup:
        return AnimationGroup(
            FadeIn(self.sym_grp, run_time=run_time),
            Flash(self.eye_grp[0], run_time=run_time / 2),
            Flash(self.eye_grp[1], run_time=run_time / 2),
            Write(self.ds_m),
            lag_ratio=0.1,
        )    

   