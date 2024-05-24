label start:
    play music "Jose Rizal - Part 1.mp3" loop
    
label intro_menu:
    scene intro_desk
    call screen intro_page

screen intro_page:
    add "intro_page/Books.png":
        xalign 0.72
        yalign 0.83

    imagebutton:
        xalign 0.83
        yalign 0.65
        idle "intro_page/Bust.png" at imageButtonScale
        action Show("bust_1")

    imagebutton:
        xalign 0.47
        yalign 0.25
        idle "intro_page/Crucifix.png" at imageButtonScale
        action Jump("main_lola")

    imagebutton:
        xalign 0.17
        yalign 0.53
        idle "intro_page/Globe.png" at imageButtonScale
        action Show("globe_1")

    imagebutton:
        xalign 0.4
        yalign 0.75
        idle "intro_page/Notebook.png" at imageButtonScale
        action Jump("main_notebook")

    imagebutton:
        xalign 0.7
        yalign 0.82
        idle "intro_page/Scrolls.png" at imageButtonScale
        action Show("scroll_1")

    imagebutton:
        xalign 0.58
        yalign 0.85
        idle "intro_page/Quill Pen.png" at imageButtonScale(zoomValue = 1.05)
        action Jump("main_quill")

    add "intro_page/Candle.png":
        xalign 0.32
        yalign 0.8



########## HELPER ###################

transform imageButtonScale(zoomValue = 1.03):
    on hover:
        linear 0.1 zoom zoomValue
    on idle:
        linear 0.1 zoom 1.0

screen content(content_name):
    add content_name:
        xalign 0.5
        yalign 0.5
    imagebutton:
        xalign 0.02
        yalign 0.05
        idle "back.png" at imageButtonScale(zoomValue = 1.1)
        action Hide()

########## NOTEBOOK #####################

screen notebook_icons:
    imagebutton:
        xalign 0.02
        yalign 0.05
        idle "back.png" at imageButtonScale(zoomValue = 1.1)
        action Jump("intro_menu")

    imagebutton:
        xalign 0.05
        yalign 0.3
        idle "main_notebook/Icons/Icon 1.png" at imageButtonScale
        action Show("content", content_name="main_notebook/Content/Content 1.png")

    imagebutton:
        xalign 0.95
        yalign 0.3
        idle "main_notebook/Icons/Icon 2.png" at imageButtonScale
        action Show("content", content_name="main_notebook/Content/Content 2.png")

    imagebutton:
        xalign 0.05
        yalign 0.55
        idle "main_notebook/Icons/Icon 3.png" at imageButtonScale
        action Show("content", content_name="main_notebook/Content/Content 3.png")

    imagebutton:
        xalign 0.90
        yalign 0.55
        idle "main_notebook/Icons/Icon 4.png" at imageButtonScale
        action Show("content", content_name="main_notebook/Content/Content 4.png")

    imagebutton:
        xalign 0.05
        yalign 0.9
        idle "main_notebook/Icons/Icon 5.png" at imageButtonScale
        action Show("content", content_name="main_notebook/Content/Content 5.png")

    imagebutton:
        xalign 0.85
        yalign 0.9
        idle "main_notebook/Icons/Icon 6.png" at imageButtonScale
        action Show("content", content_name="main_notebook/Content/Content 6.png")

label main_notebook:
    scene bg notebook
    call screen notebook_icons


################### LOLA #####################3

