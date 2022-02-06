# THIS FILE CONTAINS ALL THE DICTIONARIES USED FOR THE CHOOSING MENUS IN OPTIONSMENU.PY
from panda3d.core import *

colorsList = {
    'Amber'         :VBase4(0.9647058823529412,0.7490196078431373,0.34901960784313724, 1.0),
    'Apricot'       :VBase4(0.9803921568627451,0.5372549019607843,0.396078431372549, 1.0),                  
    'Aqua'          :VBase4(0.347656, 0.820312, 0.953125, 1.0),
    'Beige'         :VBase4(0.8,0.7529411764705882,0.611764705882353, 1.0),   
    'Black'         :VBase4(0.3, 0.3, 0.35, 1.0),
    'Blue'          :VBase4(0.191406, 0.5625, 0.773438, 1.0), 
    'Bright Red'   : VBase4(0.933594, 0.265625, 0.28125, 1.0),
    'Brown'        : VBase4(0.640625, 0.355469, 0.269531, 1.0),
    'Bubblegum'    : VBase4(0.996078431372549,0.35294117647058826,0.44313725490196076, 1.0),
    'Cartoonival Blue': VBase4(0.22745098039, 0.55686274509, 0.96862745098, 1.0),
    'Cartoonival Pink': VBase4(0.93333333333, 0.36470588235,0.81568627451, 1.0 ),  
    'Citrine'       :VBase4(0.855469, 0.933594, 0.492188, 1.0),  
    'Coral'        : VBase4(0.832031, 0.5, 0.296875, 1.0), 
    'Cream'         :VBase4(0.996094, 0.957031, 0.597656, 1.0),
    'Crimson'       :VBase4(0.6549019607843137,0.17647058823529413,0.25882352941176473, 1.0),
    'Emerald'       :VBase4(0.0392156862745098,0.8627450980392157,0.6549019607843137, 1.0),
    'Forest Green'  :VBase4(0.4117647058823529,0.6431372549019608,0.2823529411764706, 1.0),
    'Gray'          :VBase4(0.7, 0.7, 0.8, 1.0),
    'Green'         :VBase4(0.304688, 0.96875, 0.402344, 1.0),
    'Ice Blue'      :VBase4(0.7333333333333333,0.8666666666666667,0.9490196078431372, 1.0), 
    'Lavender'      :VBase4(0.726562, 0.472656, 0.859375, 1.0),
    'Lime Green'    :VBase4(0.550781, 0.824219, 0.324219, 1.0), 
    'Light Blue'    :VBase4(0.433594, 0.90625, 0.835938, 1.0),      
    'Maroon'       : VBase4(0.710938, 0.234375, 0.4375, 1.0),
    'Mint Green'    :VBase4(0.6392156862745098,0.8549019607843137,0.6705882352941176, 1.0),
    'Orange'        :VBase4(0.992188, 0.480469, 0.167969, 1.0),         
    'Peach'        : VBase4(0.96875, 0.691406, 0.699219, 1.0),
    'Periwinkle'    :VBase4(0.558594, 0.589844, 0.875, 1.0),   
    'Pink'          :VBase4(0.898438, 0.617188, 0.90625, 1.0),
    'Purple'        :VBase4(0.546875, 0.28125, 0.75, 1.0),
    'Red'          : VBase4(0.863281, 0.40625, 0.417969, 1.0),
    'Rose Pink'     :VBase4(0.8823529411764706, 0.43529411764705883, 0.6901960784313725, 1.0),                          
    'Royal Blue'    :VBase4(0.285156, 0.328125, 0.726562, 1.0),
    'Sea Green'     :VBase4(0.242188, 0.742188, 0.515625, 1.0),
    'Sienna'       : VBase4(0.570312, 0.449219, 0.164062, 1.0),        
    'Slate Blue'    :VBase4(0.460938, 0.378906, 0.824219, 1.0),
    'Spooky Purple' :VBase4(0.35294117647, 0.23137254902, 0.51372549019, 1.0),
    'Steel Blue'    :VBase4(0.3254901960784314,0.403921568627451,0.6, 1.0), 
    'Tan'          : VBase4(0.996094, 0.695312, 0.511719, 1.0),
    'Teal'          :VBase4(0.19607843137254902,0.7215686274509804,0.7098039215686275, 1.0),
    'White'        : VBase4(1.0, 1.0, 1.0, 1.0),    
    'Yellow'        :VBase4(0.996094, 0.898438, 0.320312, 1.0),              
}

