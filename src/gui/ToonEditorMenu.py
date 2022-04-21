from gui import OptionsMenu

class ToonEditorMenu(OptionsMenu):
    def __init__(self):
        frame =  super.__init__()




    def loadGUI(self):
        def funnyFunction():
            self.notify.warning("You clicked on a button that has no function yet..or does it? Only time will tell......just kidding, I'm tired.\nIf you found this, I'd like a cookie, preferably chocolate chip.")





        self.generateToonButton = DirectButton(
            parent = self.optionsScroll.getCanvas(),
            geom = generateButtonGeom,
            pos = (-0.25, 0, -4.25),
            scale = 0.2,
            text = 'Generate Toon',
            text_scale = 0.35,
            text_font = loader.loadFont(toon_font),
            relief = None,
            command = generateToon,
            clickSound = loader.loadSfx(gui_click_sound),
            rolloverSound = loader.loadSfx(gui_rollover_sound),

        )


        label_outer_font = loader.loadFont(
            'phase_3/fonts/MickeyFontMaximum.bam'
        )

        self.rotation_slider = OptionsSlider(
            aspect2d, '', -0.80, self.rotateToon, (0, 360))
        self.rotation_slider.containerFrame.setX(-1.75)
        self.rotation_slider.slider.setX(1.15)
        self.rotation_slider.slider['value'] = 180
        rotateToon()

        self.toonDNALabel = OptionsLabel(
            self.optionsScroll.getCanvas(), 'Toon DNA',  0.8)
        self.head_slider = OptionsSlider(
            self.optionsScroll.getCanvas(), 'Head:', 0.65, self.updateHead)
        self.torso_slider = OptionsSlider(
            self.optionsScroll.getCanvas(), 'Torso:', 0.50, self.updateTorso)
        self.legs_slider = OptionsSlider(
            self.optionsScroll.getCanvas(), 'Legs:', 0.35, self.updateLegs)
        self.eyelash_toggle = OptionsToggle(
            self.optionsScroll.getCanvas(), 'Eyelashes:', 0.20, self.eyelashToggle)
        self.gender_toggle = OptionsToggle(
            self.optionsScroll.getCanvas(), 'Gender:', 0.05, self.changeGender)
        self.smoothanim_toggle = OptionsToggle(
            self.optionsScroll.getCanvas(), 'Smooth Animation:', -0.1, self.smoothanimationToggle)
        self.shoes_toggle = OptionsToggle(
            self.optionsScroll.getCanvas(), 'Shoes:', -0.25, self.shoesToggle)

        self.accessory_label = OptionsLabel(
            self.optionsScroll.getCanvas(), 'Accessories', -2.9)
        self.shoes_switching_slider = OptionsSlider(
            self.optionsScroll.getCanvas(), 'Shoe Type:', -4.1, self.updateShoes)
        self.shoes_texture_menu = OptionsChoosingMenu(self.optionsScroll.getCanvas(
        ), 'Shoes:', 0, -3.9, 22, shoe_texture_dict, self.updateShoeTexture, 0)
        self.boot_short_texture_menu = OptionsChoosingMenu(self.optionsScroll.getCanvas(
        ), 'Short Boot:', 0, -3.7, 22, shoe_texture_dict, self.updateShortBootTexture, 0)
        self.boot_long_texture_menu = OptionsChoosingMenu(self.optionsScroll.getCanvas(
        ), 'Long Boot:', 0, -3.5, 15, boot_long_texture_dict, self.updateLongBootTexture, 0)
        self.glasses_menu = OptionsChoosingMenu(self.optionsScroll.getCanvas(
        ), 'Glasses:', -0.1, -3.3, 22, glasses_dict, self.updateGlasses, 0)
        self.backpack_menu = OptionsChoosingMenu(self.optionsScroll.getCanvas(
        ), 'Backpack:', -0.1, -3.1, 23, backpack_dict, self.updateBackpack, 0)
        self.glove_color_menu = OptionsChoosingMenu(self.optionsScroll.getCanvas(
        ), 'Gloves Color:', 0, -1.4, 10, colorsList, self.updateGloveColor, 0)
        self.leg_color_menu = OptionsChoosingMenu(self.optionsScroll.getCanvas(
        ), 'Leg Color:', 0, -1.2, 10, colorsList, self.updateLegsColor, 0)
        self.arm_color_menu = OptionsChoosingMenu(self.optionsScroll.getCanvas(
        ), 'Arms Color:', 0, -1, 10, colorsList, self.updateArmsColor, 0)
        self.head_color_menu = OptionsChoosingMenu(self.optionsScroll.getCanvas(
        ), 'Head Color:', 0, -0.8, 10, colorsList, self.updateHeadColor, 0)
        self.anim_menu = OptionsChoosingMenu(self.optionsScroll.getCanvas(
        ), 'Animation:', 0, -0.6, 20, anim_dict, self.updateAnim)
        self.species_menu = OptionsChoosingMenu(self.optionsScroll.getCanvas(
        ), 'Species:', 0, -0.4, 10, species_dict, self.updateSpecies)

        self.clothing_label = OptionsLabel(
            self.optionsScroll.getCanvas(), 'Clothing', -1.7)
        self.bottom_coloring_menu = OptionsChoosingMenu(self.optionsScroll.getCanvas(
        ), 'Bottom Color:', 0, -2.7, 10, colorsList, self.updateBottomColor, 0)
        self.skirts_menu = OptionsChoosingMenu(self.optionsScroll.getCanvas(
        ), 'Skirt:', 0, -2.5, 20, skirt_dict, self.updateSkirtTexture, 0)
        self.shorts_menu = OptionsChoosingMenu(self.optionsScroll.getCanvas(
        ), 'Shorts:', 0, -2.3,  20, short_dict, self.updateShortTexture, 0)
        self.shirt_color_menu = OptionsChoosingMenu(self.optionsScroll.getCanvas(
        ), 'Shirt Color:', -0.1, -2.1, 10, colorsList, self.updateShirtColor, 0)
        self.shirt_menu = OptionsChoosingMenu(self.optionsScroll.getCanvas(
        ), 'Shirt:', -0.2, -1.9, 25, shirt_dict, self.updateShirtTexture, 0)

        hatPositioningLabel = OptionsLabel(self.optionsScroll.getCanvas(), "Hat Placement", -4.50)
        backpackPositioningLabel = OptionsLabel(self.optionsScroll.getCanvas(), "Backpack Placement", -4.95)
        glassesPositioningLabel = OptionsLabel(self.optionsScroll.getCanvas(), "Glasses Placement", -5.40)


    def updateHead(self):
        '''Updates the Toon's head based on the value'''
        sliderValue = self.head_slider.slider['value']
        tested_value = int(sliderValue)

        if self.selectedToon.species == 'mi':
            if tested_value == 50:
                self.selectedToon.toonActor.delete()
                self.selectedToon.updateHead(
                    'mi', 'ls', self.selectedToon.eyelashes)
                self.selectedToon.generateActor()
            elif tested_value == 100:
                self.selectedToon.toonActor.delete()
                self.selectedToon.updateHead(
                    'mi', 'ss', self.selectedToon.eyelashes)
                self.selectedToon.generateActor()
        elif self.selectedToon.species == 'd':
            if tested_value < 20 and tested_value > 15:
                self.selectedToon.toonActor.delete()
                self.selectedToon.updateHead(
                    'd', 'ss', self.selectedToon.eyelashes)
                self.selectedToon.generateActor()
            elif tested_value < 40 and tested_value > 35:
                self.selectedToon.toonActor.delete()
                self.selectedToon.updateHead(
                    'd', 'sl', self.selectedToon.eyelashes)
                self.selectedToon.generateActor()
            elif tested_value < 60 and tested_value > 55:
                self.selectedToon.toonActor.delete()
                self.selectedToon.updateHead(
                    'd', 'ls', self.selectedToon.eyelashes)
                self.selectedToon.generateActor()
            elif tested_value < 80 and tested_value > 75:
                self.selectedToon.toonActor.delete()
                self.selectedToon.updateHead(
                    'd', 'll', self.selectedToon.eyelashes)
                self.selectedToon.generateActor()
        else:
            if tested_value < 20 and tested_value > 15:
                self.selectedToon.toonActor.delete()
                self.selectedToon.updateHead(
                    self.selectedToon.species, 'ls', self.selectedToon.eyelashes)
                self.selectedToon.generateActor()
            elif tested_value < 40 and tested_value > 35:
                self.selectedToon.toonActor.delete()
                self.selectedToon.updateHead(
                    self.selectedToon.species, 'll', self.selectedToon.eyelashes)
                self.selectedToon.generateActor()
            elif tested_value < 60 and tested_value > 55:
                self.selectedToon.toonActor.delete()
                self.selectedToon.updateHead(
                    self.selectedToon.species, 'sl', self.selectedToon.eyelashes)
                self.selectedToon.generateActor()
            elif tested_value < 80 and tested_value > 75:
                self.selectedToon.toonActor.delete()
                self.selectedToon.updateHead(
                    self.selectedToon.species, 'ss', self.selectedToon.eyelashes)
                self.selectedToon.generateActor()

        self.selectedToon.toonActor.setH(
            self.rotation_slider.slider['value'])

    def updateHeadColor(self, color_to_change_to):
        self.selectedToon.updateHeadColor(color_to_change_to)

    def updateTorso(self):
        '''Updates the Toon's torso based on the value'''
        sliderValue = self.torso_slider.slider['value']
        tested_value = int(sliderValue)

        if self.selectedToon.gender == 'm':
            if tested_value < 20 and tested_value > 15:
                self.selectedToon.updateTorso('ss')
                self.selectedToon.toonActor.delete()
                self.selectedToon.generateActor()
            elif tested_value < 40 and tested_value > 35:
                self.selectedToon.updateTorso('ms')
                self.selectedToon.toonActor.delete()
                self.selectedToon.generateActor()
            elif tested_value < 60 and tested_value > 55:
                self.selectedToon.updateTorso('ls')
                self.selectedToon.toonActor.delete()
                self.selectedToon.generateActor()
        elif self.selectedToon.gender == 'f':
            if tested_value < 20 and tested_value > 15:
                self.selectedToon.updateTorso('sd')
                self.selectedToon.toonActor.delete()
                self.selectedToon.generateActor()
            elif tested_value < 40 and tested_value > 35:
                self.selectedToon.updateTorso('md')
                self.selectedToon.toonActor.delete()
                self.selectedToon.generateActor()
            elif tested_value < 60 and tested_value > 55:
                self.selectedToon.updateTorso('ld')
                self.selectedToon.toonActor.delete()
                self.selectedToon.generateActor()

        self.selectedToon.toonActor.setH(
            self.rotation_slider.slider['value'])

    def updateArmsColor(self, color_to_change_to):
        self.selectedToon.updateArmsColor(color_to_change_to)

    def updateLegs(self):
        '''Updates the Toon's legs based on the value'''
        sliderValue = self.legs_slider.slider['value']
        tested_value = int(sliderValue)

        if tested_value < 20 and tested_value > 15:
            self.selectedToon.updateLegs('s')
            self.selectedToon.toonActor.delete()
            self.selectedToon.generateActor()
        elif tested_value < 40 and tested_value > 35:
            self.selectedToon.updateLegs('m')
            self.selectedToon.toonActor.delete()
            self.selectedToon.generateActor()
        elif tested_value < 60 and tested_value > 55:
            self.selectedToon.updateLegs('l')
            self.selectedToon.toonActor.delete()
            self.selectedToon.generateActor()

        self.selectedToon.toonActor.setH(
            self.rotation_slider.slider['value'])

    def updateLegsColor(self, color_to_change_to):
        self.selectedToon.updateLegsColor(color_to_change_to)

    def updateGloveColor(self, color_to_change_to):
        self.selectedToon.updateGloveColor(color_to_change_to)

    def rotateToon(self):
        '''Updates the Toon's rotation based on the value'''
        sliderValue = self.rotation_slider.slider['value']
        tested_value = int(sliderValue)

        self.selectedToon.toonActor.setH(tested_value)

    def changeGender(self):
        '''Changes the toon's gender based on the current gender'''
        if self.selectedToon.gender == 'm':
            self.selectedToon.gender = 'f'
            self.selectedToon.toonActor.delete()
            self.selectedToon.updateTorso(
                self.selectedToon.torso_type[0] + 'd')
            self.selectedToon.generateActor()
        elif self.selectedToon.gender == 'f':
            self.selectedToon.gender = 'm'
            self.selectedToon.toonActor.delete()
            self.selectedToon.updateTorso(
                self.selectedToon.torso_type[0] + 's')
            self.selectedToon.generateActor()

        self.selectedToon.toonActor.setH(
            self.rotation_slider.slider['value'])

    def eyelashToggle(self):
        '''Toggles the eyelashes on the Toon's head'''
        if self.selectedToon.eyelashes:
            self.selectedToon.toonActor.delete()
            self.selectedToon.eyelashes = False
            self.selectedToon.updateHead(
                self.selectedToon.species, self.selectedToon.headtype, self.selectedToon.eyelashes)
            self.selectedToon.generateActor()
        elif self.selectedToon.eyelashes == False:
            self.selectedToon.toonActor.delete()
            self.selectedToon.eyelashes = True
            self.selectedToon.updateHead(
                self.selectedToon.species, self.selectedToon.headtype, self.selectedToon.eyelashes)
            self.selectedToon.generateActor()
        self.selectedToon.toonActor.setH(
            self.rotation_slider.slider['value'])

    def smoothanimationToggle(self):
        if self.selectedToon.smooth_enabled:
            self.selectedToon.toonActor.setBlend(frameBlend=False)
            self.selectedToon.smooth_enabled = False
        else:
            self.selectedToon.toonActor.setBlend(frameBlend=True)
            self.selectedToon.smooth_enabled = True

    def shoesToggle(self):
        if self.selectedToon.wearsShoes:
            self.selectedToon.toonActor.find('**/*boots_short').hide()
            self.selectedToon.toonActor.find('**/*boots_long').hide()
            self.selectedToon.toonActor.find('**/*shoes').hide()
            self.selectedToon.toonActor.find('**/*feet').show()
            self.selectedToon.wearsShoes = False
        else:
            self.selectedToon.attachShoes(self.selectedToon.shoe_type)
            self.selectedToon.wearsShoes = True

    def updateSpecies(self, species):
        '''Updates the Toon's species'''
        self.selectedToon.toonActor.delete()
        self.selectedToon.updateSpecies(species)
        self.selectedToon.updateHead(
            self.selectedToon.species, self.selectedToon.headtype, self.selectedToon.eyelashes)
        self.selectedToon.generateActor()
        self.selectedToon.toonActor.setH(
            self.rotation_slider.slider['value'])
        self.notify.debug(f"Species has been changed to {species}")

    def updateAnim(self, anim):
        self.selectedToon.animationType = anim
        self.selectedToon.toonActor.stop()
        self.selectedToon.toonActor.loop(anim)
        self.notify.debug(f"Animation has been changed to {anim}")

    def updateBackpack(self, backpack_type):
        self.selectedToon.backpack_type = backpack_type
        self.selectedToon.attachBackpack(backpack_type)

        self.backpackXEntry.set( str( round( self.selectedToon.returnBackpackPosition().getX(), 2 ) ) )
        self.backpackYEntry.set( str( round( self.selectedToon.returnBackpackPosition().getY(), 2 ) ) )
        self.backpackZEntry.set( str( round( self.selectedToon.returnBackpackPosition().getZ(), 2 ) ) )
        self.backpackScaleEntry.set( str( ( round(self.selectedToon.backpack_model.getScale().getX(), 2), round(self.selectedToon.backpack_model.getScale().getY(), 2), round(self.selectedToon.backpack_model.getScale().getZ(), 2)  ) )    )

        self.notify.debug(f"Backpack has been changed to {backpack_type}")

    def updateGlasses(self, glasses_type):
        self.selectedToon.glasses_type = glasses_type
        self.selectedToon.attachGlasses(glasses_type)

        self.glassesXEntry.set( str( round( self.selectedToon.returnGlassesPosition().getX(), 2 ) ) )
        self.glassesYEntry.set( str( round( self.selectedToon.returnGlassesPosition().getY(), 2 ) ) )
        self.glassesZEntry.set( str( round( self.selectedToon.returnGlassesPosition().getZ(), 2 ) ) )
        self.glassesScaleEntry.set( str( ( round(self.selectedToon.glasses_model.getScale().getX(), 2), round(self.selectedToon.backpack_model.getScale().getY(), 2), round(self.selectedToon.backpack_model.getScale().getZ(), 2)  ) )    )

        self.notify.debug(f"Glasses has been changed to {glasses_type}")

    def updateShirtTexture(self, shirt_texture):
        self.selectedToon.shirt_texture = shirt_texture
        self.selectedToon.setShirtTexture(shirt_texture)
        self.notify.debug(f"Shirt Texture has been changed to {shirt_texture}")

    def updateShortTexture(self, short_texture):
        self.selectedToon.short_texture = short_texture
        self.selectedToon.setShortTexture(short_texture)
        self.notify.debug(f"Short Texture has been changed to {short_texture}")

    def updateSkirtTexture(self, skirt_texture):
        self.selectedToon.skirt_texture = skirt_texture
        self.selectedToon.setSkirtTexture(skirt_texture)
        self.notify.debug(f"Skirt Texture has been changed to {skirt_texture}")

    def updateShirtColor(self, shirt_color):
        self.selectedToon.shirt_color = shirt_color
        self.selectedToon.setShirtColor(shirt_color)
        self.notify.debug(f"Shirt color has been changed to {shirt_color}")

    def updateBottomColor(self, bottom_color):
        self.selectedToon.bottom_color = bottom_color
        self.selectedToon.setBottomColor(bottom_color)
        self.notify.debug(f"Bottom color has been changed to {bottom_color}")

    def updateShoeTexture(self, shoe_texture):
        try:
            self.selectedToon.shoe_texture = shoe_texture
            self.selectedToon.applyShoeTexture(shoe_texture)
            self.notify.debug(f"Shoe has been changed to {shoe_texture}")
        except:
            pass

    def updateShortBootTexture(self, shoe_texture):
        try:
            self.selectedToon.short_boot_texture = shoe_texture
            self.selectedToon.applyShortBootTexture(shoe_texture)
            self.notify.debug(f"Short Boots has been changed to {shoe_texture}")
        except:
            pass

    def updateLongBootTexture(self, shoe_texture):
        try:
            self.selectedToon.long_boot_texture = shoe_texture
            self.selectedToon.applyLongBootTexture(shoe_texture)
            self.notify.debug(f"Long Boots has been changed to {shoe_texture}")
        except:
            pass

    def updateShoes(self):
        """Updates the Toon's shoe type based on the thumb's position"""
        sliderValue = self.shoes_switching_slider.slider['value']
        tested_value = int(sliderValue)

        if tested_value >= 0 and tested_value <= 25:
            self.selectedToon.shoe_type = 1
            self.selectedToon.attachShoes(self.selectedToon.shoe_type)
        elif tested_value > 25 and tested_value <= 50:
            self.selectedToon.shoe_type = 2
            self.selectedToon.attachShoes(self.selectedToon.shoe_type)
        elif tested_value > 50 and tested_value <= 75:
            self.selectedToon.shoe_type = 3
            self.selectedToon.attachShoes(self.selectedToon.shoe_type)
        else:
            self.selectedToon.shoe_type = 4
            self.selectedToon.hideShoePieces()

    def generateToon(self):
        '''Just prints out the Toon's toString'''
        self.notify.info(self.selectedToon)