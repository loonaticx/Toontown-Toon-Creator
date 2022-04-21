from direct.gui.DirectGuiGlobals import FLAT, HORIZONTAL, SUNKEN, VERTICAL, RAISED, GROOVE
from direct.gui import DirectGui
from direct.gui.DirectGui import *
from direct.showbase.DirectObject import DirectObject
from panda3d.core import *
from direct.interval.LerpInterval import *
from toon.Toon import Toon
from toon.ToonDNA import *
from direct.directnotify import DirectNotifyGlobal

options_geom = 'phase_3/models/gui/ttr_m_gui_gen_buttons.bam'
gui_click_sound = 'phase_3/audio/sfx/GUI_create_toon_fwd.ogg'
gui_rollover_sound = 'phase_3/audio/sfx/GUI_rollover.ogg'
toon_font = 'phase_3/fonts/ImpressBT.ttf'

class OptionsMenu(DirectObject):
    '''The main OptionsMenu
       Houses the DirectFrame that is the entire frame.'''

    notify = DirectNotifyGlobal.directNotify.newCategory('OptionsMenu')

    def __init__(self, toon=None):
        def funnyFunction():
            self.notify.warning(
                "You clicked on a button that has no function yet..or does it? Only time will tell......just kidding, "
                "I'm tired.\nIf you found this, I'd like a cookie, preferably chocolate chip.")

        self.showOptions = True
        self.main_geom = loader.loadModel(
            'phase_3/models/gui/ttr_m_gui_sbk_settingsPanel.bam')
        self.options_geom = loader.loadModel(options_geom)
        self.icon = loader.loadModel('phase_3/models/gui/toontown-logo.bam')
        self.toontaskicons = loader.loadModel(
            'phase_3.5/models/gui/ttr_m_gui_qst_toontask_icons.bam')

        self.selectedToon = toon

        self.accept('space', self.hideOrShowOptions)
        # Removing nodes that aren't needed

        stuffToDelete1 = self.main_geom.find('**/*tabInactive')
        stuffToDelete1.removeNode()
        stuffToDelete2 = self.main_geom.find('**/*tabActive3')
        stuffToDelete2.removeNode()
        stuffToDelete3 = self.main_geom.find('**/*tabActive4')
        stuffToDelete3.removeNode()

        # Geom to get DirectFrames for.

        self.outer_page_geom = self.main_geom.find('**/*panelMain')
        self.first_page_geom = self.main_geom.find('**/*tabActive1')
        self.second_page_geom = self.main_geom.find('**/*tabActive2')

        self.slider_geom = self.options_geom.find('**/*slider1')
        self.trough_geom = self.options_geom.find('**/*lineThick')

        # There'll be nothing here, it's just the outer frame

        self.outer_page = DirectGui.DirectFrame(
            frameSize=(0, 0, 0, 0),
            geom=self.outer_page_geom,
            geom_scale=0.15,
            parent=aspect2d,
            sortOrder=3,
            pos=(0.8, 0, 0)
        )

        # First page, this'll be where the Toon controller is

        # First Tab related stuff

        self.firstTabGeom = self.icon.find('**/*eyes')

        self.first_Tab = DirectGui.DirectButton(
            geom=self.firstTabGeom,
            geom_scale=0.045,
            geom_pos=(-0.6, 0, 0.680),
            parent=self.first_page,
            command=funnyFunction,
            frameColor=(0, 0, 0, 0))

        self.optionsScroll = DirectGui.DirectScrolledFrame(
            parent=self.first_page,
            # GUI of the box
            frameSize=(-0.8, 0.85, -0.55, 0.35),
            canvasSize=(-1, 0, -7, 1),
            frameColor=(0, 0, 0, 0),

            # GUI DirectScrollBar attributes
            # Getting rid of the horizontal scroll
            horizontalScroll_frameSize=(0, 0, 0, 0),

            # The button you click and hold.
            verticalScroll_thumb_geom=self.slider_geom,
            verticalScroll_thumb_relief=None,
            verticalScroll_thumb_geom_scale=(0.1),
            verticalScroll_thumb_clickSound=loader.loadSfx(gui_click_sound),
            verticalScroll_thumb_rolloverSound=loader.loadSfx(
                gui_rollover_sound),

            # The (invisible) bar you slide across.
            verticalScroll_relief=None,
            verticalScroll_range=(0, 1),
            verticalScroll_incButton_relief=None,
            verticalScroll_decButton_relief=None,
            verticalScroll_geom=self.trough_geom,
            verticalScroll_geom_pos=(0.80, 0, -0.10),
            verticalScroll_geom_hpr=(0, 0, 90),
            verticalScroll_geom_scale=(0.2, 0.1, 0.1),
            scrollBarWidth=0.1,
        )

        self.first_page = DirectGui.DirectFrame(
            parent=self.outer_page,
            geom=self.first_page_geom,
            geom_scale=0.15,
            geom_pos=(0, 0, 0.1),
            frameColor=(0, 0, 0, 0)
        )


        self.label_inner_text = OnscreenText(
            text = 'Toon Creator',
            parent = self.first_page,
            font = OptionsLabel.label_outer_font,
            fg = (0.28, 0.75111111111,
                  1.08888888889, 1),
            scale = 0.175,
            pos = (0, 0.4)
        )


        generateButtonGeom = loader.loadModel(options_geom).find('**/*ttr_t_gui_gen_buttons_squareButton')



        textEntryGui = loader.loadModel(options_geom).find('**/*ttr_t_gui_gen_buttons_box')

