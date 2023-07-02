from manim import *

class MyEndBannerScene(Scene):
    def construct(self):
        logo_bk_color = "#2C3E50"
        self.set_camera_bk_color(logo_bk_color);
        self.banner(logo_bk_color, '$\mathbb{T}hanks$!\;')
        
    def set_camera_bk_color(self, color):
        self.camera.background_color = color

    def create_logo(self, bk_color):
        ds_sym = Tex(r'$\pi$' , color=GOLD).scale(2)
        logo_black = bk_color
        circle = Circle().shift(LEFT)
        circle1 = circle.copy()
        circle1.next_to(circle)
        top = Triangle().scale(1.5)
        top.set_stroke(color=GREEN, width=20)
        top.set_fill(RED, opacity=0.5)
        top.shift(UP * 2)
        ds_sym.move_to(top.get_center_of_mass())
        triangle = Triangle().scale(0.3)
        triangle1 = Triangle().scale(0.3)
        eye_group = VGroup(triangle , triangle1)
        circle.set_stroke(color=GREEN, width=20)
        circle1.set_stroke(color=GREEN, width=20)
        triangle.set_fill(RED, opacity=0.5)
        triangle1.set_fill(RED, opacity=0.5)
        triangle.move_to(circle.get_center_of_mass())
        triangle1.move_to(circle1.get_center_of_mass())
        logo_grp = VGroup(top, circle , circle1, eye_group, ds_sym)
        print(logo_grp.submobjects)
        return logo_grp

#[BackgroundRectangle, Triangle, Circle, Circle, VGroup(Triangle, Triangle), Tex('$\\pi$')]
    def create_text(self, tex_string):
        ds_m = Tex(tex_string).scale(2.6)
        for letter in ds_m[0]:
            letter.set_color(random_bright_color()) 
        return VGroup(ds_m).arrange(RIGHT , buff=0.2)

    def create_rings(self):
        colors = [DARK_BROWN, BLUE_E, BLUE_D, BLUE_A, TEAL_B, GREEN_B, YELLOW_E]
        radius = [4 + rad * 0.2 for rad in range(len(colors))]
        circles_group = VGroup()
        circles_group.add(*[Circle(radius=rad, stroke_width=10, color=col)
                            for rad, col in zip(radius, colors)])
        return circles_group 

    def create_Subscribe(self):
        vgroup = VGroup()
        r_color = "#FF0000"
        text = Text("Subscribe", color = WHITE , font_size= 40)
        rect = RoundedRectangle(color = r_color , fill_opacity=1 , height=1.0, width=4.5)
        rect.set_stroke(color = WHITE , width = 6 , opacity=0.6)
        vgroup.add(rect, text)
        return vgroup

    def banner(self,bk_color,banner_text):
        rings_grp = self.create_rings()
        sym_grp = self.create_logo(bk_color)
        ds_m = self.create_text(banner_text)
        ds_m.move_to(DOWN * 2)
        logo = VGroup(rings_grp, sym_grp, ds_m)   # order matters
        logo.scale(0.3)
        logo.move_to(ORIGIN - [0 , -1 , 0])
        #self.add(logo)
        eye_grp=sym_grp.submobjects[3]
        self.play(Write(rings_grp), FadeIn(sym_grp) , Flash(eye_grp[0]),Flash(eye_grp[1]),Write(ds_m))
        subscribe_btn = self.create_Subscribe()
        subscribe_btn.move_to(logo.get_bottom() * 2.5)
        hand_img = ImageMobject("asserts/cursor-png-2.ico").scale(2).set_color(color= WHITE)
        hand_img.move_to(subscribe_btn.get_bottom() - [0, 0.3 , 0])
        bell_img = ImageMobject("asserts/bell-1.ico").scale(1.2).set_color(color= WHITE)
        bell_img.move_to(subscribe_btn.submobjects[1].get_left() - [0.4 , 0 , 0])
        like_img = ImageMobject("asserts/like-ico.png").scale(0.15).set_color(color= WHITE)
        like_img.move_to(subscribe_btn.submobjects[1].get_right() + [0.5 , 0 , 0])
        self.add(subscribe_btn)
        self.add(like_img)
        self.play(bell_img.animate.scale(1.2) , like_img.animate.scale(1.2))
        self.play(FadeIn(hand_img))
        self.wait()