from manim import *
import manim
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService
from manim_voiceover.services.gtts import GTTSService
from core import common

class FractionSession(VoiceoverScene):
   def construct(self):
      # You can choose from a multitude of TTS services,
      # or in this example, record your own voice:
      self.set_speech_service(GTTSService())
      #self.set_speech_service(RecorderService())
      '''banner = common.MyBanner("$\mathbb{F}$ractions\;in\;5\;minutes\;!") 
      with self.voiceover(text="Learn fractions in 5 minutes") as tracker:
         self.play(Create(banner))
         self.wait(2)'''
       
      fraction_def_grp = self.fraction_def()
      self.add(fraction_def_grp)
      '''with self.voiceover(text="Fractions represent parts of a whole") as tracker:
         #self.play(Transform(banner, fraction_def_grp))
         self.add(fraction_def_grp)
         self.wait()''' 

      '''circle_as_parts = self.circle_as_parts()
      self.add(circle_as_parts[0]) # add circle 
      with self.voiceover(text="Half part of the circle") as tracker:
         self.play(FadeIn(circle_as_parts[1]))
         circle_as_parts[1].move_to(DOWN * 1.5)
         self.wait()
      with self.voiceover(text="one forth part of the circle") as tracker:
         self.play(FadeIn(circle_as_parts[2]))
         circle_as_parts[2].move_to(LEFT * 1.5 + UP * 1.5 )
         self.wait()'''

      rect_as_parts = self.rectangle_as_parts()   
      self.add(rect_as_parts)
      #self.play(Transform(circle_as_parts ,rect_as_parts))
      self.wait()

   def fraction_def(self):  
      plane =  NumberPlane().set_opacity(0.2)
      fraction_def = MarkupText(
         f'<span fgcolor="{RED}" underline="double" underline_color="green">Fractions</span> represents parts of a <span fgcolor="{YELLOW}">whole</span>',
         color=WHITE,
         font_size=34)
      fraction_def.shift(UP * 3) 
      fraction_def_grp = VGroup(plane , fraction_def)
      return fraction_def_grp
   
   def circle_as_parts(self):
      circle = Circle(color=RED).scale(2)
      circle_parts = VGroup(circle)
      for i in range(1,3):
         label = r"\frac{1}{" + str(2 * i) + "}"
         randon_color = random_bright_color()
         cirle_parts_label = MathTex(label , color=randon_color)
         annularSector = AnnularSector(inner_radius=0,
                         outer_radius=2, 
                         angle=PI/i, 
                         fill_opacity=0.25, 
                         color=randon_color).set_stroke(color=randon_color , width = 5)
         annularSector.rotate_about_origin(PI/i)
         cirle_parts_label.move_to(annularSector.get_center())
         circle_parts.add(VGroup(cirle_parts_label , annularSector))
      return circle_parts
   
   def rectangle_as_parts(self):
      rect = Rectangle(color=RED).scale(2)
      rect_parts = VGroup(rect)
      
      return rect_parts
     
    