# Hat Frames

        self.hatXFrame = DirectFrame(
            parent = self.optionsScroll.getCanvas(),
            geom = textEntryGui,
            relief=None,
            scale=(0.15,0.15,0.15),
            text='x position',
            text_font = loader.loadFont(toon_font),
            text_scale=0.5,
            text_pos=(0,0.5,0),
            pos = (-0.775, 0, -4.70)
        )

        self.hatXEntry = DirectEntry(
            parent=self.hatXFrame,
            text_scale=0.35,
            text_font = loader.loadFont(toon_font),
            frameSize=(-0.2,1.25,-0.55,0.5),
            relief=None,
            pos=(-0.5,0,-0.08)
        )

        self.hatYFrame = DirectFrame(
            parent = self.optionsScroll.getCanvas(),
            geom = textEntryGui,
            relief=None,
            scale=(0.15,0.15,0.15),
            text='y position',
            text_font = loader.loadFont(toon_font),
            text_scale=0.5,
            text_pos=(0,0.5,0),
            pos = (-0.45, 0, -4.70)
        )

        self.hatYEntry = DirectEntry(
            parent=self.hatYFrame,
            text_scale=0.35,
            text_font = loader.loadFont(toon_font),
            frameSize=(-0.2,1.25,-0.55,0.5),
            relief=None,
            pos=(-0.5,0,-0.08)
        )

        self.hatZFrame = DirectFrame(
            parent = self.optionsScroll.getCanvas(),
            geom = textEntryGui,
            relief=None,
            scale=(0.15,0.15,0.15),
            text='z position',
            text_font = loader.loadFont(toon_font),
            text_scale=0.5,
            text_pos=(0,0.5,0),
            pos = (-0.125, 0, -4.70)
        )

        self.hatZEntry = DirectEntry(
            parent=self.hatZFrame,
            text_scale=0.35,
            text_font = loader.loadFont(toon_font),
            frameSize=(-0.2,1.25,-0.55,0.5),
            relief=None,
            pos=(-0.5,0,-0.08)
        )

        self.hatScaleFrame = DirectFrame(
            parent = self.optionsScroll.getCanvas(),
            geom = textEntryGui,
            relief=None,
            scale=(0.15,0.15,0.15),
            text='scale',
            text_font = loader.loadFont(toon_font),
            text_scale=0.5,
            text_pos=(0,0.5,0),
            pos = (0.150, 0, -4.70)
        )

        self.hatScaleEntry = DirectEntry(
            parent=self.hatScaleFrame,
            text_scale=0.35,
            text_font = loader.loadFont(toon_font),
            frameSize=(-0.2,1.25,-0.55,0.5),
            relief=None,
            pos=(-0.5,0,-0.08)
        )


