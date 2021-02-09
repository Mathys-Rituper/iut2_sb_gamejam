import pygame
from field import cropspot
import pygame_menu

class Cropfield():
    def __init__(self, nb_spots,game):
        self.nb_spots = nb_spots
        self.spots = [cropspot.Cropspot() for x in range(nb_spots)]
        self.game = game
        self.planting_crop = "N"
        self.spots[0].crop_type="W"
        self.spots[0].maturation=1

    def field_interaction_menu(self):
        menu = pygame_menu.Menu(768, 1024, "Crop field", pygame_menu.themes.THEME_DARK)
        menu.add_label("Use the field to multiply your vegetables ! Growth time : 2 nights.","label-top")
        label_top = menu.get_widget("label-top")
        label_top.update_font({"size":label_top.get_font_info()["size"]*0.66})
        i = 1
        # Pour chaque emplacement

        for spot in self.spots:
            label = "Spot : " + str(i) + " : "
            if not spot.is_empty():
                label += spot.get_crop_name() + " - " + str(50 * int(spot.maturation)) + "%"
            else:
                label += "empty"
            menu.add_label(label)

            #Menu d'inteaction conditionnel selon l'état
            if spot.is_empty():
                menu.add_button("Plant a crop", self.get_plant_interaction_menu(spot), id=str(i-1))            # Si ce n'est pas encore mur
            elif spot.maturation != 2:
                menu.add_button("Clear spot", self.clear_spot,spot)

            # sinon (c'est mur)
            else:
                menu.add_button("Collect", (lambda: spot.recolte(), menu.draw(self.game.screen)))
            i+=1
        menu.disable()
        return menu

    def plant(self,spot,crop):
        self.game.player.dec_veg(crop)
        spot.new_culture(crop)
        print("planting",crop,"on spot",spot)


    def get_plant_interaction_menu(self,spot):
        plant_interaction_menu = pygame_menu.Menu(768, 1024, "Plant a crop", pygame_menu.themes.THEME_DARK)
        # Si le joueur n'a rien à planter
        if self.game.player.has_no_vegs():  # Si on ne peut rien planter
            plant_interaction_menu.add_label("You don't have anything to plant.")
        # Sinon
        else:
            available_crops = []
            for crop in self.game.player.veg_inv.keys():
                if self.game.player.veg_inv[crop]["amount"] > 0:
                    plant_interaction_menu.add_label(cropspot.crop_types[crop]["name"] + "(amount "+str(self.game.player.veg_inv[crop]["amount"])+') ')
                    plant_interaction_menu.add_button("Plant", self.plant,spot, crop)
            print("current user inventory after adding button : ", self.game.player.veg_inv)

        plant_interaction_menu.add_button("Return", pygame_menu.events.BACK)
        return plant_interaction_menu

    def set_current_crop(self,name,crop):
        self.planting_crop=crop

    def clear_spot(self,spot):
        spot.new_culture("N")
        print(spot.crop_type)