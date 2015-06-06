from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

class Medical(Scene):

    ouch = [
        "Your bright and sparkly pedicure attracts a shark who bites one of your toes.",
         "You get stung by a stingray.",
         "You get stung by a Portugese Man O' War.",
		 "You get stung by a jellyfish."
    ]

    def enter(self):
        print Medical.ouch[randint(0, len(self.ouch)-1)]
        print "You are injured and must seek medical attention."
        exit(1)

        ##  Do we want to add option for whether or not the player gets help?
        ##  If yes, ...??  Continue the game
        ##  If no, end the game, perhaps?


class Leaving(Scene):

    def enter(self):
        print "1. Turn around and walk along the beach."
        print "2. Stare out at the ocean."
        print "3  Walk into the Gulf of Mexico until you are knee deep in the water and can feel the waves."

        choice = raw_input("> ")

        if choice == "1":
            return 'go_back_north'
        elif choice == 3:
            return 'medical'
        else:
            exit(1)

        ##  Need to explore what we do for option 1 and 2 ... are we getting
	    ##  further away from the treasure?


class StartFacingOcean(Scene):

    def enter(self):
        print "You stand barefoot on North Padre Island sand"
        print "facing west to the Gulf of Mexico. Before you, in the sand, is a small "
        print "pink bucket with your name on it. You pick it up.  A laughing seagull "
        print "flies over your head and cackles at you, dropping one of its feathers "
        print "to the south of you."
        print "\n"
        print "Do you:"
        print "1. Catch the feather as it falls through the air and put it in your bucket."
        print "2. Wait until it falls to the sand to pick it up and put it in your bucket."
        print "3. Do not touch it because you are afraid you will contract bird flu."

        choice = raw_input("> ")

        if choice == "1" or choice == "2":
            return 'glass'
        elif choice == "3":
            return 'leaving'
        else:
            print "I don't understand that!"
            return 'start_facing_ocean'

class Glass(Scene):

    def enter(self):
        print "    Glass"
        return 'shovel'

class Shovel(Scene):

    def enter(self):
        print "You continue walking along the beach and you find a small pink plastic shovel."
        print "What would you like to do with the shovel?"
        print "\n"
        print "Do you:"
        print "1. Leave it."
        print "2. Start building a sand castle, and carve a moat around the castle."
        print "3. Put the shovel in the bucket."

        choice = raw_input(">")

        if choice == "1" or choice == "2":
            return 'leaving'
        elif choice == "3":
            return 'key'
        else:
            print "I don't understand that!"
            return 'shovel'

class Key(Scene):

    def enter(self):
        print "    Key"
        return 'treasure_chest'

class TreasureChest(Scene):

    def enter(self):
        print "You see an old chest with a heart carved on top."
        return 'finished'

class Finished(Scene):

    def enter(self):
        print "You are now rich! Congratulations!"
        return 'finished'

class Map(object):

    scenes = {
        'start_facing_ocean': StartFacingOcean(),
        'glass': Glass(),
        'shovel': Shovel(),
        'key': Key(),
        'treasure_chest': TreasureChest(),
        'leaving': Leaving(),
        'medical': Medical(),
        'finished': Finished(),
    }

    ## Need more scenes definitions ... eg., inventory, walk on beach, etc

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)



a_map = Map('start_facing_ocean')
a_game = Engine(a_map)
a_game.play()