# Backpack frames

        self.backpackXFrame = DirectFrame(
            parent = self.optionsScroll.getCanvas(),
            geom = textEntryGui,
            relief=None,
            scale=(0.15,0.15,0.15),
            text='x position',
            text_font = loader.loadFont(toon_font),
            text_scale=0.5,
            text_pos=(0,0.5,0),
            pos = (-0.775, 0, -5.15)
        )

        self.backpackXEntry = DirectEntry(
            parent=self.backpackXFrame,
            text_scale=0.35,
            text_font = loader.loadFont(toon_font),
            frameSize=(-0.2,1.25,-0.55,0.2),
            relief=None,
            pos=(-0.5,0,-0.08)
        )

        self.backpackYFrame = DirectFrame(
            parent = self.optionsScroll.getCanvas(),
            geom = textEntryGui,
            relief=None,
            scale=(0.15,0.15,0.15),
            text='y position',
            text_font = loader.loadFont(toon_font),
            text_scale=0.5,
            text_pos=(0,0.5,0),
            pos = (-0.45, 0, -5.15)
        )

        self.backpackYEntry = DirectEntry(
            parent=self.backpackYFrame,
            text_scale=0.35,
            text_font = loader.loadFont(toon_font),
            frameSize=(-0.2,1.25,-0.55,0.2),
            relief=None,
            pos=(-0.5,0,-0.08)
        )

        self.backpackZFrame = DirectFrame(
            parent = self.optionsScroll.getCanvas(),
            geom = textEntryGui,
            relief=None,
            scale=(0.15,0.15,0.15),
            text='z position',
            text_font = loader.loadFont(toon_font),
            text_scale=0.5,
            text_pos=(0,0.5,0),
            pos = (-0.125, 0, -5.15)
        )

        self.backpackZEntry = DirectEntry(
            parent=self.backpackZFrame,
            text_scale=0.35,
            text_font = loader.loadFont(toon_font),
            frameSize=(-0.2,1.25,-0.55,0.2),
            relief=None,
            pos=(-0.5,0,-0.08)
        )

        self.backpackScaleFrame = DirectFrame(
            parent = self.optionsScroll.getCanvas(),
            geom = textEntryGui,
            relief=None,
            scale=(0.15,0.15,0.15),
            text='scale',
            text_font = loader.loadFont(toon_font),
            text_scale=0.5,
            text_pos=(0,0.5,0),
            pos = (0.150, 0, -5.15)
        )

        self.backpackScaleEntry = DirectEntry(
            parent=self.backpackScaleFrame,
            text_scale=0.35,
            text_font = loader.loadFont(toon_font),
            frameSize=(-0.2,1.25,-0.55,0.2),
            relief=None,
            pos=(-0.5,0,-0.08)
        )

# Glasses frames

        self.glassesXFrame = DirectFrame(
            parent = self.optionsScroll.getCanvas(),
            geom = textEntryGui,
            relief=None,
            scale=(0.15,0.15,0.15),
            text='x position',
            text_font = loader.loadFont(toon_font),
            text_scale=0.5,
            text_pos=(0,0.5,0),
            pos = (-0.775, 0, -5.60)
        )

        self.glassesXEntry = DirectEntry(
            parent=self.glassesXFrame,
            text_scale=0.35,
            text_font = loader.loadFont(toon_font),
            frameSize=(-0.2,1.25,-0.55,0.2),
            relief=None,
            pos=(-0.5,0,-0.08)
        )

        self.glassesYFrame = DirectFrame(
            parent = self.optionsScroll.getCanvas(),
            geom = textEntryGui,
            relief=None,
            scale=(0.15,0.15,0.15),
            text='y position',
            text_font = loader.loadFont(toon_font),
            text_scale=0.5,
            text_pos=(0,0.5,0),
            pos = (-0.45, 0, -5.60)
        )

        self.glassesYEntry = DirectEntry(
            parent=self.glassesYFrame,
            text_scale=0.35,
            text_font = loader.loadFont(toon_font),
            frameSize=(-0.2,1.25,-0.55,0.2),
            relief=None,
            pos=(-0.5,0,-0.08)
        )

        self.glassesZFrame = DirectFrame(
            parent = self.optionsScroll.getCanvas(),
            geom = textEntryGui,
            relief=None,
            scale=(0.15,0.15,0.15),
            text='z position',
            text_font = loader.loadFont(toon_font),
            text_scale=0.5,
            text_pos=(0,0.5,0),
            pos = (-0.125, 0, -5.60)
        )

        self.glassesZEntry = DirectEntry(
            parent=self.glassesZFrame,
            text_scale=0.35,
            text_font = loader.loadFont(toon_font),
            frameSize=(-0.2,1.25,-0.55,0.2),
            relief=None,
            pos=(-0.5,0,-0.08)
        )

        self.glassesScaleFrame = DirectFrame(
            parent = self.optionsScroll.getCanvas(),
            geom = textEntryGui,
            relief=None,
            scale=(0.15,0.15,0.15),
            text='scale',
            text_font = loader.loadFont(toon_font),
            text_scale=0.5,
            text_pos=(0,0.5,0),
            pos = (0.150, 0, -5.60)
        )

        self.glassesScaleEntry = DirectEntry(
            parent=self.glassesScaleFrame,
            text_scale=0.35,
            text_font = loader.loadFont(toon_font),
            frameSize=(-0.2,1.25,-0.55,0.2),
            relief=None,
            pos=(-0.5,0,-0.08)
        )


    def hideOrShowOptions(self):
        if self.showOptions:
            self.showOptions = False
            self.outer_page.hide()
            self.rotation_slider.slider.hide()
        else:
            self.showOptions = True
            self.outer_page.show()
            self.rotation_slider.slider.show()


