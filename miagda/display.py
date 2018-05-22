from pygame.event import *
import pygame
from pygame import *
from miagda.render_utils import render_textrect
import pkg_resources
import toml
import miagda.gadget as gadget

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE = (0, 0, 200)
GREEN = (0, 200, 0)

class Config(dict):

    def __init__(self):
        pass

    def common(self):
        return self.get("common")

    def gadgets(self):
        return  self.get("gadgets")




class MiAgDa:



    def __init__(self):

        self.gadgets = dict()
        self.screens = dict()


        print("Start Mi Ag Da")

        toml_file =  filepath = pkg_resources.resource_filename(__name__, "data/sample.toml")
        self.config = toml.load(toml_file, Config)
        pygame.init()

        self.display_surface = pygame.display.set_mode(self.config.common()["screen_size"], pygame.RESIZABLE)
        print(pygame.display.Info())


        bg_file =  filepath = pkg_resources.resource_filename(__name__, "data/background.png")
        self.bgimage = pygame.image.load(bg_file)

        self.read_config()

        self.running = True
        while self.running:  # main game loop
            for evt in pygame.event.get():
                if evt.type == KEYDOWN and evt.key == K_ESCAPE:
                    self.running = False

                #self.currentscreen.update(evt)

            #self.currentscreen.draw(display_surface)

            self.display_surface.blit(self.bgimage, (0,0))
            self.renderWatermark()

            pygame.display.update()

            # do your non-rendering game loop computation here
            # to reduce CPU usage, call this guy:
            time.wait(20)


    def renderWatermark(self):
        filepath = pkg_resources.resource_filename(__name__, "data/Chunkfive Ex.ttf")
        font = pygame.font.Font(filepath, 24)
        text_surface = pygame.Surface((200,100), pygame.SRCALPHA)
        render_textrect("MiAgDa V0.0.1", font, text_surface, GREEN, 1)
        self.display_surface.blit(text_surface, (1920-200, 1080-50))

    def exit_player(self):
        self.running = False

    def read_config(self):

        for gadget_name, gadget_def in self.config.gadgets().items():
            gadget_type = gadget_def["type"]
            if "textFromURL" == gadget_type:
                self.gadgets[gadget_name] = gadget.TextFromUrlGadget(gadget_def)



if __name__ == "__main__":
    print("start")
    MiAgDa()