screen lolas_room:
    imagebutton:
        xalign 0.02
        yalign 0.05
        idle "back.png" at imageButtonScale(zoomValue = 1.1)
        action [Hide("box"), Jump ("start")]

    imagebutton:
        xalign 0.67
        yalign 0.55
        idle "lolas_room/room_objects/CABINET.png" at imageButtonScale(zoomValue = 1.01)
        action Show("content", content_name="lolas_room/items/cabinet_notes.png")

    imagebutton:
        xalign 0.08
        yalign 0.85
        idle "lolas_room/room_objects/BED.png" at imageButtonScale(zoomValue = 1.01)
        action Show("box")
    
    imagebutton:
        xalign 0.09
        yalign 0.1
        idle "lolas_room/room_objects/CROSS.png" at imageButtonScale(zoomValue = 1.04)
        action Show("content", content_name="lolas_room/items/cross.png")

    imagebutton:
        xalign 0.2
        yalign 0.08
        idle "lolas_room/room_objects/PHOTO1.png" at imageButtonScale(zoomValue = 1.04)
        action Jump("tarot")

    imagebutton:
        xalign 0.47
        yalign 0.35
        idle "lolas_room/room_objects/PHOTO2.png" at imageButtonScale(zoomValue = 1.07)
        action Jump("lola_rizal")

screen box:
    imagebutton:
        xalign 0.05
        yalign 0.85
        idle "lolas_room/room_objects/BOX.png" at imageButtonScale
        action [Hide(), Show("box_photos")]
        
screen box_photos:
    imagebutton:
        xalign 0.02
        yalign 0.05
        idle "back.png" at imageButtonScale(zoomValue = 1.1)
        action Hide()

    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "lolas_room/room_objects/BOX_PHOTOS.png" at imageButtonScale
        action [Hide(), Jump("box_photos_scenes")]
    

label main_lola:
    play music "bgm_lola.mp3" loop
    # scene lola_scene_1
    # pause
    scene lola_scene_2
    pause

label lola_start:
    scene lola_scene_3
    call screen lolas_room

label box_photos_scenes:
    scene worship_scene_1
    pause
    scene worship_scene_2
    pause
    scene note_scene_1
    pause
    jump lola_start

label tarot:
    scene back_frame
    pause
    scene tarot_scene
    pause
    jump lola_start

label lola_rizal:
    scene lola_rizal
    "This is my bro J. Rizz. He's a cool dude."
    jump lola_start



########## BUST #####################

screen bust_1:
    imagebutton:
        xalign 0.02
        yalign 0.05
        idle "back.png" at imageButtonScale(zoomValue = 1.1)
        action [Hide()]

    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "main_bust/1.png" at imageButtonScale
        action [Hide(), Show("bust_2")]

screen bust_2:
    imagebutton:
        xalign 0.02
        yalign 0.05
        idle "back.png" at imageButtonScale(zoomValue = 1.1)
        action [Hide()]

    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "main_bust/2.png" at imageButtonScale
        action [Hide(), Show("bust_3")]

screen bust_3:
    imagebutton:
        xalign 0.02
        yalign 0.05
        idle "back.png" at imageButtonScale(zoomValue = 1.1)
        action [Hide()]

    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "main_bust/3.png" at imageButtonScale
        action [Hide(), Show("bust_4")]

screen bust_4:
    imagebutton:
        xalign 0.02
        yalign 0.05
        idle "back.png" at imageButtonScale(zoomValue = 1.1)
        action [Hide()]

    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "main_bust/4.png" at imageButtonScale
        action [Hide(), Show("bust_5")] 

screen bust_5:
    imagebutton:
        xalign 0.02
        yalign 0.05
        idle "back.png" at imageButtonScale(zoomValue = 1.1)
        action [Hide()]

    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "main_bust/5.png" at imageButtonScale
        action [Hide(), Show("bust_6")]

screen bust_6:
    imagebutton:
        xalign 0.02
        yalign 0.05
        idle "back.png" at imageButtonScale(zoomValue = 1.1)
        action [Hide()]

    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "main_bust/6.png" at imageButtonScale
        action [Hide(), Jump("intro_menu")]


########## Quill #####################

screen quill_choose:
    imagebutton:
        xalign 0.02
        yalign 0.05
        idle "back.png" at imageButtonScale(zoomValue = 1.1)
        action Jump("intro_menu")

    imagebutton:
        xalign 0.3
        yalign 0.34
        idle "main_quill/barong.png" at imageButtonScale
        action Jump("barong")

    imagebutton:
        xalign 0.16
        yalign 0.32
        idle "main_quill/amerikana.png" at imageButtonScale
        action Jump("amerikana")