class OptionsLabel:
    '''Used as labels for the bigger letters
    Lower Z means lower on the DirectScrolledFrame'''
    notify = DirectNotifyGlobal.directNotify.newCategory('OptionsLabel')

    def __init__(self, labelParent, labelText, z):
        label_outer_font = loader.loadFont('phase_3/fonts/MinnieFont.ttf')

        self.label = DirectGui.DirectLabel(
            parent=labelParent,
            pos=(-1, 0, z),
            frameColor=(0, 0, 0, 0),
            frameSize=(0, 0.9, 0, 0.1)
        )

        self.labelText = OnscreenText(
            text=labelText,
            font=label_outer_font,
            fg=(0, 0, 0, 1),
            scale=0.1,
            align=TextNode.ALeft
        )
        self.labelText.reparentTo(self.label)


class OptionsModal(DirectGui.DirectFrame):
    '''This is the left part of any Options Modal, everything else past this class inherits from this and adds to it'''
    notify = DirectNotifyGlobal.directNotify.newCategory('OptionsModal')


    def __init__(self, modalParent, modalText, z):
        modal_font = loader.loadFont('phase_3/fonts/ImpressBT.ttf')

        self.containerFrame = DirectGui.DirectLabel(
            parent=modalParent,
            pos=(-0.95, 0, z),
            frameColor=(0, 0, 0, 0),
            frameSize=(-0.01, 0.9, -0.01, 0.06),
            scale=0.9,
        )

        self.modalTextNode = OnscreenText(
            align=TextNode.ALeft,
            text=modalText,
            font=modal_font
        )
        self.modalTextNode.reparentTo(self.containerFrame)


class OptionsSlider(OptionsModal):
    '''Creates a Slider which is useful for functions with arguments that include a range'''
    notify = DirectNotifyGlobal.directNotify.newCategory('OptionsSlider')


    def __init__(self, modalParent, modalText, z, slider_command=None, given_range=(0, 100)):
        super().__init__(modalParent, modalText, z)  # Creates the text on the left
        self.options_geom = loader.loadModel(
            'phase_3/models/gui/ttr_m_gui_gen_buttons.bam')
        self.slider_thumb_geom = self.options_geom.find('**/*slider2')
        self.slider_scroll_geom = self.options_geom.find('**/*lineSkinny')

        self.slider = DirectGui.DirectSlider(
            thumb_geom=self.slider_thumb_geom,
            thumb_geom_scale=(0.4, 0.1, 0.25),
            thumb_relief=None,
            thumb_clickSound=loader.loadSfx(gui_click_sound),
            thumb_rolloverSound=loader.loadSfx(gui_rollover_sound),
            geom=self.slider_scroll_geom,
            geom_scale=0.5,
            scale=(0.3, 0.1, 0.4),
            relief=None,
            command=slider_command,
            range=given_range
        )
        self.slider.reparentTo(self.containerFrame)
        self.slider.setPos(1.3, 0, 0)


