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
      banner = common.MyBanner("$Learn\;\mathbb{F}$raction\;in\;1\;minute\;!") 
      with self.voiceover(text="Learn fractions in 1 minute") as tracker:
         self.play(Create(banner))
         self.wait(2)
       
      fraction_def_grp = self.fraction_def()
      collect_objects_to_remove = []
      with self.voiceover(text="Fractions represent parts of a whole") as tracker:
         to = Transform(banner, fraction_def_grp)
         self.play(to)
         collect_objects_to_remove.append(to)
         self.wait()
      
      self.fraction_para()
      for i in [2 , 4 , 6 , 8 , 10]:
        self.create_circle_parts(i)
                 
      self.remove(fraction_def_grp)
      for to in collect_objects_to_remove:
         self.remove(to)
      self.end_para()
      self.wait()

   def fraction_def(self):  
      plane =  NumberPlane().set_opacity(0.2)
      fraction_def = MarkupText(
         f'A <span fgcolor="{RED}" underline="double" underline_color="green">fraction</span> is a part of a <span fgcolor="{YELLOW}">whole</span>',
         color=WHITE,
         font_size=34)
      fraction_def.shift(UP * 3) 
      fraction_def_grp = VGroup(plane , fraction_def)
      return fraction_def_grp
   
   def fraction_para(self):
      text1 = MarkupText(
         f'The word <span fgcolor="{RED}" underline="double" underline_color="green">fraction</span> is derived from the Latin word <span fgcolor="{YELLOW}">"fractio"</span>'   ,
         color=WHITE,font_size=34)
      text2 = MarkupText(f'which means to <span fgcolor="{RED}" underline="double" underline_color="green">break</span>.',color=WHITE, font_size=34)
      group1 = VGroup(text1, text2).arrange(DOWN)
      with self.voiceover(text="The word fraction is derived from the Latin word fractio which means to break") as tracker:
         self.play(Write(group1))
         self.wait()
      self.remove(group1)   
      text3 =  MarkupText(
         f'In Mathematics, <span fgcolor="{RED}" underline="double" underline_color="green">fractions</span> are represented as a numerical value,',
         color=WHITE,font_size=34)  
      text4 = MarkupText(f'which defines a part of a whole.',color=WHITE,font_size=34)
      group2 = VGroup(text3, text4).arrange(DOWN)
      with self.voiceover(text="In Mathematics, fractions are represented as a numerical value, which defines a part of a whole.") as tracker:
         self.play(Write(group2))
         self.wait()
      self.remove(group2)
      return

   def end_para(self):
      end_txt = Text("Thanks for watching !!!")
      with self.voiceover(text="Thanks for watching. If you liked this video, make sure to subscribe for more!") as tracker:
         self.add(end_txt)
         self.wait()
      return


   def create_circle_parts(self, parts = 4):
      PARTS = parts
      HALF_PARTS = int(PARTS/2)
      label = r"\frac{1}{" + str( PARTS) + "}"
      ANGLE = 360/PARTS
      start_point = (-2,0,0)
      end_point = (2,0,0)
      circle = Circle(radius=2,color=random_bright_color(),fill_opacity=1)
      circle.set_stroke(color=TEAL , width = 5)
      start_line = Line(start_point,end_point , color = DARK_BROWN)
      copy = start_line.copy()
      center = Dot(color=DARK_BROWN)
      self.play(Create(circle))
      self.play(Create(center))
      divider_grp = VGroup(copy)
      collect_mbojects = []
      voice_txt = "Circle divided into" + str(PARTS) + " equal parts." 
      with self.voiceover(text=voice_txt) as tracker:
         for i in range(HALF_PARTS):
            divider = copy.rotate(angle=math.radians(ANGLE), about_point=copy.get_center())
            to = Transform(start_line ,divider)
            self.play(to)
            divider_copy = divider.copy()
            self.add(divider_copy)
            collect_mbojects.append(divider)
            collect_mbojects.append(to)
            collect_mbojects.append(divider_copy)
      label = r"\frac{1}{" + str( PARTS) + "}"
      cirle_parts_label = MathTex(label , color=random_bright_color(),font_size=int(ANGLE/2))
      annularSector = AnnularSector(inner_radius=0,
                         outer_radius=2, 
                         angle=PI/HALF_PARTS, 
                         fill_opacity=0.25, 
                         color=RED).set_stroke(color=GREEN , width = 5)
      voice_txt = "Out of" +  str(PARTS)  + "equal parts, we are referring to 1 part."
      with self.voiceover(text=voice_txt) as tracker:
         self.play(FadeIn(annularSector))
         annularSector.move_to(RIGHT * 2 + UP * 1.5)
         cirle_parts_label.move_to(annularSector.get_center())
         self.add(cirle_parts_label) 
         self.wait(8)
      # Remove
      self.remove(circle,start_line,center,annularSector,cirle_parts_label,divider_grp)
      for line in collect_mbojects:
         self.remove(line)
      return
   
     
    