#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.2),
    on Mon Feb  1 16:34:04 2021
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.2'
expName = 'Simcolourproject_2stim_asymm_good'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/bethfisher/Downloads/Colour_Similarity_Experiment-main/Colour_Similarity_Experiment/Colour_Similarity_Experiment.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 800], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='pix')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "startup"
startupClock = core.Clock()
import pandas as pd
from psychopy import tools
import random as rnd
rnd.seed()




# Initialize components for Routine "welcome_instr"
welcome_instrClock = core.Clock()
text_54 = visual.TextStim(win=win, name='text_54',
    text='You may quit the experiment at anytime by pressing <ESC>',
    font='Arial',
    units='norm', pos=(0, -0.3), height=0.1, wrapWidth=1000, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
welcome = visual.TextStim(win=win, name='welcome',
    text='Welcome to this experiment \n\nThis will take about 45 minutes \n\n',
    font='Arial',
    units='norm', pos=(0, 0), height=0.2, wrapWidth=1000, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp = keyboard.Keyboard()
space = visual.TextStim(win=win, name='space',
    text='Press SPACE to continue ',
    font='Arial',
    units='norm', pos=(0.7, -0.7), height=0.05, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "consent"
consentClock = core.Clock()
text_53 = visual.TextStim(win=win, name='text_53',
    text='Precision Phenomenology Experiment\nJust a little bit more to read before the experiment...this is an Informed Consent Form. Please read and understand the statements below.\n\nI understand that my taking part in the study is voluntary and that I am free to leave the study at any time, without giving any reason. I understand that my medical care or legal rights will not be affected in any way.\nI agree to the use and release of study-related information about me for the purposes described in this Informed Consent Form.\nI agree to the re-use of data collected in this study for future studies in a de-identified manner as described in this Informed Consent form.\nI understand that my consent continues until and unless I withdraw my consent that can be done at any time by giving notice to the investigator. I understand that if I withdraw my consent I will not be able to continue to take part in the study.\nI understand that if I withdraw consent, the study researchers will no longer use or release information that identifies me in connection with the study unless it is needed to keep the scientific quality of the study. I understand that if I withdraw consent the study researchers may still use any study-related information about me that was collected before I withdrew consent.\nI have read and I understand the information provided in this Informed Consent Form. I have had the opportunity to ask questions and have had these questions answered satisfactorily.\nI have had time to consider the information provided in this Informed Consent Form to consider answers to my questions, and to consider whether I wish to take part in the study.\nIf you understand the statements above, and freely consent to participate in the study, press [Space] to begin the experiment.',
    font='Times New Roman',
    units='norm', pos=(0, 0), height=0.05, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_16 = keyboard.Keyboard()
image = visual.ImageStim(
    win=win,
    name='image', units='pix', 
    image='monash-logo-mono.png', mask=None,
    ori=0, pos=[0,0], size=150,75,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "instr_1"
instr_1Clock = core.Clock()
text_1 = visual.TextStim(win=win, name='text_1',
    text='Before starting the main experiment, we need to do some quick calibrations to ensure your screen is set up correctly.',
    font='Arial',
    units='norm', pos=(0, 0.4), height=0.08, wrapWidth=1.5, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
space_2 = visual.TextStim(win=win, name='space_2',
    text='Press SPACE to continue ',
    font='Arial',
    units='norm', pos=(0.7, -0.7), height=0.05, wrapWidth=1.5, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text='Warning! It is critical that these calibrations are done correctly or you will be unable to do the experiment and we will be unable to approve your payment!',
    font='Arial',
    units='norm', pos=(0,-0.4), height=0.08, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "screen_scale"
screen_scaleClock = core.Clock()
ccimage = visual.ImageStim(
    win=win,
    name='ccimage', units='pix', 
    image='card.png', mask=None,
    ori=0, pos=(-150,150), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
# Set size of card

oldt=0
x_size=8.560
y_size=5.398


if ccimage.units=='norm':
    x_scale=.05
    y_scale=.1
    dbase = .0001
    unittext=' norm units'
    vsize=2
elif ccimage.units=='pix':
    x_scale=60
    y_scale=40
    dbase = .1
    unittext=' pixels'
    vsize=win.size[1]
else:
    x_scale=.05
    y_scale=.05
    dbase = .0001
    unittext=' height units'
    vsize=1
text_37 = visual.TextStim(win=win, name='text_37',
    text="First, we need to determine the size of your screen.\nTake a credit card (or a drivers license, library card, any equivalent card),\npress it to the screen and adjust the image on your screen to be the same size as the card\n\nTo increase the image width: press 'k' on your keyboard\nTo decrease the image width: press 'j' on your keyboard\n\nWhen you are done, press <ENTER>",
    font='Arial',
    units='norm', pos=(0, -0.35), height=0.06, wrapWidth=1000, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "instr_2"
instr_2Clock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Next, we need to get you to keep your head a fixed distance from the screen.\nThis will ensure future images are the right size for your screen. On the next screen please:',
    font='Arial',
    units='norm', pos=(0,-0.2), height=0.06, wrapWidth=1000, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_3 = keyboard.Keyboard()
text_3 = visual.TextStim(win=win, name='text_3',
    text='1. Keeping your arm straight, please touch your thumb to the centre of the screen in the oval\n2. While keeping your head in the same position, lower your arm.\n3. Please keep your head in this position for the remainder of the experiment ',
    font='Arial',
    units='norm', pos=(0, -0.5), height=0.06, wrapWidth=1000, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
space_3 = visual.TextStim(win=win, name='space_3',
    text='Press SPACE to continue ',
    font='Arial',
    units='norm', pos=(0.7, -0.7), height=0.05, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "instr_3"
instr_3Clock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='1. While keeping your arm straight touch your thumb to the centre of the screen in the oval.\n2. Keep your head in the same position, but lower and relax your arm.\n3. Please keep your head in this position for the remainder of the experiment.\n4. Press SPACE to continue ',
    font='Arial',
    units='norm', pos=(0, 0.5), height=0.07, wrapWidth=1000, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()
thumb_size = 20;
calibrationline = visual.ImageStim(
    win=win,
    name='calibrationline', units='pix', 
    image='calibrationline.png', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "instr_4"
instr_4Clock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='Lastly, we need to know how far your head is from the screen.\nPlease keep your head in the same position as before.\n\nOver the next few pages we will explain how we can work out how far you are sitting from the screen.\nPlease pay attention and follow all the instructions carefully.\n\nThese first few pages will be INSTRUCTIONS ONLY. You will be instructed when the calibrations start.\n\nWhen ready, press SPACE to continue and follow the instructions on the next page.\n',
    font='Arial',
    units='norm', pos=(0, 0), height=0.07, wrapWidth=1.5, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()
space_4 = visual.TextStim(win=win, name='space_4',
    text='Press SPACE to continue ',
    font='Arial',
    units='norm', pos=(0.7, -0.7), height=0.05, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "instr_5"
instr_5Clock = core.Clock()
key_resp_6 = keyboard.Keyboard()
space_5 = visual.TextStim(win=win, name='space_5',
    text='Press SPACE to continue ',
    font='Arial',
    units='norm', pos=(0.7, -0.7), height=0.05, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instr_only = visual.TextStim(win=win, name='instr_only',
    text='INSTRUCTIONS ONLY',
    font='Arial',
    units='norm', pos=(0, 0.6), height=0.1, wrapWidth=10000, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_6 = visual.TextStim(win=win, name='text_6',
    text='1. Put a finger on <ENTER> on the keyboard.',
    font='Arial',
    units='norm', pos=(0, -0.5), height=0.06, wrapWidth=1000, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "instr_6"
instr_6Clock = core.Clock()
key_resp_8 = keyboard.Keyboard()
space_7 = visual.TextStim(win=win, name='space_7',
    text='Press SPACE to continue ',
    font='Arial',
    units='norm', pos=(0.7,-0.7), height=0.05, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instr_only_3 = visual.TextStim(win=win, name='instr_only_3',
    text='INSTRUCTIONS ONLY',
    font='Arial',
    units='norm', pos=(0, 0.6), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_8 = visual.TextStim(win=win, name='text_8',
    text='2. Close your right eye',
    font='Arial',
    units='norm', pos=(0, -0.5), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "instr_7"
instr_7Clock = core.Clock()
key_resp_7 = keyboard.Keyboard()
space_6 = visual.TextStim(win=win, name='space_6',
    text='Press SPACE to continue ',
    font='Arial',
    units='norm', pos=(0.7, -0.7), height=0.05, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instr_only_2 = visual.TextStim(win=win, name='instr_only_2',
    text='INSTRUCTIONS ONLY',
    font='Arial',
    units='norm', pos=(0, 0.6), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_7 = visual.TextStim(win=win, name='text_7',
    text='3. Stare at the middle of the screen, keeping your head in the same position as before.\nKeep your right eye closed.',
    font='Arial',
    units='norm', pos=(0, -0.4), height=0.06, wrapWidth=1000, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
center_cross = visual.ShapeStim(
    win=win, name='center_cross', vertices='cross',units='norm', 
    size=(0.05, 0.05),
    ori=0, pos=(0, 0),
    lineWidth=1.5, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)

# Initialize components for Routine "instr_8"
instr_8Clock = core.Clock()
key_resp_12 = keyboard.Keyboard()
space_11 = visual.TextStim(win=win, name='space_11',
    text='Press SPACE to continue ',
    font='Arial',
    units='norm', pos=(0.7, -0.7), height=0.05, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instr_only_5 = visual.TextStim(win=win, name='instr_only_5',
    text='INSTRUCTIONS ONLY',
    font='Arial',
    units='norm', pos=(0, 0.6), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_13 = visual.TextStim(win=win, name='text_13',
    text='4. Without moving your head or face, use your left eye to focus on the black square.\nKeep your right eye closed and do not move your head.',
    font='Arial',
    units='norm', pos=(0, -0.5), height=0.06, wrapWidth=1000, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
center_cross_3 = visual.ShapeStim(
    win=win, name='center_cross_3', vertices='cross',units='norm', 
    size=(0.05, 0.05),
    ori=0, pos=(0, 0),
    lineWidth=0.8, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
black_square = visual.Rect(
    win=win, name='black_square',units='pix', 
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=(500,0),
    lineWidth=1.5, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
text_14 = visual.TextStim(win=win, name='text_14',
    text='Stare at the square',
    font='Arial',
    units='norm', pos=(0.75, 0.08), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

# Initialize components for Routine "instr_9"
instr_9Clock = core.Clock()
key_resp_11 = keyboard.Keyboard()
space_8 = visual.TextStim(win=win, name='space_8',
    text='Press SPACE to continue ',
    font='Arial',
    units='norm', pos=(0.7, -0.7), height=0.05, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instr_only_4 = visual.TextStim(win=win, name='instr_only_4',
    text='INSTRUCTIONS ONLY',
    font='Arial',
    units='norm', pos=(0, 0.6), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_11 = visual.TextStim(win=win, name='text_11',
    text='5. During the calibration task, a white ball will disappear as it moves from right to left.\nKeep your right eye closed, stare at the black square and do not move your head.\n',
    font='Arial',
    units='norm', pos=(0, -0.5), height=0.06, wrapWidth=1000, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
center_cross_2 = visual.ShapeStim(
    win=win, name='center_cross_2', vertices='cross',units='norm', 
    size=(0.05, 0.05),
    ori=0, pos=(0, 0),
    lineWidth=0.8, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
black_square1 = visual.Rect(
    win=win, name='black_square1',units='pix', 
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=(500,0),
    lineWidth=1.5, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
text_12 = visual.TextStim(win=win, name='text_12',
    text='<--- Ball movement ',
    font='Arial',
    units='norm', pos=(0.7, 0.08), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
white_ball2 = visual.Polygon(
    win=win, name='white_ball2',units='pix', 
    edges=1000, size=[1.0, 1.0],
    ori=0, pos=(400, 0),
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)

# Initialize components for Routine "instr_10"
instr_10Clock = core.Clock()
key_resp_18 = keyboard.Keyboard()
space_17 = visual.TextStim(win=win, name='space_17',
    text='Press SPACE to continue ',
    font='Arial',
    units='norm', pos=(0.7, -0.7), height=0.05, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instr_only_7 = visual.TextStim(win=win, name='instr_only_7',
    text='INSTRUCTIONS ONLY',
    font='Arial',
    units='norm', pos=(0, 0.6), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_44 = visual.TextStim(win=win, name='text_44',
    text='6. Press the <ENTER> key as soon as the ball disappears properly from your eye sight (not due to running off screen)\nKeep your right eye closed, stare at the black square, do not move your head.',
    font='Arial',
    units='norm', pos=(0, -0.5), height=0.06, wrapWidth=1.5, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "instr_11"
instr_11Clock = core.Clock()
key_resp_21 = keyboard.Keyboard()
space_18 = visual.TextStim(win=win, name='space_18',
    text='Press SPACE to continue ',
    font='Arial',
    units='norm', pos=(0.7, -0.7), height=0.05, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instr_only_8 = visual.TextStim(win=win, name='instr_only_8',
    text='INSTRUCTIONS ONLY',
    font='Arial',
    units='norm', pos=(0,0.6), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_45 = visual.TextStim(win=win, name='text_45',
    text='7. The next page will show you a demonstration of the calibration task for a few seconds.\nDuring the actual calibration, you will need to press <ENTER> when the ball disappears.\n\nYou will do this five times so we can make sure we get the right distance.\nThe ball will reset each time.\n\nKeep your right eye closed, stare at the black square and do not move your head.',
    font='Arial',
    units='norm', pos=(0, -0.4), height=0.06, wrapWidth=1000, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "calibration_example"
calibration_exampleClock = core.Clock()
white_ball1 = visual.Polygon(
    win=win, name='white_ball1',units='pix', 
    edges=1000, size=[1.0, 1.0],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
black_square3 = visual.Rect(
    win=win, name='black_square3',units='pix', 
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1.5, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
text_19 = visual.TextStim(win=win, name='text_19',
    text='VISIBLE',
    font='Arial',
    units='norm', pos=(0, 0.5), height=0.05, wrapWidth=None, ori=0, 
    color='green', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_20 = visual.TextStim(win=win, name='text_20',
    text='INVISIBLE',
    font='Arial',
    units='norm', pos=(0, 0.5), height=0.05, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
white_ball12 = visual.Polygon(
    win=win, name='white_ball12',units='pix', 
    edges=1000, size=[1.0, 1.0],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
text_21 = visual.TextStim(win=win, name='text_21',
    text='VISIBLE',
    font='Arial',
    units='norm', pos=(0, 0.5), height=0.05, wrapWidth=None, ori=0, 
    color='green', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
text_22 = visual.TextStim(win=win, name='text_22',
    text='Press <ENTER> now!',
    font='Arial',
    units='norm', pos=(0, -0.5), height=0.05, wrapWidth=None, ori=0, 
    color='green', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
white_ball13 = visual.Polygon(
    win=win, name='white_ball13',units='pix', 
    edges=1000, size=[1.0, 1.0],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)

# Initialize components for Routine "instr_12"
instr_12Clock = core.Clock()
key_resp_13 = keyboard.Keyboard()
space_12 = visual.TextStim(win=win, name='space_12',
    text='Press SPACE to continue ',
    font='Arial',
    units='norm', pos=(0.7, -0.7), height=0.05, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instr_only_6 = visual.TextStim(win=win, name='instr_only_6',
    text='NEXT WILL BE THE ACTUAL CALIBRATION\n\nRemember to keep your right eye closed, stare at the black square and do not move your head.\n\nPress the <ENTER> key as soon as the ball disappears from your eye sight (not just due to running off the edge of the screen).\n\nWhen ready press SPACE to start viewing the distance calibration.',
    font='Arial',
    units='norm', pos=(0, 0.3), height=0.07, wrapWidth=1.5, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_15 = visual.TextStim(win=win, name='text_15',
    text='Warning! It is critical that these calibrations are done correctly or you will be unable to do the experiment and we will be unable to approve your payment!',
    font='Arial',
    units='norm', pos=(0, -0.4), height=0.06, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "ball_calibration"
ball_calibrationClock = core.Clock()
black_square2 = visual.Rect(
    win=win, name='black_square2',units='pix', 
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1.5, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
white_ball = visual.Polygon(
    win=win, name='white_ball',units='pix', 
    edges=1000, size=[1.0, 1.0],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
key_resp_19 = keyboard.Keyboard()
# Store each calibration
viewerdistancetotal = []
# Count calibrations
calibrationcount = 0
text_39 = visual.TextStim(win=win, name='text_39',
    text='default text',
    font='Arial',
    units='norm', pos=(0, -0.6), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
white_ball1_2 = visual.Polygon(
    win=win, name='white_ball1_2',units='pix', 
    edges=1000, size=[1.0, 1.0],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)

# Initialize components for Routine "viewerdistance"
viewerdistanceClock = core.Clock()
peripheral_scale = 4.5 #scaling factor for peripheral stimuli, chosen based on Freeman & Simoncelli 2011 fig 1.
radius_central = 1.5 # arbitrarily chosen 1 DVA
radius_peripheral = 10 
stimulus_size = 1 # arbitarily chosen 1 DVA
response_stim_scale = 2 
distance_threshold = 300
screen_x_threshold = 230
text_38 = visual.TextStim(win=win, name='text_38',
    text='default text',
    font='Arial',
    units='norm', pos=(0, -0.2), height=0.08, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_40 = visual.TextStim(win=win, name='text_40',
    text='The calibrations were successful!',
    font='Arial',
    units='norm', pos=(0, 0), height=0.08, wrapWidth=10000, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_20 = keyboard.Keyboard()
space_20 = visual.TextStim(win=win, name='space_20',
    text='Press SPACE to continue ',
    font='Arial',
    units='norm', pos=(0.7, -0.7), height=0.05, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "viewerdistance_unsucess"
viewerdistance_unsucessClock = core.Clock()
text_41 = visual.TextStim(win=win, name='text_41',
    text='Unfortunately the calibrations were unsuccessful.',
    font='Arial',
    units='norm', pos=(0, 0.100), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_42 = visual.TextStim(win=win, name='text_42',
    text='default text',
    font='Arial',
    units='norm', pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_43 = visual.TextStim(win=win, name='text_43',
    text='Please exit the experiment',
    font='Arial',
    units='norm', pos=(0, -0.100), height=0.08, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "stim1_instr"
stim1_instrClock = core.Clock()
stim1 = visual.MovieStim3(
    win=win, name='stim1',
    noAudio = False,
    filename='1stimmov.mp4',
    ori=0, pos=(0, 100), opacity=1,
    loop=True,
    size=600,400,
    depth=0.0,
    )
key_resp_14 = keyboard.Keyboard()
space_13 = visual.TextStim(win=win, name='space_13',
    text='Press SPACE to continue ',
    font='Arial',
    units='norm', pos=(0.7, -0.7), height=0.05, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_16 = visual.TextStim(win=win, name='text_16',
    text='Throughout the experiment, focus on the cross at the centre of the screen.\nA circle will flash out quickly on the screen.',
    font='Arial',
    units='norm', pos=(0, -0.5), height=0.06, wrapWidth=1000, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "stim_response_instr"
stim_response_instrClock = core.Clock()
movie_2 = visual.MovieStim3(
    win=win, name='movie_2',
    noAudio = False,
    filename='1stim_async_response_py.mp4',
    ori=0, pos=(0, 150), opacity=1,
    loop=True,
    size=600,400,
    depth=0.0,
    )
key_resp_15 = keyboard.Keyboard()
space_14 = visual.TextStim(win=win, name='space_14',
    text='Press SPACE to continue ',
    font='Arial',
    units='norm', pos=(0.7, -0.7), height=0.05, wrapWidth=1000, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_17 = visual.TextStim(win=win, name='text_17',
    text='Sometimes you will need to decide the similarity levels of the previous circle to a circle on the next screen.\nIgnore any size differences.\n\n0 => most similar colour (least different colour)\n7 => most different colour (least similar colour)\n\nAfter choosing, move your cursor back to the centre and click and hold the box to continue.',
    font='Arial',
    units='norm', pos=(0, -0.4), height=0.06, wrapWidth=1000, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "catch_insrt"
catch_insrtClock = core.Clock()
space_15 = visual.TextStim(win=win, name='space_15',
    text='Press SPACE to continue ',
    font='Arial',
    units='norm', pos=(0.7, -0.7), height=0.05, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_17 = keyboard.Keyboard()
movie_3 = visual.MovieStim3(
    win=win, name='movie_3',
    noAudio = False,
    filename='catch_py.mp4',
    ori=0, pos=0,100, opacity=1,
    loop=True,
    size=600,400,
    depth=-2.0,
    )
text_18 = visual.TextStim(win=win, name='text_18',
    text='Sometimes there will be a special trial where you will just be asked to click on a particular value.\nPlease click and hold the value for that trial.',
    font='Arial',
    units='norm', pos=(0, -0.5), height=0.06, wrapWidth=1000, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "colour_circle_instr_2"
colour_circle_instr_2Clock = core.Clock()
key_resp_9 = keyboard.Keyboard()
intructioncircle_1 = visual.Polygon(
    win=win, name='intructioncircle_1',units='pix', 
    edges=1000, size=(50, 50),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1, -1, -1], lineColorSpace='rgb',
    fillColor=[1, -1, -1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
instructioncircle_2 = visual.Polygon(
    win=win, name='instructioncircle_2',units='pix', 
    edges=1000, size=(50, 50),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1, 0.33, -1], lineColorSpace='rgb',
    fillColor=[1, 0.33, -1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
instructioncircle_3 = visual.Polygon(
    win=win, name='instructioncircle_3',units='pix', 
    edges=1000, size=(50, 50),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[0.33, 1, -1], lineColorSpace='rgb',
    fillColor=[0.33, 1, -1], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
instructioncircle_4 = visual.Polygon(
    win=win, name='instructioncircle_4',units='pix', 
    edges=1000, size=(50, 50),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[-1, 1, -1], lineColorSpace='rgb',
    fillColor=[-1, 1, -1], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
instructioncircle_5 = visual.Polygon(
    win=win, name='instructioncircle_5',units='pix', 
    edges=1000, size=(50, 50),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[-1, 1, 0.32], lineColorSpace='rgb',
    fillColor=[-1, 1, 0.32], fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
insturctioncircle_6 = visual.Polygon(
    win=win, name='insturctioncircle_6',units='pix', 
    edges=1000, size=(50, 50),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[-1, 0.32, 1], lineColorSpace='rgb',
    fillColor=[-1, 0.32, 1], fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)
instructioncircle_7 = visual.Polygon(
    win=win, name='instructioncircle_7',units='pix', 
    edges=1000, size=(50, 50),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[-1, -1, 1], lineColorSpace='rgb',
    fillColor=[-1, -1, 1], fillColorSpace='rgb',
    opacity=1, depth=-8.0, interpolate=True)
instructioncircle_8 = visual.Polygon(
    win=win, name='instructioncircle_8',units='pix', 
    edges=1000, size=(50, 50),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[0.33, -1, 1], lineColorSpace='rgb',
    fillColor=[0.33, -1, 1], fillColorSpace='rgb',
    opacity=1, depth=-9.0, interpolate=True)
instructioncircle_9 = visual.Polygon(
    win=win, name='instructioncircle_9',units='pix', 
    edges=1000, size=(50, 50),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1, -1, 0.33], lineColorSpace='rgb',
    fillColor=[1, -1, 0.33], fillColorSpace='rgb',
    opacity=1, depth=-10.0, interpolate=True)
space_9 = visual.TextStim(win=win, name='space_9',
    text='Press SPACE to continue ',
    font='Arial',
    units='norm', pos=(0.7, -0.7), height=0.05, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);
text_9 = visual.TextStim(win=win, name='text_9',
    text='During the test, you will see these 9 colors below',
    font='Arial',
    units='norm', pos=(0, 0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);

# Initialize components for Routine "instr_prac"
instr_pracClock = core.Clock()
space_10 = visual.TextStim(win=win, name='space_10',
    text='Press SPACE to continue ',
    font='Arial',
    units='norm', pos=(0.7, -0.7), height=0.05, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_10 = visual.TextStim(win=win, name='text_10',
    text='You are going to do a few practice trials to make you be more familiar with the experiment.\nWhen you are ready, please press SPACE to start the practice trials',
    font='Arial',
    units='norm', pos=(0, 0), height=0.06, wrapWidth=1000, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_10 = keyboard.Keyboard()

# Initialize components for Routine "Stim1_display_prac"
Stim1_display_pracClock = core.Clock()
Circle = visual.Polygon(
    win=win, name='Circle',units='pix', 
    edges=1000, size=[1.0, 1.0],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
centre_cross4_2 = visual.ShapeStim(
    win=win, name='centre_cross4_2', vertices='cross',units='norm', 
    size=(0.03, 0.03),
    ori=0, pos=(0, 0),
    lineWidth=1.5, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)

# Initialize components for Routine "response_prac"
response_pracClock = core.Clock()
mouse_5 = event.Mouse(win=win)
x, y = [None, None]
mouse_5.mouseClock = core.Clock()
# Set response size
a = (screen.size[0]/2)*0.10;
b = (screen.size[0]/2)*0.158

response1disk_5 = visual.ImageStim(
    win=win,
    name='response1disk_5', units='pix', 
    image='response67.png', mask=None,
    ori=0, pos=a,a, size=b,b,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
response3disk_5 = visual.ImageStim(
    win=win,
    name='response3disk_5', units='pix', 
    image='response45.png', mask=None,
    ori=0, pos=a,-a, size=b,b,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
response5disk_5 = visual.ImageStim(
    win=win,
    name='response5disk_5', units='pix', 
    image='response23.png', mask=None,
    ori=0, pos=-a,-a, size=b,b,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
response7disk_5 = visual.ImageStim(
    win=win,
    name='response7disk_5', units='pix', 
    image='response01.png', mask=None,
    ori=0, pos=-a,a, size=b,b,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
Circle_3 = visual.Polygon(
    win=win, name='Circle_3',units='pix', 
    edges=1000, size=[1.0, 1.0],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
text_29 = visual.TextStim(win=win, name='text_29',
    text='Please choose the similarity level of the circle with the previously cued circle.\nPlease click and hold to indicate your choice.\n0 => Most similar\n7 => Most different \n',
    font='Arial',
    units='norm', pos=(0, -0.7), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);

# Initialize components for Routine "responseprac_feedback"
responseprac_feedbackClock = core.Clock()
text_55 = visual.TextStim(win=win, name='text_55',
    text='default text',
    font='Arial',
    units='norm', pos=(0, 0), height=0.1, wrapWidth=1000, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_56 = visual.TextStim(win=win, name='text_56',
    text='default text',
    font='Arial',
    units='norm', pos=(0, -0.2), height=0.1, wrapWidth=1000, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "summary_prac"
summary_pracClock = core.Clock()
mouse_10 = event.Mouse(win=win)
x, y = [None, None]
mouse_10.mouseClock = core.Clock()
response1disk_10 = visual.ImageStim(
    win=win,
    name='response1disk_10', units='pix', 
    image='response67.png', mask=None,
    ori=0, pos=a,a, size=b,b,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
response3disk_10 = visual.ImageStim(
    win=win,
    name='response3disk_10', units='pix', 
    image='response45.png', mask=None,
    ori=0, pos=a,-a, size=b,b,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
response5disk_10 = visual.ImageStim(
    win=win,
    name='response5disk_10', units='pix', 
    image='response23.png', mask=None,
    ori=0, pos=-a,-a, size=b,b,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
response7disk_10 = visual.ImageStim(
    win=win,
    name='response7disk_10', units='pix', 
    image='response01.png', mask=None,
    ori=0, pos=-a,a, size=b,b,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
rectangle_8 = visual.Rect(
    win=win, name='rectangle_8',units='norm', 
    width=(0.1, 0.08)[0], height=(0.1, 0.08)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
pracnumber = 0;

text_49 = visual.TextStim(win=win, name='text_49',
    text='Please click and hold on the grey rectangle in the middle of the response numbers to continue',
    font='Arial',
    units='norm', pos=(0, -0.5), height=0.05, wrapWidth=1000, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
text_50 = visual.TextStim(win=win, name='text_50',
    text='default text',
    font='Arial',
    units='norm', pos=(0, -0.7), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);

# Initialize components for Routine "special_trial_prac"
special_trial_pracClock = core.Clock()
text_36 = visual.TextStim(win=win, name='text_36',
    text='SPECIAL TRIAL',
    font='Arial',
    units='norm', pos=(0,0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "catch_prac"
catch_pracClock = core.Clock()
mouse_7 = event.Mouse(win=win)
x, y = [None, None]
mouse_7.mouseClock = core.Clock()
response1disk_7 = visual.ImageStim(
    win=win,
    name='response1disk_7', units='pix', 
    image='response67.png', mask=None,
    ori=0, pos=a,a, size=b,b,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
response3disk_7 = visual.ImageStim(
    win=win,
    name='response3disk_7', units='pix', 
    image='response45.png', mask=None,
    ori=0, pos=a,-a, size=b,b,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
response5disk_7 = visual.ImageStim(
    win=win,
    name='response5disk_7', units='pix', 
    image='response23.png', mask=None,
    ori=0, pos=-a,-a, size=b,b,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
response7disk_7 = visual.ImageStim(
    win=win,
    name='response7disk_7', units='pix', 
    image='response01.png', mask=None,
    ori=0, pos=-a,a, size=b,b,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
# Set up catch trials 

catchtrialorderprac = []
for i in range(0,2):
    n = randint(0,7)
    catchtrialorderprac.append(n)

catchnumberprac = randint(0,7);

text_32 = visual.TextStim(win=win, name='text_32',
    text='default text',
    font='Arial',
    units='norm', pos=(0, -0.6), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
rectangle_5 = visual.Rect(
    win=win, name='rectangle_5',units='norm', 
    width=(0.1, 0.08)[0], height=(0.1, 0.08)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)

# Initialize components for Routine "summary2_prac"
summary2_pracClock = core.Clock()
mouse_6 = event.Mouse(win=win)
x, y = [None, None]
mouse_6.mouseClock = core.Clock()
response1disk_6 = visual.ImageStim(
    win=win,
    name='response1disk_6', units='pix', 
    image='response67.png', mask=None,
    ori=0, pos=a,a, size=b,b,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
response3disk_6 = visual.ImageStim(
    win=win,
    name='response3disk_6', units='pix', 
    image='response45.png', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
response5disk_6 = visual.ImageStim(
    win=win,
    name='response5disk_6', units='pix', 
    image='response23.png', mask=None,
    ori=0, pos=-a,-a, size=b,b,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
response7disk_6 = visual.ImageStim(
    win=win,
    name='response7disk_6', units='pix', 
    image='response01.png', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
rectangle_4 = visual.Rect(
    win=win, name='rectangle_4',units='norm', 
    width=(0.1, 0.08)[0], height=(0.1, 0.08)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
pracnumber = 0;

text_30 = visual.TextStim(win=win, name='text_30',
    text='Please click and hold the grey rectangle in the middle of the response numbers to continue',
    font='Arial',
    units='norm', pos=(0, -0.7), height=0.05, wrapWidth=1000, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
text_31 = visual.TextStim(win=win, name='text_31',
    text='default text',
    font='Arial',
    units='norm', pos=(0, -0.8), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);

# Initialize components for Routine "begin"
beginClock = core.Clock()
space_19 = visual.TextStim(win=win, name='space_19',
    text='Press SPACE to continue ',
    font='Arial',
    units='norm', pos=(0.7, -0.7), height=0.05, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_46 = visual.TextStim(win=win, name='text_46',
    text='You have finished the practice trial.\n\nNext page will be the formal test. \n\nIf you are ready, please press SPACE button to start the experiment.',
    font='Arial',
    units='norm', pos=(0, 0), height=0.08, wrapWidth=1000, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_22 = keyboard.Keyboard()

# Initialize components for Routine "Stim1_display"
Stim1_displayClock = core.Clock()
Circle_1 = visual.Polygon(
    win=win, name='Circle_1',units='pix', 
    edges=1000, size=[1.0, 1.0],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
centre_cross4 = visual.ShapeStim(
    win=win, name='centre_cross4', vertices='cross',units='norm', 
    size=(0.03, 0.03),
    ori=0, pos=(0, 0),
    lineWidth=1.5, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)

# Initialize components for Routine "response"
responseClock = core.Clock()
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
order = randint(1,100);
response1disk = visual.ImageStim(
    win=win,
    name='response1disk', 
    image='response67.png', mask=None,
    ori=0, pos=a,a, size=b,b,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
response3disk = visual.ImageStim(
    win=win,
    name='response3disk', 
    image='response45.png', mask=None,
    ori=0, pos=a,-a, size=b,b,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
response5disk = visual.ImageStim(
    win=win,
    name='response5disk', 
    image='response23.png', mask=None,
    ori=0, pos=-a,-a, size=b,b,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
response7disk = visual.ImageStim(
    win=win,
    name='response7disk', 
    image='response01.png', mask=None,
    ori=0, pos=-a,a, size=b,b,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
Circle_2 = visual.Polygon(
    win=win, name='Circle_2',units='pix', 
    edges=1000, size=[1.0, 1.0],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
text_23 = visual.TextStim(win=win, name='text_23',
    text='Please choose the similarity level of the circle with the previously cued circle.\nPlease click and hold to indicate your choice.\n0 => Most similar\n7 => Most different ',
    font='Arial',
    units='norm', pos=(0, -0.6), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);

# Initialize components for Routine "response_2"
response_2Clock = core.Clock()
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()
response1disk_2 = visual.ImageStim(
    win=win,
    name='response1disk_2', 
    image='response67.png', mask=None,
    ori=0, pos=a,a, size=b,b,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
response3disk_2 = visual.ImageStim(
    win=win,
    name='response3disk_2', 
    image='response45.png', mask=None,
    ori=0, pos=a,-a, size=b,b,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
response5disk_2 = visual.ImageStim(
    win=win,
    name='response5disk_2', 
    image='response23.png', mask=None,
    ori=0, pos=-a,-a, size=b,b,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
response7disk_2 = visual.ImageStim(
    win=win,
    name='response7disk_2', 
    image='response01.png', mask=None,
    ori=0, pos=-a,a, size=b,b,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
rectangle = visual.Rect(
    win=win, name='rectangle',units='norm', 
    width=(0.100, 0.080)[0], height=(0.100, 0.080)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
trialnumber = 0;
grey = (.2, .2, .2);


text_25 = visual.TextStim(win=win, name='text_25',
    text='Please click and hold the grey rectangle in the middle of the response numbers to continue',
    font='Arial',
    units='norm', pos=(0, -0.5), height=0.05, wrapWidth=1000, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
text_24 = visual.TextStim(win=win, name='text_24',
    text='default text',
    font='Arial',
    units='norm', pos=(0, -0.7), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);

# Initialize components for Routine "special_trial"
special_trialClock = core.Clock()
text_33 = visual.TextStim(win=win, name='text_33',
    text='SPECIAL TRIAL',
    font='Arial',
    units='norm', pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "catch_1"
catch_1Clock = core.Clock()
mouse_3 = event.Mouse(win=win)
x, y = [None, None]
mouse_3.mouseClock = core.Clock()
response1disk_3 = visual.ImageStim(
    win=win,
    name='response1disk_3', 
    image='response67.png', mask=None,
    ori=0, pos=a,a, size=b,b,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
response3disk_3 = visual.ImageStim(
    win=win,
    name='response3disk_3', 
    image='response45.png', mask=None,
    ori=0, pos=a,-a, size=b,b,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
response5disk_3 = visual.ImageStim(
    win=win,
    name='response5disk_3', 
    image='response23.png', mask=None,
    ori=0, pos=-a,-a, size=b,b,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
response7disk_3 = visual.ImageStim(
    win=win,
    name='response7disk_3', 
    image='response01.png', mask=None,
    ori=0, pos=-a,a, size=b,b,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
catchtrialorder = []
for i in range(0,20):
    n = randint(0,324)
    catchtrialorder.append(n)

text_26 = visual.TextStim(win=win, name='text_26',
    text='default text',
    font='Arial',
    units='norm', pos=(0, -0.6), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
rectangle_2 = visual.Rect(
    win=win, name='rectangle_2',units='norm', 
    width=(0.100, 0.080)[0], height=(0.100, 0.080)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor=grey, fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)

# Initialize components for Routine "response_sum"
response_sumClock = core.Clock()
mouse_11 = event.Mouse(win=win)
x, y = [None, None]
mouse_11.mouseClock = core.Clock()
response1disk_11 = visual.ImageStim(
    win=win,
    name='response1disk_11', 
    image='response67.png', mask=None,
    ori=0, pos=a,a, size=b,b,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
response3disk_11 = visual.ImageStim(
    win=win,
    name='response3disk_11', 
    image='response45.png', mask=None,
    ori=0, pos=a,-a, size=b,b,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
response5disk_11 = visual.ImageStim(
    win=win,
    name='response5disk_11', 
    image='response23.png', mask=None,
    ori=0, pos=-a,-a, size=b,b,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
response7disk_11 = visual.ImageStim(
    win=win,
    name='response7disk_11', 
    image='response01.png', mask=None,
    ori=0, pos=-a,a, size=b,b,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
rectangle_9 = visual.Rect(
    win=win, name='rectangle_9',units='norm', 
    width=(0.100, 0.080)[0], height=(0.100, 0.080)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
trialnumber = 0;

text_51 = visual.TextStim(win=win, name='text_51',
    text='Please click and hold the grey rectangle in the middle of the response numbers to continue',
    font='Arial',
    units='norm', pos=(0, -0.5), height=0.05, wrapWidth=1000, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
text_52 = visual.TextStim(win=win, name='text_52',
    text='default text',
    font='Arial',
    units='norm', pos=(0, -0.7), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);

# Initialize components for Routine "survey1"
survey1Clock = core.Clock()
copyText_1 = visual.TextStim(win=win, name='copyText_1',
    text=None,
    font='Arial',
    units='norm', pos=(-0.05, 0.1), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
import string
allLetters = list(string.ascii_lowercase+string.digits)
question_4 = visual.TextStim(win=win, name='question_4',
    text='Please answer the next 7 questions to finish the experiment. Please type your reponse and press <ENTER> to submit,\n\n1. Did you have any difficulty in seeing the location of the two circles on each trial? (y or n)\n',
    font='Arial',
    units='norm', pos=(0, 0.5), height=0.08, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
submitanswer = visual.TextStim(win=win, name='submitanswer',
    text='Press enter to submit your answer',
    font='Arial',
    units='norm', pos=(0, -0.9), height=0.08, wrapWidth=3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "survey2"
survey2Clock = core.Clock()
copyText_2 = visual.TextStim(win=win, name='copyText_2',
    text=None,
    font='Arial',
    units='norm', pos=(-0.05, 0.1), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
import string
allLetters = list(string.ascii_lowercase+string.digits)
question = visual.TextStim(win=win, name='question',
    text='2. Did you have any difficulty in knowing what colour the central circles were? (y or n)\n',
    font='Arial',
    units='norm', pos=(0, 0.5), height=0.08, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
submitanswer_2 = visual.TextStim(win=win, name='submitanswer_2',
    text='Press enter to submit your answer',
    font='Arial',
    units='norm', pos=(0, -0.9), height=0.08, wrapWidth=3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "survey3"
survey3Clock = core.Clock()
copyText_3 = visual.TextStim(win=win, name='copyText_3',
    text=None,
    font='Arial',
    units='norm', pos=(-0.05, 0.1), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
import string
allLetters = list(string.ascii_lowercase+string.digits)
question_2 = visual.TextStim(win=win, name='question_2',
    text='3. Did you have any difficulty in knowing what colour the peripheral circles were? (y or n)\n',
    font='Arial',
    units='norm', pos=(0, 0.5), height=0.08, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
submitanswer_3 = visual.TextStim(win=win, name='submitanswer_3',
    text='Press enter to submit your answer',
    font='Arial',
    units='norm', pos=(0, -0.9), height=0.08, wrapWidth=3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "survey_4"
survey_4Clock = core.Clock()
copyText_4 = visual.TextStim(win=win, name='copyText_4',
    text=None,
    font='Arial',
    units='norm', pos=(-0.05, 0.1), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
import string
allLetters = list(string.ascii_lowercase+string.digits)
question_3 = visual.TextStim(win=win, name='question_3',
    text='4. Do you have normal visual acuity, or corrected-to-normal wearing glasses or contact lenses? (y or n)',
    font='Arial',
    units='norm', pos=(0, 0.5), height=0.08, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
submitanswer_4 = visual.TextStim(win=win, name='submitanswer_4',
    text='Press enter to submit your answer',
    font='Arial',
    units='norm', pos=(0, -0.9), height=0.08, wrapWidth=3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "survey5"
survey5Clock = core.Clock()
copyText_5 = visual.TextStim(win=win, name='copyText_5',
    text=None,
    font='Arial',
    units='norm', pos=(-0.05, 0.1), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
import string
allLetters = list(string.ascii_lowercase+string.digits)
question_5 = visual.TextStim(win=win, name='question_5',
    text="5. Do you have any colour vision impairment? (y or n)\nIf yes, please describe the type (e.g) 'red-green colour blind'). ",
    font='Arial',
    units='norm', pos=(0, 0.5), height=0.08, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
submitanswer_5 = visual.TextStim(win=win, name='submitanswer_5',
    text='Press enter to submit your answer',
    font='Arial',
    units='norm', pos=(0, -0.9), height=0.08, wrapWidth=3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "survey6"
survey6Clock = core.Clock()
copyText_6 = visual.TextStim(win=win, name='copyText_6',
    text=None,
    font='Arial',
    units='norm', pos=(-0.05, 0.1), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
import string
allLetters = list(string.ascii_lowercase+string.digits)
question_6 = visual.TextStim(win=win, name='question_6',
    text="6. Did you base your judgements on any of the following stratergies? \n- colour catergories (e.g 'red','blue','green')\n- colour opponecy axes (e.g 'red to green', 'blue to yellow')\n- another stratergy \n- no particular stratergy\nPlease type which stratergy, and if you selected 'another stratergy' please describe it.\n",
    font='Arial',
    units='norm', pos=(0, 0.5), height=0.08, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
submitanswer_6 = visual.TextStim(win=win, name='submitanswer_6',
    text='Press enter to submit your answer',
    font='Arial',
    units='norm', pos=(0, -0.9), height=0.08, wrapWidth=3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "survey7"
survey7Clock = core.Clock()
copyText_7 = visual.TextStim(win=win, name='copyText_7',
    text=None,
    font='Arial',
    units='norm', pos=(-0.05, 0.1), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
import string
allLetters = list(string.ascii_lowercase+string.digits)
question_7 = visual.TextStim(win=win, name='question_7',
    text='Please type any other comments you may have. \n\nYou have now finished the experiment. Thank you for your participation!',
    font='Arial',
    units='norm', pos=(0, 0.5), height=0.08, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
submitanswer_7 = visual.TextStim(win=win, name='submitanswer_7',
    text='Press enter to submit your answer',
    font='Arial',
    units='norm', pos=(0, -0.9), height=0.08, wrapWidth=3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "startup"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
startupComponents = []
for thisComponent in startupComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
startupClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "startup"-------
while continueRoutine:
    # get current time
    t = startupClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=startupClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in startupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "startup"-------
for thisComponent in startupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "startup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "welcome_instr"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
welcome_instrComponents = [text_54, welcome, key_resp, space]
for thisComponent in welcome_instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
welcome_instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "welcome_instr"-------
while continueRoutine:
    # get current time
    t = welcome_instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=welcome_instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_54* updates
    if text_54.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_54.frameNStart = frameN  # exact frame index
        text_54.tStart = t  # local t and not account for scr refresh
        text_54.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_54, 'tStartRefresh')  # time at next scr refresh
        text_54.setAutoDraw(True)
    
    # *welcome* updates
    if welcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome.frameNStart = frameN  # exact frame index
        welcome.tStart = t  # local t and not account for scr refresh
        welcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome, 'tStartRefresh')  # time at next scr refresh
        welcome.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *space* updates
    if space.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        space.frameNStart = frameN  # exact frame index
        space.tStart = t  # local t and not account for scr refresh
        space.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space, 'tStartRefresh')  # time at next scr refresh
        space.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcome_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome_instr"-------
for thisComponent in welcome_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_54.started', text_54.tStartRefresh)
thisExp.addData('text_54.stopped', text_54.tStopRefresh)
thisExp.addData('welcome.started', welcome.tStartRefresh)
thisExp.addData('welcome.stopped', welcome.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "welcome_instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "consent"-------
continueRoutine = True
# update component parameters for each repeat
posx = ((window.innerWidth / 2) * 0.85);
posy = ((window.innerWidth / 2) * 0.85);
key_resp_16.keys = []
key_resp_16.rt = []
_key_resp_16_allKeys = []
image.setPos((-posx, posy))
# keep track of which components have finished
consentComponents = [text_53, key_resp_16, image]
for thisComponent in consentComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
consentClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "consent"-------
while continueRoutine:
    # get current time
    t = consentClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=consentClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_53* updates
    if text_53.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_53.frameNStart = frameN  # exact frame index
        text_53.tStart = t  # local t and not account for scr refresh
        text_53.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_53, 'tStartRefresh')  # time at next scr refresh
        text_53.setAutoDraw(True)
    
    # *key_resp_16* updates
    waitOnFlip = False
    if key_resp_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_16.frameNStart = frameN  # exact frame index
        key_resp_16.tStart = t  # local t and not account for scr refresh
        key_resp_16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_16, 'tStartRefresh')  # time at next scr refresh
        key_resp_16.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_16.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_16.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_16.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_16.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_16_allKeys.extend(theseKeys)
        if len(_key_resp_16_allKeys):
            key_resp_16.keys = _key_resp_16_allKeys[-1].name  # just the last key pressed
            key_resp_16.rt = _key_resp_16_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in consentComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "consent"-------
for thisComponent in consentComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_53.started', text_53.tStartRefresh)
thisExp.addData('text_53.stopped', text_53.tStopRefresh)
# check responses
if key_resp_16.keys in ['', [], None]:  # No response was made
    key_resp_16.keys = None
thisExp.addData('key_resp_16.keys',key_resp_16.keys)
if key_resp_16.keys != None:  # we had a response
    thisExp.addData('key_resp_16.rt', key_resp_16.rt)
thisExp.addData('key_resp_16.started', key_resp_16.tStartRefresh)
thisExp.addData('key_resp_16.stopped', key_resp_16.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('image.started', image.tStartRefresh)
thisExp.addData('image.stopped', image.tStopRefresh)
# the Routine "consent" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr_1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
instr_1Components = [text_1, space_2, text_2, key_resp_2]
for thisComponent in instr_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr_1"-------
while continueRoutine:
    # get current time
    t = instr_1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr_1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_1* updates
    if text_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_1.frameNStart = frameN  # exact frame index
        text_1.tStart = t  # local t and not account for scr refresh
        text_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_1, 'tStartRefresh')  # time at next scr refresh
        text_1.setAutoDraw(True)
    
    # *space_2* updates
    if space_2.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        space_2.frameNStart = frameN  # exact frame index
        space_2.tStart = t  # local t and not account for scr refresh
        space_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_2, 'tStartRefresh')  # time at next scr refresh
        space_2.setAutoDraw(True)
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_1"-------
for thisComponent in instr_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_1.started', text_1.tStartRefresh)
thisExp.addData('text_1.stopped', text_1.tStopRefresh)
thisExp.addData('space_2.started', space_2.tStartRefresh)
thisExp.addData('space_2.stopped', space_2.tStopRefresh)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "instr_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "screen_scale"-------
continueRoutine = True
# update component parameters for each repeat
ccimage.setSize((x_size*x_scale, x_size*x_scale*0.62))
# keep track of which components have finished
screen_scaleComponents = [ccimage, text_37]
for thisComponent in screen_scaleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
screen_scaleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "screen_scale"-------
while continueRoutine:
    # get current time
    t = screen_scaleClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=screen_scaleClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ccimage* updates
    if ccimage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ccimage.frameNStart = frameN  # exact frame index
        ccimage.tStart = t  # local t and not account for scr refresh
        ccimage.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ccimage, 'tStartRefresh')  # time at next scr refresh
        ccimage.setAutoDraw(True)
    keys=event.getKeys()
    
    if len(keys):
        if t-oldt<.5:
            dscale=5*dbase
            oldt=t
        else:
            dscale=dbase
            oldt=t
        if 'return' in keys:
            continueRoutine=False
        elif 'j' in keys:
            x_scale=round((x_scale-dscale)*10000)/10000
        elif 'k' in keys:
            x_scale=round((x_scale+dscale)*10000)/10000
        ccimage.size=[x_size*x_scale, x_size*x_scale*0.62]
    
    
    ratio_pxpermm = ((x_scale*x_size)/85.6)
    
    
    
    
    # *text_37* updates
    if text_37.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_37.frameNStart = frameN  # exact frame index
        text_37.tStart = t  # local t and not account for scr refresh
        text_37.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_37, 'tStartRefresh')  # time at next scr refresh
        text_37.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in screen_scaleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "screen_scale"-------
for thisComponent in screen_scaleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ccimage.started', ccimage.tStartRefresh)
thisExp.addData('ccimage.stopped', ccimage.tStopRefresh)
#Calculate ratio of pixels to mm
ratio_pxpermm = ((x_scale*x_size)/85.6)

thisExp.addData('X Scale',x_scale)
thisExp.addData('ratio_pxpermm',ratio_pxpermm)

screen_size_x = (1 / ratio_pxpermm) * (win.size[0]);
screen_size_y = (1 / ratio_pxpermm) * (win.size[1]);

thisExp.addData('screen_size_x',screen_size_x)
thisExp.addData('screen_size_y',screen_size_y)
thisExp.addData('text_37.started', text_37.tStartRefresh)
thisExp.addData('text_37.stopped', text_37.tStopRefresh)
# the Routine "screen_scale" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr_2"-------
continueRoutine = True
# update component parameters for each repeat
movie = visual.MovieStim3(
    win=win, name='movie',units='norm', 
    noAudio = False,
    filename='calibrationinsrt.mp4',
    ori=0, pos=(0, 0.4), opacity=1,
    loop=True,
    size=(0.38,0.35),
    depth=0.0,
    )
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
instr_2Components = [movie, text, key_resp_3, text_3, space_3]
for thisComponent in instr_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr_2"-------
while continueRoutine:
    # get current time
    t = instr_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *movie* updates
    if movie.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        movie.frameNStart = frameN  # exact frame index
        movie.tStart = t  # local t and not account for scr refresh
        movie.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(movie, 'tStartRefresh')  # time at next scr refresh
        movie.setAutoDraw(True)
    if movie.status == FINISHED:  # force-end the routine
        continueRoutine = False
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
    # *space_3* updates
    if space_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space_3.frameNStart = frameN  # exact frame index
        space_3.tStart = t  # local t and not account for scr refresh
        space_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_3, 'tStartRefresh')  # time at next scr refresh
        space_3.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_2"-------
for thisComponent in instr_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('movie.started', movie.tStartRefresh)
thisExp.addData('movie.stopped', movie.tStopRefresh)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
thisExp.addData('space_3.started', space_3.tStartRefresh)
thisExp.addData('space_3.stopped', space_3.tStopRefresh)
# the Routine "instr_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr_3"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# Calculate line size from ratio
line_size = thumb_size * ratio_pxpermm
calibrationline.setSize((line_size, line_size*3))
# keep track of which components have finished
instr_3Components = [text_4, key_resp_4, calibrationline]
for thisComponent in instr_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr_3"-------
while continueRoutine:
    # get current time
    t = instr_3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr_3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *calibrationline* updates
    if calibrationline.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        calibrationline.frameNStart = frameN  # exact frame index
        calibrationline.tStart = t  # local t and not account for scr refresh
        calibrationline.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(calibrationline, 'tStartRefresh')  # time at next scr refresh
        calibrationline.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_3"-------
for thisComponent in instr_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.addData('key_resp_4.started', key_resp_4.tStartRefresh)
thisExp.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
thisExp.nextEntry()
thisExp.addData("line_size", line_size);

thisExp.addData('calibrationline.started', calibrationline.tStartRefresh)
thisExp.addData('calibrationline.stopped', calibrationline.tStopRefresh)
# the Routine "instr_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr_4"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
instr_4Components = [text_5, key_resp_5, space_4]
for thisComponent in instr_4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr_4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr_4"-------
while continueRoutine:
    # get current time
    t = instr_4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr_4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_5.frameNStart = frameN  # exact frame index
        text_5.tStart = t  # local t and not account for scr refresh
        text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        text_5.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *space_4* updates
    if space_4.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        space_4.frameNStart = frameN  # exact frame index
        space_4.tStart = t  # local t and not account for scr refresh
        space_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_4, 'tStartRefresh')  # time at next scr refresh
        space_4.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_4"-------
for thisComponent in instr_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_5.started', text_5.tStartRefresh)
thisExp.addData('text_5.stopped', text_5.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('space_4.started', space_4.tStartRefresh)
thisExp.addData('space_4.stopped', space_4.tStopRefresh)
# the Routine "instr_4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr_5"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
instr_5Components = [key_resp_6, space_5, instr_only, text_6]
for thisComponent in instr_5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr_5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr_5"-------
while continueRoutine:
    # get current time
    t = instr_5Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr_5Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *space_5* updates
    if space_5.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        space_5.frameNStart = frameN  # exact frame index
        space_5.tStart = t  # local t and not account for scr refresh
        space_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_5, 'tStartRefresh')  # time at next scr refresh
        space_5.setAutoDraw(True)
    
    # *instr_only* updates
    if instr_only.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_only.frameNStart = frameN  # exact frame index
        instr_only.tStart = t  # local t and not account for scr refresh
        instr_only.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_only, 'tStartRefresh')  # time at next scr refresh
        instr_only.setAutoDraw(True)
    
    # *text_6* updates
    if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_5"-------
for thisComponent in instr_5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.addData('key_resp_6.started', key_resp_6.tStartRefresh)
thisExp.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('space_5.started', space_5.tStartRefresh)
thisExp.addData('space_5.stopped', space_5.tStopRefresh)
thisExp.addData('instr_only.started', instr_only.tStartRefresh)
thisExp.addData('instr_only.stopped', instr_only.tStopRefresh)
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)
# the Routine "instr_5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr_6"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_8.keys = []
key_resp_8.rt = []
_key_resp_8_allKeys = []
# keep track of which components have finished
instr_6Components = [key_resp_8, space_7, instr_only_3, text_8]
for thisComponent in instr_6Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr_6Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr_6"-------
while continueRoutine:
    # get current time
    t = instr_6Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr_6Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_8* updates
    waitOnFlip = False
    if key_resp_8.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.tStart = t  # local t and not account for scr refresh
        key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_8.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_8_allKeys.extend(theseKeys)
        if len(_key_resp_8_allKeys):
            key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
            key_resp_8.rt = _key_resp_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *space_7* updates
    if space_7.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        space_7.frameNStart = frameN  # exact frame index
        space_7.tStart = t  # local t and not account for scr refresh
        space_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_7, 'tStartRefresh')  # time at next scr refresh
        space_7.setAutoDraw(True)
    
    # *instr_only_3* updates
    if instr_only_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_only_3.frameNStart = frameN  # exact frame index
        instr_only_3.tStart = t  # local t and not account for scr refresh
        instr_only_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_only_3, 'tStartRefresh')  # time at next scr refresh
        instr_only_3.setAutoDraw(True)
    
    # *text_8* updates
    if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_8.frameNStart = frameN  # exact frame index
        text_8.tStart = t  # local t and not account for scr refresh
        text_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
        text_8.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_6Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_6"-------
for thisComponent in instr_6Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys = None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.addData('key_resp_8.started', key_resp_8.tStartRefresh)
thisExp.addData('key_resp_8.stopped', key_resp_8.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('space_7.started', space_7.tStartRefresh)
thisExp.addData('space_7.stopped', space_7.tStopRefresh)
thisExp.addData('instr_only_3.started', instr_only_3.tStartRefresh)
thisExp.addData('instr_only_3.stopped', instr_only_3.tStopRefresh)
thisExp.addData('text_8.started', text_8.tStartRefresh)
thisExp.addData('text_8.stopped', text_8.tStopRefresh)
# the Routine "instr_6" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr_7"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_7.keys = []
key_resp_7.rt = []
_key_resp_7_allKeys = []
# keep track of which components have finished
instr_7Components = [key_resp_7, space_6, instr_only_2, text_7, center_cross]
for thisComponent in instr_7Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr_7Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr_7"-------
while continueRoutine:
    # get current time
    t = instr_7Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr_7Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_7* updates
    waitOnFlip = False
    if key_resp_7.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.tStart = t  # local t and not account for scr refresh
        key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_7.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_7.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_7_allKeys.extend(theseKeys)
        if len(_key_resp_7_allKeys):
            key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
            key_resp_7.rt = _key_resp_7_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *space_6* updates
    if space_6.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        space_6.frameNStart = frameN  # exact frame index
        space_6.tStart = t  # local t and not account for scr refresh
        space_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_6, 'tStartRefresh')  # time at next scr refresh
        space_6.setAutoDraw(True)
    
    # *instr_only_2* updates
    if instr_only_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_only_2.frameNStart = frameN  # exact frame index
        instr_only_2.tStart = t  # local t and not account for scr refresh
        instr_only_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_only_2, 'tStartRefresh')  # time at next scr refresh
        instr_only_2.setAutoDraw(True)
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    
    # *center_cross* updates
    if center_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        center_cross.frameNStart = frameN  # exact frame index
        center_cross.tStart = t  # local t and not account for scr refresh
        center_cross.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(center_cross, 'tStartRefresh')  # time at next scr refresh
        center_cross.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_7Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_7"-------
for thisComponent in instr_7Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_7.keys in ['', [], None]:  # No response was made
    key_resp_7.keys = None
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.addData('key_resp_7.started', key_resp_7.tStartRefresh)
thisExp.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('space_6.started', space_6.tStartRefresh)
thisExp.addData('space_6.stopped', space_6.tStopRefresh)
thisExp.addData('instr_only_2.started', instr_only_2.tStartRefresh)
thisExp.addData('instr_only_2.stopped', instr_only_2.tStopRefresh)
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)
thisExp.addData('center_cross.started', center_cross.tStartRefresh)
thisExp.addData('center_cross.stopped', center_cross.tStopRefresh)
# the Routine "instr_7" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr_8"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_12.keys = []
key_resp_12.rt = []
_key_resp_12_allKeys = []
black_square.setSize((8.5*ratio_pxpermm, 8.5*ratio_pxpermm))
# keep track of which components have finished
instr_8Components = [key_resp_12, space_11, instr_only_5, text_13, center_cross_3, black_square, text_14]
for thisComponent in instr_8Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr_8Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr_8"-------
while continueRoutine:
    # get current time
    t = instr_8Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr_8Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_12* updates
    waitOnFlip = False
    if key_resp_12.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        key_resp_12.frameNStart = frameN  # exact frame index
        key_resp_12.tStart = t  # local t and not account for scr refresh
        key_resp_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_12, 'tStartRefresh')  # time at next scr refresh
        key_resp_12.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_12.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_12.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_12.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_12_allKeys.extend(theseKeys)
        if len(_key_resp_12_allKeys):
            key_resp_12.keys = _key_resp_12_allKeys[-1].name  # just the last key pressed
            key_resp_12.rt = _key_resp_12_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *space_11* updates
    if space_11.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        space_11.frameNStart = frameN  # exact frame index
        space_11.tStart = t  # local t and not account for scr refresh
        space_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_11, 'tStartRefresh')  # time at next scr refresh
        space_11.setAutoDraw(True)
    
    # *instr_only_5* updates
    if instr_only_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_only_5.frameNStart = frameN  # exact frame index
        instr_only_5.tStart = t  # local t and not account for scr refresh
        instr_only_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_only_5, 'tStartRefresh')  # time at next scr refresh
        instr_only_5.setAutoDraw(True)
    
    # *text_13* updates
    if text_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_13.frameNStart = frameN  # exact frame index
        text_13.tStart = t  # local t and not account for scr refresh
        text_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_13, 'tStartRefresh')  # time at next scr refresh
        text_13.setAutoDraw(True)
    
    # *center_cross_3* updates
    if center_cross_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        center_cross_3.frameNStart = frameN  # exact frame index
        center_cross_3.tStart = t  # local t and not account for scr refresh
        center_cross_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(center_cross_3, 'tStartRefresh')  # time at next scr refresh
        center_cross_3.setAutoDraw(True)
    
    # *black_square* updates
    if black_square.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        black_square.frameNStart = frameN  # exact frame index
        black_square.tStart = t  # local t and not account for scr refresh
        black_square.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(black_square, 'tStartRefresh')  # time at next scr refresh
        black_square.setAutoDraw(True)
    
    # *text_14* updates
    if text_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_14.frameNStart = frameN  # exact frame index
        text_14.tStart = t  # local t and not account for scr refresh
        text_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_14, 'tStartRefresh')  # time at next scr refresh
        text_14.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_8Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_8"-------
for thisComponent in instr_8Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_12.keys in ['', [], None]:  # No response was made
    key_resp_12.keys = None
thisExp.addData('key_resp_12.keys',key_resp_12.keys)
if key_resp_12.keys != None:  # we had a response
    thisExp.addData('key_resp_12.rt', key_resp_12.rt)
thisExp.addData('key_resp_12.started', key_resp_12.tStartRefresh)
thisExp.addData('key_resp_12.stopped', key_resp_12.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('space_11.started', space_11.tStartRefresh)
thisExp.addData('space_11.stopped', space_11.tStopRefresh)
thisExp.addData('instr_only_5.started', instr_only_5.tStartRefresh)
thisExp.addData('instr_only_5.stopped', instr_only_5.tStopRefresh)
thisExp.addData('text_13.started', text_13.tStartRefresh)
thisExp.addData('text_13.stopped', text_13.tStopRefresh)
thisExp.addData('center_cross_3.started', center_cross_3.tStartRefresh)
thisExp.addData('center_cross_3.stopped', center_cross_3.tStopRefresh)
thisExp.addData('black_square.started', black_square.tStartRefresh)
thisExp.addData('black_square.stopped', black_square.tStopRefresh)
thisExp.addData('text_14.started', text_14.tStartRefresh)
thisExp.addData('text_14.stopped', text_14.tStopRefresh)
# the Routine "instr_8" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr_9"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_11.keys = []
key_resp_11.rt = []
_key_resp_11_allKeys = []
black_square1.setSize((8.5*ratio_pxpermm, 8.5*ratio_pxpermm))
white_ball2.setSize((8.5*ratio_pxpermm, 8.5*ratio_pxpermm))
# keep track of which components have finished
instr_9Components = [key_resp_11, space_8, instr_only_4, text_11, center_cross_2, black_square1, text_12, white_ball2]
for thisComponent in instr_9Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr_9Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr_9"-------
while continueRoutine:
    # get current time
    t = instr_9Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr_9Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_11* updates
    waitOnFlip = False
    if key_resp_11.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        key_resp_11.frameNStart = frameN  # exact frame index
        key_resp_11.tStart = t  # local t and not account for scr refresh
        key_resp_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_11, 'tStartRefresh')  # time at next scr refresh
        key_resp_11.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_11.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_11.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_11_allKeys.extend(theseKeys)
        if len(_key_resp_11_allKeys):
            key_resp_11.keys = _key_resp_11_allKeys[-1].name  # just the last key pressed
            key_resp_11.rt = _key_resp_11_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *space_8* updates
    if space_8.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        space_8.frameNStart = frameN  # exact frame index
        space_8.tStart = t  # local t and not account for scr refresh
        space_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_8, 'tStartRefresh')  # time at next scr refresh
        space_8.setAutoDraw(True)
    
    # *instr_only_4* updates
    if instr_only_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_only_4.frameNStart = frameN  # exact frame index
        instr_only_4.tStart = t  # local t and not account for scr refresh
        instr_only_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_only_4, 'tStartRefresh')  # time at next scr refresh
        instr_only_4.setAutoDraw(True)
    
    # *text_11* updates
    if text_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_11.frameNStart = frameN  # exact frame index
        text_11.tStart = t  # local t and not account for scr refresh
        text_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
        text_11.setAutoDraw(True)
    
    # *center_cross_2* updates
    if center_cross_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        center_cross_2.frameNStart = frameN  # exact frame index
        center_cross_2.tStart = t  # local t and not account for scr refresh
        center_cross_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(center_cross_2, 'tStartRefresh')  # time at next scr refresh
        center_cross_2.setAutoDraw(True)
    
    # *black_square1* updates
    if black_square1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        black_square1.frameNStart = frameN  # exact frame index
        black_square1.tStart = t  # local t and not account for scr refresh
        black_square1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(black_square1, 'tStartRefresh')  # time at next scr refresh
        black_square1.setAutoDraw(True)
    
    # *text_12* updates
    if text_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_12.frameNStart = frameN  # exact frame index
        text_12.tStart = t  # local t and not account for scr refresh
        text_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
        text_12.setAutoDraw(True)
    
    # *white_ball2* updates
    if white_ball2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        white_ball2.frameNStart = frameN  # exact frame index
        white_ball2.tStart = t  # local t and not account for scr refresh
        white_ball2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(white_ball2, 'tStartRefresh')  # time at next scr refresh
        white_ball2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_9Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_9"-------
for thisComponent in instr_9Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_11.keys in ['', [], None]:  # No response was made
    key_resp_11.keys = None
thisExp.addData('key_resp_11.keys',key_resp_11.keys)
if key_resp_11.keys != None:  # we had a response
    thisExp.addData('key_resp_11.rt', key_resp_11.rt)
thisExp.addData('key_resp_11.started', key_resp_11.tStartRefresh)
thisExp.addData('key_resp_11.stopped', key_resp_11.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('space_8.started', space_8.tStartRefresh)
thisExp.addData('space_8.stopped', space_8.tStopRefresh)
thisExp.addData('instr_only_4.started', instr_only_4.tStartRefresh)
thisExp.addData('instr_only_4.stopped', instr_only_4.tStopRefresh)
thisExp.addData('text_11.started', text_11.tStartRefresh)
thisExp.addData('text_11.stopped', text_11.tStopRefresh)
thisExp.addData('center_cross_2.started', center_cross_2.tStartRefresh)
thisExp.addData('center_cross_2.stopped', center_cross_2.tStopRefresh)
thisExp.addData('black_square1.started', black_square1.tStartRefresh)
thisExp.addData('black_square1.stopped', black_square1.tStopRefresh)
thisExp.addData('text_12.started', text_12.tStartRefresh)
thisExp.addData('text_12.stopped', text_12.tStopRefresh)
thisExp.addData('white_ball2.started', white_ball2.tStartRefresh)
thisExp.addData('white_ball2.stopped', white_ball2.tStopRefresh)
# the Routine "instr_9" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr_10"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_18.keys = []
key_resp_18.rt = []
_key_resp_18_allKeys = []
# keep track of which components have finished
instr_10Components = [key_resp_18, space_17, instr_only_7, text_44]
for thisComponent in instr_10Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr_10Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr_10"-------
while continueRoutine:
    # get current time
    t = instr_10Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr_10Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_18* updates
    waitOnFlip = False
    if key_resp_18.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        key_resp_18.frameNStart = frameN  # exact frame index
        key_resp_18.tStart = t  # local t and not account for scr refresh
        key_resp_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_18, 'tStartRefresh')  # time at next scr refresh
        key_resp_18.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_18.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_18.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_18.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_18.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_18_allKeys.extend(theseKeys)
        if len(_key_resp_18_allKeys):
            key_resp_18.keys = _key_resp_18_allKeys[-1].name  # just the last key pressed
            key_resp_18.rt = _key_resp_18_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *space_17* updates
    if space_17.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        space_17.frameNStart = frameN  # exact frame index
        space_17.tStart = t  # local t and not account for scr refresh
        space_17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_17, 'tStartRefresh')  # time at next scr refresh
        space_17.setAutoDraw(True)
    
    # *instr_only_7* updates
    if instr_only_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_only_7.frameNStart = frameN  # exact frame index
        instr_only_7.tStart = t  # local t and not account for scr refresh
        instr_only_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_only_7, 'tStartRefresh')  # time at next scr refresh
        instr_only_7.setAutoDraw(True)
    
    # *text_44* updates
    if text_44.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_44.frameNStart = frameN  # exact frame index
        text_44.tStart = t  # local t and not account for scr refresh
        text_44.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_44, 'tStartRefresh')  # time at next scr refresh
        text_44.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_10Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_10"-------
for thisComponent in instr_10Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_18.keys in ['', [], None]:  # No response was made
    key_resp_18.keys = None
thisExp.addData('key_resp_18.keys',key_resp_18.keys)
if key_resp_18.keys != None:  # we had a response
    thisExp.addData('key_resp_18.rt', key_resp_18.rt)
thisExp.addData('key_resp_18.started', key_resp_18.tStartRefresh)
thisExp.addData('key_resp_18.stopped', key_resp_18.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('space_17.started', space_17.tStartRefresh)
thisExp.addData('space_17.stopped', space_17.tStopRefresh)
thisExp.addData('instr_only_7.started', instr_only_7.tStartRefresh)
thisExp.addData('instr_only_7.stopped', instr_only_7.tStopRefresh)
thisExp.addData('text_44.started', text_44.tStartRefresh)
thisExp.addData('text_44.stopped', text_44.tStopRefresh)
# the Routine "instr_10" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr_11"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_21.keys = []
key_resp_21.rt = []
_key_resp_21_allKeys = []
# keep track of which components have finished
instr_11Components = [key_resp_21, space_18, instr_only_8, text_45]
for thisComponent in instr_11Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr_11Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr_11"-------
while continueRoutine:
    # get current time
    t = instr_11Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr_11Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_21* updates
    waitOnFlip = False
    if key_resp_21.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        key_resp_21.frameNStart = frameN  # exact frame index
        key_resp_21.tStart = t  # local t and not account for scr refresh
        key_resp_21.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_21, 'tStartRefresh')  # time at next scr refresh
        key_resp_21.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_21.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_21.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_21.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_21.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_21_allKeys.extend(theseKeys)
        if len(_key_resp_21_allKeys):
            key_resp_21.keys = _key_resp_21_allKeys[-1].name  # just the last key pressed
            key_resp_21.rt = _key_resp_21_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *space_18* updates
    if space_18.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        space_18.frameNStart = frameN  # exact frame index
        space_18.tStart = t  # local t and not account for scr refresh
        space_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_18, 'tStartRefresh')  # time at next scr refresh
        space_18.setAutoDraw(True)
    
    # *instr_only_8* updates
    if instr_only_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_only_8.frameNStart = frameN  # exact frame index
        instr_only_8.tStart = t  # local t and not account for scr refresh
        instr_only_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_only_8, 'tStartRefresh')  # time at next scr refresh
        instr_only_8.setAutoDraw(True)
    
    # *text_45* updates
    if text_45.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_45.frameNStart = frameN  # exact frame index
        text_45.tStart = t  # local t and not account for scr refresh
        text_45.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_45, 'tStartRefresh')  # time at next scr refresh
        text_45.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_11Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_11"-------
for thisComponent in instr_11Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_21.keys in ['', [], None]:  # No response was made
    key_resp_21.keys = None
thisExp.addData('key_resp_21.keys',key_resp_21.keys)
if key_resp_21.keys != None:  # we had a response
    thisExp.addData('key_resp_21.rt', key_resp_21.rt)
thisExp.addData('key_resp_21.started', key_resp_21.tStartRefresh)
thisExp.addData('key_resp_21.stopped', key_resp_21.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('space_18.started', space_18.tStartRefresh)
thisExp.addData('space_18.stopped', space_18.tStopRefresh)
thisExp.addData('instr_only_8.started', instr_only_8.tStartRefresh)
thisExp.addData('instr_only_8.stopped', instr_only_8.tStopRefresh)
thisExp.addData('text_45.started', text_45.tStartRefresh)
thisExp.addData('text_45.stopped', text_45.tStopRefresh)
# the Routine "instr_11" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "calibration_example"-------
continueRoutine = True
# update component parameters for each repeat
black_square3.setSize((8.5*ratio_pxpermm, 8.5*ratio_pxpermm))
ballpos = (window.innerWidth/2)*0.75;
# keep track of which components have finished
calibration_exampleComponents = [white_ball1, black_square3, text_19, text_20, white_ball12, text_21, text_22, white_ball13]
for thisComponent in calibration_exampleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
calibration_exampleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "calibration_example"-------
while continueRoutine:
    # get current time
    t = calibration_exampleClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=calibration_exampleClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *white_ball1* updates
    if white_ball1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        white_ball1.frameNStart = frameN  # exact frame index
        white_ball1.tStart = t  # local t and not account for scr refresh
        white_ball1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(white_ball1, 'tStartRefresh')  # time at next scr refresh
        white_ball1.setAutoDraw(True)
    if white_ball1.status == STARTED:
        if frameN >= 250:
            # keep track of stop time/frame for later
            white_ball1.tStop = t  # not accounting for scr refresh
            white_ball1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(white_ball1, 'tStopRefresh')  # time at next scr refresh
            white_ball1.setAutoDraw(False)
    if white_ball1.status == STARTED:  # only update if drawing
        white_ball1.setPos([((-frameN*((window.innerWidth/2)*0.003))+ballpos), 0], log=False)
        white_ball1.setSize((8.5*ratio_pxpermm, 8.5*ratio_pxpermm), log=False)
    
    # *black_square3* updates
    if black_square3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        black_square3.frameNStart = frameN  # exact frame index
        black_square3.tStart = t  # local t and not account for scr refresh
        black_square3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(black_square3, 'tStartRefresh')  # time at next scr refresh
        black_square3.setAutoDraw(True)
    if black_square3.status == STARTED:  # only update if drawing
        black_square3.setPos(((window.innerWidth/2)*0.8,0), log=False)
    
    # *text_19* updates
    if text_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_19.frameNStart = frameN  # exact frame index
        text_19.tStart = t  # local t and not account for scr refresh
        text_19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_19, 'tStartRefresh')  # time at next scr refresh
        text_19.setAutoDraw(True)
    if text_19.status == STARTED:
        if frameN >= 250:
            # keep track of stop time/frame for later
            text_19.tStop = t  # not accounting for scr refresh
            text_19.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_19, 'tStopRefresh')  # time at next scr refresh
            text_19.setAutoDraw(False)
    
    # *text_20* updates
    if text_20.status == NOT_STARTED and frameN >= 250:
        # keep track of start time/frame for later
        text_20.frameNStart = frameN  # exact frame index
        text_20.tStart = t  # local t and not account for scr refresh
        text_20.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_20, 'tStartRefresh')  # time at next scr refresh
        text_20.setAutoDraw(True)
    if text_20.status == STARTED:
        if frameN >= 320:
            # keep track of stop time/frame for later
            text_20.tStop = t  # not accounting for scr refresh
            text_20.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_20, 'tStopRefresh')  # time at next scr refresh
            text_20.setAutoDraw(False)
    
    # *white_ball12* updates
    if white_ball12.status == NOT_STARTED and frameN >= 320:
        # keep track of start time/frame for later
        white_ball12.frameNStart = frameN  # exact frame index
        white_ball12.tStart = t  # local t and not account for scr refresh
        white_ball12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(white_ball12, 'tStartRefresh')  # time at next scr refresh
        white_ball12.setAutoDraw(True)
    if white_ball12.status == STARTED:
        if frameN >= 400:
            # keep track of stop time/frame for later
            white_ball12.tStop = t  # not accounting for scr refresh
            white_ball12.frameNStop = frameN  # exact frame index
            win.timeOnFlip(white_ball12, 'tStopRefresh')  # time at next scr refresh
            white_ball12.setAutoDraw(False)
    if white_ball12.status == STARTED:  # only update if drawing
        white_ball12.setPos([((-frameN*((window.innerWidth/2)*0.003))+((window.innerWidth/2)*0.05)), 0], log=False)
        white_ball12.setSize((8.5*ratio_pxpermm, 8.5*ratio_pxpermm), log=False)
    
    # *text_21* updates
    if text_21.status == NOT_STARTED and frameN >= 320:
        # keep track of start time/frame for later
        text_21.frameNStart = frameN  # exact frame index
        text_21.tStart = t  # local t and not account for scr refresh
        text_21.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_21, 'tStartRefresh')  # time at next scr refresh
        text_21.setAutoDraw(True)
    
    # *text_22* updates
    if text_22.status == NOT_STARTED and frameN >= 250:
        # keep track of start time/frame for later
        text_22.frameNStart = frameN  # exact frame index
        text_22.tStart = t  # local t and not account for scr refresh
        text_22.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_22, 'tStartRefresh')  # time at next scr refresh
        text_22.setAutoDraw(True)
    if text_22.status == STARTED:
        if frameN >= 320:
            # keep track of stop time/frame for later
            text_22.tStop = t  # not accounting for scr refresh
            text_22.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_22, 'tStopRefresh')  # time at next scr refresh
            text_22.setAutoDraw(False)
    
    # *white_ball13* updates
    if white_ball13.status == NOT_STARTED and frameN >= 400:
        # keep track of start time/frame for later
        white_ball13.frameNStart = frameN  # exact frame index
        white_ball13.tStart = t  # local t and not account for scr refresh
        white_ball13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(white_ball13, 'tStartRefresh')  # time at next scr refresh
        white_ball13.setAutoDraw(True)
    if white_ball13.status == STARTED:
        if frameN >= 550:
            # keep track of stop time/frame for later
            white_ball13.tStop = t  # not accounting for scr refresh
            white_ball13.frameNStop = frameN  # exact frame index
            win.timeOnFlip(white_ball13, 'tStopRefresh')  # time at next scr refresh
            white_ball13.setAutoDraw(False)
    if white_ball13.status == STARTED:  # only update if drawing
        white_ball13.setPos([(((-frameN+400)*((window.innerWidth/2)*0.003))+ballpos), 0], log=False)
        white_ball13.setSize((8.5*ratio_pxpermm, 8.5*ratio_pxpermm), log=False)
    if frameN == 550:
        continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in calibration_exampleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "calibration_example"-------
for thisComponent in calibration_exampleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('white_ball1.started', white_ball1.tStartRefresh)
thisExp.addData('white_ball1.stopped', white_ball1.tStopRefresh)
thisExp.addData('black_square3.started', black_square3.tStartRefresh)
thisExp.addData('black_square3.stopped', black_square3.tStopRefresh)
thisExp.addData('text_19.started', text_19.tStartRefresh)
thisExp.addData('text_19.stopped', text_19.tStopRefresh)
thisExp.addData('text_20.started', text_20.tStartRefresh)
thisExp.addData('text_20.stopped', text_20.tStopRefresh)
thisExp.addData('white_ball12.started', white_ball12.tStartRefresh)
thisExp.addData('white_ball12.stopped', white_ball12.tStopRefresh)
thisExp.addData('text_21.started', text_21.tStartRefresh)
thisExp.addData('text_21.stopped', text_21.tStopRefresh)
thisExp.addData('text_22.started', text_22.tStartRefresh)
thisExp.addData('text_22.stopped', text_22.tStopRefresh)
thisExp.addData('white_ball13.started', white_ball13.tStartRefresh)
thisExp.addData('white_ball13.stopped', white_ball13.tStopRefresh)
# the Routine "calibration_example" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr_12"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_13.keys = []
key_resp_13.rt = []
_key_resp_13_allKeys = []
# keep track of which components have finished
instr_12Components = [key_resp_13, space_12, instr_only_6, text_15]
for thisComponent in instr_12Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr_12Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr_12"-------
while continueRoutine:
    # get current time
    t = instr_12Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr_12Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_13* updates
    waitOnFlip = False
    if key_resp_13.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        key_resp_13.frameNStart = frameN  # exact frame index
        key_resp_13.tStart = t  # local t and not account for scr refresh
        key_resp_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_13, 'tStartRefresh')  # time at next scr refresh
        key_resp_13.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_13.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_13.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_13.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_13.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_13_allKeys.extend(theseKeys)
        if len(_key_resp_13_allKeys):
            key_resp_13.keys = _key_resp_13_allKeys[-1].name  # just the last key pressed
            key_resp_13.rt = _key_resp_13_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *space_12* updates
    if space_12.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        space_12.frameNStart = frameN  # exact frame index
        space_12.tStart = t  # local t and not account for scr refresh
        space_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_12, 'tStartRefresh')  # time at next scr refresh
        space_12.setAutoDraw(True)
    
    # *instr_only_6* updates
    if instr_only_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_only_6.frameNStart = frameN  # exact frame index
        instr_only_6.tStart = t  # local t and not account for scr refresh
        instr_only_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_only_6, 'tStartRefresh')  # time at next scr refresh
        instr_only_6.setAutoDraw(True)
    
    # *text_15* updates
    if text_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_15.frameNStart = frameN  # exact frame index
        text_15.tStart = t  # local t and not account for scr refresh
        text_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_15, 'tStartRefresh')  # time at next scr refresh
        text_15.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_12Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_12"-------
for thisComponent in instr_12Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_13.keys in ['', [], None]:  # No response was made
    key_resp_13.keys = None
thisExp.addData('key_resp_13.keys',key_resp_13.keys)
if key_resp_13.keys != None:  # we had a response
    thisExp.addData('key_resp_13.rt', key_resp_13.rt)
thisExp.addData('key_resp_13.started', key_resp_13.tStartRefresh)
thisExp.addData('key_resp_13.stopped', key_resp_13.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('space_12.started', space_12.tStartRefresh)
thisExp.addData('space_12.stopped', space_12.tStopRefresh)
thisExp.addData('instr_only_6.started', instr_only_6.tStartRefresh)
thisExp.addData('instr_only_6.stopped', instr_only_6.tStopRefresh)
thisExp.addData('text_15.started', text_15.tStartRefresh)
thisExp.addData('text_15.stopped', text_15.tStopRefresh)
# the Routine "instr_12" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=5, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "ball_calibration"-------
    continueRoutine = True
    # update component parameters for each repeat
    black_square2.setSize((8.5*ratio_pxpermm, 8.5*ratio_pxpermm))
    white_ball.setSize((8.5*ratio_pxpermm, 8.5*ratio_pxpermm))
    key_resp_19.keys = []
    key_resp_19.rt = []
    _key_resp_19_allKeys = []
    # Blindspot angle
    blindspot_angle = 13.5
    ballpos = (window.innerWidth/2)*0.75;
    # Convert radians to degrees
    radians_to_degrees = 57.2958
    calibrationcountext=f'{calibrationcount} of 5 angle calibrations complete'
    
    text_39.setText(calibrationcountext)
    white_ball1_2.setSize((8.5*ratio_pxpermm, 8.5*ratio_pxpermm))
    # keep track of which components have finished
    ball_calibrationComponents = [black_square2, white_ball, key_resp_19, text_39, white_ball1_2]
    for thisComponent in ball_calibrationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ball_calibrationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ball_calibration"-------
    while continueRoutine:
        # get current time
        t = ball_calibrationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ball_calibrationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *black_square2* updates
        if black_square2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            black_square2.frameNStart = frameN  # exact frame index
            black_square2.tStart = t  # local t and not account for scr refresh
            black_square2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(black_square2, 'tStartRefresh')  # time at next scr refresh
            black_square2.setAutoDraw(True)
        if black_square2.status == STARTED:  # only update if drawing
            black_square2.setPos((((window.innerWidth/2)*0.8),0), log=False)
        
        # *white_ball* updates
        if white_ball.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            white_ball.frameNStart = frameN  # exact frame index
            white_ball.tStart = t  # local t and not account for scr refresh
            white_ball.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(white_ball, 'tStartRefresh')  # time at next scr refresh
            white_ball.setAutoDraw(True)
        if white_ball.status == STARTED:
            if frameN >= 800:
                # keep track of stop time/frame for later
                white_ball.tStop = t  # not accounting for scr refresh
                white_ball.frameNStop = frameN  # exact frame index
                win.timeOnFlip(white_ball, 'tStopRefresh')  # time at next scr refresh
                white_ball.setAutoDraw(False)
        if white_ball.status == STARTED:  # only update if drawing
            white_ball.setPos([((-frameN*((window.innerWidth/2)*0.003))+ballpos), 0], log=False)
        
        # *key_resp_19* updates
        waitOnFlip = False
        if key_resp_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_19.frameNStart = frameN  # exact frame index
            key_resp_19.tStart = t  # local t and not account for scr refresh
            key_resp_19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_19, 'tStartRefresh')  # time at next scr refresh
            key_resp_19.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_19.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_19.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_19.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_19.getKeys(keyList=['return'], waitRelease=False)
            _key_resp_19_allKeys.extend(theseKeys)
            if len(_key_resp_19_allKeys):
                key_resp_19.keys = _key_resp_19_allKeys[-1].name  # just the last key pressed
                key_resp_19.rt = _key_resp_19_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *text_39* updates
        if text_39.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_39.frameNStart = frameN  # exact frame index
            text_39.tStart = t  # local t and not account for scr refresh
            text_39.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_39, 'tStartRefresh')  # time at next scr refresh
            text_39.setAutoDraw(True)
        
        # *white_ball1_2* updates
        if white_ball1_2.status == NOT_STARTED and frameN >= 800:
            # keep track of start time/frame for later
            white_ball1_2.frameNStart = frameN  # exact frame index
            white_ball1_2.tStart = t  # local t and not account for scr refresh
            white_ball1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(white_ball1_2, 'tStartRefresh')  # time at next scr refresh
            white_ball1_2.setAutoDraw(True)
        if white_ball1_2.status == STARTED:  # only update if drawing
            white_ball1_2.setPos([(((-frameN+800)*((window.innerWidth/2)*0.003))+ballpos), 0], log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ball_calibrationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ball_calibration"-------
    for thisComponent in ball_calibrationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('black_square2.started', black_square2.tStartRefresh)
    trials.addData('black_square2.stopped', black_square2.tStopRefresh)
    trials.addData('white_ball.started', white_ball.tStartRefresh)
    trials.addData('white_ball.stopped', white_ball.tStopRefresh)
    # check responses
    if key_resp_19.keys in ['', [], None]:  # No response was made
        key_resp_19.keys = None
    trials.addData('key_resp_19.keys',key_resp_19.keys)
    if key_resp_19.keys != None:  # we had a response
        trials.addData('key_resp_19.rt', key_resp_19.rt)
    trials.addData('key_resp_19.started', key_resp_19.tStartRefresh)
    trials.addData('key_resp_19.stopped', key_resp_19.tStopRefresh)
    # Final x position of white ball
    currentframe = frameN
    if currentframe < 800:
        ballposx = white_ball.pos[0]
    
    if currentframe >= 800:
        ballposx = white_ball1_2.pos[0]
    
    # X position of black square 
    squarepos = black_square2.pos[0]
    # Calulcate the distance from the screen for this calibration
    viewer_distance =  (((squarepos - ballposx))/ratio_pxpermm)/tan(blindspot_angle/radians_to_degrees)
    # Store the distance in a list 
    viewerdistancetotal.append(viewer_distance);
    # Calibration count 
    calibrationcount = calibrationcount + 1;
    
    thisExp.addData("ballposx", ballposx)
    thisExp.addData("viewer_distance", viewer_distance)
    trials.addData('text_39.started', text_39.tStartRefresh)
    trials.addData('text_39.stopped', text_39.tStopRefresh)
    trials.addData('white_ball1_2.started', white_ball1_2.tStartRefresh)
    trials.addData('white_ball1_2.stopped', white_ball1_2.tStopRefresh)
    # the Routine "ball_calibration" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 5 repeats of 'trials'


# ------Prepare to start Routine "viewerdistance"-------
continueRoutine = True
# update component parameters for each repeat
viewerdistancecm = round((sum(viewerdistancetotal)/50),3)
viewdistancetext=f'Your viewing distance is {viewerdistancecm} cm'


DVA_to_distance = (viewerdistancecm *tan(1/radians_to_degrees))*10;
radius_F = DVA_to_distance * ratio_pxpermm * radius_central; 
radius_P =  DVA_to_distance * ratio_pxpermm * radius_peripheral;
r_F =  DVA_to_distance * ratio_pxpermm * stimulus_size;
R_P =  peripheral_scale * r_F;
text_38.setText(viewdistancetext)
key_resp_20.keys = []
key_resp_20.rt = []
_key_resp_20_allKeys = []
# keep track of which components have finished
viewerdistanceComponents = [text_38, text_40, key_resp_20, space_20]
for thisComponent in viewerdistanceComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
viewerdistanceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "viewerdistance"-------
while continueRoutine:
    # get current time
    t = viewerdistanceClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=viewerdistanceClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    if viewerdistancecm*10 < distance_threshold:
        continueRoutine = False
    
    if screen_size_x < screen_x_threshold:
            continueRoutine = False
    
    
    # *text_38* updates
    if text_38.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_38.frameNStart = frameN  # exact frame index
        text_38.tStart = t  # local t and not account for scr refresh
        text_38.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_38, 'tStartRefresh')  # time at next scr refresh
        text_38.setAutoDraw(True)
    
    # *text_40* updates
    if text_40.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_40.frameNStart = frameN  # exact frame index
        text_40.tStart = t  # local t and not account for scr refresh
        text_40.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_40, 'tStartRefresh')  # time at next scr refresh
        text_40.setAutoDraw(True)
    
    # *key_resp_20* updates
    waitOnFlip = False
    if key_resp_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_20.frameNStart = frameN  # exact frame index
        key_resp_20.tStart = t  # local t and not account for scr refresh
        key_resp_20.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_20, 'tStartRefresh')  # time at next scr refresh
        key_resp_20.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_20.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_20.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_20.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_20.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_20_allKeys.extend(theseKeys)
        if len(_key_resp_20_allKeys):
            key_resp_20.keys = _key_resp_20_allKeys[-1].name  # just the last key pressed
            key_resp_20.rt = _key_resp_20_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *space_20* updates
    if space_20.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        space_20.frameNStart = frameN  # exact frame index
        space_20.tStart = t  # local t and not account for scr refresh
        space_20.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_20, 'tStartRefresh')  # time at next scr refresh
        space_20.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in viewerdistanceComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "viewerdistance"-------
for thisComponent in viewerdistanceComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData("viewerdistancecm", viewerdistancecm)
thisExp.addData("DVA_to_distance", DVA_to_distance)
thisExp.addData("radius_F", radius_F)
thisExp.addData("radius_P", radius_P)
thisExp.addData("r_F", r_F)
thisExp.addData("R_P", R_P)
thisExp.addData('text_38.started', text_38.tStartRefresh)
thisExp.addData('text_38.stopped', text_38.tStopRefresh)
thisExp.addData('text_40.started', text_40.tStartRefresh)
thisExp.addData('text_40.stopped', text_40.tStopRefresh)
# check responses
if key_resp_20.keys in ['', [], None]:  # No response was made
    key_resp_20.keys = None
thisExp.addData('key_resp_20.keys',key_resp_20.keys)
if key_resp_20.keys != None:  # we had a response
    thisExp.addData('key_resp_20.rt', key_resp_20.rt)
thisExp.addData('key_resp_20.started', key_resp_20.tStartRefresh)
thisExp.addData('key_resp_20.stopped', key_resp_20.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('space_20.started', space_20.tStartRefresh)
thisExp.addData('space_20.stopped', space_20.tStopRefresh)
# the Routine "viewerdistance" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "viewerdistance_unsucess"-------
continueRoutine = True
# update component parameters for each repeat
viewerdistancecm = round((sum(viewerdistancetotal)/50),3)
viewdistancetext=f'Your viewing distance is calculated as {viewerdistancecm} cm'

text_42.setText(viewdistancetext)
# keep track of which components have finished
viewerdistance_unsucessComponents = [text_41, text_42, text_43]
for thisComponent in viewerdistance_unsucessComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
viewerdistance_unsucessClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "viewerdistance_unsucess"-------
while continueRoutine:
    # get current time
    t = viewerdistance_unsucessClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=viewerdistance_unsucessClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    if viewerdistancecm*10 > distance_threshold and screen_size_x > screen_x_threshold:
        continueRoutine = False
    
    
    
    # *text_41* updates
    if text_41.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_41.frameNStart = frameN  # exact frame index
        text_41.tStart = t  # local t and not account for scr refresh
        text_41.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_41, 'tStartRefresh')  # time at next scr refresh
        text_41.setAutoDraw(True)
    
    # *text_42* updates
    if text_42.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_42.frameNStart = frameN  # exact frame index
        text_42.tStart = t  # local t and not account for scr refresh
        text_42.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_42, 'tStartRefresh')  # time at next scr refresh
        text_42.setAutoDraw(True)
    
    # *text_43* updates
    if text_43.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_43.frameNStart = frameN  # exact frame index
        text_43.tStart = t  # local t and not account for scr refresh
        text_43.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_43, 'tStartRefresh')  # time at next scr refresh
        text_43.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in viewerdistance_unsucessComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "viewerdistance_unsucess"-------
for thisComponent in viewerdistance_unsucessComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_41.started', text_41.tStartRefresh)
thisExp.addData('text_41.stopped', text_41.tStopRefresh)
thisExp.addData('text_42.started', text_42.tStartRefresh)
thisExp.addData('text_42.stopped', text_42.tStopRefresh)
thisExp.addData('text_43.started', text_43.tStartRefresh)
thisExp.addData('text_43.stopped', text_43.tStopRefresh)
# the Routine "viewerdistance_unsucess" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "stim1_instr"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_14.keys = []
key_resp_14.rt = []
_key_resp_14_allKeys = []
# keep track of which components have finished
stim1_instrComponents = [stim1, key_resp_14, space_13, text_16]
for thisComponent in stim1_instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
stim1_instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "stim1_instr"-------
while continueRoutine:
    # get current time
    t = stim1_instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=stim1_instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *stim1* updates
    if stim1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        stim1.frameNStart = frameN  # exact frame index
        stim1.tStart = t  # local t and not account for scr refresh
        stim1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(stim1, 'tStartRefresh')  # time at next scr refresh
        stim1.setAutoDraw(True)
    
    # *key_resp_14* updates
    if key_resp_14.status == NOT_STARTED and t >= 2-frameTolerance:
        # keep track of start time/frame for later
        key_resp_14.frameNStart = frameN  # exact frame index
        key_resp_14.tStart = t  # local t and not account for scr refresh
        key_resp_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_14, 'tStartRefresh')  # time at next scr refresh
        key_resp_14.status = STARTED
        # keyboard checking is just starting
        key_resp_14.clock.reset()  # now t=0
        key_resp_14.clearEvents(eventType='keyboard')
    if key_resp_14.status == STARTED:
        theseKeys = key_resp_14.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_14_allKeys.extend(theseKeys)
        if len(_key_resp_14_allKeys):
            key_resp_14.keys = _key_resp_14_allKeys[-1].name  # just the last key pressed
            key_resp_14.rt = _key_resp_14_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *space_13* updates
    if space_13.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        space_13.frameNStart = frameN  # exact frame index
        space_13.tStart = t  # local t and not account for scr refresh
        space_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_13, 'tStartRefresh')  # time at next scr refresh
        space_13.setAutoDraw(True)
    
    # *text_16* updates
    if text_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_16.frameNStart = frameN  # exact frame index
        text_16.tStart = t  # local t and not account for scr refresh
        text_16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_16, 'tStartRefresh')  # time at next scr refresh
        text_16.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in stim1_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "stim1_instr"-------
for thisComponent in stim1_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('stim1.started', stim1.tStartRefresh)
thisExp.addData('stim1.stopped', stim1.tStopRefresh)
# check responses
if key_resp_14.keys in ['', [], None]:  # No response was made
    key_resp_14.keys = None
thisExp.addData('key_resp_14.keys',key_resp_14.keys)
if key_resp_14.keys != None:  # we had a response
    thisExp.addData('key_resp_14.rt', key_resp_14.rt)
thisExp.addData('key_resp_14.started', key_resp_14.tStart)
thisExp.addData('key_resp_14.stopped', key_resp_14.tStop)
thisExp.nextEntry()
thisExp.addData('space_13.started', space_13.tStartRefresh)
thisExp.addData('space_13.stopped', space_13.tStopRefresh)
thisExp.addData('text_16.started', text_16.tStartRefresh)
thisExp.addData('text_16.stopped', text_16.tStopRefresh)
# the Routine "stim1_instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "stim_response_instr"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_15.keys = []
key_resp_15.rt = []
_key_resp_15_allKeys = []
# keep track of which components have finished
stim_response_instrComponents = [movie_2, key_resp_15, space_14, text_17]
for thisComponent in stim_response_instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
stim_response_instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "stim_response_instr"-------
while continueRoutine:
    # get current time
    t = stim_response_instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=stim_response_instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *movie_2* updates
    if movie_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        movie_2.frameNStart = frameN  # exact frame index
        movie_2.tStart = t  # local t and not account for scr refresh
        movie_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(movie_2, 'tStartRefresh')  # time at next scr refresh
        movie_2.setAutoDraw(True)
    
    # *key_resp_15* updates
    waitOnFlip = False
    if key_resp_15.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        key_resp_15.frameNStart = frameN  # exact frame index
        key_resp_15.tStart = t  # local t and not account for scr refresh
        key_resp_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_15, 'tStartRefresh')  # time at next scr refresh
        key_resp_15.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_15.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_15.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_15.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_15.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_15_allKeys.extend(theseKeys)
        if len(_key_resp_15_allKeys):
            key_resp_15.keys = _key_resp_15_allKeys[-1].name  # just the last key pressed
            key_resp_15.rt = _key_resp_15_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *space_14* updates
    if space_14.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        space_14.frameNStart = frameN  # exact frame index
        space_14.tStart = t  # local t and not account for scr refresh
        space_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_14, 'tStartRefresh')  # time at next scr refresh
        space_14.setAutoDraw(True)
    
    # *text_17* updates
    if text_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_17.frameNStart = frameN  # exact frame index
        text_17.tStart = t  # local t and not account for scr refresh
        text_17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_17, 'tStartRefresh')  # time at next scr refresh
        text_17.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in stim_response_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "stim_response_instr"-------
for thisComponent in stim_response_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('movie_2.started', movie_2.tStartRefresh)
thisExp.addData('movie_2.stopped', movie_2.tStopRefresh)
# check responses
if key_resp_15.keys in ['', [], None]:  # No response was made
    key_resp_15.keys = None
thisExp.addData('key_resp_15.keys',key_resp_15.keys)
if key_resp_15.keys != None:  # we had a response
    thisExp.addData('key_resp_15.rt', key_resp_15.rt)
thisExp.addData('key_resp_15.started', key_resp_15.tStartRefresh)
thisExp.addData('key_resp_15.stopped', key_resp_15.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('space_14.started', space_14.tStartRefresh)
thisExp.addData('space_14.stopped', space_14.tStopRefresh)
thisExp.addData('text_17.started', text_17.tStartRefresh)
thisExp.addData('text_17.stopped', text_17.tStopRefresh)
# the Routine "stim_response_instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "catch_insrt"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_17.keys = []
key_resp_17.rt = []
_key_resp_17_allKeys = []
# keep track of which components have finished
catch_insrtComponents = [space_15, key_resp_17, movie_3, text_18]
for thisComponent in catch_insrtComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
catch_insrtClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "catch_insrt"-------
while continueRoutine:
    # get current time
    t = catch_insrtClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=catch_insrtClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *space_15* updates
    if space_15.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        space_15.frameNStart = frameN  # exact frame index
        space_15.tStart = t  # local t and not account for scr refresh
        space_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_15, 'tStartRefresh')  # time at next scr refresh
        space_15.setAutoDraw(True)
    
    # *key_resp_17* updates
    waitOnFlip = False
    if key_resp_17.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        key_resp_17.frameNStart = frameN  # exact frame index
        key_resp_17.tStart = t  # local t and not account for scr refresh
        key_resp_17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_17, 'tStartRefresh')  # time at next scr refresh
        key_resp_17.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_17.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_17.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_17.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_17.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        _key_resp_17_allKeys.extend(theseKeys)
        if len(_key_resp_17_allKeys):
            key_resp_17.keys = _key_resp_17_allKeys[-1].name  # just the last key pressed
            key_resp_17.rt = _key_resp_17_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *movie_3* updates
    if movie_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        movie_3.frameNStart = frameN  # exact frame index
        movie_3.tStart = t  # local t and not account for scr refresh
        movie_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(movie_3, 'tStartRefresh')  # time at next scr refresh
        movie_3.setAutoDraw(True)
    
    # *text_18* updates
    if text_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_18.frameNStart = frameN  # exact frame index
        text_18.tStart = t  # local t and not account for scr refresh
        text_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_18, 'tStartRefresh')  # time at next scr refresh
        text_18.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in catch_insrtComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "catch_insrt"-------
for thisComponent in catch_insrtComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('space_15.started', space_15.tStartRefresh)
thisExp.addData('space_15.stopped', space_15.tStopRefresh)
# check responses
if key_resp_17.keys in ['', [], None]:  # No response was made
    key_resp_17.keys = None
thisExp.addData('key_resp_17.keys',key_resp_17.keys)
if key_resp_17.keys != None:  # we had a response
    thisExp.addData('key_resp_17.rt', key_resp_17.rt)
thisExp.addData('key_resp_17.started', key_resp_17.tStartRefresh)
thisExp.addData('key_resp_17.stopped', key_resp_17.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('movie_3.started', movie_3.tStartRefresh)
thisExp.addData('movie_3.stopped', movie_3.tStopRefresh)
thisExp.addData('text_18.started', text_18.tStartRefresh)
thisExp.addData('text_18.stopped', text_18.tStopRefresh)
# the Routine "catch_insrt" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "colour_circle_instr_2"-------
continueRoutine = True
# update component parameters for each repeat
# Randomly place instruction circles 
circle_position = [[(- 230), 230], [0, 230], [230, 230], [(- 230), 0], [0, 0], [230, 0], [230, (- 230)], [0, (- 230)], [(-230), (- 230)]];
shuffle(circle_position)


key_resp_9.keys = []
key_resp_9.rt = []
_key_resp_9_allKeys = []
intructioncircle_1.setPos(circle_position[1])
instructioncircle_2.setPos(circle_position[2])
instructioncircle_3.setPos(circle_position[3])
instructioncircle_4.setPos(circle_position[4])
instructioncircle_5.setPos(circle_position[5])
insturctioncircle_6.setPos(circle_position[6])
instructioncircle_7.setPos(circle_position[7])
instructioncircle_8.setPos(circle_position[8])
instructioncircle_9.setPos(circle_position[0])
# keep track of which components have finished
colour_circle_instr_2Components = [key_resp_9, intructioncircle_1, instructioncircle_2, instructioncircle_3, instructioncircle_4, instructioncircle_5, insturctioncircle_6, instructioncircle_7, instructioncircle_8, instructioncircle_9, space_9, text_9]
for thisComponent in colour_circle_instr_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
colour_circle_instr_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "colour_circle_instr_2"-------
while continueRoutine:
    # get current time
    t = colour_circle_instr_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=colour_circle_instr_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_9* updates
    waitOnFlip = False
    if key_resp_9.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.tStart = t  # local t and not account for scr refresh
        key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_9.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_9.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_9_allKeys.extend(theseKeys)
        if len(_key_resp_9_allKeys):
            key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
            key_resp_9.rt = _key_resp_9_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *intructioncircle_1* updates
    if intructioncircle_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intructioncircle_1.frameNStart = frameN  # exact frame index
        intructioncircle_1.tStart = t  # local t and not account for scr refresh
        intructioncircle_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intructioncircle_1, 'tStartRefresh')  # time at next scr refresh
        intructioncircle_1.setAutoDraw(True)
    
    # *instructioncircle_2* updates
    if instructioncircle_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructioncircle_2.frameNStart = frameN  # exact frame index
        instructioncircle_2.tStart = t  # local t and not account for scr refresh
        instructioncircle_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructioncircle_2, 'tStartRefresh')  # time at next scr refresh
        instructioncircle_2.setAutoDraw(True)
    
    # *instructioncircle_3* updates
    if instructioncircle_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructioncircle_3.frameNStart = frameN  # exact frame index
        instructioncircle_3.tStart = t  # local t and not account for scr refresh
        instructioncircle_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructioncircle_3, 'tStartRefresh')  # time at next scr refresh
        instructioncircle_3.setAutoDraw(True)
    
    # *instructioncircle_4* updates
    if instructioncircle_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructioncircle_4.frameNStart = frameN  # exact frame index
        instructioncircle_4.tStart = t  # local t and not account for scr refresh
        instructioncircle_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructioncircle_4, 'tStartRefresh')  # time at next scr refresh
        instructioncircle_4.setAutoDraw(True)
    
    # *instructioncircle_5* updates
    if instructioncircle_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructioncircle_5.frameNStart = frameN  # exact frame index
        instructioncircle_5.tStart = t  # local t and not account for scr refresh
        instructioncircle_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructioncircle_5, 'tStartRefresh')  # time at next scr refresh
        instructioncircle_5.setAutoDraw(True)
    
    # *insturctioncircle_6* updates
    if insturctioncircle_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        insturctioncircle_6.frameNStart = frameN  # exact frame index
        insturctioncircle_6.tStart = t  # local t and not account for scr refresh
        insturctioncircle_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(insturctioncircle_6, 'tStartRefresh')  # time at next scr refresh
        insturctioncircle_6.setAutoDraw(True)
    
    # *instructioncircle_7* updates
    if instructioncircle_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructioncircle_7.frameNStart = frameN  # exact frame index
        instructioncircle_7.tStart = t  # local t and not account for scr refresh
        instructioncircle_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructioncircle_7, 'tStartRefresh')  # time at next scr refresh
        instructioncircle_7.setAutoDraw(True)
    
    # *instructioncircle_8* updates
    if instructioncircle_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructioncircle_8.frameNStart = frameN  # exact frame index
        instructioncircle_8.tStart = t  # local t and not account for scr refresh
        instructioncircle_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructioncircle_8, 'tStartRefresh')  # time at next scr refresh
        instructioncircle_8.setAutoDraw(True)
    
    # *instructioncircle_9* updates
    if instructioncircle_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructioncircle_9.frameNStart = frameN  # exact frame index
        instructioncircle_9.tStart = t  # local t and not account for scr refresh
        instructioncircle_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructioncircle_9, 'tStartRefresh')  # time at next scr refresh
        instructioncircle_9.setAutoDraw(True)
    
    # *space_9* updates
    if space_9.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        space_9.frameNStart = frameN  # exact frame index
        space_9.tStart = t  # local t and not account for scr refresh
        space_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_9, 'tStartRefresh')  # time at next scr refresh
        space_9.setAutoDraw(True)
    
    # *text_9* updates
    if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_9.frameNStart = frameN  # exact frame index
        text_9.tStart = t  # local t and not account for scr refresh
        text_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
        text_9.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in colour_circle_instr_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "colour_circle_instr_2"-------
for thisComponent in colour_circle_instr_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_9.keys in ['', [], None]:  # No response was made
    key_resp_9.keys = None
thisExp.addData('key_resp_9.keys',key_resp_9.keys)
if key_resp_9.keys != None:  # we had a response
    thisExp.addData('key_resp_9.rt', key_resp_9.rt)
thisExp.addData('key_resp_9.started', key_resp_9.tStartRefresh)
thisExp.addData('key_resp_9.stopped', key_resp_9.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('intructioncircle_1.started', intructioncircle_1.tStartRefresh)
thisExp.addData('intructioncircle_1.stopped', intructioncircle_1.tStopRefresh)
thisExp.addData('instructioncircle_2.started', instructioncircle_2.tStartRefresh)
thisExp.addData('instructioncircle_2.stopped', instructioncircle_2.tStopRefresh)
thisExp.addData('instructioncircle_3.started', instructioncircle_3.tStartRefresh)
thisExp.addData('instructioncircle_3.stopped', instructioncircle_3.tStopRefresh)
thisExp.addData('instructioncircle_4.started', instructioncircle_4.tStartRefresh)
thisExp.addData('instructioncircle_4.stopped', instructioncircle_4.tStopRefresh)
thisExp.addData('instructioncircle_5.started', instructioncircle_5.tStartRefresh)
thisExp.addData('instructioncircle_5.stopped', instructioncircle_5.tStopRefresh)
thisExp.addData('insturctioncircle_6.started', insturctioncircle_6.tStartRefresh)
thisExp.addData('insturctioncircle_6.stopped', insturctioncircle_6.tStopRefresh)
thisExp.addData('instructioncircle_7.started', instructioncircle_7.tStartRefresh)
thisExp.addData('instructioncircle_7.stopped', instructioncircle_7.tStopRefresh)
thisExp.addData('instructioncircle_8.started', instructioncircle_8.tStartRefresh)
thisExp.addData('instructioncircle_8.stopped', instructioncircle_8.tStopRefresh)
thisExp.addData('instructioncircle_9.started', instructioncircle_9.tStartRefresh)
thisExp.addData('instructioncircle_9.stopped', instructioncircle_9.tStopRefresh)
thisExp.addData('space_9.started', space_9.tStartRefresh)
thisExp.addData('space_9.stopped', space_9.tStopRefresh)
thisExp.addData('text_9.started', text_9.tStartRefresh)
thisExp.addData('text_9.stopped', text_9.tStopRefresh)
# the Routine "colour_circle_instr_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr_prac"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_10.keys = []
key_resp_10.rt = []
_key_resp_10_allKeys = []
# keep track of which components have finished
instr_pracComponents = [space_10, text_10, key_resp_10]
for thisComponent in instr_pracComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr_pracClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr_prac"-------
while continueRoutine:
    # get current time
    t = instr_pracClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr_pracClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *space_10* updates
    if space_10.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        space_10.frameNStart = frameN  # exact frame index
        space_10.tStart = t  # local t and not account for scr refresh
        space_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_10, 'tStartRefresh')  # time at next scr refresh
        space_10.setAutoDraw(True)
    
    # *text_10* updates
    if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_10.frameNStart = frameN  # exact frame index
        text_10.tStart = t  # local t and not account for scr refresh
        text_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
        text_10.setAutoDraw(True)
    
    # *key_resp_10* updates
    waitOnFlip = False
    if key_resp_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_10.frameNStart = frameN  # exact frame index
        key_resp_10.tStart = t  # local t and not account for scr refresh
        key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
        key_resp_10.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_10.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_10.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_10_allKeys.extend(theseKeys)
        if len(_key_resp_10_allKeys):
            key_resp_10.keys = _key_resp_10_allKeys[-1].name  # just the last key pressed
            key_resp_10.rt = _key_resp_10_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_pracComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_prac"-------
for thisComponent in instr_pracComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('space_10.started', space_10.tStartRefresh)
thisExp.addData('space_10.stopped', space_10.tStopRefresh)
thisExp.addData('text_10.started', text_10.tStartRefresh)
thisExp.addData('text_10.stopped', text_10.tStopRefresh)
# check responses
if key_resp_10.keys in ['', [], None]:  # No response was made
    key_resp_10.keys = None
thisExp.addData('key_resp_10.keys',key_resp_10.keys)
if key_resp_10.keys != None:  # we had a response
    thisExp.addData('key_resp_10.rt', key_resp_10.rt)
thisExp.addData('key_resp_10.started', key_resp_10.tStartRefresh)
thisExp.addData('key_resp_10.stopped', key_resp_10.tStopRefresh)
thisExp.nextEntry()
# the Routine "instr_prac" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
duringprac = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('practrials.xlsx', selection='0:7'),
    seed=None, name='duringprac')
thisExp.addLoop(duringprac)  # add the loop to the experiment
thisDuringprac = duringprac.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisDuringprac.rgb)
if thisDuringprac != None:
    for paramName in thisDuringprac:
        exec('{} = thisDuringprac[paramName]'.format(paramName))

for thisDuringprac in duringprac:
    currentLoop = duringprac
    # abbreviate parameter names if possible (e.g. rgb = thisDuringprac.rgb)
    if thisDuringprac != None:
        for paramName in thisDuringprac:
            exec('{} = thisDuringprac[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Stim1_display_prac"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # Circle position and size 
    
    # Set up angle placement
    angle_1 = randint(-30,30);
    angle_2 = angle_1 + 180;
    
    x = 1
    y = 1
    
    theta_1 = (angle_1)*(pi/180)
    theta_2 = (angle_2)*(pi/180)
    
    deltax_1 = radius_F*cos(theta_1)
    deltay_1 = radius_F*sin(theta_1)
    deltax_2 = radius_P*cos(theta_2)
    deltay_2 = radius_P*sin(theta_2)
    
    
    a_1 = x + deltax_1
    b_1 = y + deltay_1
    a_2 = x + deltax_2
    b_2 = y + deltay_2
    
    
    # Set circle position 
    if Ecc == 'FF':
        circle1posx = a_1;
        circle1posy = b_1;
        circlesizeh = 2 *r_F;
        circlesizew = 2 * r_F;
    elif Ecc == 'PF':
            circle1posx = a_2;
            circle1posy = b_2;
            circlesizeh = 2 * R_P;
            circlesizew = 2 * R_P;
    
    # Randomly select circle colour
    
    Colour_1 = randint(1,9);
    
    # Set circle colour
    if Colour_1 == 1:
        Circle1_col = (1, -1, -1);
    elif Colour_1 == 2:
        Circle1_col = (1, 0.33, -1);
    elif Colour_1 == 3:
        Circle1_col = (0.32, 1, -1);
    elif Colour_1 == 4:
        Circle1_col = (-1, 1, -1);
    elif Colour_1 == 5:
        Circle1_col = (-1, 1, 0.33);
    elif Colour_1 == 6:
        Circle1_col = (-1, 0.32, 1);
    elif Colour_1 == 7:
        Circle1_col = (-1, -1, 1);
    elif Colour_1 == 8:
        Circle1_col = (0.33, -1, 1);
    elif Colour_1 == 9:
        Circle1_col = (1, -1, 0.33);
    
    Circle.setPos((circle1posx,circle1posy))
    Circle.setSize((circlesizew,circlesizeh))
    Circle.setFillColor(Circle1_col)
    Circle.setLineColor(Circle1_col)
    # keep track of which components have finished
    Stim1_display_pracComponents = [Circle, centre_cross4_2]
    for thisComponent in Stim1_display_pracComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Stim1_display_pracClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Stim1_display_prac"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Stim1_display_pracClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Stim1_display_pracClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Circle* updates
        if Circle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Circle.frameNStart = frameN  # exact frame index
            Circle.tStart = t  # local t and not account for scr refresh
            Circle.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Circle, 'tStartRefresh')  # time at next scr refresh
            Circle.setAutoDraw(True)
        if Circle.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Circle.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                Circle.tStop = t  # not accounting for scr refresh
                Circle.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Circle, 'tStopRefresh')  # time at next scr refresh
                Circle.setAutoDraw(False)
        
        # *centre_cross4_2* updates
        if centre_cross4_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            centre_cross4_2.frameNStart = frameN  # exact frame index
            centre_cross4_2.tStart = t  # local t and not account for scr refresh
            centre_cross4_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(centre_cross4_2, 'tStartRefresh')  # time at next scr refresh
            centre_cross4_2.setAutoDraw(True)
        if centre_cross4_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > centre_cross4_2.tStartRefresh + 0.500-frameTolerance:
                # keep track of stop time/frame for later
                centre_cross4_2.tStop = t  # not accounting for scr refresh
                centre_cross4_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(centre_cross4_2, 'tStopRefresh')  # time at next scr refresh
                centre_cross4_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Stim1_display_pracComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Stim1_display_prac"-------
    for thisComponent in Stim1_display_pracComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData("Colour_1", Colour_1);
    thisExp.addData("Ecc", Ecc);
    
    duringprac.addData('Circle.started', Circle.tStartRefresh)
    duringprac.addData('Circle.stopped', Circle.tStopRefresh)
    duringprac.addData('centre_cross4_2.started', centre_cross4_2.tStartRefresh)
    duringprac.addData('centre_cross4_2.stopped', centre_cross4_2.tStopRefresh)
    
    # ------Prepare to start Routine "response_prac"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_5
    mouse_5.clicked_name = []
    gotValidClick = False  # until a click is received
    
    event.clearEvents()
    
    # Count trial numbers
    
    pracnumber =  pracnumber + 1;
    
    # Randomly select circle colour
    
    Colour_2 = randint(1,9);
    
    # Set circle colour
    if Colour_2 == 1:
        Circle2_col = (1, -1, -1);
    elif Colour_2 == 2:
        Circle2_col = (1, 0.33, -1);
    elif Colour_2 == 3:
        Circle2_col = (0.32, 1, -1);
    elif Colour_2 == 4:
        Circle2_col = (-1, 1, -1);
    elif Colour_2 == 5:
        Circle2_col = (-1, 1, 0.33);
    elif Colour_2 == 6:
        Circle2_col = (-1, 0.32, 1);
    elif Colour_2 == 7:
        Circle2_col = (-1, -1, 1);
    elif Colour_2 == 8:
        Circle2_col = (0.33, -1, 1);
    elif Colour_2 == 9:
        Circle2_col = (1, -1, 0.33);
    
    
    
    Circle_3.setSize((15*ratio_pxpermm, 15*ratio_pxpermm))
    Circle_3.setFillColor(Circle2_col)
    Circle_3.setLineColor(Circle2_col)
    # keep track of which components have finished
    response_pracComponents = [mouse_5, response1disk_5, response3disk_5, response5disk_5, response7disk_5, Circle_3, text_29]
    for thisComponent in response_pracComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    response_pracClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "response_prac"-------
    while continueRoutine:
        # get current time
        t = response_pracClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=response_pracClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *mouse_5* updates
        if mouse_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            mouse_5.frameNStart = frameN  # exact frame index
            mouse_5.tStart = t  # local t and not account for scr refresh
            mouse_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_5, 'tStartRefresh')  # time at next scr refresh
            mouse_5.status = STARTED
            mouse_5.mouseClock.reset()
            prevButtonState = mouse_5.getPressed()  # if button is down already this ISN'T a new click
        if mouse_5.status == STARTED:  # only update if started and not finished!
            buttons = mouse_5.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [response1disk_5,response3disk_5,response5disk_5,response7disk_5,]:
                        if obj.contains(mouse_5):
                            gotValidClick = True
                            mouse_5.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        # Similarity for feedback
        mousexpos=mouse.getPos()[0]  # get x position of mouse
        mouseypos=mouse.getPos()[1]  # get y position of mouse
        
        # Triangle 7     
        x11d = a - b/2;
        y11d = a + b/2;
        x12d = a + b/2;
        y12d = a + b/2;
        x13d = a - b/2;
        y13d = a - b/2;
        a1d = ((y12d - y13d)*(mousexpos - x13d) + (x13d - x12d)*(mouseypos - y13d)) / ((y12d - y13d)*(x11d - x13d)+(x13d - x12d)*(y11d - y13d))
        b1d = ((y13d - y11d)*(mousexpos - x13d) + (x11d - x13d)*(mouseypos - y13d)) / ((y12d - y13d)*(x11d - x13d)+(x13d - x12d)*(y11d - y13d))
        c1d = 1 - a1d - b1d;
        
        # Triangle 6 
        x21d = a - b/2;
        y21d = a - b/2
        x22d = a + b/2
        y22d = a + b/2
        x23d = a + b/2
        y23d = a - b/2
        a2d = ((y22d - y23d)*(mousexpos - x23d) + (x23d - x22d)*(mouseypos - y23d)) / ((y22d - y23d)*(x21d - x23d)+(x23d - x22d)*(y21d - y23d))
        b2d = ((y23d - y21d)*(mousexpos - x23d) + (x21d - x23d)*(mouseypos - y23d)) / ((y22d - y23d)*(x21d - x23d)+(x23d - x22d)*(y21d - y23d))
        c2d = 1 - a2d - b2d
        
        # Triangle 5
        x31d = a - b/2
        y31d = -(a - b/2)
        x32d = a + b/2
        y32d = -(a - b/2) 
        x33d = a + b/2
        y33d = -(a + b/2)
        a3d = ((y32d - y33d)*(mousexpos - x33d) + (x33d - x32d)*(mouseypos - y33d)) / ((y32d - y33d)*(x31d - x33d)+(x33d - x32d)*(y31d - y33d))
        b3d = ((y33d - y31d)*(mousexpos - x33d) + (x31d - x33d)*(mouseypos - y33d)) / ((y32d - y33d)*(x31d - x33d)+(x33d - x32d)*(y31d - y33d))
        c3d = 1 - a3d - b3d
        
        
        # Triangle 4 
        x41d = a - b/2
        y41d = -(a - b/2)
        x42d = a + b/2
        y42d = -(a + b/2)
        x43d = a - b/2
        y43d = -(a + b/2)
        a4d = ((y42d - y43d)*(mousexpos - x43d) + (x43d - x42d)*(mouseypos - y43d)) / ((y42d - y43d)*(x41d - x43d)+(x43d - x42d)*(y41d - y43d))
        b4d = ((y43d - y41d)*(mousexpos - x43d) + (x41d - x43d)*(mouseypos - y43d)) / ((y42d - y43d)*(x41d - x43d)+(x43d - x42d)*(y41d - y43d))
        c4d = 1 - a4d - b4d
        
        #  Triangle 3
        x51d = -(a + b/2)
        y51d = -(a + b/2)
        x52d = -(a - b/2)
        y52d = -(a - b/2)
        x53d = -(a - b/2)
        y53d = -(a + b/2)
        a5d = ((y52d - y53d)*(mousexpos - x53d) + (x53d - x52d)*(mouseypos - y53d)) / ((y52d - y53d)*(x51d - x53d)+(x53d - x52d)*(y51d - y53d))
        b5d = ((y53d - y51d)*(mousexpos - x53d) + (x51d - x53d)*(mouseypos - y53d)) / ((y52d - y53d)*(x51d - x53d)+(x53d - x52d)*(y51d - y53d))
        c5d = 1 - a5d - b5d
        
        # Triangle 2
        x61d = -(a+b/2)
        y61d = -(a-b/2)
        x62d = -(a-b/2)
        y62d = -(a-b/2)
        x63d = -(a+b/2)
        y63d = - (a+b/2)
        a6d = ((y62d - y63d)*(mousexpos - x63d) + (x63d - x62d)*(mouseypos - y63d)) / ((y62d - y63d)*(x61d - x63d)+(x63d - x62d)*(y61d - y63d))
        b6d = ((y63d - y61d)*(mousexpos - x63d) + (x61d - x63d)*(mouseypos - y63d)) / ((y62d - y63d)*(x61d - x63d)+(x63d - x62d)*(y61d - y63d))
        c6d = 1 - a6d - b6d
        
        # Triangle 1 
        
        x71d = -(a + b/2)
        y71d = a + b/2
        x72d = -(a - b/2)
        y72d = a - b/2
        x73d = -(a + b/2)
        y73d = a - b/2
        a7d = ((y72d - y73d)*(mousexpos - x73d) + (x73d - x72d)*(mouseypos - y73d)) / ((y72d - y73d)*(x71d - x73d)+(x73d - x72d)*(y71d - y73d))
        b7d = ((y73d - y71d)*(mousexpos - x73d) + (x71d - x73d)*(mouseypos - y73d)) / ((y72d - y73d)*(x71d - x73d)+(x73d - x72d)*(y71d - y73d))
        c7d = 1 - a7d - b7d
        
        
        # Triangle 0 
        x81d = -(a + b/2)
        y81d = a + b/2
        x82d = -(a - b/2)
        y82d = a + b/2
        x83d = -(a - b/2)
        y83d = a - b/2
        a8d = ((y82d - y83d)*(mousexpos - x83d) + (x83d - x82d)*(mouseypos - y83d)) / ((y82d - y83d)*(x81d - x83d)+(x83d - x82d)*(y81d - y83d))
        b8d = ((y83d - y81d)*(mousexpos - x83d) + (x81d - x83d)*(mouseypos - y83d)) / ((y82d - y83d)*(x81d - x83d)+(x83d - x82d)*(y81d - y83d))
        c8d = 1 - a8d - b8d
        
        
        if (0 <= a1d <= 1) and (0 <= b1d <= 1) and (0 <= c1d <= 1):
            similarity = 7
            responsenumber = 7 
        elif (0 <= a2d <= 1) and (0 <= b2d <= 1) and (0 <= c2d <= 1):
            similarity = 6
            responsenumber = 6
        elif (0 <= a3d <= 1) and (0 <= b3d <= 1) and (0 <= c3d <= 1):
            similarity = 5
            responsenumber = 5
        elif (0 <= a4d <= 1) and (0 <= b4d <= 1) and (0 <= c4d <= 1):
            similarity = 4
            responsenumber = 4
        elif (0 <= a5d <= 1) and (0 <= b5d <= 1) and (0 <= c5d <= 1):
            similarity = 3
            responsenumber = 3
        elif (0 <= a6d <= 1) and (0 <= b6d <= 1) and (0 <= c6d <= 1):
            similarity = 2
            responsenumber = 2
        elif (0 <= a7d <= 1) and (0 <= b7d <= 1) and (0 <= c7d <= 1):
            similarity = 1
            responsenumber = 1
        elif (0 <= a8d <= 1) and (0 <= b8d <= 1) and (0 <= c8d <= 1):
            similarity = 0
            responsenumber = 0
        
        # *response1disk_5* updates
        if response1disk_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response1disk_5.frameNStart = frameN  # exact frame index
            response1disk_5.tStart = t  # local t and not account for scr refresh
            response1disk_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response1disk_5, 'tStartRefresh')  # time at next scr refresh
            response1disk_5.setAutoDraw(True)
        
        # *response3disk_5* updates
        if response3disk_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response3disk_5.frameNStart = frameN  # exact frame index
            response3disk_5.tStart = t  # local t and not account for scr refresh
            response3disk_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response3disk_5, 'tStartRefresh')  # time at next scr refresh
            response3disk_5.setAutoDraw(True)
        
        # *response5disk_5* updates
        if response5disk_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response5disk_5.frameNStart = frameN  # exact frame index
            response5disk_5.tStart = t  # local t and not account for scr refresh
            response5disk_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response5disk_5, 'tStartRefresh')  # time at next scr refresh
            response5disk_5.setAutoDraw(True)
        
        # *response7disk_5* updates
        if response7disk_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response7disk_5.frameNStart = frameN  # exact frame index
            response7disk_5.tStart = t  # local t and not account for scr refresh
            response7disk_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response7disk_5, 'tStartRefresh')  # time at next scr refresh
            response7disk_5.setAutoDraw(True)
        
        # *Circle_3* updates
        if Circle_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Circle_3.frameNStart = frameN  # exact frame index
            Circle_3.tStart = t  # local t and not account for scr refresh
            Circle_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Circle_3, 'tStartRefresh')  # time at next scr refresh
            Circle_3.setAutoDraw(True)
        
        # *text_29* updates
        if text_29.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_29.frameNStart = frameN  # exact frame index
            text_29.tStart = t  # local t and not account for scr refresh
            text_29.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_29, 'tStartRefresh')  # time at next scr refresh
            text_29.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in response_pracComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "response_prac"-------
    for thisComponent in response_pracComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for duringprac (TrialHandler)
    x, y = mouse_5.getPos()
    buttons = mouse_5.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        for obj in [response1disk_5,response3disk_5,response5disk_5,response7disk_5,]:
            if obj.contains(mouse_5):
                gotValidClick = True
                mouse_5.clicked_name.append(obj.name)
    duringprac.addData('mouse_5.x', x)
    duringprac.addData('mouse_5.y', y)
    duringprac.addData('mouse_5.leftButton', buttons[0])
    duringprac.addData('mouse_5.midButton', buttons[1])
    duringprac.addData('mouse_5.rightButton', buttons[2])
    if len(mouse_5.clicked_name):
        duringprac.addData('mouse_5.clicked_name', mouse_5.clicked_name[0])
    duringprac.addData('mouse_5.started', mouse_5.tStartRefresh)
    duringprac.addData('mouse_5.stopped', mouse_5.tStopRefresh)
    # Save similarity rating 
    mousexpos=mouse.getPos()[0]  # get x position of mouse
    mouseypos=mouse.getPos()[1]  # get y position of mouse
    
    # Triangle 7     
    x11d = a - b/2;
    y11d = a + b/2;
    x12d = a + b/2;
    y12d = a + b/2;
    x13d = a - b/2;
    y13d = a - b/2;
    a1d = ((y12d - y13d)*(mousexpos - x13d) + (x13d - x12d)*(mouseypos - y13d)) / ((y12d - y13d)*(x11d - x13d)+(x13d - x12d)*(y11d - y13d))
    b1d = ((y13d - y11d)*(mousexpos - x13d) + (x11d - x13d)*(mouseypos - y13d)) / ((y12d - y13d)*(x11d - x13d)+(x13d - x12d)*(y11d - y13d))
    c1d = 1 - a1d - b1d;
    
    # Triangle 6 
    x21d = a - b/2;
    y21d = a - b/2
    x22d = a + b/2
    y22d = a + b/2
    x23d = a + b/2
    y23d = a - b/2
    a2d = ((y22d - y23d)*(mousexpos - x23d) + (x23d - x22d)*(mouseypos - y23d)) / ((y22d - y23d)*(x21d - x23d)+(x23d - x22d)*(y21d - y23d))
    b2d = ((y23d - y21d)*(mousexpos - x23d) + (x21d - x23d)*(mouseypos - y23d)) / ((y22d - y23d)*(x21d - x23d)+(x23d - x22d)*(y21d - y23d))
    c2d = 1 - a2d - b2d
    
    # Triangle 5
    x31d = a - b/2
    y31d = -(a - b/2)
    x32d = a + b/2
    y32d = -(a - b/2) 
    x33d = a + b/2
    y33d = -(a + b/2)
    a3d = ((y32d - y33d)*(mousexpos - x33d) + (x33d - x32d)*(mouseypos - y33d)) / ((y32d - y33d)*(x31d - x33d)+(x33d - x32d)*(y31d - y33d))
    b3d = ((y33d - y31d)*(mousexpos - x33d) + (x31d - x33d)*(mouseypos - y33d)) / ((y32d - y33d)*(x31d - x33d)+(x33d - x32d)*(y31d - y33d))
    c3d = 1 - a3d - b3d
    
    
    # Triangle 4 
    x41d = a - b/2
    y41d = -(a - b/2)
    x42d = a + b/2
    y42d = -(a + b/2)
    x43d = a - b/2
    y43d = -(a + b/2)
    a4d = ((y42d - y43d)*(mousexpos - x43d) + (x43d - x42d)*(mouseypos - y43d)) / ((y42d - y43d)*(x41d - x43d)+(x43d - x42d)*(y41d - y43d))
    b4d = ((y43d - y41d)*(mousexpos - x43d) + (x41d - x43d)*(mouseypos - y43d)) / ((y42d - y43d)*(x41d - x43d)+(x43d - x42d)*(y41d - y43d))
    c4d = 1 - a4d - b4d
    
    #  Triangle 3
    x51d = -(a + b/2)
    y51d = -(a + b/2)
    x52d = -(a - b/2)
    y52d = -(a - b/2)
    x53d = -(a - b/2)
    y53d = -(a + b/2)
    a5d = ((y52d - y53d)*(mousexpos - x53d) + (x53d - x52d)*(mouseypos - y53d)) / ((y52d - y53d)*(x51d - x53d)+(x53d - x52d)*(y51d - y53d))
    b5d = ((y53d - y51d)*(mousexpos - x53d) + (x51d - x53d)*(mouseypos - y53d)) / ((y52d - y53d)*(x51d - x53d)+(x53d - x52d)*(y51d - y53d))
    c5d = 1 - a5d - b5d
    
    # Triangle 2
    x61d = -(a+b/2)
    y61d = -(a-b/2)
    x62d = -(a-b/2)
    y62d = -(a-b/2)
    x63d = -(a+b/2)
    y63d = - (a+b/2)
    a6d = ((y62d - y63d)*(mousexpos - x63d) + (x63d - x62d)*(mouseypos - y63d)) / ((y62d - y63d)*(x61d - x63d)+(x63d - x62d)*(y61d - y63d))
    b6d = ((y63d - y61d)*(mousexpos - x63d) + (x61d - x63d)*(mouseypos - y63d)) / ((y62d - y63d)*(x61d - x63d)+(x63d - x62d)*(y61d - y63d))
    c6d = 1 - a6d - b6d
    
    # Triangle 1 
    
    x71d = -(a + b/2)
    y71d = a + b/2
    x72d = -(a - b/2)
    y72d = a - b/2
    x73d = -(a + b/2)
    y73d = a - b/2
    a7d = ((y72d - y73d)*(mousexpos - x73d) + (x73d - x72d)*(mouseypos - y73d)) / ((y72d - y73d)*(x71d - x73d)+(x73d - x72d)*(y71d - y73d))
    b7d = ((y73d - y71d)*(mousexpos - x73d) + (x71d - x73d)*(mouseypos - y73d)) / ((y72d - y73d)*(x71d - x73d)+(x73d - x72d)*(y71d - y73d))
    c7d = 1 - a7d - b7d
    
    
    # Triangle 0 
    x81d = -(a + b/2)
    y81d = a + b/2
    x82d = -(a - b/2)
    y82d = a + b/2
    x83d = -(a - b/2)
    y83d = a - b/2
    a8d = ((y82d - y83d)*(mousexpos - x83d) + (x83d - x82d)*(mouseypos - y83d)) / ((y82d - y83d)*(x81d - x83d)+(x83d - x82d)*(y81d - y83d))
    b8d = ((y83d - y81d)*(mousexpos - x83d) + (x81d - x83d)*(mouseypos - y83d)) / ((y82d - y83d)*(x81d - x83d)+(x83d - x82d)*(y81d - y83d))
    c8d = 1 - a8d - b8d
    
    
    if (0 <= a1d <= 1) and (0 <= b1d <= 1) and (0 <= c1d <= 1):
        similarity = 7
    elif (0 <= a2d <= 1) and (0 <= b2d <= 1) and (0 <= c2d <= 1):
        similarity = 6
    elif (0 <= a3d <= 1) and (0 <= b3d <= 1) and (0 <= c3d <= 1):
        similarity = 5
    elif (0 <= a4d <= 1) and (0 <= b4d <= 1) and (0 <= c4d <= 1):
        similarity = 4
    elif (0 <= a5d <= 1) and (0 <= b5d <= 1) and (0 <= c5d <= 1):
        similarity = 3
    elif (0 <= a6d <= 1) and (0 <= b6d <= 1) and (0 <= c6d <= 1):
        similarity = 2
    elif (0 <= a7d <= 1) and (0 <= b7d <= 1) and (0 <= c7d <= 1):
        similarity = 1
    elif (0 <= a8d <= 1) and (0 <= b8d <= 1) and (0 <= c8d <= 1):
        similarity = 0
    
    
    thisExp.addData("Colour_2", Colour_2);
    thisExp.addData("similarity", similarity);
    thisExp.addData("response_time", mouse_5.mouseClock.getTime())  # Save time relative to start of mouse
    
    
    duringprac.addData('response1disk_5.started', response1disk_5.tStartRefresh)
    duringprac.addData('response1disk_5.stopped', response1disk_5.tStopRefresh)
    duringprac.addData('response3disk_5.started', response3disk_5.tStartRefresh)
    duringprac.addData('response3disk_5.stopped', response3disk_5.tStopRefresh)
    duringprac.addData('response5disk_5.started', response5disk_5.tStartRefresh)
    duringprac.addData('response5disk_5.stopped', response5disk_5.tStopRefresh)
    duringprac.addData('response7disk_5.started', response7disk_5.tStartRefresh)
    duringprac.addData('response7disk_5.stopped', response7disk_5.tStopRefresh)
    duringprac.addData('Circle_3.started', Circle_3.tStartRefresh)
    duringprac.addData('Circle_3.stopped', Circle_3.tStopRefresh)
    duringprac.addData('text_29.started', text_29.tStartRefresh)
    duringprac.addData('text_29.stopped', text_29.tStopRefresh)
    # the Routine "response_prac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "responseprac_feedback"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    if 0 <= responsenumber <= 1:
        responsefeedback = f'You selected {responsenumber}'
        responsefeedback1 = f'{responsenumber} indicates you found the colours very similar';
    
    if 2 <= responsenumber <= 3:
        responsefeedback = f'You selected {responsenumber}'
        responsefeedback1 = f'{responsenumber} indicates you found the colours similar';
    
    
    if 4 <= responsenumber  <= 5:
        responsefeedback = f'You selected {responsenumber}' ;
        responsefeedback1 = f'{responsenumber} indicates you found the colours different';
    
    if 6 <= responsenumber  <= 7:
        responsefeedback = f'You selected {responsenumber}' ;
        responsefeedback1 = f'{responsenumber} indicates you found the colours very different';
    
    
    text_55.setText(responsefeedback)
    text_56.setText(responsefeedback1)
    # keep track of which components have finished
    responseprac_feedbackComponents = [text_55, text_56]
    for thisComponent in responseprac_feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    responseprac_feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "responseprac_feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = responseprac_feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=responseprac_feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if 0 <= responsenumber <= 3:
            responsefeedback = f'You selected {responsenumber} indicating you found the colours are similar';
        
        
        if 4 <= responsenumber  <= 7:
            responsefeedback = f'You selected {responsenumber} indicating you found the colours are dissimilar';
        
        
        
        # *text_55* updates
        if text_55.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_55.frameNStart = frameN  # exact frame index
            text_55.tStart = t  # local t and not account for scr refresh
            text_55.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_55, 'tStartRefresh')  # time at next scr refresh
            text_55.setAutoDraw(True)
        if text_55.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_55.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                text_55.tStop = t  # not accounting for scr refresh
                text_55.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_55, 'tStopRefresh')  # time at next scr refresh
                text_55.setAutoDraw(False)
        
        # *text_56* updates
        if text_56.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_56.frameNStart = frameN  # exact frame index
            text_56.tStart = t  # local t and not account for scr refresh
            text_56.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_56, 'tStartRefresh')  # time at next scr refresh
            text_56.setAutoDraw(True)
        if text_56.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_56.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                text_56.tStop = t  # not accounting for scr refresh
                text_56.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_56, 'tStopRefresh')  # time at next scr refresh
                text_56.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in responseprac_feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "responseprac_feedback"-------
    for thisComponent in responseprac_feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    duringprac.addData('text_55.started', text_55.tStartRefresh)
    duringprac.addData('text_55.stopped', text_55.tStopRefresh)
    duringprac.addData('text_56.started', text_56.tStartRefresh)
    duringprac.addData('text_56.stopped', text_56.tStopRefresh)
    
    # ------Prepare to start Routine "summary_prac"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_10
    mouse_10.clicked_name = []
    gotValidClick = False  # until a click is received
    rectangle_8.setFillColor(grey)
    pracnumbertext = f'You have finished {pracnumber} of 7 practice questions';
    
    event.clearEvents()
    text_50.setText(pracnumbertext)
    # keep track of which components have finished
    summary_pracComponents = [mouse_10, response1disk_10, response3disk_10, response5disk_10, response7disk_10, rectangle_8, text_49, text_50]
    for thisComponent in summary_pracComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    summary_pracClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "summary_prac"-------
    while continueRoutine:
        # get current time
        t = summary_pracClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=summary_pracClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *mouse_10* updates
        if mouse_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_10.frameNStart = frameN  # exact frame index
            mouse_10.tStart = t  # local t and not account for scr refresh
            mouse_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_10, 'tStartRefresh')  # time at next scr refresh
            mouse_10.status = STARTED
            mouse_10.mouseClock.reset()
            prevButtonState = mouse_10.getPressed()  # if button is down already this ISN'T a new click
        if mouse_10.status == STARTED:  # only update if started and not finished!
            buttons = mouse_10.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [rectangle_8]:
                        if obj.contains(mouse_10):
                            gotValidClick = True
                            mouse_10.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # *response1disk_10* updates
        if response1disk_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response1disk_10.frameNStart = frameN  # exact frame index
            response1disk_10.tStart = t  # local t and not account for scr refresh
            response1disk_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response1disk_10, 'tStartRefresh')  # time at next scr refresh
            response1disk_10.setAutoDraw(True)
        
        # *response3disk_10* updates
        if response3disk_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response3disk_10.frameNStart = frameN  # exact frame index
            response3disk_10.tStart = t  # local t and not account for scr refresh
            response3disk_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response3disk_10, 'tStartRefresh')  # time at next scr refresh
            response3disk_10.setAutoDraw(True)
        
        # *response5disk_10* updates
        if response5disk_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response5disk_10.frameNStart = frameN  # exact frame index
            response5disk_10.tStart = t  # local t and not account for scr refresh
            response5disk_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response5disk_10, 'tStartRefresh')  # time at next scr refresh
            response5disk_10.setAutoDraw(True)
        
        # *response7disk_10* updates
        if response7disk_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response7disk_10.frameNStart = frameN  # exact frame index
            response7disk_10.tStart = t  # local t and not account for scr refresh
            response7disk_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response7disk_10, 'tStartRefresh')  # time at next scr refresh
            response7disk_10.setAutoDraw(True)
        
        # *rectangle_8* updates
        if rectangle_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rectangle_8.frameNStart = frameN  # exact frame index
            rectangle_8.tStart = t  # local t and not account for scr refresh
            rectangle_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rectangle_8, 'tStartRefresh')  # time at next scr refresh
            rectangle_8.setAutoDraw(True)
        
        # *text_49* updates
        if text_49.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_49.frameNStart = frameN  # exact frame index
            text_49.tStart = t  # local t and not account for scr refresh
            text_49.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_49, 'tStartRefresh')  # time at next scr refresh
            text_49.setAutoDraw(True)
        
        # *text_50* updates
        if text_50.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_50.frameNStart = frameN  # exact frame index
            text_50.tStart = t  # local t and not account for scr refresh
            text_50.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_50, 'tStartRefresh')  # time at next scr refresh
            text_50.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in summary_pracComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "summary_prac"-------
    for thisComponent in summary_pracComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for duringprac (TrialHandler)
    x, y = mouse_10.getPos()
    buttons = mouse_10.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        for obj in [rectangle_8]:
            if obj.contains(mouse_10):
                gotValidClick = True
                mouse_10.clicked_name.append(obj.name)
    duringprac.addData('mouse_10.x', x)
    duringprac.addData('mouse_10.y', y)
    duringprac.addData('mouse_10.leftButton', buttons[0])
    duringprac.addData('mouse_10.midButton', buttons[1])
    duringprac.addData('mouse_10.rightButton', buttons[2])
    if len(mouse_10.clicked_name):
        duringprac.addData('mouse_10.clicked_name', mouse_10.clicked_name[0])
    duringprac.addData('mouse_10.started', mouse_10.tStartRefresh)
    duringprac.addData('mouse_10.stopped', mouse_10.tStopRefresh)
    duringprac.addData('response1disk_10.started', response1disk_10.tStartRefresh)
    duringprac.addData('response1disk_10.stopped', response1disk_10.tStopRefresh)
    duringprac.addData('response3disk_10.started', response3disk_10.tStartRefresh)
    duringprac.addData('response3disk_10.stopped', response3disk_10.tStopRefresh)
    duringprac.addData('response5disk_10.started', response5disk_10.tStartRefresh)
    duringprac.addData('response5disk_10.stopped', response5disk_10.tStopRefresh)
    duringprac.addData('response7disk_10.started', response7disk_10.tStartRefresh)
    duringprac.addData('response7disk_10.stopped', response7disk_10.tStopRefresh)
    duringprac.addData('rectangle_8.started', rectangle_8.tStartRefresh)
    duringprac.addData('rectangle_8.stopped', rectangle_8.tStopRefresh)
    duringprac.addData('text_49.started', text_49.tStartRefresh)
    duringprac.addData('text_49.stopped', text_49.tStopRefresh)
    duringprac.addData('text_50.started', text_50.tStartRefresh)
    duringprac.addData('text_50.stopped', text_50.tStopRefresh)
    # the Routine "summary_prac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "special_trial_prac"-------
    continueRoutine = True
    routineTimer.add(0.250000)
    # update component parameters for each repeat
    # keep track of which components have finished
    special_trial_pracComponents = [text_36]
    for thisComponent in special_trial_pracComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    special_trial_pracClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "special_trial_prac"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = special_trial_pracClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=special_trial_pracClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_36* updates
        if text_36.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_36.frameNStart = frameN  # exact frame index
            text_36.tStart = t  # local t and not account for scr refresh
            text_36.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_36, 'tStartRefresh')  # time at next scr refresh
            text_36.setAutoDraw(True)
        if text_36.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_36.tStartRefresh + .250-frameTolerance:
                # keep track of stop time/frame for later
                text_36.tStop = t  # not accounting for scr refresh
                text_36.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_36, 'tStopRefresh')  # time at next scr refresh
                text_36.setAutoDraw(False)
        # Run catch trials 
        if not ((pracnumber == catchtrialorderprac[0]) or (pracnumber == catchtrialorderprac[1])):
            continueRoutine=False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in special_trial_pracComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "special_trial_prac"-------
    for thisComponent in special_trial_pracComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    duringprac.addData('text_36.started', text_36.tStartRefresh)
    duringprac.addData('text_36.stopped', text_36.tStopRefresh)
    
    # ------Prepare to start Routine "catch_prac"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_7
    mouse_7.clicked_name = []
    gotValidClick = False  # until a click is received
    # Select random number for catch trial
    
    
    
    catchtext = f'SPECIAL TRIAL PLEASE JUST CLICK AND HOLD {catchnumberprac}'
    
    event.clearEvents()
    text_32.setText(catchtext)
    rectangle_5.setFillColor(grey)
    # keep track of which components have finished
    catch_pracComponents = [mouse_7, response1disk_7, response3disk_7, response5disk_7, response7disk_7, text_32, rectangle_5]
    for thisComponent in catch_pracComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    catch_pracClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "catch_prac"-------
    while continueRoutine:
        # get current time
        t = catch_pracClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=catch_pracClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *mouse_7* updates
        if mouse_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_7.frameNStart = frameN  # exact frame index
            mouse_7.tStart = t  # local t and not account for scr refresh
            mouse_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_7, 'tStartRefresh')  # time at next scr refresh
            mouse_7.status = STARTED
            mouse_7.mouseClock.reset()
            prevButtonState = mouse_7.getPressed()  # if button is down already this ISN'T a new click
        if mouse_7.status == STARTED:  # only update if started and not finished!
            buttons = mouse_7.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [response1disk_7,response3disk_7,response5disk_7,response7disk_7]:
                        if obj.contains(mouse_7):
                            gotValidClick = True
                            mouse_7.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # *response1disk_7* updates
        if response1disk_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response1disk_7.frameNStart = frameN  # exact frame index
            response1disk_7.tStart = t  # local t and not account for scr refresh
            response1disk_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response1disk_7, 'tStartRefresh')  # time at next scr refresh
            response1disk_7.setAutoDraw(True)
        
        # *response3disk_7* updates
        if response3disk_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response3disk_7.frameNStart = frameN  # exact frame index
            response3disk_7.tStart = t  # local t and not account for scr refresh
            response3disk_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response3disk_7, 'tStartRefresh')  # time at next scr refresh
            response3disk_7.setAutoDraw(True)
        
        # *response5disk_7* updates
        if response5disk_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response5disk_7.frameNStart = frameN  # exact frame index
            response5disk_7.tStart = t  # local t and not account for scr refresh
            response5disk_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response5disk_7, 'tStartRefresh')  # time at next scr refresh
            response5disk_7.setAutoDraw(True)
        
        # *response7disk_7* updates
        if response7disk_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response7disk_7.frameNStart = frameN  # exact frame index
            response7disk_7.tStart = t  # local t and not account for scr refresh
            response7disk_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response7disk_7, 'tStartRefresh')  # time at next scr refresh
            response7disk_7.setAutoDraw(True)
        # Run catch trials 
        if not ((pracnumber == catchtrialorderprac[0]) or (pracnumber == catchtrialorderprac[1])):
            continueRoutine=False
        
        # *text_32* updates
        if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_32.frameNStart = frameN  # exact frame index
            text_32.tStart = t  # local t and not account for scr refresh
            text_32.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
            text_32.setAutoDraw(True)
        
        # *rectangle_5* updates
        if rectangle_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rectangle_5.frameNStart = frameN  # exact frame index
            rectangle_5.tStart = t  # local t and not account for scr refresh
            rectangle_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rectangle_5, 'tStartRefresh')  # time at next scr refresh
            rectangle_5.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in catch_pracComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "catch_prac"-------
    for thisComponent in catch_pracComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for duringprac (TrialHandler)
    x, y = mouse_7.getPos()
    buttons = mouse_7.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        for obj in [response1disk_7,response3disk_7,response5disk_7,response7disk_7]:
            if obj.contains(mouse_7):
                gotValidClick = True
                mouse_7.clicked_name.append(obj.name)
    duringprac.addData('mouse_7.x', x)
    duringprac.addData('mouse_7.y', y)
    duringprac.addData('mouse_7.leftButton', buttons[0])
    duringprac.addData('mouse_7.midButton', buttons[1])
    duringprac.addData('mouse_7.rightButton', buttons[2])
    if len(mouse_7.clicked_name):
        duringprac.addData('mouse_7.clicked_name', mouse_7.clicked_name[0])
    duringprac.addData('mouse_7.started', mouse_7.tStartRefresh)
    duringprac.addData('mouse_7.stopped', mouse_7.tStopRefresh)
    duringprac.addData('response1disk_7.started', response1disk_7.tStartRefresh)
    duringprac.addData('response1disk_7.stopped', response1disk_7.tStopRefresh)
    duringprac.addData('response3disk_7.started', response3disk_7.tStartRefresh)
    duringprac.addData('response3disk_7.stopped', response3disk_7.tStopRefresh)
    duringprac.addData('response5disk_7.started', response5disk_7.tStartRefresh)
    duringprac.addData('response5disk_7.stopped', response5disk_7.tStopRefresh)
    duringprac.addData('response7disk_7.started', response7disk_7.tStartRefresh)
    duringprac.addData('response7disk_7.stopped', response7disk_7.tStopRefresh)
    # Save similarity rating 
    mousexpos=mouse.getPos()[0]  # get x position of mouse
    mouseypos=mouse.getPos()[1]  # get y position of mouse
    
    # Triangle 7
    x11d = a - b/2;
    y11d = a + b/2;
    x12d = a + b/2;
    y12d = a + b/2;
    x13d = a - b/2;
    y13d = a - b/2;
    a1d = ((y12d - y13d)*(mousexpos - x13d) + (x13d - x12d)*(mouseypos - y13d)) / ((y12d - y13d)*(x11d - x13d)+(x13d - x12d)*(y11d - y13d))
    b1d = ((y13d - y11d)*(mousexpos - x13d) + (x11d - x13d)*(mouseypos - y13d)) / ((y12d - y13d)*(x11d - x13d)+(x13d - x12d)*(y11d - y13d))
    c1d = 1 - a1d - b1d;
    
    # Triangle 6 
    x21d = a - b/2;
    y21d = a - b/2
    x22d = a + b/2
    y22d = a + b/2
    x23d = a + b/2
    y23d = a - b/2
    a2d = ((y22d - y23d)*(mousexpos - x23d) + (x23d - x22d)*(mouseypos - y23d)) / ((y22d - y23d)*(x21d - x23d)+(x23d - x22d)*(y21d - y23d))
    b2d = ((y23d - y21d)*(mousexpos - x23d) + (x21d - x23d)*(mouseypos - y23d)) / ((y22d - y23d)*(x21d - x23d)+(x23d - x22d)*(y21d - y23d))
    c2d = 1 - a2d - b2d
    
    # Triangle 5
    x31d = a - b/2
    y31d = -(a - b/2)
    x32d = a + b/2
    y32d = -(a - b/2) 
    x33d = a + b/2
    y33d = -(a + b/2)
    a3d = ((y32d - y33d)*(mousexpos - x33d) + (x33d - x32d)*(mouseypos - y33d)) / ((y32d - y33d)*(x31d - x33d)+(x33d - x32d)*(y31d - y33d))
    b3d = ((y33d - y31d)*(mousexpos - x33d) + (x31d - x33d)*(mouseypos - y33d)) / ((y32d - y33d)*(x31d - x33d)+(x33d - x32d)*(y31d - y33d))
    c3d = 1 - a3d - b3d
    
    
    # Triangle 4 
    x41d = a - b/2
    y41d = -(a - b/2)
    x42d = a + b/2
    y42d = -(a + b/2)
    x43d = a - b/2
    y43d = -(a + b/2)
    a4d = ((y42d - y43d)*(mousexpos - x43d) + (x43d - x42d)*(mouseypos - y43d)) / ((y42d - y43d)*(x41d - x43d)+(x43d - x42d)*(y41d - y43d))
    b4d = ((y43d - y41d)*(mousexpos - x43d) + (x41d - x43d)*(mouseypos - y43d)) / ((y42d - y43d)*(x41d - x43d)+(x43d - x42d)*(y41d - y43d))
    c4d = 1 - a4d - b4d
    
    #  Triangle 3
    x51d = -(a + b/2)
    y51d = -(a + b/2)
    x52d = -(a - b/2)
    y52d = -(a - b/2)
    x53d = -(a - b/2)
    y53d = -(a + b/2)
    a5d = ((y52d - y53d)*(mousexpos - x53d) + (x53d - x52d)*(mouseypos - y53d)) / ((y52d - y53d)*(x51d - x53d)+(x53d - x52d)*(y51d - y53d))
    b5d = ((y53d - y51d)*(mousexpos - x53d) + (x51d - x53d)*(mouseypos - y53d)) / ((y52d - y53d)*(x51d - x53d)+(x53d - x52d)*(y51d - y53d))
    c5d = 1 - a5d - b5d
    
    # Triangle 2
    x61d = -(a+b/2)
    y61d = -(a+b/2)
    x62d = -(a-b/2)
    y62d = -(a-b/2)
    x63d = -(a+b/2)
    y63d = - (a+b/2)
    a6d = ((y62d - y63d)*(mousexpos - x63d) + (x63d - x62d)*(mouseypos - y63d)) / ((y62d - y63d)*(x61d - x63d)+(x63d - x62d)*(y61d - y63d))
    b6d = ((y63d - y61d)*(mousexpos - x63d) + (x61d - x63d)*(mouseypos - y63d)) / ((y62d - y63d)*(x61d - x63d)+(x63d - x62d)*(y61d - y63d))
    c6d = 1 - a6d - b6d
    
    # Triangle 1 
    
    x71d = -(a + b/2)
    y71d = a + b/2
    x72d = -(a - b/2)
    y72d = a - b/2
    x73d = -(a + b/2)
    y73d = a - b/2
    a7d = ((y72d - y73d)*(mousexpos - x73d) + (x73d - x72d)*(mouseypos - y73d)) / ((y72d - y73d)*(x71d - x73d)+(x73d - x72d)*(y71d - y73d))
    b7d = ((y73d - y71d)*(mousexpos - x73d) + (x71d - x73d)*(mouseypos - y73d)) / ((y72d - y73d)*(x71d - x73d)+(x73d - x72d)*(y71d - y73d))
    c7d = 1 - a7d - b7d
    
    
    # Triangle 0 
    x81d = -(a + b/2)
    y81d = a + b/2
    x82d = -(a - b/2)
    y82d = a + b/2
    x83d = -(a - b/2)
    y83d = a - b/2
    a8d = ((y82d - y83d)*(mousexpos - x83d) + (x83d - x82d)*(mouseypos - y83d)) / ((y82d - y83d)*(x81d - x83d)+(x83d - x82d)*(y81d - y83d))
    b8d = ((y83d - y81d)*(mousexpos - x83d) + (x81d - x83d)*(mouseypos - y83d)) / ((y82d - y83d)*(x81d - x83d)+(x83d - x82d)*(y81d - y83d))
    c8d = 1 - a8d - b8d
    
    if (0 <= a1d <= 1) and (0 <= b1d <= 1) and (0 <= c1d <= 1):
        catchprac = 7
        thisExp.addData("catchprac", catchprac);
    elif (0 <= a2d <= 1) and (0 <= b2d <= 1) and (0 <= c2d <= 1):
        catchprac = 6
        thisExp.addData("catchprac", catchprac);
    elif (0 <= a3d <= 1) and (0 <= b3d <= 1) and (0 <= c3d <= 1):
        catchprac = 5
        thisExp.addData("catchprac", catchprac);
    elif (0 <= a4d <= 1) and (0 <= b4d <= 1) and (0 <= c4d <= 1):
        catchprac = 4
        thisExp.addData("catchprac", catchprac);
    elif (0 <= a5d <= 1) and (0 <= b5d <= 1) and (0 <= c5d <= 1):
        catchprac = 3
        thisExp.addData("catchprac", catchprac);
    elif (0 <= a6d <= 1) and (0 <= b6d <= 1) and (0 <= c6d <= 1):
        catchprac = 2
        thisExp.addData("catchprac", catchprac);
    elif (0 <= a7d <= 1) and (0 <= b7d <= 1) and (0 <= c7d <= 1):
        catchprac = 1;
        thisExp.addData("catchprac", catchprac);
    elif (0 <= a8d <= 1) and (0 <= b8d <= 1) and (0 <= c8d <= 1):
        catchprac = 0;
        thisExp.addData("catchprac", catchprac);
    
    
    
    thisExp.addData("catchnumberprac", catchnumberprac);
    
    duringprac.addData('text_32.started', text_32.tStartRefresh)
    duringprac.addData('text_32.stopped', text_32.tStopRefresh)
    duringprac.addData('rectangle_5.started', rectangle_5.tStartRefresh)
    duringprac.addData('rectangle_5.stopped', rectangle_5.tStopRefresh)
    # the Routine "catch_prac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "summary2_prac"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_6
    mouse_6.clicked_name = []
    gotValidClick = False  # until a click is received
    response3disk_6.setPos(a,-a)
    response3disk_6.setSize(b,b)
    response7disk_6.setPos(-a,a)
    response7disk_6.setSize(b,b)
    rectangle_4.setFillColor(grey)
    pracnumbertext = f'You have finished {pracnumber} of 7 practice questions';
    
    event.clearEvents()
    
    # Run catch trials 
    if not ((pracnumber == catchtrialorderprac[0]) or (pracnumber == catchtrialorderprac[1])):
        continueRoutine=False
    text_31.setText(pracnumbertext)
    # keep track of which components have finished
    summary2_pracComponents = [mouse_6, response1disk_6, response3disk_6, response5disk_6, response7disk_6, rectangle_4, text_30, text_31]
    for thisComponent in summary2_pracComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    summary2_pracClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "summary2_prac"-------
    while continueRoutine:
        # get current time
        t = summary2_pracClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=summary2_pracClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *mouse_6* updates
        if mouse_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_6.frameNStart = frameN  # exact frame index
            mouse_6.tStart = t  # local t and not account for scr refresh
            mouse_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_6, 'tStartRefresh')  # time at next scr refresh
            mouse_6.status = STARTED
            mouse_6.mouseClock.reset()
            prevButtonState = mouse_6.getPressed()  # if button is down already this ISN'T a new click
        if mouse_6.status == STARTED:  # only update if started and not finished!
            buttons = mouse_6.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [rectangle_4]:
                        if obj.contains(mouse_6):
                            gotValidClick = True
                            mouse_6.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # *response1disk_6* updates
        if response1disk_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response1disk_6.frameNStart = frameN  # exact frame index
            response1disk_6.tStart = t  # local t and not account for scr refresh
            response1disk_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response1disk_6, 'tStartRefresh')  # time at next scr refresh
            response1disk_6.setAutoDraw(True)
        
        # *response3disk_6* updates
        if response3disk_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response3disk_6.frameNStart = frameN  # exact frame index
            response3disk_6.tStart = t  # local t and not account for scr refresh
            response3disk_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response3disk_6, 'tStartRefresh')  # time at next scr refresh
            response3disk_6.setAutoDraw(True)
        
        # *response5disk_6* updates
        if response5disk_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response5disk_6.frameNStart = frameN  # exact frame index
            response5disk_6.tStart = t  # local t and not account for scr refresh
            response5disk_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response5disk_6, 'tStartRefresh')  # time at next scr refresh
            response5disk_6.setAutoDraw(True)
        
        # *response7disk_6* updates
        if response7disk_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response7disk_6.frameNStart = frameN  # exact frame index
            response7disk_6.tStart = t  # local t and not account for scr refresh
            response7disk_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response7disk_6, 'tStartRefresh')  # time at next scr refresh
            response7disk_6.setAutoDraw(True)
        
        # *rectangle_4* updates
        if rectangle_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rectangle_4.frameNStart = frameN  # exact frame index
            rectangle_4.tStart = t  # local t and not account for scr refresh
            rectangle_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rectangle_4, 'tStartRefresh')  # time at next scr refresh
            rectangle_4.setAutoDraw(True)
        # Run catch trials 
        if not ((pracnumber == catchtrialorderprac[0]) or (pracnumber == catchtrialorderprac[1])):
            continueRoutine=False
        
        # *text_30* updates
        if text_30.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_30.frameNStart = frameN  # exact frame index
            text_30.tStart = t  # local t and not account for scr refresh
            text_30.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_30, 'tStartRefresh')  # time at next scr refresh
            text_30.setAutoDraw(True)
        
        # *text_31* updates
        if text_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_31.frameNStart = frameN  # exact frame index
            text_31.tStart = t  # local t and not account for scr refresh
            text_31.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_31, 'tStartRefresh')  # time at next scr refresh
            text_31.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in summary2_pracComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "summary2_prac"-------
    for thisComponent in summary2_pracComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for duringprac (TrialHandler)
    x, y = mouse_6.getPos()
    buttons = mouse_6.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        for obj in [rectangle_4]:
            if obj.contains(mouse_6):
                gotValidClick = True
                mouse_6.clicked_name.append(obj.name)
    duringprac.addData('mouse_6.x', x)
    duringprac.addData('mouse_6.y', y)
    duringprac.addData('mouse_6.leftButton', buttons[0])
    duringprac.addData('mouse_6.midButton', buttons[1])
    duringprac.addData('mouse_6.rightButton', buttons[2])
    if len(mouse_6.clicked_name):
        duringprac.addData('mouse_6.clicked_name', mouse_6.clicked_name[0])
    duringprac.addData('mouse_6.started', mouse_6.tStartRefresh)
    duringprac.addData('mouse_6.stopped', mouse_6.tStopRefresh)
    duringprac.addData('response1disk_6.started', response1disk_6.tStartRefresh)
    duringprac.addData('response1disk_6.stopped', response1disk_6.tStopRefresh)
    duringprac.addData('response3disk_6.started', response3disk_6.tStartRefresh)
    duringprac.addData('response3disk_6.stopped', response3disk_6.tStopRefresh)
    duringprac.addData('response5disk_6.started', response5disk_6.tStartRefresh)
    duringprac.addData('response5disk_6.stopped', response5disk_6.tStopRefresh)
    duringprac.addData('response7disk_6.started', response7disk_6.tStartRefresh)
    duringprac.addData('response7disk_6.stopped', response7disk_6.tStopRefresh)
    duringprac.addData('rectangle_4.started', rectangle_4.tStartRefresh)
    duringprac.addData('rectangle_4.stopped', rectangle_4.tStopRefresh)
    duringprac.addData('text_30.started', text_30.tStartRefresh)
    duringprac.addData('text_30.stopped', text_30.tStopRefresh)
    duringprac.addData('text_31.started', text_31.tStartRefresh)
    duringprac.addData('text_31.stopped', text_31.tStopRefresh)
    # the Routine "summary2_prac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'duringprac'


# ------Prepare to start Routine "begin"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_22.keys = []
key_resp_22.rt = []
_key_resp_22_allKeys = []
# keep track of which components have finished
beginComponents = [space_19, text_46, key_resp_22]
for thisComponent in beginComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
beginClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "begin"-------
while continueRoutine:
    # get current time
    t = beginClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=beginClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *space_19* updates
    if space_19.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        space_19.frameNStart = frameN  # exact frame index
        space_19.tStart = t  # local t and not account for scr refresh
        space_19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_19, 'tStartRefresh')  # time at next scr refresh
        space_19.setAutoDraw(True)
    
    # *text_46* updates
    if text_46.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_46.frameNStart = frameN  # exact frame index
        text_46.tStart = t  # local t and not account for scr refresh
        text_46.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_46, 'tStartRefresh')  # time at next scr refresh
        text_46.setAutoDraw(True)
    
    # *key_resp_22* updates
    waitOnFlip = False
    if key_resp_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_22.frameNStart = frameN  # exact frame index
        key_resp_22.tStart = t  # local t and not account for scr refresh
        key_resp_22.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_22, 'tStartRefresh')  # time at next scr refresh
        key_resp_22.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_22.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_22.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_22.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_22.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_22_allKeys.extend(theseKeys)
        if len(_key_resp_22_allKeys):
            key_resp_22.keys = _key_resp_22_allKeys[-1].name  # just the last key pressed
            key_resp_22.rt = _key_resp_22_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in beginComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "begin"-------
for thisComponent in beginComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('space_19.started', space_19.tStartRefresh)
thisExp.addData('space_19.stopped', space_19.tStopRefresh)
thisExp.addData('text_46.started', text_46.tStartRefresh)
thisExp.addData('text_46.stopped', text_46.tStopRefresh)
# check responses
if key_resp_22.keys in ['', [], None]:  # No response was made
    key_resp_22.keys = None
thisExp.addData('key_resp_22.keys',key_resp_22.keys)
if key_resp_22.keys != None:  # we had a response
    thisExp.addData('key_resp_22.rt', key_resp_22.rt)
thisExp.addData('key_resp_22.started', key_resp_22.tStartRefresh)
thisExp.addData('key_resp_22.stopped', key_resp_22.tStopRefresh)
thisExp.nextEntry()
# the Routine "begin" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Stimconditions.xlsx', selection='0:162'),
        seed=order, name='trials_2')
    thisExp.addLoop(trials_2)  # add the loop to the experiment
    thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    for thisTrial_2 in trials_2:
        currentLoop = trials_2
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                exec('{} = thisTrial_2[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Stim1_display"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        # Circle position and size 
        
        x = 1
        y = 1
        
        angle_1 = randint(-30,30);
        angle_2 = angle_1 + 180;
        
        theta_1 = (angle_1)*(pi/180)
        theta_2 = (angle_2)*(pi/180)
        
        deltax_1 = radius_F*cos(theta_1)
        deltay_1 = radius_F*sin(theta_1)
        deltax_2 = radius_P*cos(theta_2)
        deltay_2 = radius_P*sin(theta_2)
        
        
        a_1 = x + deltax_1
        b_1 = y + deltay_1
        a_2 = x + deltax_2
        b_2 = y + deltay_2
        
        
        # Set circle colour
        if Colour1 == 1:
            Circle1_colour = (1, -1, -1);
        elif Colour1 == 2:
            Circle1_colour = (1, 0.33, -1);
        elif Colour1 == 3:
            Circle1_colour = (0.32, 1, -1);
        elif Colour1 == 4:
            Circle1_colour = (-1, 1, -1);
        elif Colour1 == 5:
            Circle1_colour = (-1, 1, 0.33);
        elif Colour1 == 6:
            Circle1_colour = (-1, 0.32, 1);
        elif Colour1 == 7:
            Circle1_colour = (-1, -1, 1);
        elif Colour1 == 8:
            Circle1_colour = (0.33, -1, 1);
        elif Colour1 == 9:
            Circle1_colour = (1, -1, 0.33);
        
        
        # Set circle position and size
        if Ecc == 'FF':
            circle1posx = a_1;
            circle1posy = b_1;
            circlesizeh = 2 *r_F;
            circlesizew = 2 * r_F;
        elif Ecc == 'PF':
                circle1posx = a_2;
                circle1posy = b_2;
                circlesizeh = 2 * R_P;
                circlesizew = 2 * R_P;
        
        
        
        Circle_1.setPos((circle1posx,circle1posy))
        Circle_1.setSize((circlesizew,circlesizeh))
        Circle_1.setFillColor(Circle1_colour)
        Circle_1.setLineColor(Circle1_colour)
        # keep track of which components have finished
        Stim1_displayComponents = [Circle_1, centre_cross4]
        for thisComponent in Stim1_displayComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Stim1_displayClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Stim1_display"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Stim1_displayClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Stim1_displayClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Circle_1* updates
            if Circle_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Circle_1.frameNStart = frameN  # exact frame index
                Circle_1.tStart = t  # local t and not account for scr refresh
                Circle_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Circle_1, 'tStartRefresh')  # time at next scr refresh
                Circle_1.setAutoDraw(True)
            if Circle_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Circle_1.tStartRefresh + 0.25-frameTolerance:
                    # keep track of stop time/frame for later
                    Circle_1.tStop = t  # not accounting for scr refresh
                    Circle_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Circle_1, 'tStopRefresh')  # time at next scr refresh
                    Circle_1.setAutoDraw(False)
            
            # *centre_cross4* updates
            if centre_cross4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                centre_cross4.frameNStart = frameN  # exact frame index
                centre_cross4.tStart = t  # local t and not account for scr refresh
                centre_cross4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(centre_cross4, 'tStartRefresh')  # time at next scr refresh
                centre_cross4.setAutoDraw(True)
            if centre_cross4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > centre_cross4.tStartRefresh + 0.500-frameTolerance:
                    # keep track of stop time/frame for later
                    centre_cross4.tStop = t  # not accounting for scr refresh
                    centre_cross4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(centre_cross4, 'tStopRefresh')  # time at next scr refresh
                    centre_cross4.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Stim1_displayComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Stim1_display"-------
        for thisComponent in Stim1_displayComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData("Colour1", Colour1);
        thisExp.addData("Ecc", Ecc);
        
        trials_2.addData('Circle_1.started', Circle_1.tStartRefresh)
        trials_2.addData('Circle_1.stopped', Circle_1.tStopRefresh)
        trials_2.addData('centre_cross4.started', centre_cross4.tStartRefresh)
        trials_2.addData('centre_cross4.stopped', centre_cross4.tStopRefresh)
        
        # ------Prepare to start Routine "response"-------
        continueRoutine = True
        # update component parameters for each repeat
        # setup some python lists for storing info about the mouse
        mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        # Count trial numbers
        event.clearEvents() 
        trialnumber =  trialnumber + 1;
        
        
        # Set circle colour
        if Colour2 == 1:
            Circle2_colour = (1, -1, -1);
        elif Colour2 == 2:
            Circle2_colour = (1, 0.33, -1);
        elif Colour2 == 3:
            Circle2_colour = (0.32, 1, -1);
        elif Colour2 == 4:
            Circle2_colour = (-1, 1, -1);
        elif Colour2 == 5:
            Circle2_colour = (-1, 1, 0.33);
        elif Colour2 == 6:
            Circle2_colour = (-1, 0.32, 1);
        elif Colour2 == 7:
            Circle2_colour = (-1, -1, 1);
        elif Colour2 == 8:
            Circle2_colour = (0.33, -1, 1);
        elif Colour2 == 9:
            Circle2_colour = (1, -1, 0.33);
        
        Circle_2.setSize((15*ratio_pxpermm, 15*ratio_pxpermm))
        Circle_2.setFillColor(Circle2_colour)
        Circle_2.setLineColor(Circle2_colour)
        # keep track of which components have finished
        responseComponents = [mouse, response1disk, response3disk, response5disk, response7disk, Circle_2, text_23]
        for thisComponent in responseComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        responseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "response"-------
        while continueRoutine:
            # get current time
            t = responseClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=responseClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # *mouse* updates
            if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse.frameNStart = frameN  # exact frame index
                mouse.tStart = t  # local t and not account for scr refresh
                mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
                mouse.status = STARTED
                mouse.mouseClock.reset()
                prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
            if mouse.status == STARTED:  # only update if started and not finished!
                buttons = mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [response1disk,response3disk,response5disk,response7disk]:
                            if obj.contains(mouse):
                                gotValidClick = True
                                mouse.clicked_name.append(obj.name)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # *response1disk* updates
            if response1disk.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                response1disk.frameNStart = frameN  # exact frame index
                response1disk.tStart = t  # local t and not account for scr refresh
                response1disk.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response1disk, 'tStartRefresh')  # time at next scr refresh
                response1disk.setAutoDraw(True)
            
            # *response3disk* updates
            if response3disk.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                response3disk.frameNStart = frameN  # exact frame index
                response3disk.tStart = t  # local t and not account for scr refresh
                response3disk.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response3disk, 'tStartRefresh')  # time at next scr refresh
                response3disk.setAutoDraw(True)
            
            # *response5disk* updates
            if response5disk.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                response5disk.frameNStart = frameN  # exact frame index
                response5disk.tStart = t  # local t and not account for scr refresh
                response5disk.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response5disk, 'tStartRefresh')  # time at next scr refresh
                response5disk.setAutoDraw(True)
            
            # *response7disk* updates
            if response7disk.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                response7disk.frameNStart = frameN  # exact frame index
                response7disk.tStart = t  # local t and not account for scr refresh
                response7disk.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response7disk, 'tStartRefresh')  # time at next scr refresh
                response7disk.setAutoDraw(True)
            
            # *Circle_2* updates
            if Circle_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Circle_2.frameNStart = frameN  # exact frame index
                Circle_2.tStart = t  # local t and not account for scr refresh
                Circle_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Circle_2, 'tStartRefresh')  # time at next scr refresh
                Circle_2.setAutoDraw(True)
            
            # *text_23* updates
            if text_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_23.frameNStart = frameN  # exact frame index
                text_23.tStart = t  # local t and not account for scr refresh
                text_23.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_23, 'tStartRefresh')  # time at next scr refresh
                text_23.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in responseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "response"-------
        for thisComponent in responseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for trials_2 (TrialHandler)
        x, y = mouse.getPos()
        buttons = mouse.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            for obj in [response1disk,response3disk,response5disk,response7disk]:
                if obj.contains(mouse):
                    gotValidClick = True
                    mouse.clicked_name.append(obj.name)
        trials_2.addData('mouse.x', x)
        trials_2.addData('mouse.y', y)
        trials_2.addData('mouse.leftButton', buttons[0])
        trials_2.addData('mouse.midButton', buttons[1])
        trials_2.addData('mouse.rightButton', buttons[2])
        if len(mouse.clicked_name):
            trials_2.addData('mouse.clicked_name', mouse.clicked_name[0])
        trials_2.addData('mouse.started', mouse.tStart)
        trials_2.addData('mouse.stopped', mouse.tStop)
        # Save similarity rating 
        mousexpos=mouse.getPos()[0]  # get x position of mouse
        mouseypos=mouse.getPos()[1]  # get y position of mouse
        
        # Triangle 7
        x11d = a - b/2;
        y11d = a + b/2;
        x12d = a + b/2;
        y12d = a + b/2;
        x13d = a - b/2;
        y13d = a - b/2;
        a1d = ((y12d - y13d)*(mousexpos - x13d) + (x13d - x12d)*(mouseypos - y13d)) / ((y12d - y13d)*(x11d - x13d)+(x13d - x12d)*(y11d - y13d))
        b1d = ((y13d - y11d)*(mousexpos - x13d) + (x11d - x13d)*(mouseypos - y13d)) / ((y12d - y13d)*(x11d - x13d)+(x13d - x12d)*(y11d - y13d))
        c1d = 1 - a1d - b1d;
        
        # Triangle 6 
        x21d = a - b/2;
        y21d = a - b/2
        x22d = a + b/2
        y22d = a + b/2
        x23d = a + b/2
        y23d = a - b/2
        a2d = ((y22d - y23d)*(mousexpos - x23d) + (x23d - x22d)*(mouseypos - y23d)) / ((y22d - y23d)*(x21d - x23d)+(x23d - x22d)*(y21d - y23d))
        b2d = ((y23d - y21d)*(mousexpos - x23d) + (x21d - x23d)*(mouseypos - y23d)) / ((y22d - y23d)*(x21d - x23d)+(x23d - x22d)*(y21d - y23d))
        c2d = 1 - a2d - b2d
        
        # Triangle 5
        x31d = a - b/2
        y31d = -(a - b/2)
        x32d = a + b/2
        y32d = -(a - b/2) 
        x33d = a + b/2
        y33d = -(a + b/2)
        a3d = ((y32d - y33d)*(mousexpos - x33d) + (x33d - x32d)*(mouseypos - y33d)) / ((y32d - y33d)*(x31d - x33d)+(x33d - x32d)*(y31d - y33d))
        b3d = ((y33d - y31d)*(mousexpos - x33d) + (x31d - x33d)*(mouseypos - y33d)) / ((y32d - y33d)*(x31d - x33d)+(x33d - x32d)*(y31d - y33d))
        c3d = 1 - a3d - b3d
        
        
        # Triangle 4 
        x41d = a - b/2
        y41d = -(a - b/2)
        x42d = a + b/2
        y42d = -(a + b/2)
        x43d = a - b/2
        y43d = -(a + b/2)
        a4d = ((y42d - y43d)*(mousexpos - x43d) + (x43d - x42d)*(mouseypos - y43d)) / ((y42d - y43d)*(x41d - x43d)+(x43d - x42d)*(y41d - y43d))
        b4d = ((y43d - y41d)*(mousexpos - x43d) + (x41d - x43d)*(mouseypos - y43d)) / ((y42d - y43d)*(x41d - x43d)+(x43d - x42d)*(y41d - y43d))
        c4d = 1 - a4d - b4d
        
        #  Triangle 3
        x51d = -(a + b/2)
        y51d = -(a + b/2)
        x52d = -(a - b/2)
        y52d = -(a - b/2)
        x53d = -(a - b/2)
        y53d = -(a + b/2)
        a5d = ((y52d - y53d)*(mousexpos - x53d) + (x53d - x52d)*(mouseypos - y53d)) / ((y52d - y53d)*(x51d - x53d)+(x53d - x52d)*(y51d - y53d))
        b5d = ((y53d - y51d)*(mousexpos - x53d) + (x51d - x53d)*(mouseypos - y53d)) / ((y52d - y53d)*(x51d - x53d)+(x53d - x52d)*(y51d - y53d))
        c5d = 1 - a5d - b5d
        
        # Triangle 2
        x61d = -(a+b/2)
        y61d = -(a-b/2)
        x62d = -(a-b/2)
        y62d = -(a-b/2)
        x63d = -(a+b/2)
        y63d = - (a+b/2)
        a6d = ((y62d - y63d)*(mousexpos - x63d) + (x63d - x62d)*(mouseypos - y63d)) / ((y62d - y63d)*(x61d - x63d)+(x63d - x62d)*(y61d - y63d))
        b6d = ((y63d - y61d)*(mousexpos - x63d) + (x61d - x63d)*(mouseypos - y63d)) / ((y62d - y63d)*(x61d - x63d)+(x63d - x62d)*(y61d - y63d))
        c6d = 1 - a6d - b6d
        
        # Triangle 1 
        
        x71d = -(a + b/2)
        y71d = a + b/2
        x72d = -(a - b/2)
        y72d = a - b/2
        x73d = -(a + b/2)
        y73d = a - b/2
        a7d = ((y72d - y73d)*(mousexpos - x73d) + (x73d - x72d)*(mouseypos - y73d)) / ((y72d - y73d)*(x71d - x73d)+(x73d - x72d)*(y71d - y73d))
        b7d = ((y73d - y71d)*(mousexpos - x73d) + (x71d - x73d)*(mouseypos - y73d)) / ((y72d - y73d)*(x71d - x73d)+(x73d - x72d)*(y71d - y73d))
        c7d = 1 - a7d - b7d
        
        
        # Triangle 0 
        x81d = -(a + b/2)
        y81d = a + b/2
        x82d = -(a - b/2)
        y82d = a + b/2
        x83d = -(a - b/2)
        y83d = a - b/2
        a8d = ((y82d - y83d)*(mousexpos - x83d) + (x83d - x82d)*(mouseypos - y83d)) / ((y82d - y83d)*(x81d - x83d)+(x83d - x82d)*(y81d - y83d))
        b8d = ((y83d - y81d)*(mousexpos - x83d) + (x81d - x83d)*(mouseypos - y83d)) / ((y82d - y83d)*(x81d - x83d)+(x83d - x82d)*(y81d - y83d))
        c8d = 1 - a8d - b8d
        
        if (0 <= a1d <= 1) and (0 <= b1d <= 1) and (0 <= c1d <= 1):
            similarity = 7
        elif (0 <= a2d <= 1) and (0 <= b2d <= 1) and (0 <= c2d <= 1):
            similarity = 6
        elif (0 <= a3d <= 1) and (0 <= b3d <= 1) and (0 <= c3d <= 1):
            similarity = 5
        elif (0 <= a4d <= 1) and (0 <= b4d <= 1) and (0 <= c4d <= 1):
            similarity = 4
        elif (0 <= a5d <= 1) and (0 <= b5d <= 1) and (0 <= c5d <= 1):
            similarity = 3
        elif (0 <= a6d <= 1) and (0 <= b6d <= 1) and (0 <= c6d <= 1):
            similarity = 2
        elif (0 <= a7d <= 1) and (0 <= b7d <= 1) and (0 <= c7d <= 1):
            similarity = 1
        elif (0 <= a8d <= 1) and (0 <= b8d <= 1) and (0 <= c8d <= 1):
            similarity = 0
        
        thisExp.addData("Colour2", Colour2);
        thisExp.addData("Ecc", Ecc);
        thisExp.addData("similarity", similarity);
        thisExp.addData("response_time", mouse.mouseClock.getTime())  # Save time relative to start of mouse
        
        
        trials_2.addData('response1disk.started', response1disk.tStartRefresh)
        trials_2.addData('response1disk.stopped', response1disk.tStopRefresh)
        trials_2.addData('response3disk.started', response3disk.tStartRefresh)
        trials_2.addData('response3disk.stopped', response3disk.tStopRefresh)
        trials_2.addData('response5disk.started', response5disk.tStartRefresh)
        trials_2.addData('response5disk.stopped', response5disk.tStopRefresh)
        trials_2.addData('response7disk.started', response7disk.tStartRefresh)
        trials_2.addData('response7disk.stopped', response7disk.tStopRefresh)
        trials_2.addData('Circle_2.started', Circle_2.tStartRefresh)
        trials_2.addData('Circle_2.stopped', Circle_2.tStopRefresh)
        trials_2.addData('text_23.started', text_23.tStartRefresh)
        trials_2.addData('text_23.stopped', text_23.tStopRefresh)
        # the Routine "response" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "response_2"-------
        continueRoutine = True
        # update component parameters for each repeat
        # setup some python lists for storing info about the mouse_2
        mouse_2.clicked_name = []
        gotValidClick = False  # until a click is received
        rectangle.setFillColor(grey)
        trialnumbertext = f'You have finished {trialnumber} of 324 questions';
        
        event.clearEvents()
        text_24.setText(trialnumbertext)
        # keep track of which components have finished
        response_2Components = [mouse_2, response1disk_2, response3disk_2, response5disk_2, response7disk_2, rectangle, text_25, text_24]
        for thisComponent in response_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        response_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "response_2"-------
        while continueRoutine:
            # get current time
            t = response_2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=response_2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # *mouse_2* updates
            if mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_2.frameNStart = frameN  # exact frame index
                mouse_2.tStart = t  # local t and not account for scr refresh
                mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
                mouse_2.status = STARTED
                mouse_2.mouseClock.reset()
                prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
            if mouse_2.status == STARTED:  # only update if started and not finished!
                buttons = mouse_2.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [rectangle]:
                            if obj.contains(mouse_2):
                                gotValidClick = True
                                mouse_2.clicked_name.append(obj.name)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # *response1disk_2* updates
            if response1disk_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                response1disk_2.frameNStart = frameN  # exact frame index
                response1disk_2.tStart = t  # local t and not account for scr refresh
                response1disk_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response1disk_2, 'tStartRefresh')  # time at next scr refresh
                response1disk_2.setAutoDraw(True)
            
            # *response3disk_2* updates
            if response3disk_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                response3disk_2.frameNStart = frameN  # exact frame index
                response3disk_2.tStart = t  # local t and not account for scr refresh
                response3disk_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response3disk_2, 'tStartRefresh')  # time at next scr refresh
                response3disk_2.setAutoDraw(True)
            
            # *response5disk_2* updates
            if response5disk_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                response5disk_2.frameNStart = frameN  # exact frame index
                response5disk_2.tStart = t  # local t and not account for scr refresh
                response5disk_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response5disk_2, 'tStartRefresh')  # time at next scr refresh
                response5disk_2.setAutoDraw(True)
            
            # *response7disk_2* updates
            if response7disk_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                response7disk_2.frameNStart = frameN  # exact frame index
                response7disk_2.tStart = t  # local t and not account for scr refresh
                response7disk_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response7disk_2, 'tStartRefresh')  # time at next scr refresh
                response7disk_2.setAutoDraw(True)
            
            # *rectangle* updates
            if rectangle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rectangle.frameNStart = frameN  # exact frame index
                rectangle.tStart = t  # local t and not account for scr refresh
                rectangle.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rectangle, 'tStartRefresh')  # time at next scr refresh
                rectangle.setAutoDraw(True)
            
            # *text_25* updates
            if text_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_25.frameNStart = frameN  # exact frame index
                text_25.tStart = t  # local t and not account for scr refresh
                text_25.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_25, 'tStartRefresh')  # time at next scr refresh
                text_25.setAutoDraw(True)
            
            # *text_24* updates
            if text_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_24.frameNStart = frameN  # exact frame index
                text_24.tStart = t  # local t and not account for scr refresh
                text_24.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_24, 'tStartRefresh')  # time at next scr refresh
                text_24.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in response_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "response_2"-------
        for thisComponent in response_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for trials_2 (TrialHandler)
        x, y = mouse_2.getPos()
        buttons = mouse_2.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            for obj in [rectangle]:
                if obj.contains(mouse_2):
                    gotValidClick = True
                    mouse_2.clicked_name.append(obj.name)
        trials_2.addData('mouse_2.x', x)
        trials_2.addData('mouse_2.y', y)
        trials_2.addData('mouse_2.leftButton', buttons[0])
        trials_2.addData('mouse_2.midButton', buttons[1])
        trials_2.addData('mouse_2.rightButton', buttons[2])
        if len(mouse_2.clicked_name):
            trials_2.addData('mouse_2.clicked_name', mouse_2.clicked_name[0])
        trials_2.addData('mouse_2.started', mouse_2.tStart)
        trials_2.addData('mouse_2.stopped', mouse_2.tStop)
        trials_2.addData('response1disk_2.started', response1disk_2.tStartRefresh)
        trials_2.addData('response1disk_2.stopped', response1disk_2.tStopRefresh)
        trials_2.addData('response3disk_2.started', response3disk_2.tStartRefresh)
        trials_2.addData('response3disk_2.stopped', response3disk_2.tStopRefresh)
        trials_2.addData('response5disk_2.started', response5disk_2.tStartRefresh)
        trials_2.addData('response5disk_2.stopped', response5disk_2.tStopRefresh)
        trials_2.addData('response7disk_2.started', response7disk_2.tStartRefresh)
        trials_2.addData('response7disk_2.stopped', response7disk_2.tStopRefresh)
        trials_2.addData('rectangle.started', rectangle.tStartRefresh)
        trials_2.addData('rectangle.stopped', rectangle.tStopRefresh)
        trials_2.addData('text_25.started', text_25.tStartRefresh)
        trials_2.addData('text_25.stopped', text_25.tStopRefresh)
        trials_2.addData('text_24.started', text_24.tStartRefresh)
        trials_2.addData('text_24.stopped', text_24.tStopRefresh)
        # the Routine "response_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "special_trial"-------
        continueRoutine = True
        routineTimer.add(0.250000)
        # update component parameters for each repeat
        # keep track of which components have finished
        special_trialComponents = [text_33]
        for thisComponent in special_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        special_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "special_trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = special_trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=special_trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_33* updates
            if text_33.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_33.frameNStart = frameN  # exact frame index
                text_33.tStart = t  # local t and not account for scr refresh
                text_33.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_33, 'tStartRefresh')  # time at next scr refresh
                text_33.setAutoDraw(True)
            if text_33.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_33.tStartRefresh + .250-frameTolerance:
                    # keep track of stop time/frame for later
                    text_33.tStop = t  # not accounting for scr refresh
                    text_33.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_33, 'tStopRefresh')  # time at next scr refresh
                    text_33.setAutoDraw(False)
            # Run catch trials 
            if not ((trialnumber == catchtrialorder[0]) or (trialnumber == catchtrialorder[1]) or (trialnumber == catchtrialorder[2]) or (trialnumber == catchtrialorder[3]) or (trialnumber == catchtrialorder[4]) or (trialnumber == catchtrialorder[5]) or (trialnumber == catchtrialorder[6]) or (trialnumber == catchtrialorder[7]) or (trialnumber == catchtrialorder[8]) or (trialnumber == catchtrialorder[9]) or (trialnumber == catchtrialorder[10]) or (trialnumber == catchtrialorder[11]) or (trialnumber == catchtrialorder[12]) or (trialnumber == catchtrialorder[13]) or (trialnumber == catchtrialorder[14]) or (trialnumber == catchtrialorder[15]) or (trialnumber == catchtrialorder[16]) or (trialnumber == catchtrialorder[17]) or (trialnumber == catchtrialorder[18]) or (trialnumber == catchtrialorder[19])):
                continueRoutine=False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in special_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "special_trial"-------
        for thisComponent in special_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_2.addData('text_33.started', text_33.tStartRefresh)
        trials_2.addData('text_33.stopped', text_33.tStopRefresh)
        
        # ------Prepare to start Routine "catch_1"-------
        continueRoutine = True
        # update component parameters for each repeat
        # setup some python lists for storing info about the mouse_3
        mouse_3.clicked_name = []
        gotValidClick = False  # until a click is received
        # Select random number for catch trial
        
        catchnumber = randint(0,7);
        
        event.clearEvents()
        
        catchtext = f'SPECIAL TRIAL PLEASE CLICK AND HOLD {catchnumber}'
        text_26.setText(catchtext)
        # keep track of which components have finished
        catch_1Components = [mouse_3, response1disk_3, response3disk_3, response5disk_3, response7disk_3, text_26, rectangle_2]
        for thisComponent in catch_1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        catch_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "catch_1"-------
        while continueRoutine:
            # get current time
            t = catch_1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=catch_1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # *mouse_3* updates
            if mouse_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_3.frameNStart = frameN  # exact frame index
                mouse_3.tStart = t  # local t and not account for scr refresh
                mouse_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_3, 'tStartRefresh')  # time at next scr refresh
                mouse_3.status = STARTED
                mouse_3.mouseClock.reset()
                prevButtonState = mouse_3.getPressed()  # if button is down already this ISN'T a new click
            if mouse_3.status == STARTED:  # only update if started and not finished!
                buttons = mouse_3.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [response1disk_3,response3disk_3,response5disk_3,response7disk_3,]:
                            if obj.contains(mouse_3):
                                gotValidClick = True
                                mouse_3.clicked_name.append(obj.name)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # *response1disk_3* updates
            if response1disk_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                response1disk_3.frameNStart = frameN  # exact frame index
                response1disk_3.tStart = t  # local t and not account for scr refresh
                response1disk_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response1disk_3, 'tStartRefresh')  # time at next scr refresh
                response1disk_3.setAutoDraw(True)
            
            # *response3disk_3* updates
            if response3disk_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                response3disk_3.frameNStart = frameN  # exact frame index
                response3disk_3.tStart = t  # local t and not account for scr refresh
                response3disk_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response3disk_3, 'tStartRefresh')  # time at next scr refresh
                response3disk_3.setAutoDraw(True)
            
            # *response5disk_3* updates
            if response5disk_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                response5disk_3.frameNStart = frameN  # exact frame index
                response5disk_3.tStart = t  # local t and not account for scr refresh
                response5disk_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response5disk_3, 'tStartRefresh')  # time at next scr refresh
                response5disk_3.setAutoDraw(True)
            
            # *response7disk_3* updates
            if response7disk_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                response7disk_3.frameNStart = frameN  # exact frame index
                response7disk_3.tStart = t  # local t and not account for scr refresh
                response7disk_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response7disk_3, 'tStartRefresh')  # time at next scr refresh
                response7disk_3.setAutoDraw(True)
            # Run catch trials 
            if not ((trialnumber == catchtrialorder[0]) or (trialnumber == catchtrialorder[1]) or (trialnumber == catchtrialorder[2]) or (trialnumber == catchtrialorder[3]) or (trialnumber == catchtrialorder[4]) or (trialnumber == catchtrialorder[5]) or (trialnumber == catchtrialorder[6]) or (trialnumber == catchtrialorder[7]) or (trialnumber == catchtrialorder[8]) or (trialnumber == catchtrialorder[9]) or (trialnumber == catchtrialorder[10]) or (trialnumber == catchtrialorder[11]) or (trialnumber == catchtrialorder[12]) or (trialnumber == catchtrialorder[13]) or (trialnumber == catchtrialorder[14]) or (trialnumber == catchtrialorder[15]) or (trialnumber == catchtrialorder[16]) or (trialnumber == catchtrialorder[17]) or (trialnumber == catchtrialorder[18]) or (trialnumber == catchtrialorder[19])):
                continueRoutine=False
            
            # *text_26* updates
            if text_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_26.frameNStart = frameN  # exact frame index
                text_26.tStart = t  # local t and not account for scr refresh
                text_26.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_26, 'tStartRefresh')  # time at next scr refresh
                text_26.setAutoDraw(True)
            
            # *rectangle_2* updates
            if rectangle_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rectangle_2.frameNStart = frameN  # exact frame index
                rectangle_2.tStart = t  # local t and not account for scr refresh
                rectangle_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rectangle_2, 'tStartRefresh')  # time at next scr refresh
                rectangle_2.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in catch_1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "catch_1"-------
        for thisComponent in catch_1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for trials_2 (TrialHandler)
        x, y = mouse_3.getPos()
        buttons = mouse_3.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            for obj in [response1disk_3,response3disk_3,response5disk_3,response7disk_3,]:
                if obj.contains(mouse_3):
                    gotValidClick = True
                    mouse_3.clicked_name.append(obj.name)
        trials_2.addData('mouse_3.x', x)
        trials_2.addData('mouse_3.y', y)
        trials_2.addData('mouse_3.leftButton', buttons[0])
        trials_2.addData('mouse_3.midButton', buttons[1])
        trials_2.addData('mouse_3.rightButton', buttons[2])
        if len(mouse_3.clicked_name):
            trials_2.addData('mouse_3.clicked_name', mouse_3.clicked_name[0])
        trials_2.addData('mouse_3.started', mouse_3.tStart)
        trials_2.addData('mouse_3.stopped', mouse_3.tStop)
        trials_2.addData('response1disk_3.started', response1disk_3.tStartRefresh)
        trials_2.addData('response1disk_3.stopped', response1disk_3.tStopRefresh)
        trials_2.addData('response3disk_3.started', response3disk_3.tStartRefresh)
        trials_2.addData('response3disk_3.stopped', response3disk_3.tStopRefresh)
        trials_2.addData('response5disk_3.started', response5disk_3.tStartRefresh)
        trials_2.addData('response5disk_3.stopped', response5disk_3.tStopRefresh)
        trials_2.addData('response7disk_3.started', response7disk_3.tStartRefresh)
        trials_2.addData('response7disk_3.stopped', response7disk_3.tStopRefresh)
        # Save similarity rating 
        mousexpos=mouse.getPos()[0]  # get x position of mouse
        mouseypos=mouse.getPos()[1]  # get y position of mouse
        
        # Triangle 7
        x11d = a - b/2;
        y11d = a + b/2;
        x12d = a + b/2;
        y12d = a + b/2;
        x13d = a - b/2;
        y13d = a - b/2;
        a1d = ((y12d - y13d)*(mousexpos - x13d) + (x13d - x12d)*(mouseypos - y13d)) / ((y12d - y13d)*(x11d - x13d)+(x13d - x12d)*(y11d - y13d))
        b1d = ((y13d - y11d)*(mousexpos - x13d) + (x11d - x13d)*(mouseypos - y13d)) / ((y12d - y13d)*(x11d - x13d)+(x13d - x12d)*(y11d - y13d))
        c1d = 1 - a1d - b1d;
        
        # Triangle 6 
        x21d = a - b/2;
        y21d = a - b/2
        x22d = a + b/2
        y22d = a + b/2
        x23d = a + b/2
        y23d = a - b/2
        a2d = ((y22d - y23d)*(mousexpos - x23d) + (x23d - x22d)*(mouseypos - y23d)) / ((y22d - y23d)*(x21d - x23d)+(x23d - x22d)*(y21d - y23d))
        b2d = ((y23d - y21d)*(mousexpos - x23d) + (x21d - x23d)*(mouseypos - y23d)) / ((y22d - y23d)*(x21d - x23d)+(x23d - x22d)*(y21d - y23d))
        c2d = 1 - a2d - b2d
        
        # Triangle 5
        x31d = a - b/2
        y31d = -(a - b/2)
        x32d = a + b/2
        y32d = -(a - b/2) 
        x33d = a + b/2
        y33d = -(a + b/2)
        a3d = ((y32d - y33d)*(mousexpos - x33d) + (x33d - x32d)*(mouseypos - y33d)) / ((y32d - y33d)*(x31d - x33d)+(x33d - x32d)*(y31d - y33d))
        b3d = ((y33d - y31d)*(mousexpos - x33d) + (x31d - x33d)*(mouseypos - y33d)) / ((y32d - y33d)*(x31d - x33d)+(x33d - x32d)*(y31d - y33d))
        c3d = 1 - a3d - b3d
        
        
        # Triangle 4 
        x41d = a - b/2
        y41d = -(a - b/2)
        x42d = a + b/2
        y42d = -(a + b/2)
        x43d = a - b/2
        y43d = -(a + b/2)
        a4d = ((y42d - y43d)*(mousexpos - x43d) + (x43d - x42d)*(mouseypos - y43d)) / ((y42d - y43d)*(x41d - x43d)+(x43d - x42d)*(y41d - y43d))
        b4d = ((y43d - y41d)*(mousexpos - x43d) + (x41d - x43d)*(mouseypos - y43d)) / ((y42d - y43d)*(x41d - x43d)+(x43d - x42d)*(y41d - y43d))
        c4d = 1 - a4d - b4d
        
        #  Triangle 3
        x51d = -(a + b/2)
        y51d = -(a + b/2)
        x52d = -(a - b/2)
        y52d = -(a - b/2)
        x53d = -(a - b/2)
        y53d = -(a + b/2)
        a5d = ((y52d - y53d)*(mousexpos - x53d) + (x53d - x52d)*(mouseypos - y53d)) / ((y52d - y53d)*(x51d - x53d)+(x53d - x52d)*(y51d - y53d))
        b5d = ((y53d - y51d)*(mousexpos - x53d) + (x51d - x53d)*(mouseypos - y53d)) / ((y52d - y53d)*(x51d - x53d)+(x53d - x52d)*(y51d - y53d))
        c5d = 1 - a5d - b5d
        
        # Triangle 2
        x61d = -(a+b/2)
        y61d = -(a+b/2)
        x62d = -(a-b/2)
        y62d = -(a-b/2)
        x63d = -(a+b/2)
        y63d = - (a+b/2)
        a6d = ((y62d - y63d)*(mousexpos - x63d) + (x63d - x62d)*(mouseypos - y63d)) / ((y62d - y63d)*(x61d - x63d)+(x63d - x62d)*(y61d - y63d))
        b6d = ((y63d - y61d)*(mousexpos - x63d) + (x61d - x63d)*(mouseypos - y63d)) / ((y62d - y63d)*(x61d - x63d)+(x63d - x62d)*(y61d - y63d))
        c6d = 1 - a6d - b6d
        
        # Triangle 1 
        
        x71d = -(a + b/2)
        y71d = a + b/2
        x72d = -(a - b/2)
        y72d = a - b/2
        x73d = -(a + b/2)
        y73d = a - b/2
        a7d = ((y72d - y73d)*(mousexpos - x73d) + (x73d - x72d)*(mouseypos - y73d)) / ((y72d - y73d)*(x71d - x73d)+(x73d - x72d)*(y71d - y73d))
        b7d = ((y73d - y71d)*(mousexpos - x73d) + (x71d - x73d)*(mouseypos - y73d)) / ((y72d - y73d)*(x71d - x73d)+(x73d - x72d)*(y71d - y73d))
        c7d = 1 - a7d - b7d
        
        
        # Triangle 0 
        x81d = -(a + b/2)
        y81d = a + b/2
        x82d = -(a - b/2)
        y82d = a + b/2
        x83d = -(a - b/2)
        y83d = a - b/2
        a8d = ((y82d - y83d)*(mousexpos - x83d) + (x83d - x82d)*(mouseypos - y83d)) / ((y82d - y83d)*(x81d - x83d)+(x83d - x82d)*(y81d - y83d))
        b8d = ((y83d - y81d)*(mousexpos - x83d) + (x81d - x83d)*(mouseypos - y83d)) / ((y82d - y83d)*(x81d - x83d)+(x83d - x82d)*(y81d - y83d))
        c8d = 1 - a8d - b8d
        
        
        
        
        
        if (0 <= a1d <= 1) and (0 <= b1d <= 1) and (0 <= c1d <= 1):
            catchresponse  = 7
        elif (0 <= a2d <= 1) and (0 <= b2d <= 1) and (0 <= c2d <= 1):
            catchresponse  = 6
        elif (0 <= a3d <= 1) and (0 <= b3d <= 1) and (0 <= c3d <= 1):
            catchresponse  = 5
        elif (0 <= a4d <= 1) and (0 <= b4d <= 1) and (0 <= c4d <= 1):
            catchresponse  = 4
        elif (0 <= a5d <= 1) and (0 <= b5d <= 1) and (0 <= c5d <= 1):
            catchresponse  = 3
        elif (0 <= a6d <= 1) and (0 <= b6d <= 1) and (0 <= c6d <= 1):
            catchresponse  = 2
        elif (0 <= a7d <= 1) and (0 <= b7d <= 1) and (0 <= c7d <= 1):
            catchresponse  = 1
        elif (0 <= a8d <= 1) and (0 <= b8d <= 1) and (0 <= c8d <= 1):
            catchresponse = 0
        
        
        thisExp.addData("catchresponse", catchresponse);
        thisExp.addData("catchnumber", catchnumber);
        thisExp.addData("catchtrialorder", catchtrialorder);
        thisExp.addData("response_time_catch", mouse_3.mouseClock.getTime())  # Save time relative to start of mouse
        
        
        trials_2.addData('text_26.started', text_26.tStartRefresh)
        trials_2.addData('text_26.stopped', text_26.tStopRefresh)
        trials_2.addData('rectangle_2.started', rectangle_2.tStartRefresh)
        trials_2.addData('rectangle_2.stopped', rectangle_2.tStopRefresh)
        # the Routine "catch_1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "response_sum"-------
        continueRoutine = True
        # update component parameters for each repeat
        # setup some python lists for storing info about the mouse_11
        mouse_11.clicked_name = []
        gotValidClick = False  # until a click is received
        rectangle_9.setFillColor(grey)
        trialnumbertext = f'You have finished {trialnumber} of 324 questions';
        
        event.clearEvents()
        
        # Run catch trials 
        if not ((trialnumber == catchtrialorder[0]) or (trialnumber == catchtrialorder[1]) or (trialnumber == catchtrialorder[2]) or (trialnumber == catchtrialorder[3]) or (trialnumber == catchtrialorder[4]) or (trialnumber == catchtrialorder[5]) or (trialnumber == catchtrialorder[6]) or (trialnumber == catchtrialorder[7]) or (trialnumber == catchtrialorder[8]) or (trialnumber == catchtrialorder[9]) or (trialnumber == catchtrialorder[10]) or (trialnumber == catchtrialorder[11]) or (trialnumber == catchtrialorder[12]) or (trialnumber == catchtrialorder[13]) or (trialnumber == catchtrialorder[14]) or (trialnumber == catchtrialorder[15]) or (trialnumber == catchtrialorder[16]) or (trialnumber == catchtrialorder[17]) or (trialnumber == catchtrialorder[18]) or (trialnumber == catchtrialorder[19])):
            continueRoutine=False
        text_52.setText(trialnumbertext)
        # keep track of which components have finished
        response_sumComponents = [mouse_11, response1disk_11, response3disk_11, response5disk_11, response7disk_11, rectangle_9, text_51, text_52]
        for thisComponent in response_sumComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        response_sumClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "response_sum"-------
        while continueRoutine:
            # get current time
            t = response_sumClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=response_sumClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # *mouse_11* updates
            if mouse_11.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_11.frameNStart = frameN  # exact frame index
                mouse_11.tStart = t  # local t and not account for scr refresh
                mouse_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_11, 'tStartRefresh')  # time at next scr refresh
                mouse_11.status = STARTED
                mouse_11.mouseClock.reset()
                prevButtonState = mouse_11.getPressed()  # if button is down already this ISN'T a new click
            if mouse_11.status == STARTED:  # only update if started and not finished!
                buttons = mouse_11.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [rectangle]:
                            if obj.contains(mouse_11):
                                gotValidClick = True
                                mouse_11.clicked_name.append(obj.name)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # *response1disk_11* updates
            if response1disk_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                response1disk_11.frameNStart = frameN  # exact frame index
                response1disk_11.tStart = t  # local t and not account for scr refresh
                response1disk_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response1disk_11, 'tStartRefresh')  # time at next scr refresh
                response1disk_11.setAutoDraw(True)
            
            # *response3disk_11* updates
            if response3disk_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                response3disk_11.frameNStart = frameN  # exact frame index
                response3disk_11.tStart = t  # local t and not account for scr refresh
                response3disk_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response3disk_11, 'tStartRefresh')  # time at next scr refresh
                response3disk_11.setAutoDraw(True)
            
            # *response5disk_11* updates
            if response5disk_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                response5disk_11.frameNStart = frameN  # exact frame index
                response5disk_11.tStart = t  # local t and not account for scr refresh
                response5disk_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response5disk_11, 'tStartRefresh')  # time at next scr refresh
                response5disk_11.setAutoDraw(True)
            
            # *response7disk_11* updates
            if response7disk_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                response7disk_11.frameNStart = frameN  # exact frame index
                response7disk_11.tStart = t  # local t and not account for scr refresh
                response7disk_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response7disk_11, 'tStartRefresh')  # time at next scr refresh
                response7disk_11.setAutoDraw(True)
            
            # *rectangle_9* updates
            if rectangle_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rectangle_9.frameNStart = frameN  # exact frame index
                rectangle_9.tStart = t  # local t and not account for scr refresh
                rectangle_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rectangle_9, 'tStartRefresh')  # time at next scr refresh
                rectangle_9.setAutoDraw(True)
            # Run catch trials 
            if not ((trialnumber == catchtrialorder[0]) or (trialnumber == catchtrialorder[1]) or (trialnumber == catchtrialorder[2]) or (trialnumber == catchtrialorder[3]) or (trialnumber == catchtrialorder[4]) or (trialnumber == catchtrialorder[5]) or (trialnumber == catchtrialorder[6]) or (trialnumber == catchtrialorder[7]) or (trialnumber == catchtrialorder[8]) or (trialnumber == catchtrialorder[9]) or (trialnumber == catchtrialorder[10]) or (trialnumber == catchtrialorder[11]) or (trialnumber == catchtrialorder[12]) or (trialnumber == catchtrialorder[13]) or (trialnumber == catchtrialorder[14]) or (trialnumber == catchtrialorder[15]) or (trialnumber == catchtrialorder[16]) or (trialnumber == catchtrialorder[17]) or (trialnumber == catchtrialorder[18]) or (trialnumber == catchtrialorder[19])):
                continueRoutine=False
            
            # *text_51* updates
            if text_51.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_51.frameNStart = frameN  # exact frame index
                text_51.tStart = t  # local t and not account for scr refresh
                text_51.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_51, 'tStartRefresh')  # time at next scr refresh
                text_51.setAutoDraw(True)
            
            # *text_52* updates
            if text_52.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_52.frameNStart = frameN  # exact frame index
                text_52.tStart = t  # local t and not account for scr refresh
                text_52.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_52, 'tStartRefresh')  # time at next scr refresh
                text_52.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in response_sumComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "response_sum"-------
        for thisComponent in response_sumComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for trials_2 (TrialHandler)
        x, y = mouse_11.getPos()
        buttons = mouse_11.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            for obj in [rectangle]:
                if obj.contains(mouse_11):
                    gotValidClick = True
                    mouse_11.clicked_name.append(obj.name)
        trials_2.addData('mouse_11.x', x)
        trials_2.addData('mouse_11.y', y)
        trials_2.addData('mouse_11.leftButton', buttons[0])
        trials_2.addData('mouse_11.midButton', buttons[1])
        trials_2.addData('mouse_11.rightButton', buttons[2])
        if len(mouse_11.clicked_name):
            trials_2.addData('mouse_11.clicked_name', mouse_11.clicked_name[0])
        trials_2.addData('mouse_11.started', mouse_11.tStart)
        trials_2.addData('mouse_11.stopped', mouse_11.tStop)
        trials_2.addData('response1disk_11.started', response1disk_11.tStartRefresh)
        trials_2.addData('response1disk_11.stopped', response1disk_11.tStopRefresh)
        trials_2.addData('response3disk_11.started', response3disk_11.tStartRefresh)
        trials_2.addData('response3disk_11.stopped', response3disk_11.tStopRefresh)
        trials_2.addData('response5disk_11.started', response5disk_11.tStartRefresh)
        trials_2.addData('response5disk_11.stopped', response5disk_11.tStopRefresh)
        trials_2.addData('response7disk_11.started', response7disk_11.tStartRefresh)
        trials_2.addData('response7disk_11.stopped', response7disk_11.tStopRefresh)
        trials_2.addData('rectangle_9.started', rectangle_9.tStartRefresh)
        trials_2.addData('rectangle_9.stopped', rectangle_9.tStopRefresh)
        trials_2.addData('text_51.started', text_51.tStartRefresh)
        trials_2.addData('text_51.stopped', text_51.tStopRefresh)
        trials_2.addData('text_52.started', text_52.tStartRefresh)
        trials_2.addData('text_52.stopped', text_52.tStopRefresh)
        # the Routine "response_sum" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials_2'
    
    thisExp.nextEntry()
    
# completed 2 repeats of 'trials_3'


# ------Prepare to start Routine "survey1"-------
continueRoutine = True
# update component parameters for each repeat
textFill_5 = ''
# keep track of which components have finished
survey1Components = [copyText_1, question_4, submitanswer]
for thisComponent in survey1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
survey1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "survey1"-------
while continueRoutine:
    # get current time
    t = survey1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=survey1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *copyText_1* updates
    if copyText_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        copyText_1.frameNStart = frameN  # exact frame index
        copyText_1.tStart = t  # local t and not account for scr refresh
        copyText_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(copyText_1, 'tStartRefresh')  # time at next scr refresh
        copyText_1.setAutoDraw(True)
    keys = event.getKeys()
    if 'escape' in keys:
        core.quit()  # So you can quit
    else:
        if keys:
            if keys[0] == 'space':
                textFill_1 += ' '  # Adds a space instead of 'space'
            if keys[0] == 'backspace':
                textFill_1 = textFill_1[:-1]  # Deletes 
            elif keys[0] == 'period':
                textFill_1 += '.'
            elif keys[0] in allLetters:
                textFill_1+=keys[0]  # Adds character to text if in alphabet.
            copyText_1.setText(textFill_1)  # Set new text on screen
    
    # *question_4* updates
    if question_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        question_4.frameNStart = frameN  # exact frame index
        question_4.tStart = t  # local t and not account for scr refresh
        question_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(question_4, 'tStartRefresh')  # time at next scr refresh
        question_4.setAutoDraw(True)
    
    # *submitanswer* updates
    if submitanswer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        submitanswer.frameNStart = frameN  # exact frame index
        submitanswer.tStart = t  # local t and not account for scr refresh
        submitanswer.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(submitanswer, 'tStartRefresh')  # time at next scr refresh
        submitanswer.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in survey1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "survey1"-------
for thisComponent in survey1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('copyText_1.started', copyText_1.tStartRefresh)
thisExp.addData('copyText_1.stopped', copyText_1.tStopRefresh)
thisExp.addData('answer1', textFill_1)
thisExp.nextEntry()



thisExp.addData('question_4.started', question_4.tStartRefresh)
thisExp.addData('question_4.stopped', question_4.tStopRefresh)
thisExp.addData('submitanswer.started', submitanswer.tStartRefresh)
thisExp.addData('submitanswer.stopped', submitanswer.tStopRefresh)
# the Routine "survey1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "survey2"-------
continueRoutine = True
# update component parameters for each repeat
textFill_2 = ''
# keep track of which components have finished
survey2Components = [copyText_2, question, submitanswer_2]
for thisComponent in survey2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
survey2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "survey2"-------
while continueRoutine:
    # get current time
    t = survey2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=survey2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *copyText_2* updates
    if copyText_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        copyText_2.frameNStart = frameN  # exact frame index
        copyText_2.tStart = t  # local t and not account for scr refresh
        copyText_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(copyText_2, 'tStartRefresh')  # time at next scr refresh
        copyText_2.setAutoDraw(True)
    keys = event.getKeys()
    if 'escape' in keys:
        core.quit()  # So you can quit
    else:
        if keys:
            if keys[0] == 'space':
                textFill_2 += ' '  # Adds a space instead of 'space'
            if keys[0] == 'backspace':
                textFill_2 = textFill_2[:-1]  # Deletes 
            elif keys[0] == 'period':
                textFill_2 += '.'
            elif keys[0] in allLetters:
                textFill_2+=keys[0]  # Adds character to text if in alphabet.
            copyText_2.setText(textFill_2)  # Set new text on screen
    
    # *question* updates
    if question.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        question.frameNStart = frameN  # exact frame index
        question.tStart = t  # local t and not account for scr refresh
        question.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(question, 'tStartRefresh')  # time at next scr refresh
        question.setAutoDraw(True)
    
    # *submitanswer_2* updates
    if submitanswer_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        submitanswer_2.frameNStart = frameN  # exact frame index
        submitanswer_2.tStart = t  # local t and not account for scr refresh
        submitanswer_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(submitanswer_2, 'tStartRefresh')  # time at next scr refresh
        submitanswer_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in survey2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "survey2"-------
for thisComponent in survey2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('copyText_2.started', copyText_2.tStartRefresh)
thisExp.addData('copyText_2.stopped', copyText_2.tStopRefresh)
thisExp.addData('answer2', textFill_2)
thisExp.nextEntry()



thisExp.addData('question.started', question.tStartRefresh)
thisExp.addData('question.stopped', question.tStopRefresh)
thisExp.addData('submitanswer_2.started', submitanswer_2.tStartRefresh)
thisExp.addData('submitanswer_2.stopped', submitanswer_2.tStopRefresh)
# the Routine "survey2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "survey3"-------
continueRoutine = True
# update component parameters for each repeat
textFill_3 = ''
# keep track of which components have finished
survey3Components = [copyText_3, question_2, submitanswer_3]
for thisComponent in survey3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
survey3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "survey3"-------
while continueRoutine:
    # get current time
    t = survey3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=survey3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *copyText_3* updates
    if copyText_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        copyText_3.frameNStart = frameN  # exact frame index
        copyText_3.tStart = t  # local t and not account for scr refresh
        copyText_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(copyText_3, 'tStartRefresh')  # time at next scr refresh
        copyText_3.setAutoDraw(True)
    keys = event.getKeys()
    if 'escape' in keys:
        core.quit()  # So you can quit
    else:
        if keys:
            if keys[0] == 'space':
                textFill_3 += ' '  # Adds a space instead of 'space'
            if keys[0] == 'backspace':
                textFill_3 = textFill_3[:-1]  # Deletes 
            elif keys[0] == 'period':
                textFill_3 += '.'
            elif keys[0] in allLetters:
                textFill_3+=keys[0]  # Adds character to text if in alphabet.
            copyText_3.setText(textFill_3)  # Set new text on screen
    
    # *question_2* updates
    if question_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        question_2.frameNStart = frameN  # exact frame index
        question_2.tStart = t  # local t and not account for scr refresh
        question_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(question_2, 'tStartRefresh')  # time at next scr refresh
        question_2.setAutoDraw(True)
    
    # *submitanswer_3* updates
    if submitanswer_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        submitanswer_3.frameNStart = frameN  # exact frame index
        submitanswer_3.tStart = t  # local t and not account for scr refresh
        submitanswer_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(submitanswer_3, 'tStartRefresh')  # time at next scr refresh
        submitanswer_3.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in survey3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "survey3"-------
for thisComponent in survey3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('copyText_3.started', copyText_3.tStartRefresh)
thisExp.addData('copyText_3.stopped', copyText_3.tStopRefresh)
thisExp.addData('answer3', textFill_3)
thisExp.nextEntry()



thisExp.addData('question_2.started', question_2.tStartRefresh)
thisExp.addData('question_2.stopped', question_2.tStopRefresh)
thisExp.addData('submitanswer_3.started', submitanswer_3.tStartRefresh)
thisExp.addData('submitanswer_3.stopped', submitanswer_3.tStopRefresh)
# the Routine "survey3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "survey_4"-------
continueRoutine = True
# update component parameters for each repeat
textFill_4 = ''
# keep track of which components have finished
survey_4Components = [copyText_4, question_3, submitanswer_4]
for thisComponent in survey_4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
survey_4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "survey_4"-------
while continueRoutine:
    # get current time
    t = survey_4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=survey_4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *copyText_4* updates
    if copyText_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        copyText_4.frameNStart = frameN  # exact frame index
        copyText_4.tStart = t  # local t and not account for scr refresh
        copyText_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(copyText_4, 'tStartRefresh')  # time at next scr refresh
        copyText_4.setAutoDraw(True)
    keys = event.getKeys()
    if 'escape' in keys:
        core.quit()  # So you can quit
    else:
        if keys:
            if keys[0] == 'space':
                textFill_4 += ' '  # Adds a space instead of 'space'
            if keys[0] == 'backspace':
                textFill_4 = textFill_4[:-1]  # Deletes 
            elif keys[0] == 'period':
                textFill_4 += '.'
            elif keys[0] in allLetters:
                textFill_4+=keys[0]  # Adds character to text if in alphabet.
            copyText_4.setText(textFill_4)  # Set new text on screen
    
    # *question_3* updates
    if question_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        question_3.frameNStart = frameN  # exact frame index
        question_3.tStart = t  # local t and not account for scr refresh
        question_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(question_3, 'tStartRefresh')  # time at next scr refresh
        question_3.setAutoDraw(True)
    
    # *submitanswer_4* updates
    if submitanswer_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        submitanswer_4.frameNStart = frameN  # exact frame index
        submitanswer_4.tStart = t  # local t and not account for scr refresh
        submitanswer_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(submitanswer_4, 'tStartRefresh')  # time at next scr refresh
        submitanswer_4.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in survey_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "survey_4"-------
for thisComponent in survey_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('copyText_4.started', copyText_4.tStartRefresh)
thisExp.addData('copyText_4.stopped', copyText_4.tStopRefresh)
thisExp.addData('answer4', textFill_4)
thisExp.nextEntry()



thisExp.addData('question_3.started', question_3.tStartRefresh)
thisExp.addData('question_3.stopped', question_3.tStopRefresh)
thisExp.addData('submitanswer_4.started', submitanswer_4.tStartRefresh)
thisExp.addData('submitanswer_4.stopped', submitanswer_4.tStopRefresh)
# the Routine "survey_4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "survey5"-------
continueRoutine = True
# update component parameters for each repeat
textFill_5 = ''
# keep track of which components have finished
survey5Components = [copyText_5, question_5, submitanswer_5]
for thisComponent in survey5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
survey5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "survey5"-------
while continueRoutine:
    # get current time
    t = survey5Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=survey5Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *copyText_5* updates
    if copyText_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        copyText_5.frameNStart = frameN  # exact frame index
        copyText_5.tStart = t  # local t and not account for scr refresh
        copyText_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(copyText_5, 'tStartRefresh')  # time at next scr refresh
        copyText_5.setAutoDraw(True)
    keys = event.getKeys()
    if 'escape' in keys:
        core.quit()  # So you can quit
    else:
        if keys:
            #if keys[0] == 'space':
                #textFill_5 += ' '  # Adds a space instead of 'space'
            if keys[0] == 'backspace':
                textFill_5 = textFill_5[:-1]  # Deletes 
            elif keys[0] == 'period':
                textFill_5 += '.'
            elif keys[0] in allLetters:
                textFill_5+=keys[0]  # Adds character to text if in alphabet.
            copyText_5.setText(textFill_5)  # Set new text on screen
    
    # *question_5* updates
    if question_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        question_5.frameNStart = frameN  # exact frame index
        question_5.tStart = t  # local t and not account for scr refresh
        question_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(question_5, 'tStartRefresh')  # time at next scr refresh
        question_5.setAutoDraw(True)
    
    # *submitanswer_5* updates
    if submitanswer_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        submitanswer_5.frameNStart = frameN  # exact frame index
        submitanswer_5.tStart = t  # local t and not account for scr refresh
        submitanswer_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(submitanswer_5, 'tStartRefresh')  # time at next scr refresh
        submitanswer_5.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in survey5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "survey5"-------
for thisComponent in survey5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('copyText_5.started', copyText_5.tStartRefresh)
thisExp.addData('copyText_5.stopped', copyText_5.tStopRefresh)
thisExp.addData('answer5', textFill_5)
thisExp.nextEntry()



thisExp.addData('question_5.started', question_5.tStartRefresh)
thisExp.addData('question_5.stopped', question_5.tStopRefresh)
thisExp.addData('submitanswer_5.started', submitanswer_5.tStartRefresh)
thisExp.addData('submitanswer_5.stopped', submitanswer_5.tStopRefresh)
# the Routine "survey5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "survey6"-------
continueRoutine = True
# update component parameters for each repeat
textFill_6 = ''
# keep track of which components have finished
survey6Components = [copyText_6, question_6, submitanswer_6]
for thisComponent in survey6Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
survey6Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "survey6"-------
while continueRoutine:
    # get current time
    t = survey6Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=survey6Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *copyText_6* updates
    if copyText_6.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        copyText_6.frameNStart = frameN  # exact frame index
        copyText_6.tStart = t  # local t and not account for scr refresh
        copyText_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(copyText_6, 'tStartRefresh')  # time at next scr refresh
        copyText_6.setAutoDraw(True)
    keys = event.getKeys()
    if 'escape' in keys:
        core.quit()  # So you can quit
    else:
        if keys:
            if keys[0] == 'space':
                textFill_6 += ' '  # Adds a space instead of 'space'
            if keys[0] == 'backspace':
                textFill_6 = textFill_6[:-1]  # Deletes 
            elif keys[0] == 'period':
                textFill_6 += '.'
            elif keys[0] in allLetters:
                textFill_6+=keys[0]  # Adds character to text if in alphabet.
            copyText_6.setText(textFill_6)  # Set new text on screen
    
    # *question_6* updates
    if question_6.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        question_6.frameNStart = frameN  # exact frame index
        question_6.tStart = t  # local t and not account for scr refresh
        question_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(question_6, 'tStartRefresh')  # time at next scr refresh
        question_6.setAutoDraw(True)
    
    # *submitanswer_6* updates
    if submitanswer_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        submitanswer_6.frameNStart = frameN  # exact frame index
        submitanswer_6.tStart = t  # local t and not account for scr refresh
        submitanswer_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(submitanswer_6, 'tStartRefresh')  # time at next scr refresh
        submitanswer_6.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in survey6Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "survey6"-------
for thisComponent in survey6Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('copyText_6.started', copyText_6.tStartRefresh)
thisExp.addData('copyText_6.stopped', copyText_6.tStopRefresh)
thisExp.addData('answer6', textFill_6)
thisExp.nextEntry()



thisExp.addData('question_6.started', question_6.tStartRefresh)
thisExp.addData('question_6.stopped', question_6.tStopRefresh)
thisExp.addData('submitanswer_6.started', submitanswer_6.tStartRefresh)
thisExp.addData('submitanswer_6.stopped', submitanswer_6.tStopRefresh)
# the Routine "survey6" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "survey7"-------
continueRoutine = True
# update component parameters for each repeat
textFill_7 = ''
# keep track of which components have finished
survey7Components = [copyText_7, question_7, submitanswer_7]
for thisComponent in survey7Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
survey7Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "survey7"-------
while continueRoutine:
    # get current time
    t = survey7Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=survey7Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *copyText_7* updates
    if copyText_7.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        copyText_7.frameNStart = frameN  # exact frame index
        copyText_7.tStart = t  # local t and not account for scr refresh
        copyText_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(copyText_7, 'tStartRefresh')  # time at next scr refresh
        copyText_7.setAutoDraw(True)
    keys = event.getKeys()
    if 'escape' in keys:
        core.quit()  # So you can quit
    else:
        if keys:
            if keys[0] == 'space':
                textFill_7 += ' '  # Adds a space instead of 'space'
            if keys[0] == 'backspace':
                textFill_7 = textFill_7[:-1]  # Deletes 
            elif keys[0] == 'period':
                textFill_7 += '.'
            elif keys[0] in allLetters:
                textFill_7+=keys[0]  # Adds character to text if in alphabet.
            copyText_7.setText(textFill_7)  # Set new text on screen
    
    # *question_7* updates
    if question_7.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        question_7.frameNStart = frameN  # exact frame index
        question_7.tStart = t  # local t and not account for scr refresh
        question_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(question_7, 'tStartRefresh')  # time at next scr refresh
        question_7.setAutoDraw(True)
    
    # *submitanswer_7* updates
    if submitanswer_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        submitanswer_7.frameNStart = frameN  # exact frame index
        submitanswer_7.tStart = t  # local t and not account for scr refresh
        submitanswer_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(submitanswer_7, 'tStartRefresh')  # time at next scr refresh
        submitanswer_7.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in survey7Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "survey7"-------
for thisComponent in survey7Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('copyText_7.started', copyText_7.tStartRefresh)
thisExp.addData('copyText_7.stopped', copyText_7.tStopRefresh)
thisExp.addData('answer7', textFill_7)
thisExp.nextEntry()



thisExp.addData('question_7.started', question_7.tStartRefresh)
thisExp.addData('question_7.stopped', question_7.tStopRefresh)
thisExp.addData('submitanswer_7.started', submitanswer_7.tStartRefresh)
thisExp.addData('submitanswer_7.stopped', submitanswer_7.tStopRefresh)
# the Routine "survey7" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