class OptionsToggle(OptionsModal):
    '''Creates a toggle that creates an off/on switch'''
    notify = DirectNotifyGlobal.directNotify.newCategory('OptionsToggle')


    def __init__(self, modalParent, modalText, z, toggle_command=None):
        super().__init__(modalParent, modalText, z)  # Creates the text on the left
        self.options_geom = loader.loadModel(
            'phase_3/models/gui/ttr_m_gui_gen_buttons.bam')
        self.toggle_thumb_geom = self.options_geom.find('**/*toggleButton')
        self.warm_geom = self.options_geom.find('**/*toggleWarm')
        self.cold_geom = self.options_geom.find('**/*toggleCool')

        def executeFunction(self, toggle_command=None):
            if toggle_command:
                toggle_command()

            animateToggle()

        self.button = DirectGui.DirectCheckButton(
            scale=0.15,
            relief=None,
            boxImageScale=1,
            boxPlacement=('right'),
            boxImage=(self.warm_geom, self.cold_geom),
            boxRelief=None,
            pressEffect=1,
            clickSound=loader.loadSfx(gui_click_sound),
            rolloverSound=loader.loadSfx(gui_rollover_sound),
            command=executeFunction,
            extraArgs=[toggle_command]
        )

        self.button.reparentTo(self.containerFrame)
        self.button.setPos(1.25, 0, 0.025)

        # The button on the thing.
        self.toggle_thumb_geom.setScale(1)
        self.toggle_thumb_geom.setPos(0.6, 0, -0.15)
        self.toggle_thumb_geom.reparentTo(self.button)

        def animateToggle():
            if self.button['indicatorValue']:
                toggle_forward_interval = LerpPosInterval(
                    self.toggle_thumb_geom, 0.15, (1.2, 0, -0.15), (0.6, 0, -0.15))
                toggle_forward_interval.start()
            else:
                toggle_back_interval = LerpPosInterval(
                    self.toggle_thumb_geom, 0.15, (0.6, 0, -0.15), (1.2, 0, -0.15))
                toggle_back_interval.start()