label main_quill:
    scene bg quill
    show barong_amerikano:
        xalign 1.0
        yalign 0.05
    show rizal_hubad:
        xalign 0.7
        yalign 0.8
    call screen quill_choose

label amerikana:
    scene bg quill
    show barong:
        xalign 0.3
        yalign 0.34
    show rizal_amerikana:
        xalign 0.7
        yalign 0.8
    show amerikana text1:
        xalign 1.0
        yalign 0.05
    pause
    show amerikana text2
    pause
    show amerikana text3
    pause
    show amerikana text4
    pause
    show amerikana text5
    pause
    jump main_quill

label barong:
    scene bg quill
    show amerikana:
        xalign 0.16
        yalign 0.32
    show rizal_barong:
        xalign 0.7
        yalign 0.8
    show barong text1:
        xalign 1.0
        yalign 0.05
    pause
    show barong text2
    pause
    show barong text3
    pause
    show barong text4
    pause
    show barong text5
    pause
    jump main_quill


###### SCROLLS #####################
transform scrolling:
    yalign -0.5
    linear 20.0 yalign 1.1


screen scroll_1:
    imagebutton:
        xalign 0.02
        yalign 0.05
        idle "back.png" at imageButtonScale(zoomValue = 1.1)
        action [Hide()]

    imagebutton:
        xalign 0.5
        idle "main_scrolls/scroll_1.png" at imageButtonScale, scrolling
        action [Hide(), Show("scroll_2")]

screen scroll_2:
    imagebutton:
        xalign 0.02
        yalign 0.05
        idle "back.png" at imageButtonScale(zoomValue = 1.1)
        action [Hide()]

    imagebutton:
        xalign 0.5
        idle "main_scrolls/scroll_2.png" at imageButtonScale, scrolling
        action [Hide()]


######### GLOBE #####################

### Fuck this, let's brute force
screen globe_1:
    imagebutton:
        idle "main_globe/globe_1.png"
        action [Hide(), Show("globe_2")]

    imagebutton:
        xalign 0.02
        yalign 0.05
        idle "back.png" at imageButtonScale(zoomValue = 1.1)
        action [Hide()]

screen globe_2:
    imagebutton:
        idle "main_globe/globe_2.png"
        action [Hide(), Show("globe_3")]

    imagebutton:
        xalign 0.02
        yalign 0.05
        idle "back.png" at imageButtonScale(zoomValue = 1.1)
        action [Hide()]

screen globe_3:
    imagebutton:
        idle "main_globe/globe_3.png"
        action [Hide(), Show("globe_4")]

    imagebutton:
        xalign 0.02
        yalign 0.05
        idle "back.png" at imageButtonScale(zoomValue = 1.1)
        action [Hide()]

screen globe_4:
    imagebutton:
        idle "main_globe/globe_4.png"
        action [Hide(), Show("globe_5")]

    imagebutton:
        xalign 0.02
        yalign 0.05
        idle "back.png" at imageButtonScale(zoomValue = 1.1)
        action [Hide()]

screen globe_5:
    imagebutton:
        idle "main_globe/globe_5.png"
        action [Hide(), Show("globe_6")]

    imagebutton:
        xalign 0.02
        yalign 0.05
        idle "back.png" at imageButtonScale(zoomValue = 1.1)
        action [Hide()]

screen globe_6:
    imagebutton:
        idle "main_globe/globe_6.png"
        action [Hide(), Show("globe_7")]

    imagebutton:
        xalign 0.02
        yalign 0.05
        idle "back.png" at imageButtonScale(zoomValue = 1.1)
        action [Hide()]

screen globe_7:
    imagebutton:
        idle "main_globe/globe_7.png"
        action [Hide(), Show("globe_8")]

    imagebutton:
        xalign 0.02
        yalign 0.05
        idle "back.png" at imageButtonScale(zoomValue = 1.1)
        action [Hide()] 

