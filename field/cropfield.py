import pygame
from field import cropspot
import pygame_menu

class Cropfield():
    def __init__(self, nb_spots,game):
        self.nb_spots = nb_spots
        self.spots = [cropspot.Cropspot() for x in range(nb_spots)]
        self.game = game

    def field_interaction_menu(self):
        menu = pygame_menu.Menu(200, 300, "Crop field", pygame_menu.themes.THEME_DARK)
        menu.add_label("Use the field to multiply your vegetables ! Growth time : 2 nights.")
        # Pour chaque emplacement
        for spot in self.spots:
            i = 1
            label = "Spot : " + str(i) + " : "
            if not spot.is_empty():
                label += spot.crop_type["name"] + " - " + str(50 * spot.maturation) + "%"
            else:
                label += "empty"
            # Si rien n'est planté dessus pour le moment
            if spot.is_empty():

                plant_interaction_menu = pygame_menu.Menu(200, 300, "Plant a crop", pygame_menu.themes.THEME_DARK)
                # Si le joueur n'a rien à planter
                if self.game.player.has_no_vegs(): #Si on ne peut rien planter
                    plant_interaction_menu.add_label("You don't have anything to plant.")
                # Sinon
                else:
                    for crop in self.game.player.veg_inv.keys():
                        if self.game.player.veg_inv[crop]["amount"] > 0:
                            plant_interaction_menu.add_label(
                                self.game.player.veg_inv[crop]["name"] + " (current count" + self.game.player.veg_inv[crop][
                                    "amount"] + ")")
                            plant_interaction_menu.add_button("Plant", (lambda : spot.new_culture(crop), self.game.player.dec_veg(crop), menu.draw(self.game.screen)))
                plant_interaction_menu.add_button("Return", pygame_menu.events.BACK)

                menu.add_button("Plant a crop", plant_interaction_menu)

            # Si ce n'est pas encore mur
            elif spot.maturation != 2:
                menu.add_button("Clear spot", (lambda: spot.new_culture('N'), menu.draw(self.game.screen)))

            # sinon (c'est mur)
            else:
                menu.add_button("Collect", (lambda: spot.recolte(), menu.draw(self.game.screen)))
            menu.add_button("CLOSE", pygame_menu.events.CLOSE)
        return menu