class OptionsChoosingMenu(OptionsModal):
    '''modalParent - sets parent as the parent of the menu
       modalText(string) - what text does the model show?
       x(float) - What position in the x-position (left or right) do you want the menu?
       z(float) - What position in the z direction (up or down) do you want the menu?
       height_of_selectables(float) - How much space do you want in the selection menu? Lower numbers means a bigger height
       width_of_clickable(float) - How big do you want the button you click to open a selectable menu
       used_dictionary - What dictionary should this menu read from?
       chosen_command - What function does this menu run once an object in the selection menu is chosen?
       keyOrValue - 0 returns the key, 1 returns the value in the used_dictionary 
    '''

    notify = DirectNotifyGlobal.directNotify.newCategory('OptionsChoosingMenu')

    def __init__(self, modalParent, modalText, x, z, width_of_clickable, used_dictionary=None, chosen_command=None, keyOrValue=1):
        super().__init__(modalParent, modalText, z)
        self.options_geom = loader.loadModel(
            options_geom)
        self.clickable = self.generateClickableFrame(
            x, width_of_clickable, chosen_command, keyOrValue, used_dictionary)
        self.selectables = self.generateSelectablesFrame(
            x, used_dictionary, width_of_clickable)
        self.populateBoolean = False
        self.selectable_gui_font = loader.loadFont(toon_font)

    def generateClickableFrame(self,
                               x,
                               width_of_clickable,
                               function_to_execute,
                               keyOrValueNum,
                               selectables_dictionary
                               ):
        '''Creates the small frame that the player will click on'''
        dynamicFrameFile = loader.loadModel(
            'phase_3/models/gui/ttr_m_gui_gen_dynamicFrame.bam')
        top_left_model = dynamicFrameFile.find('**/*topLeft')
        top_middle_model = dynamicFrameFile.find('**/*topMiddle')
        top_right_model = dynamicFrameFile.find('**/topRight')
        center_left_model = dynamicFrameFile.find('**/*centerLeft')
        center_middle_model = dynamicFrameFile.find('**/*centerMiddle')
        center_right_model = dynamicFrameFile.find('**/*centerRight')
        bottom_left_model = dynamicFrameFile.find('**/*bottomLeft')
        bottom_middle_model = dynamicFrameFile.find('**/*bottomMiddle')
        bottom_right_model = dynamicFrameFile.find('**/*bottomRight')

        self.clickable_node = NodePath('clickable_frame_node')

        # The Top Left piece
        top_left_model.setScale(0.05)
        top_left_model.reparentTo(self.clickable_node)
        top_left_model.setPos(0, 0, 0.5)

        # The top middle piece
        top_middle_model.reparentTo(self.clickable_node)
        top_middle_model.setScale(0.05)
        top_middle_model.setPos(top_left_model.getX() +
                                0.05, 0, top_left_model.getZ())

        # The Top Middle repetitions
        for i in range(1, width_of_clickable):
            self.top_center_copy = top_middle_model.copyTo(self.clickable_node)
            self.top_center_copy.setPos(
                top_middle_model.getX()+(i*0.05), 0, top_middle_model.getZ())

        # The Top Right piece
        top_right_model.reparentTo(self.clickable_node)
        top_right_model.setScale(0.05)
        top_right_model.setPos(self.top_center_copy.getX()+0.05, 0, 0.5)

        # The Middle Left piece

        center_left_model.reparentTo(self.clickable_node)
        center_left_model.setScale(0.05)
        center_left_model.setPos(
            top_left_model.getX(), 0, top_left_model.getZ()-0.05)

        center_middle_model.reparentTo(self.clickable_node)
        center_middle_model.setScale(0.05)
        center_middle_model.setPos(
            center_left_model.getX()+0.05, 0, center_left_model.getZ())

        # The Center Middle repetitions
        for i in range(1, width_of_clickable):
            self.center_middle_copy = center_middle_model.copyTo(
                self.clickable_node)
            self.center_middle_copy.setPos(
                center_middle_model.getX()+(i*0.05), 0, center_middle_model.getZ())

        # The Center Right piece
        center_right_model.setScale(0.05)
        center_right_model.reparentTo(self.clickable_node)
        center_right_model.setPos(
            self.center_middle_copy.getX()+0.05, 0, center_middle_model.getZ())

        bottom_left_model.setScale(0.05)
        bottom_left_model.reparentTo(self.clickable_node)
        bottom_left_model.setPos(
            center_left_model.getX(), 0, center_left_model.getZ()-0.05)

        bottom_middle_model.setScale(0.05)
        bottom_middle_model.reparentTo(self.clickable_node)
        bottom_middle_model.setPos(
            bottom_left_model.getX()+0.05, 0, center_left_model.getZ()-0.05)

        # The Bottom Middle repetitions
        for i in range(1, width_of_clickable):
            self.bottom_middle_copy = bottom_middle_model.copyTo(
                self.clickable_node)
            self.bottom_middle_copy.setPos(
                bottom_middle_model.getX()+(i*0.05), 0, bottom_middle_model.getZ())

        bottom_right_model.setScale(0.05)
        bottom_right_model.reparentTo(self.clickable_node)
        bottom_right_model.setPos(
            self.bottom_middle_copy.getX()+0.05, 0, bottom_middle_model.getZ())

        self.clickable_node.setPos(0.5, 0, -0.45)
        self.clickable_node.flattenStrong()

        # The actual button
        self.clickable_button = DirectFrame(
            geom=self.clickable_node,
            parent=self.containerFrame,
            pos=(x, 0, 0),
            relief=None
        )

        self.clickable_text = DirectButton(
            parent=self.clickable_button,
            text='None',
            text_scale=0.075,
            text_font=loader.loadFont(toon_font),
            text_align=TextNode.ALeft,
            pos=(0.5, 0, -0.025),
            relief=None,
            frameSize=(0, width_of_clickable*0.055, -0.05, 0.1),
            command=self.showSelectables,
            extraArgs=[function_to_execute,
                       keyOrValueNum, selectables_dictionary],
            clickSound=loader.loadSfx(gui_click_sound),
            rolloverSound=loader.loadSfx(gui_rollover_sound),
        )

        return self.clickable_button

    def showAndHide(self, function, args_to_insert):
        '''This basically reparents clickable so you can see it again and hides the selectables_frame'''
        self.clickable.show()
        self.clickable_text['text'] = args_to_insert
        self.selectablesFrame.hide()
        function(args_to_insert)

    def generateSelectablesFrame(self,
                                 x_position,
                                 selectables_dictionary=None,
                                 width=6,
                                 height=6):
        '''Creates the selectable menu based on the provided args'''
        dynamicFrameFile = loader.loadModel(
            'phase_3/models/gui/ttr_m_gui_gen_dynamicFrame.bam')
        top_left_model = dynamicFrameFile.find('**/*topLeft')
        top_middle_model = dynamicFrameFile.find('**/*topMiddle')
        top_right_model = dynamicFrameFile.find('**/topRight')
        center_left_model = dynamicFrameFile.find('**/*centerLeft')
        center_middle_model = dynamicFrameFile.find('**/*centerMiddle')
        center_right_model = dynamicFrameFile.find('**/*centerRight')
        bottom_left_model = dynamicFrameFile.find('**/*bottomLeft')
        bottom_middle_model = dynamicFrameFile.find('**/*bottomMiddle')
        bottom_right_model = dynamicFrameFile.find('**/*bottomRight')

        self.selectable_dynamic_frame = NodePath('selectable_frame')

        top_piece = NodePath('top_half')

        # The Top Left piece
        top_left_model.setScale(0.05)
        top_left_model.reparentTo(top_piece)
        top_left_model.setPos(0, 0, 0)

        # The top middle piece
        top_middle_model.setScale(0.05)
        top_middle_model.reparentTo(top_piece)
        top_middle_model.setPos(top_left_model.getX() +
                                0.05, 0, top_left_model.getZ())

        # The Top Middle repetitions
        for i in range(1, width):
            self.top_center_copy = top_middle_model.copyTo(top_piece)
            self.top_center_copy.setPos(top_middle_model.getX()+(0.05*i), 0, 0)

        # The Top Right piece
        top_right_model.setScale(0.05)
        top_right_model.reparentTo(top_piece)
        top_right_model.setPos(top_middle_model.getX()+(0.05*width), 0, 0)

        top_piece.flattenStrong()
        top_piece.reparentTo(self.selectable_dynamic_frame)
        top_piece.setPos(0, 0, 0)
        # Let's make a node that we can duplicate.

        middle_piece = NodePath('middle_half')
        middle_piece.reparentTo(self.selectable_dynamic_frame)
        middle_piece.setPos(0, 0, -0.05)

        center_left_model.setScale(0.05)
        center_left_model.reparentTo(middle_piece)
        center_left_model.setPos(0, 0, 0)

        center_middle_model.setScale(0.05)
        center_middle_model.reparentTo(middle_piece)
        center_middle_model.setPos(0.05, 0, 0)

        # The Center Middle repetitions
        for i in range(1, width+1):
            self.center_middle_copy = center_middle_model.copyTo(middle_piece)
            self.center_middle_copy.setPos(0.05*i, 0, 0)

        center_right_model.setScale(0.05)
        center_right_model.reparentTo(middle_piece)
        center_right_model.setPos((width+1)*0.05, 0, 0)

        # Now let's duplicate the amount of times the thing is made.

        middle_piece.flattenStrong()

        for i in range(1, height):
            self.middle_piece_copy = middle_piece.copyTo(
                self.selectable_dynamic_frame)
            self.middle_piece_copy.setPos(0, 0, (i * -0.05))

        bottom_piece = NodePath('bottom_half')
        bottom_piece.reparentTo(self.selectable_dynamic_frame)
        bottom_piece.setPos(0, 0, height * -0.05)

        bottom_left_model.setScale(0.05)
        bottom_left_model.reparentTo(bottom_piece)
        bottom_left_model.setPos(0, 0, -0.05)

        bottom_middle_model.setScale(0.05)
        bottom_middle_model.reparentTo(bottom_piece)
        bottom_middle_model.setPos(0.05, 0, -0.05)

        # The Bottom Middle repetitions
        for i in range(1, width+1):
            self.bottom_middle_copy = bottom_middle_model.copyTo(bottom_piece)
            self.bottom_middle_copy.setPos((0.05*i), 0, -0.05)

        # self.selectable_dynamic_frame.ls()
        bottom_right_model.setScale(0.05)
        bottom_right_model.reparentTo(bottom_piece)
        bottom_right_model.setPos((width+1)*0.05, 0, -0.05)

        bottom_piece.flattenStrong()

        self.slider_geom = self.options_geom.find('**/*slider1')
        self.trough_geom = self.options_geom.find('**/*lineSkinny')

        self.selectablesFrame = DirectGui.DirectFrame(
            geom=self.selectable_dynamic_frame,
            parent=self.containerFrame,
            pos=((x_position+0.5), 0, 0.05),
            relief=None,
        )

        # If you want to debug the amount of items ya got, uncomment the line under.

        #print(f"{self.modalTextNode['text']} : {len(selectables_dictionary)} items")

        selectable_height = (len(selectables_dictionary)) * -0.1005

        self.selectableScrollFrame = DirectGui.DirectScrolledFrame(
            parent=self.selectablesFrame,
            frameSize=(0, width*0.052, -0.4, 0),
            canvasSize=(0, 1.5, selectable_height, 0),

            verticalScroll_incButton_relief=None,
            verticalScroll_decButton_relief=None,
            verticalScroll_range=(0, 0.5),
            verticalScroll_value=0,
            verticalScroll_manageButtons=True,
            verticalScroll_resizeThumb=True,
            verticalScroll_relief=None,
            verticalScroll_thumb_relief=None,
            verticalScroll_thumb_geom=self.slider_geom,
            verticalScroll_thumb_geom_scale=0.05,
            verticalScroll_thumb_geom_pos=(0, 0, 0),

            verticalScroll_geom=self.trough_geom,
            verticalScroll_geom_scale=0.085,
            verticalScroll_geom_pos=(width*0.049, 0, -0.175),
            verticalScroll_geom_hpr=(0, 0, 90),

            horizontalScroll_relief=None,
            horizontalScroll_thumb_relief=None,
            horizontalScroll_incButton_relief=None,
            horizontalScroll_decButton_relief=None,
            scrollBarWidth=0.05,
            relief=None,
        )

        self.selectablesFrame.hide()

    def showSelectables(self,
                        command_to_execute,
                        keyOrValue,
                        selectables_dictionary):
        self.selectablesFrame.show()
        self.clickable.hide()

        if self.populateBoolean:
            pass  # We've already populated it.
        else:
            self.notify.info('Generating Selectable Frame for the first time')
            if keyOrValue == 1:  # If we want to return the values
                i = 0
                for item in selectables_dictionary.keys():
                    i += 1
                    button = DirectButton(
                        parent=self.selectableScrollFrame.getCanvas(),
                        text=item,
                        text_font=self.selectable_gui_font,
                        text_align=TextNode.ALeft,
                        text_scale=0.3,
                        scale=0.2,
                        pos=(0, 0, 0 - (i*0.1)),
                        pad=(5, 0),
                        relief=None,
                        command=self.showAndHide,
                        clickSound=loader.loadSfx(gui_click_sound),
                        rolloverSound=loader.loadSfx(gui_rollover_sound),
                        extraArgs=[command_to_execute,
                                   selectables_dictionary[item]]
                    )
            else:  # If we want to return the key
                i = 0
                for item in selectables_dictionary.keys():
                    i += 1
                    button = DirectButton(
                        parent=self.selectableScrollFrame.getCanvas(),
                        text=item,
                        text_font=self.selectable_gui_font,
                        text_align=TextNode.ALeft,
                        text_scale=0.3,
                        scale=0.2,
                        pos=(0, 0, 0 - (i*0.1)),
                        pad=(5, 0),
                        relief=None,
                        command=self.showAndHide,
                        clickSound=loader.loadSfx(gui_click_sound),
                        rolloverSound=loader.loadSfx(gui_rollover_sound),
                        extraArgs=[command_to_execute, item]
                    )
            self.populateBoolean = True