species_dict = {
             'Bear'         :'b',
             'Cat'          :'ca',
             'Crocodile'    :'cr',
             'Deer'         :'de',
             'Dog '         :'d',
             'Duck'         :'du',
             'Horse'        :'h',
             'Monkey'       :'mo',
             'Mouse'        :'mi',
             'Pig'          :'p',
             'Rabbit'       :'r',
             'Riggy'        :'ri'
              }

# How does this work?
# "Animation Name" - "file_of_animation"

anim_dict = {
    'Angry'    : 'angry',
    'Applause' : 'applause',
    'begCycle' : 'begCycle',
    'begOut'   : 'begOut',
    'Book'     : 'book',
    'Bored'    : 'bored',
    'Bow'      : 'bow',
    'Cast'     : 'cast',
    'Cast(Long)': 'castlong',
    'Climb'    : 'climb',
    'Confused' : 'confused',
    'Cringe'   : 'cringe',
    'Curtsy'   : 'curtsy',
    'Down'     : 'down',
    'Duck'     : 'duck',
    'Eat(Neutral)': 'eat_neutral',
    'Eat N\' Run' : 'eatnrun',
    'Firehose' : 'firehose',
    'Fish again': 'fishAGAIN',
    'Fish'     : 'fish',
    'Fish End' : 'fishEND',
    'Fish (neutral)': 'fishneutral',
    'Flashlight' : 'flashlight',
    'Game Neutral': 'gameneutral',
    'Game Run'  : 'gamerun',
    'Game Throw': 'gameThrow',
    'Give'      : 'give',
    'Happy Dance' : 'happy-dance',
    'Hold Bottle' : 'hold-bottle',
    'Hold Magnet' : 'hold-magnet',
    'Hypnotize' : 'hypnotize',
    'into Beg'  : 'intoBeg',
    'into Sit'  : 'intoSit',
    'Juggle'    : 'juggle',
    'Left'      : 'left',
    'Left Point': 'left-point',
    'Lose'      : 'lose',
    'Lose Walk' : 'losewalk',
    'Melt'      : 'melt',
    'Neutral'   : 'neutral',
    'Pie Throw' : 'pie-throw',
    'Pole'      : 'pole',
    'Pole (Neutral)' : 'poleneutral',
    'Press Button' : 'press-button',
    'Remote Attack' : 'remoteAttack',
    'Riggy Neutral': 'riggyNeutral',
    'Riggy Walk': 'riggyWalk',
    'Run'       : 'run',
    'Sad(Neutral)' : 'sad-neutral',
    'Scientist (Emcee)' : 'scientistEmcee',
    'Scientist (Jealous)' : 'scientistJealous',
    'Scientist (Work)' : ' scientistWork',
    'Shrug'         : 'shrug',
    'Sit'           : 'sit',
    'Skate (Boost)' : 'skateBoost',
    'Skate (Brake)' : 'skateBrake',
    'Skate (Run)'  : 'skateRun',
    'Side Step (Left)' : 'sidestep-left', 
    'Spit'      : 'spit',
    'Sprinkle'  : 'sprinkle-dust',
    'Struggle'  : 'struggle',
    'Surprise'  : 'surprise',
    'Swim'      : 'swim',
    'Swing'     : 'swing',
    'Teleport'  : 'teleport',
    'Think'     : 'think',
    'Victory Dance' : 'victory-dance',
    'Walk'      : 'walk',
    'Water Gun' : 'water-gun',
    'Wave'      : 'wave',

}

# Backpack model, (potentially texture if reskin), (potentially what to retexture), small scale, medium scale, large scale, accessory scale
# Yes I manually positioned all of these per torso type for you. You're welcome.