screen globe_8:
    imagebutton:
        idle "main_globe/globe_8.png"
        action [Hide(), Show("globe_9")]

    imagebutton:
        xalign 0.02
        yalign 0.05
        idle "back.png" at imageButtonScale(zoomValue = 1.1)
        action [Hide()]

screen globe_9:
    imagebutton:
        idle "main_globe/globe_9.png"
        action [Hide(), Show("globe_10")]

    imagebutton:
        xalign 0.02
        yalign 0.05
        idle "back.png" at imageButtonScale(zoomValue = 1.1)
        action [Hide()]

screen globe_10:
    imagebutton:
        idle "main_globe/globe_10.png"
        action [Hide(), Show("globe_11")]

    imagebutton:
        xalign 0.02
        yalign 0.05
        idle "back.png" at imageButtonScale(zoomValue = 1.1)
        action [Hide()]

screen globe_11:
    imagebutton:
        idle "main_globe/globe_11.png"
        action [Hide(), Show("globe_12")]

    imagebutton:
        xalign 0.02
        yalign 0.05
        idle "back.png" at imageButtonScale(zoomValue = 1.1)
        action [Hide()]

screen globe_12:
    imagebutton:
        idle "main_globe/globe_12.png"
        action [Hide(), Show("globe_13")]

    imagebutton:
        xalign 0.02
        yalign 0.05
        idle "back.png" at imageButtonScale(zoomValue = 1.1)
        action [Hide()]

screen globe_13:
    imagebutton:
        idle "main_globe/globe_13.png"
        action [Hide(), Show("globe_14")]

    imagebutton:
        xalign 0.02
        yalign 0.05
        idle "back.png" at imageButtonScale(zoomValue = 1.1)
        action [Hide()]

screen globe_14:
    imagebutton:
        idle "main_globe/globe_14.png"
        action [Hide(), Show("globe_15")]

    imagebutton:
        xalign 0.02
        yalign 0.05
        idle "back.png" at imageButtonScale(zoomValue = 1.1)
        action [Hide()]

screen globe_15:
    imagebutton:
        idle "main_globe/globe_15.png"
        action [Hide(), Show("globe_16")]

    imagebutton:
        xalign 0.02
        yalign 0.05
        idle "back.png" at imageButtonScale(zoomValue = 1.1)
        action [Hide()]

screen globe_16:
    imagebutton:
        idle "main_globe/globe_16.png"
        action [Hide(), Show("globe_17")]

    imagebutton:
        xalign 0.02
        yalign 0.05
        idle "back.png" at imageButtonScale(zoomValue = 1.1)
        action [Hide()]

screen globe_17:
    imagebutton:
        idle "main_globe/globe_17.png"
        action [Hide(), Show("globe_18")]

    imagebutton:
        xalign 0.02
        yalign 0.05
        idle "back.png" at imageButtonScale(zoomValue = 1.1)
        action [Hide()]

screen globe_18:
    imagebutton:
        idle "main_globe/globe_18.png"
        action [Hide(), Show("globe_19")]

    imagebutton:
        xalign 0.02
        yalign 0.05
        idle "back.png" at imageButtonScale(zoomValue = 1.1)
        action [Hide()]

screen globe_19:
    imagebutton:
        idle "main_globe/globe_19.png"
        action [Hide(), Show("globe_20")]

    imagebutton:
        xalign 0.02
        yalign 0.05
        idle "back.png" at imageButtonScale(zoomValue = 1.1)
        action [Hide()]

screen globe_20:
    imagebutton:
        idle "main_globe/globe_20.png"
        action [Hide(), Show("globe_21")]

    imagebutton:
        xalign 0.02
        yalign 0.05
        idle "back.png" at imageButtonScale(zoomValue = 1.1)
        action [Hide()] 

screen globe_21:
    imagebutton:
        idle "main_globe/globe_21.png"
        action [Hide(), Show("globe_22")]

    imagebutton:
        xalign 0.02
        yalign 0.05
        idle "back.png" at imageButtonScale(zoomValue = 1.1)
        action [Hide()]

