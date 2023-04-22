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
        banner = MyBanner.MyBanner("$\mathbb{F}$ractions\;in\;5\;minitues\;!") 
        with self.voiceover(text="Welcome to Math Learning.") as tracker:
           self.play(Create(banner))
           self.wait(2)
        
    