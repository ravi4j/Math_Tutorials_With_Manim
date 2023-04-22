from manim import *
import manim
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService
from manim_voiceover.services.gtts import GTTSService
import MyBanner

class MyBannerDemo(VoiceoverScene):
    def construct(self):
        # You can choose from a multitude of TTS services,
        # or in this example, record your own voice:
        self.set_speech_service(GTTSService())
         #self.set_speech_service(RecorderService())
        banner = MyBanner.MyBanner() 
        V_Title = "Fraction" 
        title = Title(f"Math Tutorial : {V_Title}")
        self.play(Create(banner))
        self.play(Unwrite(banner))
        with self.voiceover(text="Welcome to Math Learning.") as tracker:
            self.play(Write(banner.create_text("Fraction")))
            self.wait(2)
        
    