screen globe_22:
    imagebutton:
        idle "main_globe/globe_22.png"
        action [Hide(), Show("globe_23")]

    imagebutton:
        xalign 0.02
        yalign 0.05
        idle "back.png" at imageButtonScale(zoomValue = 1.1)
        action [Hide()]

screen globe_23:
    imagebutton:
        idle "main_globe/globe_23.png"
        action [Hide(), Show("globe_24")]

    imagebutton:
        xalign 0.02
        yalign 0.05
        idle "back.png" at imageButtonScale(zoomValue = 1.1)
        action [Hide()]

screen globe_24:
    imagebutton:
        idle "main_globe/globe_24.png"
        action [Hide(), Show("globe_25")]

    imagebutton:
        xalign 0.02
        yalign 0.05
        idle "back.png" at imageButtonScale(zoomValue = 1.1)
        action [Hide()]

screen globe_25:
    imagebutton:
        idle "main_globe/globe_25.png"
        action [Hide(), Show("globe_26")]

    imagebutton:
        xalign 0.02
        yalign 0.05
        idle "back.png" at imageButtonScale(zoomValue = 1.1)
        action [Hide()]

screen globe_26:
    imagebutton:
        idle "main_globe/globe_26.png"
        action [Hide(), Show("globe_27")]

    imagebutton:
        xalign 0.02
        yalign 0.05
        idle "back.png" at imageButtonScale(zoomValue = 1.1)
        action [Hide()]

screen globe_27:
    imagebutton:
        idle "main_globe/globe_27.png"
        action [Hide(), Show("globe_28")]

    imagebutton:
        xalign 0.02
        yalign 0.05
        idle "back.png" at imageButtonScale(zoomValue = 1.1)
        action [Hide()]

screen globe_28:
    imagebutton:
        idle "main_globe/globe_28.png"
        action [Hide(), Show("globe_29")]

    imagebutton:
        xalign 0.02
        yalign 0.05
        idle "back.png" at imageButtonScale(zoomValue = 1.1)
        action [Hide()]

screen globe_29:
    imagebutton:
        idle "main_globe/globe_29.png"
        action [Hide(), Show("globe_30")]

    imagebutton:
        xalign 0.02
        yalign 0.05
        idle "back.png" at imageButtonScale(zoomValue = 1.1)
        action [Hide()]

screen globe_30:
    imagebutton:
        idle "main_globe/globe_30.png"
        action [Hide(), Show("globe_31")]

    imagebutton:
        xalign 0.02
        yalign 0.05
        idle "back.png" at imageButtonScale(zoomValue = 1.1)
        action [Hide()]

screen globe_31:
    imagebutton:
        idle "main_globe/globe_31.png"
        action [Hide(), Show("globe_32")]

    imagebutton:
        xalign 0.02
        yalign 0.05
        idle "back.png" at imageButtonScale(zoomValue = 1.1)
        action [Hide()]

screen globe_32:
    imagebutton:
        idle "main_globe/globe_32.png"
        action [Hide(), Show("globe_33")]

    imagebutton:
        xalign 0.02
        yalign 0.05
        idle "back.png" at imageButtonScale(zoomValue = 1.1)
        action [Hide()]

screen globe_33:
    imagebutton:
        idle "main_globe/globe_33.png"
        action [Hide(), Show("globe_34")]

    imagebutton:
        xalign 0.02
        yalign 0.05
        idle "back.png" at imageButtonScale(zoomValue = 1.1)
        action [Hide()]

screen globe_34:
    imagebutton:
        idle "main_globe/globe_34.png"
        action [Hide(), Show("globe_35")]

    imagebutton:
        xalign 0.02
        yalign 0.05
        idle "back.png" at imageButtonScale(zoomValue = 1.1)
        action [Hide()]

screen globe_35:
    imagebutton:
        idle "main_globe/globe_35.png"
        action [Hide()]

    imagebutton:
        xalign 0.02
        yalign 0.05
        idle "back.png" at imageButtonScale(zoomValue = 1.1)
        action [Hide()]
