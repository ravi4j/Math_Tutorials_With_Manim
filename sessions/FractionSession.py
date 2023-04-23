import math
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
      banner = common.MyBanner("$\mathbb{F}$ractions\;in\;5\;minutes\;!") 
      with self.voiceover(text="Learn fractions in 5 minutes") as tracker:
         self.play(Create(banner))
         self.wait(2)
       
      fraction_def_grp = self.fraction_def()
      self.add(fraction_def_grp)
      with self.voiceover(text="Fractions represent parts of a whole") as tracker:
         self.play(Transform(banner, fraction_def_grp))
         self.add(fraction_def_grp)
         self.wait()
      
      for i in [2 , 4 , 6 , 8 , 10]:
         voice_txt = "Divided circle into" + str(i) + " equal parts"
         with self.voiceover(text=voice_txt) as tracker:
            self.create_circle_parts(i)
            self.wait()

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
   
   def create_circle_parts(self, parts = 4):
      PARTS = parts
      HALF_PARTS = int(PARTS/2)
      label = r"\frac{1}{" + str( PARTS) + "}"
      ANGLE = 360/PARTS
      start_point = (-2,0,0)
      end_point = (2,0,0)
      circle = Circle(radius=2,color=RED,fill_opacity=1)
      circle.set_stroke(color=WHITE , width = 5)
      start_line = Line(start_point,end_point)
      copy = start_line.copy()
      center = Dot()
      self.play(Create(circle))
      self.play(Create(center))
      divider_grp = VGroup()
      for i in range(HALF_PARTS):
         divider = copy.rotate(angle=math.radians(ANGLE), about_point=copy.get_center())
         to = Transform(start_line ,divider)
         self.play(to)
         divider_grp.add(divider.copy())
         self.add(divider.copy()) 
      label = r"\;=\;\frac{1}{" + str( PARTS) + "}"
      randon_color = random_bright_color()
      cirle_parts_label = MathTex(label , color=randon_color , font_size = 144)
      cirle_parts_label.move_to(RIGHT * 4)
      self.add(cirle_parts_label) 
      annularSector = AnnularSector(inner_radius=0,
                         outer_radius=2, 
                         angle=PI/HALF_PARTS, 
                         fill_opacity=0.25, 
                         color=randon_color).set_stroke(color=randon_color , width = 5)
      self.add(annularSector) 
      self.wait()
      # Remove
      self.remove(annularSector,cirle_parts_label,divider_grp)
   
     
    