backpack_dict = {
    'A Broken Jetpack': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_jetPack.bam', (0.5,-1.25,0), (0.35,-0.75,0.3), (0.3,-0.9,0.45), 0.32],
    'Angel Wings': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_angelWings.bam', (0.25,-1.25,-0.1), (0.3,-0.75,-0.15), (0.2,-1.25,0.25), 0.3],
    'The Attack Pack': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_gags.bam', (0.4,-1.5,0.1), (0.3,-1,0.1), (0.25,-1,0.25), 0.32],
    'Banana Bowtie': ['phase_4/models/accessories/ttr_m_chr_avt_acc_pac_bowtie.bam', 'phase_4/maps/ttr_t_chr_avt_acc_hat_ribbonTasty_4.jpg', (0.25,-0.5,0.475), (0.25,-0.25,0.45), (0.25,-0.34,0.65), 0.25],
    'Basic Backpack': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_backpack.bam', (0.4,-1.5,0.1), (0.3,-1.1,0.1), (0.3,-1.25,0.2), 0.32],
    'Bat Wings': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_batWings.bam',(0.25,-1.25,-0.1), (0.3,-0.75,-0.15), (0.2,-1.25,0.25), 0.3],
    'Bear Backpack': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_stuffedAnimalBackpackA.bam', (0.3,-1.6,-0.5), (0.3,-1.35,-0.4), (0.3,-1.4,-0.25), 0.25],
    'Bee Wings': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_beeWings.bam', (0.25,-1.25,-0.1), (0.3,-0.75,-0.15), (0.2,-1.25,0.25), 0.3],
    'Bird Wings': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_birdWings.bam', (0.25,-1.25,-0.1), (0.3,-0.75,-0.15), (0.2,-1.25,0.25), 0.3],
    'Blue Backpack': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_stuffedAnimalBackpackDog.bam', (0.35,-1.6, 0.1), (0.35,-1.25,0.1), (0.35,-1,0.1), 0.3],
    'Blue Winter Scarf': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_scarf.bam', 'phase_4/maps/tt_t_chr_avt_acc_pac_scarf.jpg', (0.25,-0.7,0.5), (0.25,-0.45,0.5), (0.25,-0.6,0.75), 1],
    'Butterfly Wings': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_butterflyWings.bam', (0.25,-1.25,-0.1), (0.3,-0.75,-0.15), (0.2,-1.25,0.25), 0.3],
    'Carrot Bowtie': ['phase_4/models/accessories/ttr_m_chr_avt_acc_pac_bowtie.bam', 'phase_4/maps/ttr_t_chr_avt_acc_hat_ribbonPolka_2.jpg', (0.25,-0.5,0.475), (0.25,-0.25,0.45), (0.25,-0.34,0.65), 0.25],
    'Chocolate Bowtie': ['phase_4/models/accessories/ttr_m_chr_avt_acc_pac_bowtie.bam', 'phase_4/maps/ttr_t_chr_avt_acc_hat_ribbonTasty_3.jpg', (0.25,-0.5,0.475), (0.25,-0.25,0.45), (0.25,-0.34,0.65), 0.25],
    'Crazy Bowtie': ['phase_4/models/accessories/ttr_m_chr_avt_acc_pac_bowtie.bam', 'phase_4/maps/ttr_t_chr_avt_acc_hat_ribbonPolka_5.jpg', (0.25,-0.5,0.475), (0.25,-0.25,0.45), (0.25,-0.34,0.65), 0.25], 
    'Dragon Fly Wings': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_dragonFlyWings.bam', (0.25,-1.25,-0.1), (0.3,-0.75,-0.15), (0.2,-1.25,0.25), 0.3],
    'Dragon Wings': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_dragonWing.bam', (0.25,-1.25,-0.1), (0.3,-0.75,-0.15), (0.2,-1.25,0.25), 0.3],
    'Dreamland Bowtie': ['phase_4/models/accessories/ttr_m_chr_avt_acc_pac_bowtie.bam', 'phase_4/maps/ttr_t_chr_avt_acc_hat_ribbonPolka_4.jpg', (0.25,-0.5,0.475), (0.25,-0.25,0.45), (0.25,-0.34,0.65), 0.25],
    'Emergency Cream Pack': ['phase_4/models/accessories/ttr_m_chr_avt_acc_pac_creamPack.bam', (0.25,-1.25,0.1), (0.25,-0.75,0.1), (0.25,-0.85,0.25), 0.32],
    'Emergency Seltzer': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_scubaTank.bam', 'phase_4/maps/ttr_t_chr_avt_acc_pac_seltzerTank.jpg', (0.25,-1.5,0.1), (0.25,-1.1,0.1), (0.25,-1.1,0.25), 0.25],
    'Extraordinaire Bowtie': ['phase_4/models/accessories/ttr_m_chr_avt_acc_pac_bowtie.bam', 'phase_4/maps/ttr_t_chr_avt_acc_hat_ribbonToonfest.jpg', (0.25,-0.5,0.475), (0.25,-0.25,0.45), (0.25,-0.34,0.65), 0.25],
    'Fairy Wings': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_butterflyWings.bam', 'phase_4/maps/tt_t_chr_avt_acc_pac_butterflyWingsStyle1.jpg' , (0.25,-1.5,-0.1), (0.3,-1.25,-0.15), (0.2,-1.25,0.25), 0.3],
    'The Flunk-Trunk': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_flunky.bam', (0.35,-1.5, -0.15), (0.35,-1,-0.05), (0.2,-1,0.1), 0.3],
    'Green Fancy Bowtie': ['phase_4/models/accessories/ttr_m_chr_avt_acc_pac_bowtie.bam', 'phase_4/maps/ttr_t_chr_avt_acc_hat_ribbonFancy_2.jpg', (0.25,-0.5,0.475), (0.25,-0.25,0.45), (0.25,-0.34,0.65), 0.25],
    'Green Fancy Scarf':['phase_4/models/accessories/tt_m_chr_avt_acc_pac_scarf.bam', 'phase_4/maps/tt_t_chr_avt_acc_pac_scarf2.jpg', (0.25,-0.7,0.5), (0.25,-0.45,0.5), (0.25,-0.6,0.75), 1],
    'Holiday Scarf': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_scarf.bam', 'phase_4/maps/tt_t_chr_avt_acc_pac_scarfChristmas.jpg', (0.25,-0.7,0.5), (0.25,-0.45,0.5), (0.25,-0.6,0.75), 1],
    'Infinity and Beyond Backpack': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_airplane.bam', (0.35,-1, 0.1), (0.2,-0.5,0.1), (0.2,-0.6,0.45), 0.2],
    'Jellybean Jar': ['phase_4/models/accessories/ttr_m_chr_avt_acc_pac_jellybeanJar.bam', (0.4,-1.25,-0.15), (0.3,-1,-0.15), (0.25,-1.1,0.025), 0.32],
    'Kitty Kit': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_stuffedAnimalBackpackCat.bam', (0.35,-1.6, 0.1), (0.35,-1.25,0.1), (0.35,-1,0.1), 0.3],
    'Lipstick Jetpack': ['phase_4/models/accessories/ttr_m_chr_avt_acc_pac_lipstickPack.bam', (0.5,-1.25,0), (0.35,-0.75,0.3), (0.3,-0.9,0.45), 0.32],
    'Melodyland Bowtie':  ['phase_4/models/accessories/ttr_m_chr_avt_acc_pac_bowtie.bam', 'phase_4/maps/ttr_t_chr_avt_acc_hat_ribbonPolka_3.jpg', (0.25,-0.5,0.475), (0.25,-0.25,0.45), (0.25,-0.34,0.65), 0.25],
    'Oil Pale Pack': ['phase_4/models/accessories/ttr_m_chr_avt_acc_pac_oilJar.bam', 'phase_4/maps/ttr_t_chr_avt_acc_pac_oilJar.jpg', 'phase_4/maps/ttr_t_chr_avt_acc_pac_oilJar_a.rgb', (0.4,-1.25,-0.15), (0.3,-1,-0.15), (0.25,-1.1,0.025), 0.32],
    'One-Toon Band': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_band.bam', (0.4,-1.5,0.1), (0.3,-1,0.1), (0.25,-1,0.25), 0.32],
    'Orange Knapsack': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_backpack.bam', 'phase_4/maps/tt_t_chr_avt_acc_pac_backpackOrange.jpg', (0.4,-1.5,0.1), (0.3,-1.1,0.1), (0.3,-1.25,0.2), 0.32],
    'Pink Winter Scarf': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_scarf.bam', 'phase_4/maps/tt_t_chr_avt_acc_pac_scarf1.jpg', (0.25,-0.7,0.5), (0.25,-0.45,0.5), (0.25,-0.6,0.75), 1],
    'Pirate Sword': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_woodenSword.bam', (0.35,-1.5, -0.15), (0.35,-1,-0.05), (0.25,-1.1,0.1), 0.3],
    'Polka Bowtie': ['phase_4/models/accessories/ttr_m_chr_avt_acc_pac_bowtie.bam', 'phase_4/maps/ttr_t_chr_avt_acc_hat_ribbonPolka_1.jpg', (0.25,-0.5,0.475), (0.25,-0.25,0.45), (0.25,-0.34,0.65), 0.25],
    'Portable Blanket': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_supertoonCape.bam', 'phase_4/maps/ttr_t_chr_avt_acc_pac_superSleepy.jpg' ,(0.35,-1.1, 0.55), (0.35, -0.75, 0.55), (0.25,-0.8,0.75), 0.3],
    'Purple Fancy Bowtie': ['phase_4/models/accessories/ttr_m_chr_avt_acc_pac_bowtie.bam', 'phase_4/maps/ttr_t_chr_avt_acc_hat_ribbonFancy_3.jpg', (0.25,-0.5,0.475), (0.25,-0.25,0.45), (0.25,-0.34,0.65), 0.25],
    'Purple Pouch': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_backpack.bam', 'phase_4/maps/tt_t_chr_avt_acc_pac_backpackPurple.jpg', (0.4,-1.5,0.1), (0.3,-1.1,0.1), (0.3,-1.25,0.2), 0.32],
    'Rainbow Scarf': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_scarf.bam', 'phase_4/maps/tt_t_chr_avt_acc_pac_scarfRainbow.jpg', (0.25,-0.7,0.5), (0.25,-0.45,0.5), (0.25,-0.6,0.75), 1],
    'Rainbow Wings': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_angelWings.bam', 'phase_4/maps/tt_t_chr_avt_acc_pac_angelWingsMultiColor.jpg', (0.25,-1.5,-0.1), (0.3,-1.25,-0.15), (0.2,-1.25,0.25), 0.3],
    'Red Bowtie': ['phase_4/models/accessories/ttr_m_chr_avt_acc_pac_bowtie.bam', 'phase_4/maps/ttr_t_chr_avt_acc_hat_ribbonPink_1.jpg', (0.25,-0.5,0.475), (0.25,-0.25,0.45), (0.25,-0.34,0.65), 0.25],
    'Red Fancy Bowtie':  ['phase_4/models/accessories/ttr_m_chr_avt_acc_pac_bowtie.bam', 'phase_4/maps/ttr_t_chr_avt_acc_hat_ribbonFancy_1.jpg', (0.25,-0.5,0.475), (0.25,-0.25,0.45), (0.25,-0.34,0.65), 0.25],
    'Red Polka-pack': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_backpack.bam', 'phase_4/maps/tt_t_chr_avt_acc_pac_backpackPolkaDotRed.jpg', (0.4,-1.5,0.1), (0.3,-1.1,0.1), (0.3,-1.25,0.2), 0.32],
    'Resistance Cape': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_supertoonCape.bam', 'phase_4/maps/ttr_t_chr_avt_acc_pac_crashcashCape.jpg', (0.35,-1.1, 0.55), (0.35, -0.75, 0.55), (0.25,-0.8,0.75), 0.3],
    "Santa's Bag": ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_santa.bam', (0.3,-1.25,0), (0.3,-0.75,0), (0.3,-0.75,0), 1],
    'Scuba Tank': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_scubaTank.bam', (0.25,-1.5,0.1), (0.25,-1.1,0.1), (0.25,-1.1,0.25), 0.25],
    'Shark Fin': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_sharkFin.bam', (0.35,-1.4, 0), (0.35, -1, 0), (0.25,-1.1,0), 0.35],
    'Sly Scarf':['phase_4/models/accessories/tt_m_chr_avt_acc_pac_scarf.bam', 'phase_4/maps/ttr_t_chr_avt_acc_pac_scarfSleuth.jpg', (0.25,-0.7,0.5), (0.25,-0.45,0.5), (0.25,-0.6,0.75), 1],
    'Soft Scarf':['phase_4/models/accessories/tt_m_chr_avt_acc_pac_scarf.bam', 'phase_4/maps/tt_t_chr_avt_acc_pac_scarfSoft.jpg', (0.25,-0.7,0.5), (0.25,-0.45,0.5), (0.25,-0.6,0.75), 1],
    'Spider Legs': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_spiderLegs.bam', (0.25,-1.5,0.25), (0.3,-1,0), (0.2,-1.25,0.25), 0.3],
    'Starry Bowtie': ['phase_4/models/accessories/ttr_m_chr_avt_acc_pac_bowtie.bam', 'phase_4/maps/ttr_t_chr_avt_acc_hat_ribbonPink_2.jpg', (0.25,-0.5,0.475), (0.25,-0.25,0.45), (0.25,-0.34,0.65), 0.25],
    'Starry Scarf': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_scarf.bam', 'phase_4/maps/tt_t_chr_avt_acc_pac_scarf_starry.jpg', (0.25,-0.7,0.5), (0.25,-0.45,0.5), (0.25,-0.6,0.75), 1],
    'Strawberry Bowtie': ['phase_4/models/accessories/ttr_m_chr_avt_acc_pac_bowtie.bam', 'phase_4/maps/ttr_t_chr_avt_acc_hat_ribbonTasty_1.jpg', (0.25,-0.5,0.475), (0.25,-0.25,0.45), (0.25,-0.34,0.65), 0.25],
    'Strawberry Cape': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_supertoonCape.bam', 'phase_4/maps/ttr_t_chr_avt_acc_pac_superStrawberry.jpg', (0.35,-1.1, 0.55), (0.35, -0.75, 0.55), (0.25,-0.8,0.75), 0.3],
    "SuperToon's Cape": ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_supertoonCape.bam', (0.35,-1.1, 0.55), (0.35, -0.75, 0.55), (0.25,-0.8,0.75), 0.3],
    'Teal Bowtie': ['phase_4/models/accessories/ttr_m_chr_avt_acc_pac_bowtie.bam', 'phase_4/maps/ttr_t_chr_avt_acc_hat_ribbonPink_4.jpg', (0.25,-0.5,0.475), (0.25,-0.25,0.45), (0.25,-0.34,0.65), 0.25],
    'Token Tote': ['phase_4/models/accessories/ttr_m_chr_avt_acc_pac_jellybeanJar.bam', 'phase_4/maps/ttr_t_avt_acc_pac_jellybeanJarTokens.jpg', 'phase_4/maps/ttr_t_avt_acc_pac_jellybeanJarTokens_a.rgb', (0.4,-1.25,-0.15), (0.3,-1,-0.15), (0.25,-1.1,0.025), 0.32],
    'ToonFest 2016 Blue Attendee Backpack': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_stuffedAnimalBackpackA.bam', 'phase_4/maps/ttr_t_chr_avt_acc_pac_stuffedAnimalBackpackTFBlue.jpg', (0.3,-1.6,-0.5), (0.3,-1.35,-0.4), (0.3,-1.4,-0.25), 0.25],
    'ToonFest 2016 Blue Backpack': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_backpack.bam', 'phase_4/maps/ttr_t_chr_avt_acc_pac_backpackTFBlue.jpg', (0.4,-1.5,0.1), (0.3,-1.1,0.1), (0.3,-1.25,0.2), 0.32],
    'ToonFest 2016 Pink Attendee Backpack': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_stuffedAnimalBackpackA.bam', 'phase_4/maps/ttr_t_chr_avt_acc_pac_stuffedAnimalBackpackTFPink.jpg', (0.3,-1.6,-0.5), (0.3,-1.35,-0.4), (0.3,-1.4,-0.25), 0.25],
    'ToonFest 2016 Pink Backpack': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_backpack.bam', 'phase_4/maps/ttr_t_chr_avt_acc_pac_backpackTFPink.jpg', (0.4,-1.5,0.1), (0.3,-1.1,0.1), (0.3,-1.25,0.2), 0.32],
    'Toonosaur Tail': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_dinosaurTail.bam',  (0.35,-1.4, 0), (0.35, -0.75, 0), (0.25,-1,0), 0.3],
    'Trainee Travel Pack':  ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_backpack.bam', 'phase_4/maps/ttr_t_chr_avt_acc_pac_backpackTrainee.jpg', (0.4,-1.5,0.1), (0.3,-1.1,0.1), (0.3,-1.25,0.2), 0.32],
    'Treasure Trove': ['phase_4/models/accessories/ttr_m_chr_avt_acc_pac_jellybeanJar.bam', 'phase_4/maps/ttr_t_avt_acc_pac_jellybeanJarTreasures.jpg', 'phase_4/maps/ttr_t_avt_acc_pac_jellybeanJarTreasures_a.rgb', (0.4,-1.25,-0.15), (0.3,-1,-0.15), (0.25,-1.1,0.025), 0.32],
    'Vampire Cloak': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_vampireCape.bam', (0.35,-1.1, 0.55), (0.35, -0.75, 0.55), (0.25,-0.8,0.75), 0.3],
    'Vanilla Bowtie' : ['phase_4/models/accessories/ttr_m_chr_avt_acc_pac_bowtie.bam', 'phase_4/maps/ttr_t_chr_avt_acc_hat_ribbonTasty_2.jpg', (0.25,-0.5,0.475), (0.25,-0.25,0.45), (0.25,-0.34,0.65), 0.25],
    'Yellow Polka-pack': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_backpack.bam', 'phase_4/maps/tt_t_chr_avt_acc_pac_backpackPolkaDotYellow.jpg', (0.4,-1.5,0.1), (0.3,-1.1,0.1), (0.3,-1.25,0.2), 0.32],
}