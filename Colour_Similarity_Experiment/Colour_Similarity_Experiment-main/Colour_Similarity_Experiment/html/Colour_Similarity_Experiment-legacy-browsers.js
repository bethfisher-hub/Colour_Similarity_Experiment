/************************************* 
 * Colour_Similarity_Experiment Test *
 *************************************/

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'pix',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'Colour_Similarity_Experiment';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(startupRoutineBegin());
flowScheduler.add(startupRoutineEachFrame());
flowScheduler.add(startupRoutineEnd());
flowScheduler.add(welcome_instrRoutineBegin());
flowScheduler.add(welcome_instrRoutineEachFrame());
flowScheduler.add(welcome_instrRoutineEnd());
flowScheduler.add(consentRoutineBegin());
flowScheduler.add(consentRoutineEachFrame());
flowScheduler.add(consentRoutineEnd());
flowScheduler.add(instr_1RoutineBegin());
flowScheduler.add(instr_1RoutineEachFrame());
flowScheduler.add(instr_1RoutineEnd());
flowScheduler.add(screen_scaleRoutineBegin());
flowScheduler.add(screen_scaleRoutineEachFrame());
flowScheduler.add(screen_scaleRoutineEnd());
flowScheduler.add(instr_2RoutineBegin());
flowScheduler.add(instr_2RoutineEachFrame());
flowScheduler.add(instr_2RoutineEnd());
flowScheduler.add(instr_3RoutineBegin());
flowScheduler.add(instr_3RoutineEachFrame());
flowScheduler.add(instr_3RoutineEnd());
flowScheduler.add(instr_4RoutineBegin());
flowScheduler.add(instr_4RoutineEachFrame());
flowScheduler.add(instr_4RoutineEnd());
flowScheduler.add(instr_5RoutineBegin());
flowScheduler.add(instr_5RoutineEachFrame());
flowScheduler.add(instr_5RoutineEnd());
flowScheduler.add(instr_6RoutineBegin());
flowScheduler.add(instr_6RoutineEachFrame());
flowScheduler.add(instr_6RoutineEnd());
flowScheduler.add(instr_7RoutineBegin());
flowScheduler.add(instr_7RoutineEachFrame());
flowScheduler.add(instr_7RoutineEnd());
flowScheduler.add(instr_8RoutineBegin());
flowScheduler.add(instr_8RoutineEachFrame());
flowScheduler.add(instr_8RoutineEnd());
flowScheduler.add(instr_9RoutineBegin());
flowScheduler.add(instr_9RoutineEachFrame());
flowScheduler.add(instr_9RoutineEnd());
flowScheduler.add(instr_10RoutineBegin());
flowScheduler.add(instr_10RoutineEachFrame());
flowScheduler.add(instr_10RoutineEnd());
flowScheduler.add(instr_11RoutineBegin());
flowScheduler.add(instr_11RoutineEachFrame());
flowScheduler.add(instr_11RoutineEnd());
flowScheduler.add(calibration_exampleRoutineBegin());
flowScheduler.add(calibration_exampleRoutineEachFrame());
flowScheduler.add(calibration_exampleRoutineEnd());
flowScheduler.add(instr_12RoutineBegin());
flowScheduler.add(instr_12RoutineEachFrame());
flowScheduler.add(instr_12RoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin, trialsLoopScheduler);
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(viewerdistanceRoutineBegin());
flowScheduler.add(viewerdistanceRoutineEachFrame());
flowScheduler.add(viewerdistanceRoutineEnd());
flowScheduler.add(viewerdistance_unsucessRoutineBegin());
flowScheduler.add(viewerdistance_unsucessRoutineEachFrame());
flowScheduler.add(viewerdistance_unsucessRoutineEnd());
flowScheduler.add(stim1_instrRoutineBegin());
flowScheduler.add(stim1_instrRoutineEachFrame());
flowScheduler.add(stim1_instrRoutineEnd());
flowScheduler.add(stim_response_instrRoutineBegin());
flowScheduler.add(stim_response_instrRoutineEachFrame());
flowScheduler.add(stim_response_instrRoutineEnd());
flowScheduler.add(catch_insrtRoutineBegin());
flowScheduler.add(catch_insrtRoutineEachFrame());
flowScheduler.add(catch_insrtRoutineEnd());
flowScheduler.add(colour_circle_instr_2RoutineBegin());
flowScheduler.add(colour_circle_instr_2RoutineEachFrame());
flowScheduler.add(colour_circle_instr_2RoutineEnd());
flowScheduler.add(instr_pracRoutineBegin());
flowScheduler.add(instr_pracRoutineEachFrame());
flowScheduler.add(instr_pracRoutineEnd());
const duringpracLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(duringpracLoopBegin, duringpracLoopScheduler);
flowScheduler.add(duringpracLoopScheduler);
flowScheduler.add(duringpracLoopEnd);
flowScheduler.add(beginRoutineBegin());
flowScheduler.add(beginRoutineEachFrame());
flowScheduler.add(beginRoutineEnd());
const trials_3LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_3LoopBegin, trials_3LoopScheduler);
flowScheduler.add(trials_3LoopScheduler);
flowScheduler.add(trials_3LoopEnd);
flowScheduler.add(survey1RoutineBegin());
flowScheduler.add(survey1RoutineEachFrame());
flowScheduler.add(survey1RoutineEnd());
flowScheduler.add(survey2RoutineBegin());
flowScheduler.add(survey2RoutineEachFrame());
flowScheduler.add(survey2RoutineEnd());
flowScheduler.add(survey3RoutineBegin());
flowScheduler.add(survey3RoutineEachFrame());
flowScheduler.add(survey3RoutineEnd());
flowScheduler.add(survey_4RoutineBegin());
flowScheduler.add(survey_4RoutineEachFrame());
flowScheduler.add(survey_4RoutineEnd());
flowScheduler.add(survey5RoutineBegin());
flowScheduler.add(survey5RoutineEachFrame());
flowScheduler.add(survey5RoutineEnd());
flowScheduler.add(survey6RoutineBegin());
flowScheduler.add(survey6RoutineEachFrame());
flowScheduler.add(survey6RoutineEnd());
flowScheduler.add(survey7RoutineBegin());
flowScheduler.add(survey7RoutineEachFrame());
flowScheduler.add(survey7RoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  });


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.1.2';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  psychoJS.setRedirectUrls('https://app.prolific.co/submissions/complete?cc=3C83396B', '');

  return Scheduler.Event.NEXT;
}


var startupClock;
var thisExp;
var win;
var event;
var shuffle;
var random;
var range;
var randint;
var pi;
var sin;
var cos;
var tan;
var sum;
var welcome_instrClock;
var text_54;
var welcome;
var key_resp;
var space;
var consentClock;
var text_53;
var key_resp_16;
var image;
var instr_1Clock;
var text_1;
var space_2;
var text_2;
var key_resp_2;
var screen_scaleClock;
var ccimage;
var round;
var oldt;
var x_size;
var y_size;
var x_scale;
var y_scale;
var dbase;
var unittext;
var vsize;
var text_37;
var instr_2Clock;
var text;
var key_resp_3;
var text_3;
var space_3;
var instr_3Clock;
var text_4;
var key_resp_4;
var thumb_size;
var calibrationline;
var instr_4Clock;
var text_5;
var key_resp_5;
var space_4;
var instr_5Clock;
var key_resp_6;
var space_5;
var instr_only;
var text_6;
var instr_6Clock;
var key_resp_8;
var space_7;
var instr_only_3;
var text_8;
var instr_7Clock;
var key_resp_7;
var space_6;
var instr_only_2;
var text_7;
var center_cross;
var instr_8Clock;
var key_resp_12;
var space_11;
var instr_only_5;
var text_13;
var center_cross_3;
var black_square;
var text_14;
var instr_9Clock;
var key_resp_11;
var space_8;
var instr_only_4;
var text_11;
var center_cross_2;
var black_square1;
var text_12;
var white_ball2;
var instr_10Clock;
var key_resp_18;
var space_17;
var instr_only_7;
var text_44;
var instr_11Clock;
var key_resp_21;
var space_18;
var instr_only_8;
var text_45;
var calibration_exampleClock;
var white_ball1;
var black_square3;
var text_19;
var text_20;
var white_ball12;
var text_21;
var text_22;
var white_ball13;
var instr_12Clock;
var key_resp_13;
var space_12;
var instr_only_6;
var text_15;
var ball_calibrationClock;
var black_square2;
var white_ball;
var key_resp_19;
var viewerdistancetotal;
var calibrationcount;
var text_39;
var white_ball1_2;
var viewerdistanceClock;
var peripheral_scale;
var radius_central;
var radius_peripheral;
var stimulus_size;
var response_stim_scale;
var distance_threshold;
var screen_x_threshold;
var text_38;
var text_40;
var key_resp_20;
var space_20;
var viewerdistance_unsucessClock;
var text_41;
var text_42;
var text_43;
var stim1_instrClock;
var stim1Clock;
var stim1;
var key_resp_14;
var space_13;
var text_16;
var stim_response_instrClock;
var movie_2Clock;
var movie_2;
var key_resp_15;
var space_14;
var text_17;
var catch_insrtClock;
var space_15;
var key_resp_17;
var movie_3Clock;
var movie_3;
var text_18;
var colour_circle_instr_2Clock;
var key_resp_9;
var intructioncircle_1;
var instructioncircle_2;
var instructioncircle_3;
var instructioncircle_4;
var instructioncircle_5;
var insturctioncircle_6;
var instructioncircle_7;
var instructioncircle_8;
var instructioncircle_9;
var space_9;
var text_9;
var instr_pracClock;
var space_10;
var text_10;
var key_resp_10;
var Stim1_display_pracClock;
var Circle;
var centre_cross4_2;
var response_pracClock;
var mouse_5;
var a;
var b;
var response1disk_5;
var response3disk_5;
var response5disk_5;
var response7disk_5;
var Circle_3;
var text_29;
var responseprac_feedbackClock;
var text_55;
var text_56;
var summary_pracClock;
var mouse_10;
var response1disk_10;
var response3disk_10;
var response5disk_10;
var response7disk_10;
var rectangle_8;
var pracnumber;
var text_49;
var text_50;
var special_trial_pracClock;
var text_36;
var catch_pracClock;
var mouse_7;
var response1disk_7;
var response3disk_7;
var response5disk_7;
var response7disk_7;
var catchtrialorderprac;
var catchnumberprac;
var text_32;
var rectangle_5;
var summary2_pracClock;
var mouse_6;
var response1disk_6;
var response3disk_6;
var response5disk_6;
var response7disk_6;
var rectangle_4;
var text_30;
var text_31;
var beginClock;
var space_19;
var text_46;
var key_resp_22;
var Stim1_displayClock;
var Circle_1;
var centre_cross4;
var responseClock;
var mouse;
var order;
var response1disk;
var response3disk;
var response5disk;
var response7disk;
var Circle_2;
var text_23;
var response_2Clock;
var mouse_2;
var response1disk_2;
var response3disk_2;
var response5disk_2;
var response7disk_2;
var rectangle;
var trialnumber;
var grey;
var text_25;
var text_24;
var special_trialClock;
var text_33;
var catch_1Clock;
var mouse_3;
var response1disk_3;
var response3disk_3;
var response5disk_3;
var response7disk_3;
var text_26;
var rectangle_2;
var response_sumClock;
var mouse_11;
var response1disk_11;
var response3disk_11;
var response5disk_11;
var response7disk_11;
var rectangle_9;
var text_51;
var text_52;
var survey1Clock;
var copyText_1;
var question_4;
var submitanswer;
var survey2Clock;
var copyText_2;
var question;
var submitanswer_2;
var survey3Clock;
var copyText_3;
var question_2;
var submitanswer_3;
var survey_4Clock;
var copyText_4;
var question_3;
var submitanswer_4;
var survey5Clock;
var copyText_5;
var question_5;
var submitanswer_5;
var survey6Clock;
var copyText_6;
var question_6;
var submitanswer_6;
var survey7Clock;
var copyText_7;
var question_7;
var submitanswer_7;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "startup"
  startupClock = new util.Clock();
  // Code to convert python to javascript that is not automatically converted
  
  thisExp=psychoJS.experiment;
  win=psychoJS.window;
  event=psychoJS.eventManager
  shuffle = function (a) {
      return util.shuffle(a);
  }
  random = function (a) {
      return Math.random();
  }
  range = function(start, end) {
      var ans = [];
      for (let i = start; i <= end; i++) {
          ans.push(i);
      }
      return ans;
  }
  
  
  randint = function(min, maxplusone) {
    return Math.floor(Math.random() * (maxplusone - min) ) + min;
  }
  
  Array.prototype.append = [].push
  pi=Math.PI;
  sin = Math.sin;
  cos = Math.cos;
  tan = Math.tan;
  
  sum = function (arr) {
  return arr.reduce((a,b)=>a+b)
  }
  
  
  
  // Initialize components for Routine "welcome_instr"
  welcome_instrClock = new util.Clock();
  text_54 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_54',
    text: 'You may quit the experiment at anytime by pressing <ESC>',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.3)], height: 0.1,  wrapWidth: 1000, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: 0.0 
  });
  
  welcome = new visual.TextStim({
    win: psychoJS.window,
    name: 'welcome',
    text: 'Welcome to this experiment \n\nThis will take about 45 minutes \n\n',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], height: 0.2,  wrapWidth: 1000, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -1.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  space = new visual.TextStim({
    win: psychoJS.window,
    name: 'space',
    text: 'Press SPACE to continue ',
    font: 'Arial',
    units: 'norm', 
    pos: [0.7, (- 0.7)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "consent"
  consentClock = new util.Clock();
  text_53 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_53',
    text: 'Precision Phenomenology Experiment\nJust a little bit more to read before the experiment...this is an Informed Consent Form. Please read and understand the statements below.\n\nI understand that my taking part in the study is voluntary and that I am free to leave the study at any time, without giving any reason. I understand that my medical care or legal rights will not be affected in any way.\nI agree to the use and release of study-related information about me for the purposes described in this Informed Consent Form.\nI agree to the re-use of data collected in this study for future studies in a de-identified manner as described in this Informed Consent form.\nI understand that my consent continues until and unless I withdraw my consent that can be done at any time by giving notice to the investigator. I understand that if I withdraw my consent I will not be able to continue to take part in the study.\nI understand that if I withdraw consent, the study researchers will no longer use or release information that identifies me in connection with the study unless it is needed to keep the scientific quality of the study. I understand that if I withdraw consent the study researchers may still use any study-related information about me that was collected before I withdrew consent.\nI have read and I understand the information provided in this Informed Consent Form. I have had the opportunity to ask questions and have had these questions answered satisfactorily.\nI have had time to consider the information provided in this Informed Consent Form to consider answers to my questions, and to consider whether I wish to take part in the study.\nIf you understand the statements above, and freely consent to participate in the study, press [Space] to begin the experiment.',
    font: 'Times New Roman',
    units: 'norm', 
    pos: [0, 0], height: 0.05,  wrapWidth: 1.5, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  key_resp_16 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', units : 'pix', 
    image : 'monash-logo-mono.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [150, 75],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  // Initialize components for Routine "instr_1"
  instr_1Clock = new util.Clock();
  text_1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_1',
    text: 'Before starting the main experiment, we need to do some quick calibrations to ensure your screen is set up correctly.',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.4], height: 0.08,  wrapWidth: 1.5, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: 0.0 
  });
  
  space_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_2',
    text: 'Press SPACE to continue ',
    font: 'Arial',
    units: 'norm', 
    pos: [0.7, (- 0.7)], height: 0.05,  wrapWidth: 1.5, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -1.0 
  });
  
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: 'Warning! It is critical that these calibrations are done correctly or you will be unable to do the experiment and we will be unable to approve your payment!',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.4)], height: 0.08,  wrapWidth: 1.5, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "screen_scale"
  screen_scaleClock = new util.Clock();
  ccimage = new visual.ImageStim({
    win : psychoJS.window,
    name : 'ccimage', units : 'pix', 
    image : 'card.png', mask : undefined,
    ori : 0, pos : [(- 150), 150], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  // Functions needed for Javascript
  
  event=psychoJS.eventManager;
  thisExp=psychoJS.experiment;
  win=psychoJS.window;
  
  round = function (a) {
      return Math.round(a);
  }
  
  
  oldt = 0;
  x_size = 8.56;
  y_size = 5.398;
  if ((ccimage.units === "norm")) {
      x_scale = 0.05;
      y_scale = 0.1;
      dbase = 0.0001;
      unittext = " norm units";
      vsize = 2;
  } else {
      if ((ccimage.units === "pix")) {
          x_scale = 60;
          y_scale = 40;
          dbase = 0.1;
          unittext = " pixels";
          vsize = screen.height;
      } else {
          x_scale = 0.05;
          y_scale = 0.05;
          dbase = 0.0001;
          unittext = " height units";
          vsize = 1;
      }
  }
  
  text_37 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_37',
    text: "First, we need to determine the size of your screen.\nTake a credit card (or a drivers license, library card, any equivalent card),\npress it to the screen and adjust the image on your screen to be the same size as the card\n\nTo increase the image width: press 'k' on your keyboard\nTo decrease the image width: press 'j' on your keyboard\n\nWhen you are done, press <ENTER>",
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.35)], height: 0.06,  wrapWidth: 1000, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "instr_2"
  instr_2Clock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Next, we need to get you to keep your head a fixed distance from the screen.\nThis will ensure future images are the right size for your screen. On the next screen please:',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.2)], height: 0.06,  wrapWidth: 1000, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -1.0 
  });
  
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: '1. Keeping your arm straight, please touch your thumb to the centre of the screen in the oval\n2. While keeping your head in the same position, lower your arm.\n3. Please keep your head in this position for the remainder of the experiment ',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.5)], height: 0.06,  wrapWidth: 1000, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -3.0 
  });
  
  space_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_3',
    text: 'Press SPACE to continue ',
    font: 'Arial',
    units: 'norm', 
    pos: [0.7, (- 0.7)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -4.0 
  });
  
  // Initialize components for Routine "instr_3"
  instr_3Clock = new util.Clock();
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: '1. While keeping your arm straight touch your thumb to the centre of the screen in the oval.\n2. Keep your head in the same position, but lower and relax your arm.\n3. Please keep your head in this position for the remainder of the experiment.\n4. Press SPACE to continue ',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.5], height: 0.07,  wrapWidth: 1000, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  thumb_size = 20;
  
  calibrationline = new visual.ImageStim({
    win : psychoJS.window,
    name : 'calibrationline', units : 'pix', 
    image : 'calibrationline.png', mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  // Initialize components for Routine "instr_4"
  instr_4Clock = new util.Clock();
  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: 'Lastly, we need to know how far your head is from the screen.\nPlease keep your head in the same position as before.\n\nOver the next few pages we will explain how we can work out how far you are sitting from the screen.\nPlease pay attention and follow all the instructions carefully.\n\nThese first few pages will be INSTRUCTIONS ONLY. You will be instructed when the calibrations start.\n\nWhen ready, press SPACE to continue and follow the instructions on the next page.\n',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], height: 0.07,  wrapWidth: 1.5, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  space_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_4',
    text: 'Press SPACE to continue ',
    font: 'Arial',
    units: 'norm', 
    pos: [0.7, (- 0.7)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "instr_5"
  instr_5Clock = new util.Clock();
  key_resp_6 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  space_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_5',
    text: 'Press SPACE to continue ',
    font: 'Arial',
    units: 'norm', 
    pos: [0.7, (- 0.7)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -1.0 
  });
  
  instr_only = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_only',
    text: 'INSTRUCTIONS ONLY',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.6], height: 0.1,  wrapWidth: 10000, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  text_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_6',
    text: '1. Put a finger on <ENTER> on the keyboard.',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.5)], height: 0.06,  wrapWidth: 1000, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "instr_6"
  instr_6Clock = new util.Clock();
  key_resp_8 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  space_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_7',
    text: 'Press SPACE to continue ',
    font: 'Arial',
    units: 'norm', 
    pos: [0.7, (- 0.7)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -1.0 
  });
  
  instr_only_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_only_3',
    text: 'INSTRUCTIONS ONLY',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.6], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  text_8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_8',
    text: '2. Close your right eye',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.5)], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "instr_7"
  instr_7Clock = new util.Clock();
  key_resp_7 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  space_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_6',
    text: 'Press SPACE to continue ',
    font: 'Arial',
    units: 'norm', 
    pos: [0.7, (- 0.7)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -1.0 
  });
  
  instr_only_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_only_2',
    text: 'INSTRUCTIONS ONLY',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.6], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  text_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_7',
    text: '3. Stare at the middle of the screen, keeping your head in the same position as before.\nKeep your right eye closed.',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.4)], height: 0.06,  wrapWidth: 1000, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -3.0 
  });
  
  center_cross = new visual.ShapeStim ({
    win: psychoJS.window, name: 'center_cross', units : 'norm', 
    vertices: 'cross', size:[0.05, 0.05],
    ori: 0, pos: [0, 0],
    lineWidth: 1.5, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -4, interpolate: true,
  });
  
  // Initialize components for Routine "instr_8"
  instr_8Clock = new util.Clock();
  key_resp_12 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  space_11 = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_11',
    text: 'Press SPACE to continue ',
    font: 'Arial',
    units: 'norm', 
    pos: [0.7, (- 0.7)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -1.0 
  });
  
  instr_only_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_only_5',
    text: 'INSTRUCTIONS ONLY',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.6], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  text_13 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_13',
    text: '4. Without moving your head or face, use your left eye to focus on the black square.\nKeep your right eye closed and do not move your head.',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.5)], height: 0.06,  wrapWidth: 1000, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -3.0 
  });
  
  center_cross_3 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'center_cross_3', units : 'norm', 
    vertices: 'cross', size:[0.05, 0.05],
    ori: 0, pos: [0, 0],
    lineWidth: 0.8, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -4, interpolate: true,
  });
  
  black_square = new visual.Rect ({
    win: psychoJS.window, name: 'black_square', units : 'pix', 
    width: [1.0, 1.0][0], height: [1.0, 1.0][1],
    ori: 0, pos: [500, 0],
    lineWidth: 1.5, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: 1, depth: -5, interpolate: true,
  });
  
  text_14 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_14',
    text: 'Stare at the square',
    font: 'Arial',
    units: 'norm', 
    pos: [0.75, 0.08], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -6.0 
  });
  
  // Initialize components for Routine "instr_9"
  instr_9Clock = new util.Clock();
  key_resp_11 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  space_8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_8',
    text: 'Press SPACE to continue ',
    font: 'Arial',
    units: 'norm', 
    pos: [0.7, (- 0.7)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -1.0 
  });
  
  instr_only_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_only_4',
    text: 'INSTRUCTIONS ONLY',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.6], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  text_11 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_11',
    text: '5. During the calibration task, a white ball will disappear as it moves from right to left.\nKeep your right eye closed, stare at the black square and do not move your head.\n',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.5)], height: 0.06,  wrapWidth: 1000, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -3.0 
  });
  
  center_cross_2 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'center_cross_2', units : 'norm', 
    vertices: 'cross', size:[0.05, 0.05],
    ori: 0, pos: [0, 0],
    lineWidth: 0.8, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -4, interpolate: true,
  });
  
  black_square1 = new visual.Rect ({
    win: psychoJS.window, name: 'black_square1', units : 'pix', 
    width: [1.0, 1.0][0], height: [1.0, 1.0][1],
    ori: 0, pos: [500, 0],
    lineWidth: 1.5, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: 1, depth: -5, interpolate: true,
  });
  
  text_12 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_12',
    text: '<--- Ball movement ',
    font: 'Arial',
    units: 'norm', 
    pos: [0.7, 0.08], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -6.0 
  });
  
  white_ball2 = new visual.Polygon ({
    win: psychoJS.window, name: 'white_ball2', units : 'pix', 
    edges: 1000, size:[1.0, 1.0],
    ori: 0, pos: [400, 0],
    lineWidth: 1, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1, depth: -7, interpolate: true,
  });
  
  // Initialize components for Routine "instr_10"
  instr_10Clock = new util.Clock();
  key_resp_18 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  space_17 = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_17',
    text: 'Press SPACE to continue ',
    font: 'Arial',
    units: 'norm', 
    pos: [0.7, (- 0.7)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -1.0 
  });
  
  instr_only_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_only_7',
    text: 'INSTRUCTIONS ONLY',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.6], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  text_44 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_44',
    text: '6. Press the <ENTER> key as soon as the ball disappears properly from your eye sight (not due to running off screen)\nKeep your right eye closed, stare at the black square, do not move your head.',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.5)], height: 0.06,  wrapWidth: 1.5, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "instr_11"
  instr_11Clock = new util.Clock();
  key_resp_21 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  space_18 = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_18',
    text: 'Press SPACE to continue ',
    font: 'Arial',
    units: 'norm', 
    pos: [0.7, (- 0.7)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -1.0 
  });
  
  instr_only_8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_only_8',
    text: 'INSTRUCTIONS ONLY',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.6], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  text_45 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_45',
    text: '7. The next page will show you a demonstration of the calibration task for a few seconds.\nDuring the actual calibration, you will need to press <ENTER> when the ball disappears.\n\nYou will do this five times so we can make sure we get the right distance.\nThe ball will reset each time.\n\nKeep your right eye closed, stare at the black square and do not move your head.',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.4)], height: 0.06,  wrapWidth: 1000, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "calibration_example"
  calibration_exampleClock = new util.Clock();
  white_ball1 = new visual.Polygon ({
    win: psychoJS.window, name: 'white_ball1', units : 'pix', 
    edges: 1000, size:[1.0, 1.0],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  black_square3 = new visual.Rect ({
    win: psychoJS.window, name: 'black_square3', units : 'pix', 
    width: [1.0, 1.0][0], height: [1.0, 1.0][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1.5, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  text_19 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_19',
    text: 'VISIBLE',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.5], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('green'),  opacity: 1,
    depth: -2.0 
  });
  
  text_20 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_20',
    text: 'INVISIBLE',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.5], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('red'),  opacity: 1,
    depth: -3.0 
  });
  
  white_ball12 = new visual.Polygon ({
    win: psychoJS.window, name: 'white_ball12', units : 'pix', 
    edges: 1000, size:[1.0, 1.0],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1, depth: -4, interpolate: true,
  });
  
  text_21 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_21',
    text: 'VISIBLE',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.5], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('green'),  opacity: 1,
    depth: -5.0 
  });
  
  text_22 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_22',
    text: 'Press <ENTER> now!',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.5)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('green'),  opacity: 1,
    depth: -6.0 
  });
  
  white_ball13 = new visual.Polygon ({
    win: psychoJS.window, name: 'white_ball13', units : 'pix', 
    edges: 1000, size:[1.0, 1.0],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1, depth: -7, interpolate: true,
  });
  
  // Initialize components for Routine "instr_12"
  instr_12Clock = new util.Clock();
  key_resp_13 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  space_12 = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_12',
    text: 'Press SPACE to continue ',
    font: 'Arial',
    units: 'norm', 
    pos: [0.7, (- 0.7)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -1.0 
  });
  
  instr_only_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_only_6',
    text: 'NEXT WILL BE THE ACTUAL CALIBRATION\n\nRemember to keep your right eye closed, stare at the black square and do not move your head.\n\nPress the <ENTER> key as soon as the ball disappears from your eye sight (not just due to running off the edge of the screen).\n\nWhen ready press SPACE to start viewing the distance calibration.',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.3], height: 0.07,  wrapWidth: 1.5, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  text_15 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_15',
    text: 'Warning! It is critical that these calibrations are done correctly or you will be unable to do the experiment and we will be unable to approve your payment!',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.4)], height: 0.06,  wrapWidth: 1.5, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "ball_calibration"
  ball_calibrationClock = new util.Clock();
  black_square2 = new visual.Rect ({
    win: psychoJS.window, name: 'black_square2', units : 'pix', 
    width: [1.0, 1.0][0], height: [1.0, 1.0][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1.5, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  white_ball = new visual.Polygon ({
    win: psychoJS.window, name: 'white_ball', units : 'pix', 
    edges: 1000, size:[1.0, 1.0],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color('white'),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  key_resp_19 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  
  viewerdistancetotal = [];
  calibrationcount = 0;
  
  text_39 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_39',
    text: 'default text',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.6)], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  white_ball1_2 = new visual.Polygon ({
    win: psychoJS.window, name: 'white_ball1_2', units : 'pix', 
    edges: 1000, size:[1.0, 1.0],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color('white'),
    opacity: 1, depth: -5, interpolate: true,
  });
  
  // Initialize components for Routine "viewerdistance"
  viewerdistanceClock = new util.Clock();
  peripheral_scale = 4.5;
  radius_central = 1.5;
  radius_peripheral = 10;
  stimulus_size = 1;
  response_stim_scale = 2;
  distance_threshold = 300;
  screen_x_threshold = 230;
  
  text_38 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_38',
    text: 'default text',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.2)], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -1.0 
  });
  
  text_40 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_40',
    text: 'The calibrations were successful!',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], height: 0.08,  wrapWidth: 10000, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  key_resp_20 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  space_20 = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_20',
    text: 'Press SPACE to continue ',
    font: 'Arial',
    units: 'norm', 
    pos: [0.7, (- 0.7)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -4.0 
  });
  
  // Initialize components for Routine "viewerdistance_unsucess"
  viewerdistance_unsucessClock = new util.Clock();
  text_41 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_41',
    text: 'Unfortunately the calibrations were unsuccessful.',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.1], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  text_42 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_42',
    text: 'default text',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color('red'),  opacity: 1,
    depth: -2.0 
  });
  
  text_43 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_43',
    text: 'Please exit the experiment',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.1)], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color('red'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "stim1_instr"
  stim1_instrClock = new util.Clock();
  stim1Clock = new util.Clock();
  stim1 = new visual.MovieStim({
    win: psychoJS.window,
    name: 'stim1',
    units: undefined,
    movie: '1stimmov.mp4',
    pos: [0, 100],
    size: [600, 400],
    ori: 0,
    opacity: 1,
    loop: true,
    noAudio: false,
    });
  key_resp_14 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  space_13 = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_13',
    text: 'Press SPACE to continue ',
    font: 'Arial',
    units: 'norm', 
    pos: [0.7, (- 0.7)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  text_16 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_16',
    text: 'Throughout the experiment, focus on the cross at the centre of the screen.\nA circle will flash out quickly on the screen.',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.5)], height: 0.06,  wrapWidth: 1000, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "stim_response_instr"
  stim_response_instrClock = new util.Clock();
  movie_2Clock = new util.Clock();
  movie_2 = new visual.MovieStim({
    win: psychoJS.window,
    name: 'movie_2',
    units: undefined,
    movie: '1stim_async_response_py.mp4',
    pos: [0, 150],
    size: [600, 400],
    ori: 0,
    opacity: 1,
    loop: true,
    noAudio: false,
    });
  key_resp_15 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  space_14 = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_14',
    text: 'Press SPACE to continue ',
    font: 'Arial',
    units: 'norm', 
    pos: [0.7, (- 0.7)], height: 0.05,  wrapWidth: 1000, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  text_17 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_17',
    text: 'Sometimes you will need to decide the similarity levels of the previous circle to a circle on the next screen.\nIgnore any size differences.\n\n0 => most similar colour (least different colour)\n7 => most different colour (least similar colour)\n\nAfter choosing, move your cursor back to the centre and click and hold the box to continue.',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.4)], height: 0.06,  wrapWidth: 1000, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "catch_insrt"
  catch_insrtClock = new util.Clock();
  space_15 = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_15',
    text: 'Press SPACE to continue ',
    font: 'Arial',
    units: 'norm', 
    pos: [0.7, (- 0.7)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_17 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  movie_3Clock = new util.Clock();
  movie_3 = new visual.MovieStim({
    win: psychoJS.window,
    name: 'movie_3',
    units: undefined,
    movie: 'catch_py.mp4',
    pos: [0, 100],
    size: [600, 400],
    ori: 0,
    opacity: 1,
    loop: true,
    noAudio: false,
    });
  text_18 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_18',
    text: 'Sometimes there will be a special trial where you will just be asked to click on a particular value.\nPlease click and hold the value for that trial.',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.5)], height: 0.06,  wrapWidth: 1000, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "colour_circle_instr_2"
  colour_circle_instr_2Clock = new util.Clock();
  key_resp_9 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  intructioncircle_1 = new visual.Polygon ({
    win: psychoJS.window, name: 'intructioncircle_1', units : 'pix', 
    edges: 1000, size:[50, 50],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, (- 1), (- 1)]),
    fillColor: new util.Color([1, (- 1), (- 1)]),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  instructioncircle_2 = new visual.Polygon ({
    win: psychoJS.window, name: 'instructioncircle_2', units : 'pix', 
    edges: 1000, size:[50, 50],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 0.33, (- 1)]),
    fillColor: new util.Color([1, 0.33, (- 1)]),
    opacity: 1, depth: -3, interpolate: true,
  });
  
  instructioncircle_3 = new visual.Polygon ({
    win: psychoJS.window, name: 'instructioncircle_3', units : 'pix', 
    edges: 1000, size:[50, 50],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([0.33, 1, (- 1)]),
    fillColor: new util.Color([0.33, 1, (- 1)]),
    opacity: 1, depth: -4, interpolate: true,
  });
  
  instructioncircle_4 = new visual.Polygon ({
    win: psychoJS.window, name: 'instructioncircle_4', units : 'pix', 
    edges: 1000, size:[50, 50],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([(- 1), 1, (- 1)]),
    fillColor: new util.Color([(- 1), 1, (- 1)]),
    opacity: 1, depth: -5, interpolate: true,
  });
  
  instructioncircle_5 = new visual.Polygon ({
    win: psychoJS.window, name: 'instructioncircle_5', units : 'pix', 
    edges: 1000, size:[50, 50],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([(- 1), 1, 0.32]),
    fillColor: new util.Color([(- 1), 1, 0.32]),
    opacity: 1, depth: -6, interpolate: true,
  });
  
  insturctioncircle_6 = new visual.Polygon ({
    win: psychoJS.window, name: 'insturctioncircle_6', units : 'pix', 
    edges: 1000, size:[50, 50],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([(- 1), 0.32, 1]),
    fillColor: new util.Color([(- 1), 0.32, 1]),
    opacity: 1, depth: -7, interpolate: true,
  });
  
  instructioncircle_7 = new visual.Polygon ({
    win: psychoJS.window, name: 'instructioncircle_7', units : 'pix', 
    edges: 1000, size:[50, 50],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([(- 1), (- 1), 1]),
    fillColor: new util.Color([(- 1), (- 1), 1]),
    opacity: 1, depth: -8, interpolate: true,
  });
  
  instructioncircle_8 = new visual.Polygon ({
    win: psychoJS.window, name: 'instructioncircle_8', units : 'pix', 
    edges: 1000, size:[50, 50],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([0.33, (- 1), 1]),
    fillColor: new util.Color([0.33, (- 1), 1]),
    opacity: 1, depth: -9, interpolate: true,
  });
  
  instructioncircle_9 = new visual.Polygon ({
    win: psychoJS.window, name: 'instructioncircle_9', units : 'pix', 
    edges: 1000, size:[50, 50],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, (- 1), 0.33]),
    fillColor: new util.Color([1, (- 1), 0.33]),
    opacity: 1, depth: -10, interpolate: true,
  });
  
  space_9 = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_9',
    text: 'Press SPACE to continue ',
    font: 'Arial',
    units: 'norm', 
    pos: [0.7, (- 0.7)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -11.0 
  });
  
  text_9 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_9',
    text: 'During the test, you will see these 9 colors below',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.8], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -12.0 
  });
  
  // Initialize components for Routine "instr_prac"
  instr_pracClock = new util.Clock();
  space_10 = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_10',
    text: 'Press SPACE to continue ',
    font: 'Arial',
    units: 'norm', 
    pos: [0.7, (- 0.7)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: 0.0 
  });
  
  text_10 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_10',
    text: 'You are going to do a few practice trials to make you be more familiar with the experiment.\nWhen you are ready, please press SPACE to start the practice trials',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], height: 0.06,  wrapWidth: 1000, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -1.0 
  });
  
  key_resp_10 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Stim1_display_prac"
  Stim1_display_pracClock = new util.Clock();
  Circle = new visual.Polygon ({
    win: psychoJS.window, name: 'Circle', units : 'pix', 
    edges: 1000, size:[1.0, 1.0],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color(1.0),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  centre_cross4_2 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'centre_cross4_2', units : 'norm', 
    vertices: 'cross', size:[0.03, 0.03],
    ori: 0, pos: [0, 0],
    lineWidth: 1.5, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  // Initialize components for Routine "response_prac"
  response_pracClock = new util.Clock();
  mouse_5 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_5.mouseClock = new util.Clock();
  a = ((window.innerWidth / 2) * 0.1);
  b = ((window.innerWidth / 2) * 0.158);
  response1disk_5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response1disk_5', units : 'pix', 
    image : 'response67.png', mask : undefined,
    ori : 0, pos : [a, a], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  response3disk_5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response3disk_5', units : 'pix', 
    image : 'response45.png', mask : undefined,
    ori : 0, pos : [a, (- a)], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  response5disk_5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response5disk_5', units : 'pix', 
    image : 'response23.png', mask : undefined,
    ori : 0, pos : [(- a), (- a)], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  response7disk_5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response7disk_5', units : 'pix', 
    image : 'response01.png', mask : undefined,
    ori : 0, pos : [(- a), a], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -5.0 
  });
  Circle_3 = new visual.Polygon ({
    win: psychoJS.window, name: 'Circle_3', units : 'pix', 
    edges: 1000, size:[1.0, 1.0],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color(1.0),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -6, interpolate: true,
  });
  
  text_29 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_29',
    text: 'Please choose the similarity level of the circle with the previously cued circle.\nPlease click and hold to indicate your choice.\n0 => Most similar\n7 => Most different \n',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.7)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -7.0 
  });
  
  // Initialize components for Routine "responseprac_feedback"
  responseprac_feedbackClock = new util.Clock();
  text_55 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_55',
    text: 'default text',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], height: 0.1,  wrapWidth: 1000, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  text_56 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_56',
    text: 'default text',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.2)], height: 0.1,  wrapWidth: 1000, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "summary_prac"
  summary_pracClock = new util.Clock();
  mouse_10 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_10.mouseClock = new util.Clock();
  response1disk_10 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response1disk_10', units : 'pix', 
    image : 'response67.png', mask : undefined,
    ori : 0, pos : [a, a], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  response3disk_10 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response3disk_10', units : 'pix', 
    image : 'response45.png', mask : undefined,
    ori : 0, pos : [a, (- a)], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  response5disk_10 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response5disk_10', units : 'pix', 
    image : 'response23.png', mask : undefined,
    ori : 0, pos : [(- a), (- a)], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  response7disk_10 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response7disk_10', units : 'pix', 
    image : 'response01.png', mask : undefined,
    ori : 0, pos : [(- a), a], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  rectangle_8 = new visual.Rect ({
    win: psychoJS.window, name: 'rectangle_8', units : 'norm', 
    width: [0.1, 0.08][0], height: [0.1, 0.08][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color('white'),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -5, interpolate: true,
  });
  
  pracnumber = 0;
  
  text_49 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_49',
    text: 'Please click and hold on the grey rectangle in the middle of the response numbers to continue',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.5)], height: 0.05,  wrapWidth: 1000, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -7.0 
  });
  
  text_50 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_50',
    text: 'default text',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.7)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -8.0 
  });
  
  // Initialize components for Routine "special_trial_prac"
  special_trial_pracClock = new util.Clock();
  text_36 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_36',
    text: 'SPECIAL TRIAL',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "catch_prac"
  catch_pracClock = new util.Clock();
  mouse_7 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_7.mouseClock = new util.Clock();
  response1disk_7 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response1disk_7', units : 'pix', 
    image : 'response67.png', mask : undefined,
    ori : 0, pos : [a, a], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  response3disk_7 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response3disk_7', units : 'pix', 
    image : 'response45.png', mask : undefined,
    ori : 0, pos : [a, (- a)], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  response5disk_7 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response5disk_7', units : 'pix', 
    image : 'response23.png', mask : undefined,
    ori : 0, pos : [(- a), (- a)], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  response7disk_7 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response7disk_7', units : 'pix', 
    image : 'response01.png', mask : undefined,
    ori : 0, pos : [(- a), a], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  
  
  catchtrialorderprac = Array.from({length: 2}, () => Math.floor(Math.random() * 7));
  
  catchnumberprac = (Math.floor((Math.random() * ((7 - 0) + 1))) + 0);
  
  text_32 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_32',
    text: 'default text',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.6)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -6.0 
  });
  
  rectangle_5 = new visual.Rect ({
    win: psychoJS.window, name: 'rectangle_5', units : 'norm', 
    width: [0.1, 0.08][0], height: [0.1, 0.08][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color('white'),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -7, interpolate: true,
  });
  
  // Initialize components for Routine "summary2_prac"
  summary2_pracClock = new util.Clock();
  mouse_6 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_6.mouseClock = new util.Clock();
  response1disk_6 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response1disk_6', units : 'pix', 
    image : 'response67.png', mask : undefined,
    ori : 0, pos : [a, a], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  response3disk_6 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response3disk_6', units : 'pix', 
    image : 'response45.png', mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  response5disk_6 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response5disk_6', units : 'pix', 
    image : 'response23.png', mask : undefined,
    ori : 0, pos : [(- a), (- a)], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  response7disk_6 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response7disk_6', units : 'pix', 
    image : 'response01.png', mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  rectangle_4 = new visual.Rect ({
    win: psychoJS.window, name: 'rectangle_4', units : 'norm', 
    width: [0.1, 0.08][0], height: [0.1, 0.08][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color('white'),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -5, interpolate: true,
  });
  
  pracnumber = 0;
  
  text_30 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_30',
    text: 'Please click and hold the grey rectangle in the middle of the response numbers to continue',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.7)], height: 0.05,  wrapWidth: 1000, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -7.0 
  });
  
  text_31 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_31',
    text: 'default text',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.8)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -8.0 
  });
  
  // Initialize components for Routine "begin"
  beginClock = new util.Clock();
  space_19 = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_19',
    text: 'Press SPACE to continue ',
    font: 'Arial',
    units: 'norm', 
    pos: [0.7, (- 0.7)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: 0.0 
  });
  
  text_46 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_46',
    text: 'You have finished the practice trial.\n\nNext page will be the formal test. \n\nIf you are ready, please press SPACE button to start the experiment.',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], height: 0.08,  wrapWidth: 1000, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -1.0 
  });
  
  key_resp_22 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Stim1_display"
  Stim1_displayClock = new util.Clock();
  Circle_1 = new visual.Polygon ({
    win: psychoJS.window, name: 'Circle_1', units : 'pix', 
    edges: 1000, size:[1.0, 1.0],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color(1.0),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  centre_cross4 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'centre_cross4', units : 'norm', 
    vertices: 'cross', size:[0.03, 0.03],
    ori: 0, pos: [0, 0],
    lineWidth: 1.5, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  // Initialize components for Routine "response"
  responseClock = new util.Clock();
  mouse = new core.Mouse({
    win: psychoJS.window,
  });
  mouse.mouseClock = new util.Clock();
  order = (Math.floor((Math.random() * ((100 - 1) + 1))) + 1);
  
  response1disk = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response1disk', units : undefined, 
    image : 'response67.png', mask : undefined,
    ori : 0, pos : [a, a], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  response3disk = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response3disk', units : undefined, 
    image : 'response45.png', mask : undefined,
    ori : 0, pos : [a, (- a)], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  response5disk = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response5disk', units : undefined, 
    image : 'response23.png', mask : undefined,
    ori : 0, pos : [(- a), (- a)], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  response7disk = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response7disk', units : undefined, 
    image : 'response01.png', mask : undefined,
    ori : 0, pos : [(- a), a], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -5.0 
  });
  Circle_2 = new visual.Polygon ({
    win: psychoJS.window, name: 'Circle_2', units : 'pix', 
    edges: 1000, size:[1.0, 1.0],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color(1.0),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -6, interpolate: true,
  });
  
  text_23 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_23',
    text: 'Please choose the similarity level of the circle with the previously cued circle.\nPlease click and hold to indicate your choice.\n0 => Most similar\n7 => Most different ',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.6)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -7.0 
  });
  
  // Initialize components for Routine "response_2"
  response_2Clock = new util.Clock();
  mouse_2 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_2.mouseClock = new util.Clock();
  response1disk_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response1disk_2', units : undefined, 
    image : 'response67.png', mask : undefined,
    ori : 0, pos : [a, a], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  response3disk_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response3disk_2', units : undefined, 
    image : 'response45.png', mask : undefined,
    ori : 0, pos : [a, (- a)], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  response5disk_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response5disk_2', units : undefined, 
    image : 'response23.png', mask : undefined,
    ori : 0, pos : [(- a), (- a)], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  response7disk_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response7disk_2', units : undefined, 
    image : 'response01.png', mask : undefined,
    ori : 0, pos : [(- a), a], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  rectangle = new visual.Rect ({
    win: psychoJS.window, name: 'rectangle', units : 'norm', 
    width: [0.1, 0.08][0], height: [0.1, 0.08][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color('white'),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -5, interpolate: true,
  });
  
  trialnumber = 0;
  grey = [0.2, 0.2, 0.2];
  
  text_25 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_25',
    text: 'Please click and hold the grey rectangle in the middle of the response numbers to continue',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.5)], height: 0.05,  wrapWidth: 1000, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -7.0 
  });
  
  text_24 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_24',
    text: 'default text',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.7)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -8.0 
  });
  
  // Initialize components for Routine "special_trial"
  special_trialClock = new util.Clock();
  text_33 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_33',
    text: 'SPECIAL TRIAL',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "catch_1"
  catch_1Clock = new util.Clock();
  mouse_3 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_3.mouseClock = new util.Clock();
  response1disk_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response1disk_3', units : undefined, 
    image : 'response67.png', mask : undefined,
    ori : 0, pos : [a, a], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  response3disk_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response3disk_3', units : undefined, 
    image : 'response45.png', mask : undefined,
    ori : 0, pos : [a, (- a)], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  response5disk_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response5disk_3', units : undefined, 
    image : 'response23.png', mask : undefined,
    ori : 0, pos : [(- a), (- a)], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  response7disk_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response7disk_3', units : undefined, 
    image : 'response01.png', mask : undefined,
    ori : 0, pos : [(- a), a], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  // Set up catch trials
  
  //catchtrialorder = Array.from({length: 20}, () => Math.floor(Math.random() * 324));
  
  text_26 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_26',
    text: 'default text',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.6)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -6.0 
  });
  
  rectangle_2 = new visual.Rect ({
    win: psychoJS.window, name: 'rectangle_2', units : 'norm', 
    width: [0.1, 0.08][0], height: [0.1, 0.08][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color('white'),
    fillColor: new util.Color(grey),
    opacity: 1, depth: -7, interpolate: true,
  });
  
  // Initialize components for Routine "response_sum"
  response_sumClock = new util.Clock();
  mouse_11 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_11.mouseClock = new util.Clock();
  response1disk_11 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response1disk_11', units : undefined, 
    image : 'response67.png', mask : undefined,
    ori : 0, pos : [a, a], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  response3disk_11 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response3disk_11', units : undefined, 
    image : 'response45.png', mask : undefined,
    ori : 0, pos : [a, (- a)], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  response5disk_11 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response5disk_11', units : undefined, 
    image : 'response23.png', mask : undefined,
    ori : 0, pos : [(- a), (- a)], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  response7disk_11 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'response7disk_11', units : undefined, 
    image : 'response01.png', mask : undefined,
    ori : 0, pos : [(- a), a], size : [b, b],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  rectangle_9 = new visual.Rect ({
    win: psychoJS.window, name: 'rectangle_9', units : 'norm', 
    width: [0.1, 0.08][0], height: [0.1, 0.08][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color('white'),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -5, interpolate: true,
  });
  
  trialnumber = 0;
  
  text_51 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_51',
    text: 'Please click and hold the grey rectangle in the middle of the response numbers to continue',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.5)], height: 0.05,  wrapWidth: 1000, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -7.0 
  });
  
  text_52 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_52',
    text: 'default text',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.7)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -8.0 
  });
  
  // Initialize components for Routine "survey1"
  survey1Clock = new util.Clock();
  copyText_1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'copyText_1',
    text: '',
    font: 'Arial',
    units: 'norm', 
    pos: [(- 0.05), 0.1], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  question_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'question_4',
    text: 'Please answer the next 7 questions to finish the experiment. Please type your reponse and press <ENTER> to submit,\n\n1. Did you have any difficulty in seeing the location of the two circles on each trial? (y or n)\n',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.5], height: 0.08,  wrapWidth: 1.5, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  submitanswer = new visual.TextStim({
    win: psychoJS.window,
    name: 'submitanswer',
    text: 'Press enter to submit your answer',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.9)], height: 0.08,  wrapWidth: 3, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "survey2"
  survey2Clock = new util.Clock();
  copyText_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'copyText_2',
    text: '',
    font: 'Arial',
    units: 'norm', 
    pos: [(- 0.05), 0.1], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  question = new visual.TextStim({
    win: psychoJS.window,
    name: 'question',
    text: '2. Did you have any difficulty in knowing what colour the central circles were? (y or n)\n',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.5], height: 0.08,  wrapWidth: 1.5, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  submitanswer_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'submitanswer_2',
    text: 'Press enter to submit your answer',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.9)], height: 0.08,  wrapWidth: 3, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "survey3"
  survey3Clock = new util.Clock();
  copyText_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'copyText_3',
    text: '',
    font: 'Arial',
    units: 'norm', 
    pos: [(- 0.05), 0.1], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  question_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'question_2',
    text: '3. Did you have any difficulty in knowing what colour the peripheral circles were? (y or n)\n',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.5], height: 0.08,  wrapWidth: 1.5, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  submitanswer_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'submitanswer_3',
    text: 'Press enter to submit your answer',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.9)], height: 0.08,  wrapWidth: 3, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "survey_4"
  survey_4Clock = new util.Clock();
  copyText_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'copyText_4',
    text: '',
    font: 'Arial',
    units: 'norm', 
    pos: [(- 0.05), 0.1], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  question_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'question_3',
    text: '4. Do you have normal visual acuity, or corrected-to-normal wearing glasses or contact lenses? (y or n)',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.5], height: 0.08,  wrapWidth: 1.5, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  submitanswer_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'submitanswer_4',
    text: 'Press enter to submit your answer',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.9)], height: 0.08,  wrapWidth: 3, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "survey5"
  survey5Clock = new util.Clock();
  copyText_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'copyText_5',
    text: '',
    font: 'Arial',
    units: 'norm', 
    pos: [(- 0.05), 0.1], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  question_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'question_5',
    text: "5. Do you have any colour vision impairment? (y or n)\nIf yes, please describe the type (e.g) 'red-green colour blind'). ",
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.5], height: 0.08,  wrapWidth: 1.5, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  submitanswer_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'submitanswer_5',
    text: 'Press enter to submit your answer',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.9)], height: 0.08,  wrapWidth: 3, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "survey6"
  survey6Clock = new util.Clock();
  copyText_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'copyText_6',
    text: '',
    font: 'Arial',
    units: 'norm', 
    pos: [(- 0.05), 0.1], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  question_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'question_6',
    text: "6. Did you base your judgements on any of the following stratergies? \n- colour catergories (e.g 'red','blue','green')\n- colour opponecy axes (e.g 'red to green', 'blue to yellow')\n- another stratergy \n- no particular stratergy\nPlease type which stratergy, and if you selected 'another stratergy' please describe it.\n",
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.5], height: 0.08,  wrapWidth: 1.5, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  submitanswer_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'submitanswer_6',
    text: 'Press enter to submit your answer',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.9)], height: 0.08,  wrapWidth: 3, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "survey7"
  survey7Clock = new util.Clock();
  copyText_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'copyText_7',
    text: '',
    font: 'Arial',
    units: 'norm', 
    pos: [(- 0.05), 0.1], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  question_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'question_7',
    text: 'Please type any other comments you may have. \n\nYou have now finished the experiment. Thank you for your participation!',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.5], height: 0.08,  wrapWidth: 1.5, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  submitanswer_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'submitanswer_7',
    text: 'Press enter to submit your answer',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.9)], height: 0.08,  wrapWidth: 3, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var startupComponents;
function startupRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'startup'-------
    t = 0;
    startupClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // keep track of which components have finished
    startupComponents = [];
    
    startupComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


var continueRoutine;
function startupRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'startup'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = startupClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    startupComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function startupRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'startup'-------
    startupComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "startup" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_allKeys;
var welcome_instrComponents;
function welcome_instrRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'welcome_instr'-------
    t = 0;
    welcome_instrClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    welcome_instrComponents = [];
    welcome_instrComponents.push(text_54);
    welcome_instrComponents.push(welcome);
    welcome_instrComponents.push(key_resp);
    welcome_instrComponents.push(space);
    
    welcome_instrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function welcome_instrRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'welcome_instr'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = welcome_instrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_54* updates
    if (t >= 0.0 && text_54.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_54.tStart = t;  // (not accounting for frame time here)
      text_54.frameNStart = frameN;  // exact frame index
      
      text_54.setAutoDraw(true);
    }

    
    // *welcome* updates
    if (t >= 0.0 && welcome.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      welcome.tStart = t;  // (not accounting for frame time here)
      welcome.frameNStart = frameN;  // exact frame index
      
      welcome.setAutoDraw(true);
    }

    
    // *key_resp* updates
    if (t >= 2 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *space* updates
    if (t >= 2 && space.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space.tStart = t;  // (not accounting for frame time here)
      space.frameNStart = frameN;  // exact frame index
      
      space.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    welcome_instrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function welcome_instrRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'welcome_instr'-------
    welcome_instrComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "welcome_instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var posx;
var posy;
var _key_resp_16_allKeys;
var consentComponents;
function consentRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'consent'-------
    t = 0;
    consentClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    posx = ((window.innerWidth / 2) * 0.8);
    posy = ((window.innerHeight / 2) * 0.8);
    key_resp_16.keys = undefined;
    key_resp_16.rt = undefined;
    _key_resp_16_allKeys = [];
    image.setPos([(- posx), posy]);
    // keep track of which components have finished
    consentComponents = [];
    consentComponents.push(text_53);
    consentComponents.push(key_resp_16);
    consentComponents.push(image);
    
    consentComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function consentRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'consent'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = consentClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_53* updates
    if (t >= 0.0 && text_53.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_53.tStart = t;  // (not accounting for frame time here)
      text_53.frameNStart = frameN;  // exact frame index
      
      text_53.setAutoDraw(true);
    }

    
    // *key_resp_16* updates
    if (t >= 0.0 && key_resp_16.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_16.tStart = t;  // (not accounting for frame time here)
      key_resp_16.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_16.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_16.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_16.clearEvents(); });
    }

    if (key_resp_16.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_16.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_16_allKeys = _key_resp_16_allKeys.concat(theseKeys);
      if (_key_resp_16_allKeys.length > 0) {
        key_resp_16.keys = _key_resp_16_allKeys[_key_resp_16_allKeys.length - 1].name;  // just the last key pressed
        key_resp_16.rt = _key_resp_16_allKeys[_key_resp_16_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *image* updates
    if (t >= 0.0 && image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image.tStart = t;  // (not accounting for frame time here)
      image.frameNStart = frameN;  // exact frame index
      
      image.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    consentComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function consentRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'consent'-------
    consentComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_16.keys', key_resp_16.keys);
    if (typeof key_resp_16.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_16.rt', key_resp_16.rt);
        routineTimer.reset();
        }
    
    key_resp_16.stop();
    // the Routine "consent" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_2_allKeys;
var instr_1Components;
function instr_1RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'instr_1'-------
    t = 0;
    instr_1Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // keep track of which components have finished
    instr_1Components = [];
    instr_1Components.push(text_1);
    instr_1Components.push(space_2);
    instr_1Components.push(text_2);
    instr_1Components.push(key_resp_2);
    
    instr_1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function instr_1RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'instr_1'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instr_1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_1* updates
    if (t >= 0.0 && text_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_1.tStart = t;  // (not accounting for frame time here)
      text_1.frameNStart = frameN;  // exact frame index
      
      text_1.setAutoDraw(true);
    }

    
    // *space_2* updates
    if (t >= 2 && space_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_2.tStart = t;  // (not accounting for frame time here)
      space_2.frameNStart = frameN;  // exact frame index
      
      space_2.setAutoDraw(true);
    }

    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }

    
    // *key_resp_2* updates
    if (t >= 2 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }

    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instr_1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instr_1RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'instr_1'-------
    instr_1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        routineTimer.reset();
        }
    
    key_resp_2.stop();
    // the Routine "instr_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var screen_scaleComponents;
function screen_scaleRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'screen_scale'-------
    t = 0;
    screen_scaleClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    ccimage.setSize([(x_size * x_scale), ((x_size * x_scale) * 0.62)]);
    // keep track of which components have finished
    screen_scaleComponents = [];
    screen_scaleComponents.push(ccimage);
    screen_scaleComponents.push(text_37);
    
    screen_scaleComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


var _pj;
var keys;
var dscale;
var ratio_pxpermm;
function screen_scaleRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'screen_scale'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = screen_scaleClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *ccimage* updates
    if (t >= 0.0 && ccimage.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ccimage.tStart = t;  // (not accounting for frame time here)
      ccimage.frameNStart = frameN;  // exact frame index
      
      ccimage.setAutoDraw(true);
    }

    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    keys = event.getKeys();
    if (keys.length) {
        if (((t - oldt) < 0.5)) {
            dscale = (5 * dbase);
            oldt = t;
        } else {
            dscale = dbase;
            oldt = t;
        }
        if (_pj.in_es6("return", keys)) {
            continueRoutine = false;
        } else {
            if (_pj.in_es6("j", keys)) {
                x_scale = (round(((x_scale - dscale) * 10000)) / 10000);
            } else {
                if (_pj.in_es6("k", keys)) {
                    x_scale = (round(((x_scale + dscale) * 10000)) / 10000);
                }
            }
        }
        ccimage.size = [(x_size * x_scale), ((x_size * x_scale) * 0.62)];
    }
    ratio_pxpermm = ((x_scale * x_size) / 85.6);
    
    
    // *text_37* updates
    if (t >= 0.0 && text_37.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_37.tStart = t;  // (not accounting for frame time here)
      text_37.frameNStart = frameN;  // exact frame index
      
      text_37.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    screen_scaleComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var screen_size_x;
var screen_size_y;
function screen_scaleRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'screen_scale'-------
    screen_scaleComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    ratio_pxpermm = ((x_scale * x_size) / 85.6);
    thisExp.addData("X Scale", x_scale);
    thisExp.addData("ratio_pxpermm", ratio_pxpermm);
    screen_size_x = ((1 / ratio_pxpermm) * psychoJS.window.size[0]);
    screen_size_y = ((1 / ratio_pxpermm) * screen.height);
    thisExp.addData("screen_size_x", screen_size_x);
    thisExp.addData("screen_size_y", screen_size_y);
    thisExp.addData('testsize', psychoJS.window.size[0]);
    
    
    // the Routine "screen_scale" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var movieClock;
var movie;
var _key_resp_3_allKeys;
var instr_2Components;
function instr_2RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'instr_2'-------
    t = 0;
    instr_2Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    movieClock = new util.Clock();
    movie = new visual.MovieStim({
      win: psychoJS.window,
      name: 'movie',
      units: 'norm',
      movie: 'calibrationinsrt.mp4',
      pos: [0, 0.4],
      size: [0.38, 0.35],
      ori: 0,
      opacity: 1,
      loop: true,
      noAudio: false,
      });
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    // keep track of which components have finished
    instr_2Components = [];
    instr_2Components.push(movie);
    instr_2Components.push(text);
    instr_2Components.push(key_resp_3);
    instr_2Components.push(text_3);
    instr_2Components.push(space_3);
    
    instr_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


var frameRemains;
function instr_2RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'instr_2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instr_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *movie* updates
    if (t >= 0 && movie.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      movie.tStart = t;  // (not accounting for frame time here)
      movie.frameNStart = frameN;  // exact frame index
      
      movie.setAutoDraw(true);
    }

    frameRemains = 0 + undefined - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (movie.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      movie.setAutoDraw(false);
    }

    if (movie.status === PsychoJS.Status.FINISHED) {  // force-end the routine
        continueRoutine = false;
    }
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    
    // *key_resp_3* updates
    if (t >= 0.0 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_3.tStart = t;  // (not accounting for frame time here)
      key_resp_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.clearEvents(); });
    }

    if (key_resp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_3.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_3.rt = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_3* updates
    if (t >= 0.0 && text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_3.tStart = t;  // (not accounting for frame time here)
      text_3.frameNStart = frameN;  // exact frame index
      
      text_3.setAutoDraw(true);
    }

    
    // *space_3* updates
    if (t >= 0.0 && space_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_3.tStart = t;  // (not accounting for frame time here)
      space_3.frameNStart = frameN;  // exact frame index
      
      space_3.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instr_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instr_2RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'instr_2'-------
    instr_2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_3.keys', key_resp_3.keys);
    if (typeof key_resp_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_3.rt', key_resp_3.rt);
        routineTimer.reset();
        }
    
    key_resp_3.stop();
    // the Routine "instr_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_4_allKeys;
var line_size;
var instr_3Components;
function instr_3RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'instr_3'-------
    t = 0;
    instr_3Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_4.keys = undefined;
    key_resp_4.rt = undefined;
    _key_resp_4_allKeys = [];
    line_size = (thumb_size * ratio_pxpermm);
    
    calibrationline.setSize([line_size, (line_size * 3)]);
    // keep track of which components have finished
    instr_3Components = [];
    instr_3Components.push(text_4);
    instr_3Components.push(key_resp_4);
    instr_3Components.push(calibrationline);
    
    instr_3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function instr_3RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'instr_3'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instr_3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_4* updates
    if (t >= 0.0 && text_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_4.tStart = t;  // (not accounting for frame time here)
      text_4.frameNStart = frameN;  // exact frame index
      
      text_4.setAutoDraw(true);
    }

    
    // *key_resp_4* updates
    if (t >= 0.0 && key_resp_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_4.tStart = t;  // (not accounting for frame time here)
      key_resp_4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_4.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.start(); }); // start on screen flip
    }

    if (key_resp_4.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_4.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_4_allKeys = _key_resp_4_allKeys.concat(theseKeys);
      if (_key_resp_4_allKeys.length > 0) {
        key_resp_4.keys = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].name;  // just the last key pressed
        key_resp_4.rt = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *calibrationline* updates
    if (t >= 0.0 && calibrationline.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      calibrationline.tStart = t;  // (not accounting for frame time here)
      calibrationline.frameNStart = frameN;  // exact frame index
      
      calibrationline.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instr_3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instr_3RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'instr_3'-------
    instr_3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_4.keys', key_resp_4.keys);
    if (typeof key_resp_4.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_4.rt', key_resp_4.rt);
        routineTimer.reset();
        }
    
    key_resp_4.stop();
    thisExp.addData("line_size", line_size);
    
    // the Routine "instr_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_5_allKeys;
var instr_4Components;
function instr_4RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'instr_4'-------
    t = 0;
    instr_4Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_5.keys = undefined;
    key_resp_5.rt = undefined;
    _key_resp_5_allKeys = [];
    // keep track of which components have finished
    instr_4Components = [];
    instr_4Components.push(text_5);
    instr_4Components.push(key_resp_5);
    instr_4Components.push(space_4);
    
    instr_4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function instr_4RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'instr_4'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instr_4Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_5* updates
    if (t >= 0.0 && text_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_5.tStart = t;  // (not accounting for frame time here)
      text_5.frameNStart = frameN;  // exact frame index
      
      text_5.setAutoDraw(true);
    }

    
    // *key_resp_5* updates
    if (t >= 2 && key_resp_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_5.tStart = t;  // (not accounting for frame time here)
      key_resp_5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_5.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.clearEvents(); });
    }

    if (key_resp_5.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_5.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_5_allKeys = _key_resp_5_allKeys.concat(theseKeys);
      if (_key_resp_5_allKeys.length > 0) {
        key_resp_5.keys = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].name;  // just the last key pressed
        key_resp_5.rt = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *space_4* updates
    if (t >= 2 && space_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_4.tStart = t;  // (not accounting for frame time here)
      space_4.frameNStart = frameN;  // exact frame index
      
      space_4.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instr_4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instr_4RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'instr_4'-------
    instr_4Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_5.keys', key_resp_5.keys);
    if (typeof key_resp_5.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_5.rt', key_resp_5.rt);
        routineTimer.reset();
        }
    
    key_resp_5.stop();
    // the Routine "instr_4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_6_allKeys;
var instr_5Components;
function instr_5RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'instr_5'-------
    t = 0;
    instr_5Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_6.keys = undefined;
    key_resp_6.rt = undefined;
    _key_resp_6_allKeys = [];
    // keep track of which components have finished
    instr_5Components = [];
    instr_5Components.push(key_resp_6);
    instr_5Components.push(space_5);
    instr_5Components.push(instr_only);
    instr_5Components.push(text_6);
    
    instr_5Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function instr_5RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'instr_5'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instr_5Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_6* updates
    if (t >= 2 && key_resp_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_6.tStart = t;  // (not accounting for frame time here)
      key_resp_6.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_6.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.clearEvents(); });
    }

    if (key_resp_6.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_6.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_6_allKeys = _key_resp_6_allKeys.concat(theseKeys);
      if (_key_resp_6_allKeys.length > 0) {
        key_resp_6.keys = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].name;  // just the last key pressed
        key_resp_6.rt = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *space_5* updates
    if (t >= 2 && space_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_5.tStart = t;  // (not accounting for frame time here)
      space_5.frameNStart = frameN;  // exact frame index
      
      space_5.setAutoDraw(true);
    }

    
    // *instr_only* updates
    if (t >= 0.0 && instr_only.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_only.tStart = t;  // (not accounting for frame time here)
      instr_only.frameNStart = frameN;  // exact frame index
      
      instr_only.setAutoDraw(true);
    }

    
    // *text_6* updates
    if (t >= 0.0 && text_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_6.tStart = t;  // (not accounting for frame time here)
      text_6.frameNStart = frameN;  // exact frame index
      
      text_6.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instr_5Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instr_5RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'instr_5'-------
    instr_5Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_6.keys', key_resp_6.keys);
    if (typeof key_resp_6.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_6.rt', key_resp_6.rt);
        routineTimer.reset();
        }
    
    key_resp_6.stop();
    // the Routine "instr_5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_8_allKeys;
var instr_6Components;
function instr_6RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'instr_6'-------
    t = 0;
    instr_6Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_8.keys = undefined;
    key_resp_8.rt = undefined;
    _key_resp_8_allKeys = [];
    // keep track of which components have finished
    instr_6Components = [];
    instr_6Components.push(key_resp_8);
    instr_6Components.push(space_7);
    instr_6Components.push(instr_only_3);
    instr_6Components.push(text_8);
    
    instr_6Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function instr_6RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'instr_6'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instr_6Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_8* updates
    if (t >= 2 && key_resp_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_8.tStart = t;  // (not accounting for frame time here)
      key_resp_8.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_8.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_8.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_8.clearEvents(); });
    }

    if (key_resp_8.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_8.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_8_allKeys = _key_resp_8_allKeys.concat(theseKeys);
      if (_key_resp_8_allKeys.length > 0) {
        key_resp_8.keys = _key_resp_8_allKeys[_key_resp_8_allKeys.length - 1].name;  // just the last key pressed
        key_resp_8.rt = _key_resp_8_allKeys[_key_resp_8_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *space_7* updates
    if (t >= 2 && space_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_7.tStart = t;  // (not accounting for frame time here)
      space_7.frameNStart = frameN;  // exact frame index
      
      space_7.setAutoDraw(true);
    }

    
    // *instr_only_3* updates
    if (t >= 0.0 && instr_only_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_only_3.tStart = t;  // (not accounting for frame time here)
      instr_only_3.frameNStart = frameN;  // exact frame index
      
      instr_only_3.setAutoDraw(true);
    }

    
    // *text_8* updates
    if (t >= 0.0 && text_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_8.tStart = t;  // (not accounting for frame time here)
      text_8.frameNStart = frameN;  // exact frame index
      
      text_8.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instr_6Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instr_6RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'instr_6'-------
    instr_6Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_8.keys', key_resp_8.keys);
    if (typeof key_resp_8.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_8.rt', key_resp_8.rt);
        routineTimer.reset();
        }
    
    key_resp_8.stop();
    // the Routine "instr_6" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_7_allKeys;
var instr_7Components;
function instr_7RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'instr_7'-------
    t = 0;
    instr_7Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_7.keys = undefined;
    key_resp_7.rt = undefined;
    _key_resp_7_allKeys = [];
    // keep track of which components have finished
    instr_7Components = [];
    instr_7Components.push(key_resp_7);
    instr_7Components.push(space_6);
    instr_7Components.push(instr_only_2);
    instr_7Components.push(text_7);
    instr_7Components.push(center_cross);
    
    instr_7Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function instr_7RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'instr_7'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instr_7Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_7* updates
    if (t >= 2 && key_resp_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_7.tStart = t;  // (not accounting for frame time here)
      key_resp_7.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_7.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_7.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_7.clearEvents(); });
    }

    if (key_resp_7.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_7.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_7_allKeys = _key_resp_7_allKeys.concat(theseKeys);
      if (_key_resp_7_allKeys.length > 0) {
        key_resp_7.keys = _key_resp_7_allKeys[_key_resp_7_allKeys.length - 1].name;  // just the last key pressed
        key_resp_7.rt = _key_resp_7_allKeys[_key_resp_7_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *space_6* updates
    if (t >= 2 && space_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_6.tStart = t;  // (not accounting for frame time here)
      space_6.frameNStart = frameN;  // exact frame index
      
      space_6.setAutoDraw(true);
    }

    
    // *instr_only_2* updates
    if (t >= 0.0 && instr_only_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_only_2.tStart = t;  // (not accounting for frame time here)
      instr_only_2.frameNStart = frameN;  // exact frame index
      
      instr_only_2.setAutoDraw(true);
    }

    
    // *text_7* updates
    if (t >= 0.0 && text_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_7.tStart = t;  // (not accounting for frame time here)
      text_7.frameNStart = frameN;  // exact frame index
      
      text_7.setAutoDraw(true);
    }

    
    // *center_cross* updates
    if (t >= 0.0 && center_cross.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      center_cross.tStart = t;  // (not accounting for frame time here)
      center_cross.frameNStart = frameN;  // exact frame index
      
      center_cross.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instr_7Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instr_7RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'instr_7'-------
    instr_7Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_7.keys', key_resp_7.keys);
    if (typeof key_resp_7.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_7.rt', key_resp_7.rt);
        routineTimer.reset();
        }
    
    key_resp_7.stop();
    // the Routine "instr_7" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_12_allKeys;
var instr_8Components;
function instr_8RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'instr_8'-------
    t = 0;
    instr_8Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_12.keys = undefined;
    key_resp_12.rt = undefined;
    _key_resp_12_allKeys = [];
    black_square.setSize([(8.5 * ratio_pxpermm), (8.5 * ratio_pxpermm)]);
    // keep track of which components have finished
    instr_8Components = [];
    instr_8Components.push(key_resp_12);
    instr_8Components.push(space_11);
    instr_8Components.push(instr_only_5);
    instr_8Components.push(text_13);
    instr_8Components.push(center_cross_3);
    instr_8Components.push(black_square);
    instr_8Components.push(text_14);
    
    instr_8Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function instr_8RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'instr_8'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instr_8Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_12* updates
    if (t >= 2 && key_resp_12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_12.tStart = t;  // (not accounting for frame time here)
      key_resp_12.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_12.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_12.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_12.clearEvents(); });
    }

    if (key_resp_12.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_12.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_12_allKeys = _key_resp_12_allKeys.concat(theseKeys);
      if (_key_resp_12_allKeys.length > 0) {
        key_resp_12.keys = _key_resp_12_allKeys[_key_resp_12_allKeys.length - 1].name;  // just the last key pressed
        key_resp_12.rt = _key_resp_12_allKeys[_key_resp_12_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *space_11* updates
    if (t >= 2 && space_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_11.tStart = t;  // (not accounting for frame time here)
      space_11.frameNStart = frameN;  // exact frame index
      
      space_11.setAutoDraw(true);
    }

    
    // *instr_only_5* updates
    if (t >= 0.0 && instr_only_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_only_5.tStart = t;  // (not accounting for frame time here)
      instr_only_5.frameNStart = frameN;  // exact frame index
      
      instr_only_5.setAutoDraw(true);
    }

    
    // *text_13* updates
    if (t >= 0.0 && text_13.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_13.tStart = t;  // (not accounting for frame time here)
      text_13.frameNStart = frameN;  // exact frame index
      
      text_13.setAutoDraw(true);
    }

    
    // *center_cross_3* updates
    if (t >= 0.0 && center_cross_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      center_cross_3.tStart = t;  // (not accounting for frame time here)
      center_cross_3.frameNStart = frameN;  // exact frame index
      
      center_cross_3.setAutoDraw(true);
    }

    
    // *black_square* updates
    if (t >= 0.0 && black_square.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      black_square.tStart = t;  // (not accounting for frame time here)
      black_square.frameNStart = frameN;  // exact frame index
      
      black_square.setAutoDraw(true);
    }

    
    // *text_14* updates
    if (t >= 0.0 && text_14.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_14.tStart = t;  // (not accounting for frame time here)
      text_14.frameNStart = frameN;  // exact frame index
      
      text_14.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instr_8Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instr_8RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'instr_8'-------
    instr_8Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_12.keys', key_resp_12.keys);
    if (typeof key_resp_12.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_12.rt', key_resp_12.rt);
        routineTimer.reset();
        }
    
    key_resp_12.stop();
    // the Routine "instr_8" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_11_allKeys;
var instr_9Components;
function instr_9RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'instr_9'-------
    t = 0;
    instr_9Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_11.keys = undefined;
    key_resp_11.rt = undefined;
    _key_resp_11_allKeys = [];
    black_square1.setSize([(8.5 * ratio_pxpermm), (8.5 * ratio_pxpermm)]);
    white_ball2.setSize([(8.5 * ratio_pxpermm), (8.5 * ratio_pxpermm)]);
    // keep track of which components have finished
    instr_9Components = [];
    instr_9Components.push(key_resp_11);
    instr_9Components.push(space_8);
    instr_9Components.push(instr_only_4);
    instr_9Components.push(text_11);
    instr_9Components.push(center_cross_2);
    instr_9Components.push(black_square1);
    instr_9Components.push(text_12);
    instr_9Components.push(white_ball2);
    
    instr_9Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function instr_9RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'instr_9'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instr_9Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_11* updates
    if (t >= 2 && key_resp_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_11.tStart = t;  // (not accounting for frame time here)
      key_resp_11.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_11.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_11.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_11.clearEvents(); });
    }

    if (key_resp_11.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_11.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_11_allKeys = _key_resp_11_allKeys.concat(theseKeys);
      if (_key_resp_11_allKeys.length > 0) {
        key_resp_11.keys = _key_resp_11_allKeys[_key_resp_11_allKeys.length - 1].name;  // just the last key pressed
        key_resp_11.rt = _key_resp_11_allKeys[_key_resp_11_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *space_8* updates
    if (t >= 2 && space_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_8.tStart = t;  // (not accounting for frame time here)
      space_8.frameNStart = frameN;  // exact frame index
      
      space_8.setAutoDraw(true);
    }

    
    // *instr_only_4* updates
    if (t >= 0.0 && instr_only_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_only_4.tStart = t;  // (not accounting for frame time here)
      instr_only_4.frameNStart = frameN;  // exact frame index
      
      instr_only_4.setAutoDraw(true);
    }

    
    // *text_11* updates
    if (t >= 0.0 && text_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_11.tStart = t;  // (not accounting for frame time here)
      text_11.frameNStart = frameN;  // exact frame index
      
      text_11.setAutoDraw(true);
    }

    
    // *center_cross_2* updates
    if (t >= 0.0 && center_cross_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      center_cross_2.tStart = t;  // (not accounting for frame time here)
      center_cross_2.frameNStart = frameN;  // exact frame index
      
      center_cross_2.setAutoDraw(true);
    }

    
    // *black_square1* updates
    if (t >= 0.0 && black_square1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      black_square1.tStart = t;  // (not accounting for frame time here)
      black_square1.frameNStart = frameN;  // exact frame index
      
      black_square1.setAutoDraw(true);
    }

    
    // *text_12* updates
    if (t >= 0.0 && text_12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_12.tStart = t;  // (not accounting for frame time here)
      text_12.frameNStart = frameN;  // exact frame index
      
      text_12.setAutoDraw(true);
    }

    
    // *white_ball2* updates
    if (t >= 0.0 && white_ball2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      white_ball2.tStart = t;  // (not accounting for frame time here)
      white_ball2.frameNStart = frameN;  // exact frame index
      
      white_ball2.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instr_9Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instr_9RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'instr_9'-------
    instr_9Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_11.keys', key_resp_11.keys);
    if (typeof key_resp_11.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_11.rt', key_resp_11.rt);
        routineTimer.reset();
        }
    
    key_resp_11.stop();
    // the Routine "instr_9" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_18_allKeys;
var instr_10Components;
function instr_10RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'instr_10'-------
    t = 0;
    instr_10Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_18.keys = undefined;
    key_resp_18.rt = undefined;
    _key_resp_18_allKeys = [];
    // keep track of which components have finished
    instr_10Components = [];
    instr_10Components.push(key_resp_18);
    instr_10Components.push(space_17);
    instr_10Components.push(instr_only_7);
    instr_10Components.push(text_44);
    
    instr_10Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function instr_10RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'instr_10'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instr_10Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_18* updates
    if (t >= 2 && key_resp_18.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_18.tStart = t;  // (not accounting for frame time here)
      key_resp_18.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_18.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_18.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_18.clearEvents(); });
    }

    if (key_resp_18.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_18.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_18_allKeys = _key_resp_18_allKeys.concat(theseKeys);
      if (_key_resp_18_allKeys.length > 0) {
        key_resp_18.keys = _key_resp_18_allKeys[_key_resp_18_allKeys.length - 1].name;  // just the last key pressed
        key_resp_18.rt = _key_resp_18_allKeys[_key_resp_18_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *space_17* updates
    if (t >= 2 && space_17.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_17.tStart = t;  // (not accounting for frame time here)
      space_17.frameNStart = frameN;  // exact frame index
      
      space_17.setAutoDraw(true);
    }

    
    // *instr_only_7* updates
    if (t >= 0.0 && instr_only_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_only_7.tStart = t;  // (not accounting for frame time here)
      instr_only_7.frameNStart = frameN;  // exact frame index
      
      instr_only_7.setAutoDraw(true);
    }

    
    // *text_44* updates
    if (t >= 0.0 && text_44.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_44.tStart = t;  // (not accounting for frame time here)
      text_44.frameNStart = frameN;  // exact frame index
      
      text_44.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instr_10Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instr_10RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'instr_10'-------
    instr_10Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_18.keys', key_resp_18.keys);
    if (typeof key_resp_18.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_18.rt', key_resp_18.rt);
        routineTimer.reset();
        }
    
    key_resp_18.stop();
    // the Routine "instr_10" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_21_allKeys;
var instr_11Components;
function instr_11RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'instr_11'-------
    t = 0;
    instr_11Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_21.keys = undefined;
    key_resp_21.rt = undefined;
    _key_resp_21_allKeys = [];
    // keep track of which components have finished
    instr_11Components = [];
    instr_11Components.push(key_resp_21);
    instr_11Components.push(space_18);
    instr_11Components.push(instr_only_8);
    instr_11Components.push(text_45);
    
    instr_11Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function instr_11RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'instr_11'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instr_11Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_21* updates
    if (t >= 2 && key_resp_21.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_21.tStart = t;  // (not accounting for frame time here)
      key_resp_21.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_21.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_21.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_21.clearEvents(); });
    }

    if (key_resp_21.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_21.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_21_allKeys = _key_resp_21_allKeys.concat(theseKeys);
      if (_key_resp_21_allKeys.length > 0) {
        key_resp_21.keys = _key_resp_21_allKeys[_key_resp_21_allKeys.length - 1].name;  // just the last key pressed
        key_resp_21.rt = _key_resp_21_allKeys[_key_resp_21_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *space_18* updates
    if (t >= 2 && space_18.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_18.tStart = t;  // (not accounting for frame time here)
      space_18.frameNStart = frameN;  // exact frame index
      
      space_18.setAutoDraw(true);
    }

    
    // *instr_only_8* updates
    if (t >= 0.0 && instr_only_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_only_8.tStart = t;  // (not accounting for frame time here)
      instr_only_8.frameNStart = frameN;  // exact frame index
      
      instr_only_8.setAutoDraw(true);
    }

    
    // *text_45* updates
    if (t >= 0.0 && text_45.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_45.tStart = t;  // (not accounting for frame time here)
      text_45.frameNStart = frameN;  // exact frame index
      
      text_45.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instr_11Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instr_11RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'instr_11'-------
    instr_11Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_21.keys', key_resp_21.keys);
    if (typeof key_resp_21.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_21.rt', key_resp_21.rt);
        routineTimer.reset();
        }
    
    key_resp_21.stop();
    // the Routine "instr_11" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var ballpos;
var calibration_exampleComponents;
function calibration_exampleRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'calibration_example'-------
    t = 0;
    calibration_exampleClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    black_square3.setSize([(8.5 * ratio_pxpermm), (8.5 * ratio_pxpermm)]);
    ballpos = ((window.innerWidth / 2) * 0.75);
    
    // keep track of which components have finished
    calibration_exampleComponents = [];
    calibration_exampleComponents.push(white_ball1);
    calibration_exampleComponents.push(black_square3);
    calibration_exampleComponents.push(text_19);
    calibration_exampleComponents.push(text_20);
    calibration_exampleComponents.push(white_ball12);
    calibration_exampleComponents.push(text_21);
    calibration_exampleComponents.push(text_22);
    calibration_exampleComponents.push(white_ball13);
    
    calibration_exampleComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function calibration_exampleRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'calibration_example'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = calibration_exampleClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *white_ball1* updates
    if (t >= 0.0 && white_ball1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      white_ball1.tStart = t;  // (not accounting for frame time here)
      white_ball1.frameNStart = frameN;  // exact frame index
      
      white_ball1.setAutoDraw(true);
    }

    if (white_ball1.status === PsychoJS.Status.STARTED && frameN >= 250) {
      white_ball1.setAutoDraw(false);
    }
    
    if (white_ball1.status === PsychoJS.Status.STARTED){ // only update if being drawn
      white_ball1.setPos([(((- frameN) * ((window.innerWidth / 2) * 0.003)) + ballpos), 0]);
      white_ball1.setSize([(8.5 * ratio_pxpermm), (8.5 * ratio_pxpermm)]);
    }
    
    // *black_square3* updates
    if (t >= 0.0 && black_square3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      black_square3.tStart = t;  // (not accounting for frame time here)
      black_square3.frameNStart = frameN;  // exact frame index
      
      black_square3.setAutoDraw(true);
    }

    
    if (black_square3.status === PsychoJS.Status.STARTED){ // only update if being drawn
      black_square3.setPos([((window.innerWidth / 2) * 0.8), 0]);
    }
    
    // *text_19* updates
    if (t >= 0.0 && text_19.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_19.tStart = t;  // (not accounting for frame time here)
      text_19.frameNStart = frameN;  // exact frame index
      
      text_19.setAutoDraw(true);
    }

    if (text_19.status === PsychoJS.Status.STARTED && frameN >= 250) {
      text_19.setAutoDraw(false);
    }
    
    // *text_20* updates
    if (frameN >= 250 && text_20.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_20.tStart = t;  // (not accounting for frame time here)
      text_20.frameNStart = frameN;  // exact frame index
      
      text_20.setAutoDraw(true);
    }

    if (text_20.status === PsychoJS.Status.STARTED && frameN >= 320) {
      text_20.setAutoDraw(false);
    }
    
    // *white_ball12* updates
    if (frameN >= 320 && white_ball12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      white_ball12.tStart = t;  // (not accounting for frame time here)
      white_ball12.frameNStart = frameN;  // exact frame index
      
      white_ball12.setAutoDraw(true);
    }

    if (white_ball12.status === PsychoJS.Status.STARTED && frameN >= 400) {
      white_ball12.setAutoDraw(false);
    }
    
    if (white_ball12.status === PsychoJS.Status.STARTED){ // only update if being drawn
      white_ball12.setPos([(((- frameN) * ((window.innerWidth / 2) * 0.003)) + ((window.innerWidth / 2) * 0.05)), 0]);
      white_ball12.setSize([(8.5 * ratio_pxpermm), (8.5 * ratio_pxpermm)]);
    }
    
    // *text_21* updates
    if (frameN >= 320 && text_21.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_21.tStart = t;  // (not accounting for frame time here)
      text_21.frameNStart = frameN;  // exact frame index
      
      text_21.setAutoDraw(true);
    }

    
    // *text_22* updates
    if (frameN >= 250 && text_22.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_22.tStart = t;  // (not accounting for frame time here)
      text_22.frameNStart = frameN;  // exact frame index
      
      text_22.setAutoDraw(true);
    }

    if (text_22.status === PsychoJS.Status.STARTED && frameN >= 320) {
      text_22.setAutoDraw(false);
    }
    
    // *white_ball13* updates
    if (frameN >= 400 && white_ball13.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      white_ball13.tStart = t;  // (not accounting for frame time here)
      white_ball13.frameNStart = frameN;  // exact frame index
      
      white_ball13.setAutoDraw(true);
    }

    if (white_ball13.status === PsychoJS.Status.STARTED && frameN >= 550) {
      white_ball13.setAutoDraw(false);
    }
    
    if (white_ball13.status === PsychoJS.Status.STARTED){ // only update if being drawn
      white_ball13.setPos([((((- frameN) + 400) * ((window.innerWidth / 2) * 0.003)) + ballpos), 0]);
      white_ball13.setSize([(8.5 * ratio_pxpermm), (8.5 * ratio_pxpermm)]);
    }
    if ((frameN === 550)) {
        continueRoutine = false;
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    calibration_exampleComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function calibration_exampleRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'calibration_example'-------
    calibration_exampleComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "calibration_example" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_13_allKeys;
var instr_12Components;
function instr_12RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'instr_12'-------
    t = 0;
    instr_12Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_13.keys = undefined;
    key_resp_13.rt = undefined;
    _key_resp_13_allKeys = [];
    // keep track of which components have finished
    instr_12Components = [];
    instr_12Components.push(key_resp_13);
    instr_12Components.push(space_12);
    instr_12Components.push(instr_only_6);
    instr_12Components.push(text_15);
    
    instr_12Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function instr_12RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'instr_12'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instr_12Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_13* updates
    if (t >= 2 && key_resp_13.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_13.tStart = t;  // (not accounting for frame time here)
      key_resp_13.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_13.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_13.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_13.clearEvents(); });
    }

    if (key_resp_13.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_13.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_13_allKeys = _key_resp_13_allKeys.concat(theseKeys);
      if (_key_resp_13_allKeys.length > 0) {
        key_resp_13.keys = _key_resp_13_allKeys[_key_resp_13_allKeys.length - 1].name;  // just the last key pressed
        key_resp_13.rt = _key_resp_13_allKeys[_key_resp_13_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *space_12* updates
    if (t >= 2 && space_12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_12.tStart = t;  // (not accounting for frame time here)
      space_12.frameNStart = frameN;  // exact frame index
      
      space_12.setAutoDraw(true);
    }

    
    // *instr_only_6* updates
    if (t >= 0.0 && instr_only_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_only_6.tStart = t;  // (not accounting for frame time here)
      instr_only_6.frameNStart = frameN;  // exact frame index
      
      instr_only_6.setAutoDraw(true);
    }

    
    // *text_15* updates
    if (t >= 0.0 && text_15.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_15.tStart = t;  // (not accounting for frame time here)
      text_15.frameNStart = frameN;  // exact frame index
      
      text_15.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instr_12Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instr_12RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'instr_12'-------
    instr_12Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_13.keys', key_resp_13.keys);
    if (typeof key_resp_13.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_13.rt', key_resp_13.rt);
        routineTimer.reset();
        }
    
    key_resp_13.stop();
    // the Routine "instr_12" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var trials;
var currentLoop;
function trialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 5, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'trials'
  });
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment
  currentLoop = trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials.forEach(function() {
    const snapshot = trials.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(ball_calibrationRoutineBegin(snapshot));
    thisScheduler.add(ball_calibrationRoutineEachFrame(snapshot));
    thisScheduler.add(ball_calibrationRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}


var duringprac;
function duringpracLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  duringprac = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'practrials.xlsx', '0:7'),
    seed: undefined, name: 'duringprac'
  });
  psychoJS.experiment.addLoop(duringprac); // add the loop to the experiment
  currentLoop = duringprac;  // we're now the current loop

  // Schedule all the trials in the trialList:
  duringprac.forEach(function() {
    const snapshot = duringprac.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(Stim1_display_pracRoutineBegin(snapshot));
    thisScheduler.add(Stim1_display_pracRoutineEachFrame(snapshot));
    thisScheduler.add(Stim1_display_pracRoutineEnd(snapshot));
    thisScheduler.add(response_pracRoutineBegin(snapshot));
    thisScheduler.add(response_pracRoutineEachFrame(snapshot));
    thisScheduler.add(response_pracRoutineEnd(snapshot));
    thisScheduler.add(responseprac_feedbackRoutineBegin(snapshot));
    thisScheduler.add(responseprac_feedbackRoutineEachFrame(snapshot));
    thisScheduler.add(responseprac_feedbackRoutineEnd(snapshot));
    thisScheduler.add(summary_pracRoutineBegin(snapshot));
    thisScheduler.add(summary_pracRoutineEachFrame(snapshot));
    thisScheduler.add(summary_pracRoutineEnd(snapshot));
    thisScheduler.add(special_trial_pracRoutineBegin(snapshot));
    thisScheduler.add(special_trial_pracRoutineEachFrame(snapshot));
    thisScheduler.add(special_trial_pracRoutineEnd(snapshot));
    thisScheduler.add(catch_pracRoutineBegin(snapshot));
    thisScheduler.add(catch_pracRoutineEachFrame(snapshot));
    thisScheduler.add(catch_pracRoutineEnd(snapshot));
    thisScheduler.add(summary2_pracRoutineBegin(snapshot));
    thisScheduler.add(summary2_pracRoutineEachFrame(snapshot));
    thisScheduler.add(summary2_pracRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function duringpracLoopEnd() {
  psychoJS.experiment.removeLoop(duringprac);

  return Scheduler.Event.NEXT;
}


var trials_3;
function trials_3LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_3 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 2, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'trials_3'
  });
  psychoJS.experiment.addLoop(trials_3); // add the loop to the experiment
  currentLoop = trials_3;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials_3.forEach(function() {
    const snapshot = trials_3.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    const trials_2LoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(trials_2LoopBegin, trials_2LoopScheduler);
    thisScheduler.add(trials_2LoopScheduler);
    thisScheduler.add(trials_2LoopEnd);
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


var trials_2;
function trials_2LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_2 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'Stimconditions.xlsx', '0:162'),
    seed: order, name: 'trials_2'
  });
  psychoJS.experiment.addLoop(trials_2); // add the loop to the experiment
  currentLoop = trials_2;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials_2.forEach(function() {
    const snapshot = trials_2.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(Stim1_displayRoutineBegin(snapshot));
    thisScheduler.add(Stim1_displayRoutineEachFrame(snapshot));
    thisScheduler.add(Stim1_displayRoutineEnd(snapshot));
    thisScheduler.add(responseRoutineBegin(snapshot));
    thisScheduler.add(responseRoutineEachFrame(snapshot));
    thisScheduler.add(responseRoutineEnd(snapshot));
    thisScheduler.add(response_2RoutineBegin(snapshot));
    thisScheduler.add(response_2RoutineEachFrame(snapshot));
    thisScheduler.add(response_2RoutineEnd(snapshot));
    thisScheduler.add(special_trialRoutineBegin(snapshot));
    thisScheduler.add(special_trialRoutineEachFrame(snapshot));
    thisScheduler.add(special_trialRoutineEnd(snapshot));
    thisScheduler.add(catch_1RoutineBegin(snapshot));
    thisScheduler.add(catch_1RoutineEachFrame(snapshot));
    thisScheduler.add(catch_1RoutineEnd(snapshot));
    thisScheduler.add(response_sumRoutineBegin(snapshot));
    thisScheduler.add(response_sumRoutineEachFrame(snapshot));
    thisScheduler.add(response_sumRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function trials_2LoopEnd() {
  psychoJS.experiment.removeLoop(trials_2);

  return Scheduler.Event.NEXT;
}


function trials_3LoopEnd() {
  psychoJS.experiment.removeLoop(trials_3);

  return Scheduler.Event.NEXT;
}


var _key_resp_19_allKeys;
var blindspot_angle;
var radians_to_degrees;
var calibrationcountext;
var ball_calibrationComponents;
function ball_calibrationRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'ball_calibration'-------
    t = 0;
    ball_calibrationClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    black_square2.setSize([(8.5 * ratio_pxpermm), (8.5 * ratio_pxpermm)]);
    white_ball.setSize([(8.5 * ratio_pxpermm), (8.5 * ratio_pxpermm)]);
    key_resp_19.keys = undefined;
    key_resp_19.rt = undefined;
    _key_resp_19_allKeys = [];
    blindspot_angle = 13.5;
    ballpos = ((window.innerWidth / 2) * 0.75);
    radians_to_degrees = 57.2958;
    calibrationcountext = `${calibrationcount} of 5 angle calibrations complete`;
    
    text_39.setText(calibrationcountext);
    white_ball1_2.setSize([(8.5 * ratio_pxpermm), (8.5 * ratio_pxpermm)]);
    // keep track of which components have finished
    ball_calibrationComponents = [];
    ball_calibrationComponents.push(black_square2);
    ball_calibrationComponents.push(white_ball);
    ball_calibrationComponents.push(key_resp_19);
    ball_calibrationComponents.push(text_39);
    ball_calibrationComponents.push(white_ball1_2);
    
    ball_calibrationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function ball_calibrationRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'ball_calibration'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = ball_calibrationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *black_square2* updates
    if (t >= 0.0 && black_square2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      black_square2.tStart = t;  // (not accounting for frame time here)
      black_square2.frameNStart = frameN;  // exact frame index
      
      black_square2.setAutoDraw(true);
    }

    
    if (black_square2.status === PsychoJS.Status.STARTED){ // only update if being drawn
      black_square2.setPos([((window.innerWidth / 2) * 0.8), 0]);
    }
    
    // *white_ball* updates
    if (t >= 0.0 && white_ball.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      white_ball.tStart = t;  // (not accounting for frame time here)
      white_ball.frameNStart = frameN;  // exact frame index
      
      white_ball.setAutoDraw(true);
    }

    if (white_ball.status === PsychoJS.Status.STARTED && frameN >= 800) {
      white_ball.setAutoDraw(false);
    }
    
    if (white_ball.status === PsychoJS.Status.STARTED){ // only update if being drawn
      white_ball.setPos([(((- frameN) * ((window.innerWidth / 2) * 0.003)) + ballpos), 0]);
    }
    
    // *key_resp_19* updates
    if (t >= 0.0 && key_resp_19.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_19.tStart = t;  // (not accounting for frame time here)
      key_resp_19.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_19.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_19.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_19.clearEvents(); });
    }

    if (key_resp_19.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_19.getKeys({keyList: ['return'], waitRelease: false});
      _key_resp_19_allKeys = _key_resp_19_allKeys.concat(theseKeys);
      if (_key_resp_19_allKeys.length > 0) {
        key_resp_19.keys = _key_resp_19_allKeys[_key_resp_19_allKeys.length - 1].name;  // just the last key pressed
        key_resp_19.rt = _key_resp_19_allKeys[_key_resp_19_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_39* updates
    if (t >= 0.0 && text_39.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_39.tStart = t;  // (not accounting for frame time here)
      text_39.frameNStart = frameN;  // exact frame index
      
      text_39.setAutoDraw(true);
    }

    
    // *white_ball1_2* updates
    if (frameN >= 800 && white_ball1_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      white_ball1_2.tStart = t;  // (not accounting for frame time here)
      white_ball1_2.frameNStart = frameN;  // exact frame index
      
      white_ball1_2.setAutoDraw(true);
    }

    
    if (white_ball1_2.status === PsychoJS.Status.STARTED){ // only update if being drawn
      white_ball1_2.setPos([((((- frameN) + 800) * ((window.innerWidth / 2) * 0.003)) + ballpos), 0]);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    ball_calibrationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var currentframe;
var ballposx;
var squarepos;
var viewer_distance;
function ball_calibrationRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'ball_calibration'-------
    ball_calibrationComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_19.keys', key_resp_19.keys);
    if (typeof key_resp_19.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_19.rt', key_resp_19.rt);
        routineTimer.reset();
        }
    
    key_resp_19.stop();
    currentframe = frameN;
    if ((currentframe < 800)) {
        ballposx = white_ball.pos[0];
    }
    if ((currentframe >= 800)) {
        ballposx = white_ball1_2.pos[0];
    }
    squarepos = black_square2.pos[0];
    viewer_distance = (((squarepos - ballposx) / ratio_pxpermm) / tan((blindspot_angle / radians_to_degrees)));
    viewerdistancetotal.append(viewer_distance);
    calibrationcount = (calibrationcount + 1);
    thisExp.addData("ballposx", ballposx);
    thisExp.addData("viewer_distance", viewer_distance);
    
    // the Routine "ball_calibration" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var viewerdistancecmSort;
var len;
var mid;
var viewerdistancemm;
var viewerdistancecm;
var viewdistancetext;
var DVA_to_distance;
var radius_F;
var radius_P;
var r_F;
var R_P;
var _key_resp_20_allKeys;
var viewerdistanceComponents;
function viewerdistanceRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'viewerdistance'-------
    t = 0;
    viewerdistanceClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // Find median of viewer distance
    viewerdistancecmSort = viewerdistancetotal.sort();
    len = 5;
    mid = Math.ceil(len/2)
    viewerdistancemm =
       len % 2 == 0 ? (viewerdistancecmSort[mid] + viewerdistancecmSort[mid - 1]) / 2 : viewerdistancecmSort[mid - 1];
    
    viewerdistancecm = Math.round((viewerdistancemm / 10), 3);
    viewdistancetext = `Your viewing distance is ${viewerdistancecm} cm`;
    DVA_to_distance = ((viewerdistancecm * tan((1 / radians_to_degrees))) * 10);
    radius_F = ((DVA_to_distance * ratio_pxpermm) * radius_central);
    radius_P = ((DVA_to_distance * ratio_pxpermm) * radius_peripheral);
    r_F = ((DVA_to_distance * ratio_pxpermm) * stimulus_size);
    R_P = (peripheral_scale * r_F);
    
    text_38.setText(viewdistancetext);
    key_resp_20.keys = undefined;
    key_resp_20.rt = undefined;
    _key_resp_20_allKeys = [];
    // keep track of which components have finished
    viewerdistanceComponents = [];
    viewerdistanceComponents.push(text_38);
    viewerdistanceComponents.push(text_40);
    viewerdistanceComponents.push(key_resp_20);
    viewerdistanceComponents.push(space_20);
    
    viewerdistanceComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function viewerdistanceRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'viewerdistance'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = viewerdistanceClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    if (((viewerdistancecm * 10) < distance_threshold)) {
        continueRoutine = false;
    }
    if ((screen_size_x < screen_x_threshold)) {
        continueRoutine = false;
    }
    
    
    // *text_38* updates
    if (t >= 0.0 && text_38.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_38.tStart = t;  // (not accounting for frame time here)
      text_38.frameNStart = frameN;  // exact frame index
      
      text_38.setAutoDraw(true);
    }

    
    // *text_40* updates
    if (t >= 0.0 && text_40.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_40.tStart = t;  // (not accounting for frame time here)
      text_40.frameNStart = frameN;  // exact frame index
      
      text_40.setAutoDraw(true);
    }

    
    // *key_resp_20* updates
    if (t >= 0.0 && key_resp_20.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_20.tStart = t;  // (not accounting for frame time here)
      key_resp_20.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_20.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_20.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_20.clearEvents(); });
    }

    if (key_resp_20.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_20.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_20_allKeys = _key_resp_20_allKeys.concat(theseKeys);
      if (_key_resp_20_allKeys.length > 0) {
        key_resp_20.keys = _key_resp_20_allKeys[_key_resp_20_allKeys.length - 1].name;  // just the last key pressed
        key_resp_20.rt = _key_resp_20_allKeys[_key_resp_20_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *space_20* updates
    if (t >= 2 && space_20.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_20.tStart = t;  // (not accounting for frame time here)
      space_20.frameNStart = frameN;  // exact frame index
      
      space_20.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    viewerdistanceComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function viewerdistanceRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'viewerdistance'-------
    viewerdistanceComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    thisExp.addData("viewerdistancecm", viewerdistancecm);
    thisExp.addData("DVA_to_distance", DVA_to_distance);
    thisExp.addData("radius_F", radius_F);
    thisExp.addData("radius_P", radius_P);
    thisExp.addData("r_F", r_F);
    thisExp.addData("R_P", R_P);
    
    psychoJS.experiment.addData('key_resp_20.keys', key_resp_20.keys);
    if (typeof key_resp_20.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_20.rt', key_resp_20.rt);
        routineTimer.reset();
        }
    
    key_resp_20.stop();
    // the Routine "viewerdistance" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var viewerdistance_unsucessComponents;
function viewerdistance_unsucessRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'viewerdistance_unsucess'-------
    t = 0;
    viewerdistance_unsucessClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    viewerdistancecm = Math.round((sum(viewerdistancetotal) / 50), 3);
    viewdistancetext = `Your viewing distance is calculated as ${viewerdistancecm} cm`;
    
    text_42.setText(viewdistancetext);
    // keep track of which components have finished
    viewerdistance_unsucessComponents = [];
    viewerdistance_unsucessComponents.push(text_41);
    viewerdistance_unsucessComponents.push(text_42);
    viewerdistance_unsucessComponents.push(text_43);
    
    viewerdistance_unsucessComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function viewerdistance_unsucessRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'viewerdistance_unsucess'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = viewerdistance_unsucessClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    if ((((viewerdistancecm * 10) > distance_threshold) && (screen_size_x > screen_x_threshold))) {
        continueRoutine = false;
    }
    
    
    // *text_41* updates
    if (t >= 0.0 && text_41.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_41.tStart = t;  // (not accounting for frame time here)
      text_41.frameNStart = frameN;  // exact frame index
      
      text_41.setAutoDraw(true);
    }

    
    // *text_42* updates
    if (t >= 0.0 && text_42.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_42.tStart = t;  // (not accounting for frame time here)
      text_42.frameNStart = frameN;  // exact frame index
      
      text_42.setAutoDraw(true);
    }

    
    // *text_43* updates
    if (t >= 0.0 && text_43.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_43.tStart = t;  // (not accounting for frame time here)
      text_43.frameNStart = frameN;  // exact frame index
      
      text_43.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    viewerdistance_unsucessComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function viewerdistance_unsucessRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'viewerdistance_unsucess'-------
    viewerdistance_unsucessComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "viewerdistance_unsucess" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_14_allKeys;
var stim1_instrComponents;
function stim1_instrRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'stim1_instr'-------
    t = 0;
    stim1_instrClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_14.keys = undefined;
    key_resp_14.rt = undefined;
    _key_resp_14_allKeys = [];
    // keep track of which components have finished
    stim1_instrComponents = [];
    stim1_instrComponents.push(stim1);
    stim1_instrComponents.push(key_resp_14);
    stim1_instrComponents.push(space_13);
    stim1_instrComponents.push(text_16);
    
    stim1_instrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function stim1_instrRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'stim1_instr'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = stim1_instrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *stim1* updates
    if (t >= 0.0 && stim1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stim1.tStart = t;  // (not accounting for frame time here)
      stim1.frameNStart = frameN;  // exact frame index
      
      stim1.setAutoDraw(true);
    }

    
    // *key_resp_14* updates
    if (t >= 2 && key_resp_14.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_14.tStart = t;  // (not accounting for frame time here)
      key_resp_14.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      key_resp_14.clock.reset();
      key_resp_14.start();
      key_resp_14.clearEvents();
    }

    if (key_resp_14.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_14.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_14_allKeys = _key_resp_14_allKeys.concat(theseKeys);
      if (_key_resp_14_allKeys.length > 0) {
        key_resp_14.keys = _key_resp_14_allKeys[_key_resp_14_allKeys.length - 1].name;  // just the last key pressed
        key_resp_14.rt = _key_resp_14_allKeys[_key_resp_14_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *space_13* updates
    if (t >= 2 && space_13.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_13.tStart = t;  // (not accounting for frame time here)
      space_13.frameNStart = frameN;  // exact frame index
      
      space_13.setAutoDraw(true);
    }

    
    // *text_16* updates
    if (t >= 0.0 && text_16.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_16.tStart = t;  // (not accounting for frame time here)
      text_16.frameNStart = frameN;  // exact frame index
      
      text_16.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    stim1_instrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function stim1_instrRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'stim1_instr'-------
    stim1_instrComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_14.keys', key_resp_14.keys);
    if (typeof key_resp_14.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_14.rt', key_resp_14.rt);
        routineTimer.reset();
        }
    
    key_resp_14.stop();
    // the Routine "stim1_instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_15_allKeys;
var stim_response_instrComponents;
function stim_response_instrRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'stim_response_instr'-------
    t = 0;
    stim_response_instrClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_15.keys = undefined;
    key_resp_15.rt = undefined;
    _key_resp_15_allKeys = [];
    // keep track of which components have finished
    stim_response_instrComponents = [];
    stim_response_instrComponents.push(movie_2);
    stim_response_instrComponents.push(key_resp_15);
    stim_response_instrComponents.push(space_14);
    stim_response_instrComponents.push(text_17);
    
    stim_response_instrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function stim_response_instrRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'stim_response_instr'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = stim_response_instrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *movie_2* updates
    if (t >= 0.0 && movie_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      movie_2.tStart = t;  // (not accounting for frame time here)
      movie_2.frameNStart = frameN;  // exact frame index
      
      movie_2.setAutoDraw(true);
    }

    
    // *key_resp_15* updates
    if (t >= 2 && key_resp_15.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_15.tStart = t;  // (not accounting for frame time here)
      key_resp_15.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_15.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_15.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_15.clearEvents(); });
    }

    if (key_resp_15.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_15.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_15_allKeys = _key_resp_15_allKeys.concat(theseKeys);
      if (_key_resp_15_allKeys.length > 0) {
        key_resp_15.keys = _key_resp_15_allKeys[_key_resp_15_allKeys.length - 1].name;  // just the last key pressed
        key_resp_15.rt = _key_resp_15_allKeys[_key_resp_15_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *space_14* updates
    if (t >= 2 && space_14.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_14.tStart = t;  // (not accounting for frame time here)
      space_14.frameNStart = frameN;  // exact frame index
      
      space_14.setAutoDraw(true);
    }

    
    // *text_17* updates
    if (t >= 0.0 && text_17.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_17.tStart = t;  // (not accounting for frame time here)
      text_17.frameNStart = frameN;  // exact frame index
      
      text_17.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    stim_response_instrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function stim_response_instrRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'stim_response_instr'-------
    stim_response_instrComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_15.keys', key_resp_15.keys);
    if (typeof key_resp_15.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_15.rt', key_resp_15.rt);
        routineTimer.reset();
        }
    
    key_resp_15.stop();
    // the Routine "stim_response_instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_17_allKeys;
var catch_insrtComponents;
function catch_insrtRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'catch_insrt'-------
    t = 0;
    catch_insrtClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_17.keys = undefined;
    key_resp_17.rt = undefined;
    _key_resp_17_allKeys = [];
    // keep track of which components have finished
    catch_insrtComponents = [];
    catch_insrtComponents.push(space_15);
    catch_insrtComponents.push(key_resp_17);
    catch_insrtComponents.push(movie_3);
    catch_insrtComponents.push(text_18);
    
    catch_insrtComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function catch_insrtRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'catch_insrt'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = catch_insrtClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *space_15* updates
    if (t >= 2 && space_15.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_15.tStart = t;  // (not accounting for frame time here)
      space_15.frameNStart = frameN;  // exact frame index
      
      space_15.setAutoDraw(true);
    }

    
    // *key_resp_17* updates
    if (t >= 2 && key_resp_17.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_17.tStart = t;  // (not accounting for frame time here)
      key_resp_17.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_17.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_17.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_17.clearEvents(); });
    }

    if (key_resp_17.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_17.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _key_resp_17_allKeys = _key_resp_17_allKeys.concat(theseKeys);
      if (_key_resp_17_allKeys.length > 0) {
        key_resp_17.keys = _key_resp_17_allKeys[_key_resp_17_allKeys.length - 1].name;  // just the last key pressed
        key_resp_17.rt = _key_resp_17_allKeys[_key_resp_17_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *movie_3* updates
    if (t >= 0.0 && movie_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      movie_3.tStart = t;  // (not accounting for frame time here)
      movie_3.frameNStart = frameN;  // exact frame index
      
      movie_3.setAutoDraw(true);
    }

    
    // *text_18* updates
    if (t >= 0.0 && text_18.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_18.tStart = t;  // (not accounting for frame time here)
      text_18.frameNStart = frameN;  // exact frame index
      
      text_18.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    catch_insrtComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function catch_insrtRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'catch_insrt'-------
    catch_insrtComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_17.keys', key_resp_17.keys);
    if (typeof key_resp_17.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_17.rt', key_resp_17.rt);
        routineTimer.reset();
        }
    
    key_resp_17.stop();
    // the Routine "catch_insrt" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var circle_position;
var _key_resp_9_allKeys;
var colour_circle_instr_2Components;
function colour_circle_instr_2RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'colour_circle_instr_2'-------
    t = 0;
    colour_circle_instr_2Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    circle_position = [[(- 230), 230], [0, 230], [230, 230], [(- 230), 0], [0, 0], [230, 0], [230, (- 230)], [0, (- 230)], [(- 230), (- 230)]];
    shuffle(circle_position);
    
    key_resp_9.keys = undefined;
    key_resp_9.rt = undefined;
    _key_resp_9_allKeys = [];
    intructioncircle_1.setPos(circle_position[1]);
    instructioncircle_2.setPos(circle_position[2]);
    instructioncircle_3.setPos(circle_position[3]);
    instructioncircle_4.setPos(circle_position[4]);
    instructioncircle_5.setPos(circle_position[5]);
    insturctioncircle_6.setPos(circle_position[6]);
    instructioncircle_7.setPos(circle_position[7]);
    instructioncircle_8.setPos(circle_position[8]);
    instructioncircle_9.setPos(circle_position[0]);
    // keep track of which components have finished
    colour_circle_instr_2Components = [];
    colour_circle_instr_2Components.push(key_resp_9);
    colour_circle_instr_2Components.push(intructioncircle_1);
    colour_circle_instr_2Components.push(instructioncircle_2);
    colour_circle_instr_2Components.push(instructioncircle_3);
    colour_circle_instr_2Components.push(instructioncircle_4);
    colour_circle_instr_2Components.push(instructioncircle_5);
    colour_circle_instr_2Components.push(insturctioncircle_6);
    colour_circle_instr_2Components.push(instructioncircle_7);
    colour_circle_instr_2Components.push(instructioncircle_8);
    colour_circle_instr_2Components.push(instructioncircle_9);
    colour_circle_instr_2Components.push(space_9);
    colour_circle_instr_2Components.push(text_9);
    
    colour_circle_instr_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function colour_circle_instr_2RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'colour_circle_instr_2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = colour_circle_instr_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_9* updates
    if (t >= 2 && key_resp_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_9.tStart = t;  // (not accounting for frame time here)
      key_resp_9.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_9.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_9.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_9.clearEvents(); });
    }

    if (key_resp_9.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_9.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_9_allKeys = _key_resp_9_allKeys.concat(theseKeys);
      if (_key_resp_9_allKeys.length > 0) {
        key_resp_9.keys = _key_resp_9_allKeys[_key_resp_9_allKeys.length - 1].name;  // just the last key pressed
        key_resp_9.rt = _key_resp_9_allKeys[_key_resp_9_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *intructioncircle_1* updates
    if (t >= 0.0 && intructioncircle_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      intructioncircle_1.tStart = t;  // (not accounting for frame time here)
      intructioncircle_1.frameNStart = frameN;  // exact frame index
      
      intructioncircle_1.setAutoDraw(true);
    }

    
    // *instructioncircle_2* updates
    if (t >= 0.0 && instructioncircle_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructioncircle_2.tStart = t;  // (not accounting for frame time here)
      instructioncircle_2.frameNStart = frameN;  // exact frame index
      
      instructioncircle_2.setAutoDraw(true);
    }

    
    // *instructioncircle_3* updates
    if (t >= 0.0 && instructioncircle_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructioncircle_3.tStart = t;  // (not accounting for frame time here)
      instructioncircle_3.frameNStart = frameN;  // exact frame index
      
      instructioncircle_3.setAutoDraw(true);
    }

    
    // *instructioncircle_4* updates
    if (t >= 0.0 && instructioncircle_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructioncircle_4.tStart = t;  // (not accounting for frame time here)
      instructioncircle_4.frameNStart = frameN;  // exact frame index
      
      instructioncircle_4.setAutoDraw(true);
    }

    
    // *instructioncircle_5* updates
    if (t >= 0.0 && instructioncircle_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructioncircle_5.tStart = t;  // (not accounting for frame time here)
      instructioncircle_5.frameNStart = frameN;  // exact frame index
      
      instructioncircle_5.setAutoDraw(true);
    }

    
    // *insturctioncircle_6* updates
    if (t >= 0.0 && insturctioncircle_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      insturctioncircle_6.tStart = t;  // (not accounting for frame time here)
      insturctioncircle_6.frameNStart = frameN;  // exact frame index
      
      insturctioncircle_6.setAutoDraw(true);
    }

    
    // *instructioncircle_7* updates
    if (t >= 0.0 && instructioncircle_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructioncircle_7.tStart = t;  // (not accounting for frame time here)
      instructioncircle_7.frameNStart = frameN;  // exact frame index
      
      instructioncircle_7.setAutoDraw(true);
    }

    
    // *instructioncircle_8* updates
    if (t >= 0.0 && instructioncircle_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructioncircle_8.tStart = t;  // (not accounting for frame time here)
      instructioncircle_8.frameNStart = frameN;  // exact frame index
      
      instructioncircle_8.setAutoDraw(true);
    }

    
    // *instructioncircle_9* updates
    if (t >= 0.0 && instructioncircle_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructioncircle_9.tStart = t;  // (not accounting for frame time here)
      instructioncircle_9.frameNStart = frameN;  // exact frame index
      
      instructioncircle_9.setAutoDraw(true);
    }

    
    // *space_9* updates
    if (t >= 2 && space_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_9.tStart = t;  // (not accounting for frame time here)
      space_9.frameNStart = frameN;  // exact frame index
      
      space_9.setAutoDraw(true);
    }

    
    // *text_9* updates
    if (t >= 0.0 && text_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_9.tStart = t;  // (not accounting for frame time here)
      text_9.frameNStart = frameN;  // exact frame index
      
      text_9.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    colour_circle_instr_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function colour_circle_instr_2RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'colour_circle_instr_2'-------
    colour_circle_instr_2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_9.keys', key_resp_9.keys);
    if (typeof key_resp_9.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_9.rt', key_resp_9.rt);
        routineTimer.reset();
        }
    
    key_resp_9.stop();
    // the Routine "colour_circle_instr_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_10_allKeys;
var instr_pracComponents;
function instr_pracRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'instr_prac'-------
    t = 0;
    instr_pracClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_10.keys = undefined;
    key_resp_10.rt = undefined;
    _key_resp_10_allKeys = [];
    // keep track of which components have finished
    instr_pracComponents = [];
    instr_pracComponents.push(space_10);
    instr_pracComponents.push(text_10);
    instr_pracComponents.push(key_resp_10);
    
    instr_pracComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function instr_pracRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'instr_prac'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instr_pracClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *space_10* updates
    if (t >= 2 && space_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_10.tStart = t;  // (not accounting for frame time here)
      space_10.frameNStart = frameN;  // exact frame index
      
      space_10.setAutoDraw(true);
    }

    
    // *text_10* updates
    if (t >= 0.0 && text_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_10.tStart = t;  // (not accounting for frame time here)
      text_10.frameNStart = frameN;  // exact frame index
      
      text_10.setAutoDraw(true);
    }

    
    // *key_resp_10* updates
    if (t >= 0.0 && key_resp_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_10.tStart = t;  // (not accounting for frame time here)
      key_resp_10.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_10.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_10.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_10.clearEvents(); });
    }

    if (key_resp_10.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_10.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_10_allKeys = _key_resp_10_allKeys.concat(theseKeys);
      if (_key_resp_10_allKeys.length > 0) {
        key_resp_10.keys = _key_resp_10_allKeys[_key_resp_10_allKeys.length - 1].name;  // just the last key pressed
        key_resp_10.rt = _key_resp_10_allKeys[_key_resp_10_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instr_pracComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instr_pracRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'instr_prac'-------
    instr_pracComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_10.keys', key_resp_10.keys);
    if (typeof key_resp_10.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_10.rt', key_resp_10.rt);
        routineTimer.reset();
        }
    
    key_resp_10.stop();
    // the Routine "instr_prac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var angle_1;
var angle_2;
var x;
var y;
var theta_1;
var theta_2;
var deltax_1;
var deltay_1;
var deltax_2;
var deltay_2;
var a_1;
var b_1;
var a_2;
var b_2;
var circle1posx;
var circle1posy;
var circlesizeh;
var circlesizew;
var Colour_1;
var Circle1_col;
var Stim1_display_pracComponents;
function Stim1_display_pracRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'Stim1_display_prac'-------
    t = 0;
    Stim1_display_pracClock.reset(); // clock
    frameN = -1;
    routineTimer.add(0.500000);
    // update component parameters for each repeat
    angle_1 = (Math.floor((Math.random() * ((30 - (- 30)) + 1))) + (- 30));
    angle_2 = (angle_1 + 180);
    x = 1;
    y = 1;
    theta_1 = (angle_1 * (pi / 180));
    theta_2 = (angle_2 * (pi / 180));
    deltax_1 = (radius_F * cos(theta_1));
    deltay_1 = (radius_F * sin(theta_1));
    deltax_2 = (radius_P * cos(theta_2));
    deltay_2 = (radius_P * sin(theta_2));
    a_1 = (x + deltax_1);
    b_1 = (y + deltay_1);
    a_2 = (x + deltax_2);
    b_2 = (y + deltay_2);
    if ((Ecc === "FF")) {
        circle1posx = a_1;
        circle1posy = b_1;
        circlesizeh = (2 * r_F);
        circlesizew = (2 * r_F);
    } else {
        if ((Ecc === "PF")) {
            circle1posx = a_2;
            circle1posy = b_2;
            circlesizeh = (2 * R_P);
            circlesizew = (2 * R_P);
        }
    }
    Colour_1 = (Math.floor((Math.random() * ((9 - 1) + 1))) + 1);
    if ((Colour_1 === 1)) {
        Circle1_col = [1, (- 1), (- 1)];
    } else {
        if ((Colour_1 === 2)) {
            Circle1_col = [1, 0.33, (- 1)];
        } else {
            if ((Colour_1 === 3)) {
                Circle1_col = [0.32, 1, (- 1)];
            } else {
                if ((Colour_1 === 4)) {
                    Circle1_col = [(- 1), 1, (- 1)];
                } else {
                    if ((Colour_1 === 5)) {
                        Circle1_col = [(- 1), 1, 0.33];
                    } else {
                        if ((Colour_1 === 6)) {
                            Circle1_col = [(- 1), 0.32, 1];
                        } else {
                            if ((Colour_1 === 7)) {
                                Circle1_col = [(- 1), (- 1), 1];
                            } else {
                                if ((Colour_1 === 8)) {
                                    Circle1_col = [0.33, (- 1), 1];
                                } else {
                                    if ((Colour_1 === 9)) {
                                        Circle1_col = [1, (- 1), 0.33];
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    
    Circle.setPos([circle1posx, circle1posy]);
    Circle.setSize([circlesizew, circlesizeh]);
    Circle.setFillColor(new util.Color(Circle1_col));
    Circle.setLineColor(new util.Color(Circle1_col));
    // keep track of which components have finished
    Stim1_display_pracComponents = [];
    Stim1_display_pracComponents.push(Circle);
    Stim1_display_pracComponents.push(centre_cross4_2);
    
    Stim1_display_pracComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function Stim1_display_pracRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'Stim1_display_prac'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = Stim1_display_pracClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Circle* updates
    if (t >= 0.0 && Circle.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Circle.tStart = t;  // (not accounting for frame time here)
      Circle.frameNStart = frameN;  // exact frame index
      
      Circle.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.25 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Circle.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Circle.setAutoDraw(false);
    }
    
    // *centre_cross4_2* updates
    if (t >= 0 && centre_cross4_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      centre_cross4_2.tStart = t;  // (not accounting for frame time here)
      centre_cross4_2.frameNStart = frameN;  // exact frame index
      
      centre_cross4_2.setAutoDraw(true);
    }

    frameRemains = 0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (centre_cross4_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      centre_cross4_2.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Stim1_display_pracComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Stim1_display_pracRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'Stim1_display_prac'-------
    Stim1_display_pracComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    thisExp.addData("Colour_1", Colour_1);
    thisExp.addData("Ecc", Ecc);
    
    return Scheduler.Event.NEXT;
  };
}


var gotValidClick;
var Colour_2;
var Circle2_col;
var response_pracComponents;
function response_pracRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'response_prac'-------
    t = 0;
    response_pracClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_5
    mouse_5.clicked_name = [];
    gotValidClick = false; // until a click is received
    event.clearEvents();
    pracnumber = (pracnumber + 1);
    Colour_2 = (Math.floor((Math.random() * ((9 - 1) + 1))) + 1);
    if ((Colour_2 === 1)) {
        Circle2_col = [1, (- 1), (- 1)];
    } else {
        if ((Colour_2 === 2)) {
            Circle2_col = [1, 0.33, (- 1)];
        } else {
            if ((Colour_2 === 3)) {
                Circle2_col = [0.32, 1, (- 1)];
            } else {
                if ((Colour_2 === 4)) {
                    Circle2_col = [(- 1), 1, (- 1)];
                } else {
                    if ((Colour_2 === 5)) {
                        Circle2_col = [(- 1), 1, 0.33];
                    } else {
                        if ((Colour_2 === 6)) {
                            Circle2_col = [(- 1), 0.32, 1];
                        } else {
                            if ((Colour_2 === 7)) {
                                Circle2_col = [(- 1), (- 1), 1];
                            } else {
                                if ((Colour_2 === 8)) {
                                    Circle2_col = [0.33, (- 1), 1];
                                } else {
                                    if ((Colour_2 === 9)) {
                                        Circle2_col = [1, (- 1), 0.33];
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    
    Circle_3.setSize([(15 * ratio_pxpermm), (15 * ratio_pxpermm)]);
    Circle_3.setFillColor(new util.Color(Circle2_col));
    Circle_3.setLineColor(new util.Color(Circle2_col));
    // keep track of which components have finished
    response_pracComponents = [];
    response_pracComponents.push(mouse_5);
    response_pracComponents.push(response1disk_5);
    response_pracComponents.push(response3disk_5);
    response_pracComponents.push(response5disk_5);
    response_pracComponents.push(response7disk_5);
    response_pracComponents.push(Circle_3);
    response_pracComponents.push(text_29);
    
    response_pracComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


var prevButtonState;
var mousexpos;
var mouseypos;
var x11d;
var y11d;
var x12d;
var y12d;
var x13d;
var y13d;
var a1d;
var b1d;
var c1d;
var x21d;
var y21d;
var x22d;
var y22d;
var x23d;
var y23d;
var a2d;
var b2d;
var c2d;
var x31d;
var y31d;
var x32d;
var y32d;
var x33d;
var y33d;
var a3d;
var b3d;
var c3d;
var x41d;
var y41d;
var x42d;
var y42d;
var x43d;
var y43d;
var a4d;
var b4d;
var c4d;
var x51d;
var y51d;
var x52d;
var y52d;
var x53d;
var y53d;
var a5d;
var b5d;
var c5d;
var x61d;
var y61d;
var x62d;
var y62d;
var x63d;
var y63d;
var a6d;
var b6d;
var c6d;
var x71d;
var y71d;
var x72d;
var y72d;
var x73d;
var y73d;
var a7d;
var b7d;
var c7d;
var x81d;
var y81d;
var x82d;
var y82d;
var x83d;
var y83d;
var a8d;
var b8d;
var c8d;
var similarity;
var responsenumber;
function response_pracRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'response_prac'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = response_pracClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // *mouse_5* updates
    if (t >= 0 && mouse_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_5.tStart = t;  // (not accounting for frame time here)
      mouse_5.frameNStart = frameN;  // exact frame index
      
      mouse_5.status = PsychoJS.Status.STARTED;
      mouse_5.mouseClock.reset();
      prevButtonState = mouse_5.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_5.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      let buttons = mouse_5.getPressed();
      if (!buttons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = buttons;
        if (buttons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [response1disk_5,response3disk_5,response5disk_5,response7disk_5,]) {
            if (obj.contains(mouse_5)) {
              gotValidClick = true;
              mouse_5.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    mousexpos = mouse.getPos()[0];
    mouseypos = mouse.getPos()[1];
    x11d = (a - (b / 2));
    y11d = (a + (b / 2));
    x12d = (a + (b / 2));
    y12d = (a + (b / 2));
    x13d = (a - (b / 2));
    y13d = (a - (b / 2));
    a1d = ((((y12d - y13d) * (mousexpos - x13d)) + ((x13d - x12d) * (mouseypos - y13d))) / (((y12d - y13d) * (x11d - x13d)) + ((x13d - x12d) * (y11d - y13d))));
    b1d = ((((y13d - y11d) * (mousexpos - x13d)) + ((x11d - x13d) * (mouseypos - y13d))) / (((y12d - y13d) * (x11d - x13d)) + ((x13d - x12d) * (y11d - y13d))));
    c1d = ((1 - a1d) - b1d);
    x21d = (a - (b / 2));
    y21d = (a - (b / 2));
    x22d = (a + (b / 2));
    y22d = (a + (b / 2));
    x23d = (a + (b / 2));
    y23d = (a - (b / 2));
    a2d = ((((y22d - y23d) * (mousexpos - x23d)) + ((x23d - x22d) * (mouseypos - y23d))) / (((y22d - y23d) * (x21d - x23d)) + ((x23d - x22d) * (y21d - y23d))));
    b2d = ((((y23d - y21d) * (mousexpos - x23d)) + ((x21d - x23d) * (mouseypos - y23d))) / (((y22d - y23d) * (x21d - x23d)) + ((x23d - x22d) * (y21d - y23d))));
    c2d = ((1 - a2d) - b2d);
    x31d = (a - (b / 2));
    y31d = (- (a - (b / 2)));
    x32d = (a + (b / 2));
    y32d = (- (a - (b / 2)));
    x33d = (a + (b / 2));
    y33d = (- (a + (b / 2)));
    a3d = ((((y32d - y33d) * (mousexpos - x33d)) + ((x33d - x32d) * (mouseypos - y33d))) / (((y32d - y33d) * (x31d - x33d)) + ((x33d - x32d) * (y31d - y33d))));
    b3d = ((((y33d - y31d) * (mousexpos - x33d)) + ((x31d - x33d) * (mouseypos - y33d))) / (((y32d - y33d) * (x31d - x33d)) + ((x33d - x32d) * (y31d - y33d))));
    c3d = ((1 - a3d) - b3d);
    x41d = (a - (b / 2));
    y41d = (- (a - (b / 2)));
    x42d = (a + (b / 2));
    y42d = (- (a + (b / 2)));
    x43d = (a - (b / 2));
    y43d = (- (a + (b / 2)));
    a4d = ((((y42d - y43d) * (mousexpos - x43d)) + ((x43d - x42d) * (mouseypos - y43d))) / (((y42d - y43d) * (x41d - x43d)) + ((x43d - x42d) * (y41d - y43d))));
    b4d = ((((y43d - y41d) * (mousexpos - x43d)) + ((x41d - x43d) * (mouseypos - y43d))) / (((y42d - y43d) * (x41d - x43d)) + ((x43d - x42d) * (y41d - y43d))));
    c4d = ((1 - a4d) - b4d);
    x51d = (- (a + (b / 2)));
    y51d = (- (a + (b / 2)));
    x52d = (- (a - (b / 2)));
    y52d = (- (a - (b / 2)));
    x53d = (- (a - (b / 2)));
    y53d = (- (a + (b / 2)));
    a5d = ((((y52d - y53d) * (mousexpos - x53d)) + ((x53d - x52d) * (mouseypos - y53d))) / (((y52d - y53d) * (x51d - x53d)) + ((x53d - x52d) * (y51d - y53d))));
    b5d = ((((y53d - y51d) * (mousexpos - x53d)) + ((x51d - x53d) * (mouseypos - y53d))) / (((y52d - y53d) * (x51d - x53d)) + ((x53d - x52d) * (y51d - y53d))));
    c5d = ((1 - a5d) - b5d);
    x61d = (- (a + (b / 2)));
    y61d = (- (a - (b / 2)));
    x62d = (- (a - (b / 2)));
    y62d = (- (a - (b / 2)));
    x63d = (- (a + (b / 2)));
    y63d = (- (a + (b / 2)));
    a6d = ((((y62d - y63d) * (mousexpos - x63d)) + ((x63d - x62d) * (mouseypos - y63d))) / (((y62d - y63d) * (x61d - x63d)) + ((x63d - x62d) * (y61d - y63d))));
    b6d = ((((y63d - y61d) * (mousexpos - x63d)) + ((x61d - x63d) * (mouseypos - y63d))) / (((y62d - y63d) * (x61d - x63d)) + ((x63d - x62d) * (y61d - y63d))));
    c6d = ((1 - a6d) - b6d);
    x71d = (- (a + (b / 2)));
    y71d = (a + (b / 2));
    x72d = (- (a - (b / 2)));
    y72d = (a - (b / 2));
    x73d = (- (a + (b / 2)));
    y73d = (a - (b / 2));
    a7d = ((((y72d - y73d) * (mousexpos - x73d)) + ((x73d - x72d) * (mouseypos - y73d))) / (((y72d - y73d) * (x71d - x73d)) + ((x73d - x72d) * (y71d - y73d))));
    b7d = ((((y73d - y71d) * (mousexpos - x73d)) + ((x71d - x73d) * (mouseypos - y73d))) / (((y72d - y73d) * (x71d - x73d)) + ((x73d - x72d) * (y71d - y73d))));
    c7d = ((1 - a7d) - b7d);
    x81d = (- (a + (b / 2)));
    y81d = (a + (b / 2));
    x82d = (- (a - (b / 2)));
    y82d = (a + (b / 2));
    x83d = (- (a - (b / 2)));
    y83d = (a - (b / 2));
    a8d = ((((y82d - y83d) * (mousexpos - x83d)) + ((x83d - x82d) * (mouseypos - y83d))) / (((y82d - y83d) * (x81d - x83d)) + ((x83d - x82d) * (y81d - y83d))));
    b8d = ((((y83d - y81d) * (mousexpos - x83d)) + ((x81d - x83d) * (mouseypos - y83d))) / (((y82d - y83d) * (x81d - x83d)) + ((x83d - x82d) * (y81d - y83d))));
    c8d = ((1 - a8d) - b8d);
    if (((((0 <= a1d) && (a1d <= 1)) && ((0 <= b1d) && (b1d <= 1))) && ((0 <= c1d) && (c1d <= 1)))) {
        similarity = 7;
        responsenumber = 7;
    } else {
        if (((((0 <= a2d) && (a2d <= 1)) && ((0 <= b2d) && (b2d <= 1))) && ((0 <= c2d) && (c2d <= 1)))) {
            similarity = 6;
            responsenumber = 6;
        } else {
            if (((((0 <= a3d) && (a3d <= 1)) && ((0 <= b3d) && (b3d <= 1))) && ((0 <= c3d) && (c3d <= 1)))) {
                similarity = 5;
                responsenumber = 5;
            } else {
                if (((((0 <= a4d) && (a4d <= 1)) && ((0 <= b4d) && (b4d <= 1))) && ((0 <= c4d) && (c4d <= 1)))) {
                    similarity = 4;
                    responsenumber = 4;
                } else {
                    if (((((0 <= a5d) && (a5d <= 1)) && ((0 <= b5d) && (b5d <= 1))) && ((0 <= c5d) && (c5d <= 1)))) {
                        similarity = 3;
                        responsenumber = 3;
                    } else {
                        if (((((0 <= a6d) && (a6d <= 1)) && ((0 <= b6d) && (b6d <= 1))) && ((0 <= c6d) && (c6d <= 1)))) {
                            similarity = 2;
                            responsenumber = 2;
                        } else {
                            if (((((0 <= a7d) && (a7d <= 1)) && ((0 <= b7d) && (b7d <= 1))) && ((0 <= c7d) && (c7d <= 1)))) {
                                similarity = 1;
                                responsenumber = 1;
                            } else {
                                if (((((0 <= a8d) && (a8d <= 1)) && ((0 <= b8d) && (b8d <= 1))) && ((0 <= c8d) && (c8d <= 1)))) {
                                    similarity = 0;
                                    responsenumber = 0;
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    
    
    // *response1disk_5* updates
    if (t >= 0.0 && response1disk_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response1disk_5.tStart = t;  // (not accounting for frame time here)
      response1disk_5.frameNStart = frameN;  // exact frame index
      
      response1disk_5.setAutoDraw(true);
    }

    
    // *response3disk_5* updates
    if (t >= 0.0 && response3disk_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response3disk_5.tStart = t;  // (not accounting for frame time here)
      response3disk_5.frameNStart = frameN;  // exact frame index
      
      response3disk_5.setAutoDraw(true);
    }

    
    // *response5disk_5* updates
    if (t >= 0.0 && response5disk_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response5disk_5.tStart = t;  // (not accounting for frame time here)
      response5disk_5.frameNStart = frameN;  // exact frame index
      
      response5disk_5.setAutoDraw(true);
    }

    
    // *response7disk_5* updates
    if (t >= 0.0 && response7disk_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response7disk_5.tStart = t;  // (not accounting for frame time here)
      response7disk_5.frameNStart = frameN;  // exact frame index
      
      response7disk_5.setAutoDraw(true);
    }

    
    // *Circle_3* updates
    if (t >= 0.0 && Circle_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Circle_3.tStart = t;  // (not accounting for frame time here)
      Circle_3.frameNStart = frameN;  // exact frame index
      
      Circle_3.setAutoDraw(true);
    }

    
    // *text_29* updates
    if (t >= 0.0 && text_29.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_29.tStart = t;  // (not accounting for frame time here)
      text_29.frameNStart = frameN;  // exact frame index
      
      text_29.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    response_pracComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function response_pracRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'response_prac'-------
    response_pracComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // store data for thisExp (ExperimentHandler)
    const xys = mouse_5.getPos();
    const buttons = mouse_5.getPressed();
    psychoJS.experiment.addData('mouse_5.x', xys[0]);
    psychoJS.experiment.addData('mouse_5.y', xys[1]);
    psychoJS.experiment.addData('mouse_5.leftButton', buttons[0]);
    psychoJS.experiment.addData('mouse_5.midButton', buttons[1]);
    psychoJS.experiment.addData('mouse_5.rightButton', buttons[2]);
    if (mouse_5.clicked_name.length > 0) {
      psychoJS.experiment.addData('mouse_5.clicked_name', mouse_5.clicked_name[0]);}
    mousexpos = mouse.getPos()[0];
    mouseypos = mouse.getPos()[1];
    x11d = (a - (b / 2));
    y11d = (a + (b / 2));
    x12d = (a + (b / 2));
    y12d = (a + (b / 2));
    x13d = (a - (b / 2));
    y13d = (a - (b / 2));
    a1d = ((((y12d - y13d) * (mousexpos - x13d)) + ((x13d - x12d) * (mouseypos - y13d))) / (((y12d - y13d) * (x11d - x13d)) + ((x13d - x12d) * (y11d - y13d))));
    b1d = ((((y13d - y11d) * (mousexpos - x13d)) + ((x11d - x13d) * (mouseypos - y13d))) / (((y12d - y13d) * (x11d - x13d)) + ((x13d - x12d) * (y11d - y13d))));
    c1d = ((1 - a1d) - b1d);
    x21d = (a - (b / 2));
    y21d = (a - (b / 2));
    x22d = (a + (b / 2));
    y22d = (a + (b / 2));
    x23d = (a + (b / 2));
    y23d = (a - (b / 2));
    a2d = ((((y22d - y23d) * (mousexpos - x23d)) + ((x23d - x22d) * (mouseypos - y23d))) / (((y22d - y23d) * (x21d - x23d)) + ((x23d - x22d) * (y21d - y23d))));
    b2d = ((((y23d - y21d) * (mousexpos - x23d)) + ((x21d - x23d) * (mouseypos - y23d))) / (((y22d - y23d) * (x21d - x23d)) + ((x23d - x22d) * (y21d - y23d))));
    c2d = ((1 - a2d) - b2d);
    x31d = (a - (b / 2));
    y31d = (- (a - (b / 2)));
    x32d = (a + (b / 2));
    y32d = (- (a - (b / 2)));
    x33d = (a + (b / 2));
    y33d = (- (a + (b / 2)));
    a3d = ((((y32d - y33d) * (mousexpos - x33d)) + ((x33d - x32d) * (mouseypos - y33d))) / (((y32d - y33d) * (x31d - x33d)) + ((x33d - x32d) * (y31d - y33d))));
    b3d = ((((y33d - y31d) * (mousexpos - x33d)) + ((x31d - x33d) * (mouseypos - y33d))) / (((y32d - y33d) * (x31d - x33d)) + ((x33d - x32d) * (y31d - y33d))));
    c3d = ((1 - a3d) - b3d);
    x41d = (a - (b / 2));
    y41d = (- (a - (b / 2)));
    x42d = (a + (b / 2));
    y42d = (- (a + (b / 2)));
    x43d = (a - (b / 2));
    y43d = (- (a + (b / 2)));
    a4d = ((((y42d - y43d) * (mousexpos - x43d)) + ((x43d - x42d) * (mouseypos - y43d))) / (((y42d - y43d) * (x41d - x43d)) + ((x43d - x42d) * (y41d - y43d))));
    b4d = ((((y43d - y41d) * (mousexpos - x43d)) + ((x41d - x43d) * (mouseypos - y43d))) / (((y42d - y43d) * (x41d - x43d)) + ((x43d - x42d) * (y41d - y43d))));
    c4d = ((1 - a4d) - b4d);
    x51d = (- (a + (b / 2)));
    y51d = (- (a + (b / 2)));
    x52d = (- (a - (b / 2)));
    y52d = (- (a - (b / 2)));
    x53d = (- (a - (b / 2)));
    y53d = (- (a + (b / 2)));
    a5d = ((((y52d - y53d) * (mousexpos - x53d)) + ((x53d - x52d) * (mouseypos - y53d))) / (((y52d - y53d) * (x51d - x53d)) + ((x53d - x52d) * (y51d - y53d))));
    b5d = ((((y53d - y51d) * (mousexpos - x53d)) + ((x51d - x53d) * (mouseypos - y53d))) / (((y52d - y53d) * (x51d - x53d)) + ((x53d - x52d) * (y51d - y53d))));
    c5d = ((1 - a5d) - b5d);
    x61d = (- (a + (b / 2)));
    y61d = (- (a - (b / 2)));
    x62d = (- (a - (b / 2)));
    y62d = (- (a - (b / 2)));
    x63d = (- (a + (b / 2)));
    y63d = (- (a + (b / 2)));
    a6d = ((((y62d - y63d) * (mousexpos - x63d)) + ((x63d - x62d) * (mouseypos - y63d))) / (((y62d - y63d) * (x61d - x63d)) + ((x63d - x62d) * (y61d - y63d))));
    b6d = ((((y63d - y61d) * (mousexpos - x63d)) + ((x61d - x63d) * (mouseypos - y63d))) / (((y62d - y63d) * (x61d - x63d)) + ((x63d - x62d) * (y61d - y63d))));
    c6d = ((1 - a6d) - b6d);
    x71d = (- (a + (b / 2)));
    y71d = (a + (b / 2));
    x72d = (- (a - (b / 2)));
    y72d = (a - (b / 2));
    x73d = (- (a + (b / 2)));
    y73d = (a - (b / 2));
    a7d = ((((y72d - y73d) * (mousexpos - x73d)) + ((x73d - x72d) * (mouseypos - y73d))) / (((y72d - y73d) * (x71d - x73d)) + ((x73d - x72d) * (y71d - y73d))));
    b7d = ((((y73d - y71d) * (mousexpos - x73d)) + ((x71d - x73d) * (mouseypos - y73d))) / (((y72d - y73d) * (x71d - x73d)) + ((x73d - x72d) * (y71d - y73d))));
    c7d = ((1 - a7d) - b7d);
    x81d = (- (a + (b / 2)));
    y81d = (a + (b / 2));
    x82d = (- (a - (b / 2)));
    y82d = (a + (b / 2));
    x83d = (- (a - (b / 2)));
    y83d = (a - (b / 2));
    a8d = ((((y82d - y83d) * (mousexpos - x83d)) + ((x83d - x82d) * (mouseypos - y83d))) / (((y82d - y83d) * (x81d - x83d)) + ((x83d - x82d) * (y81d - y83d))));
    b8d = ((((y83d - y81d) * (mousexpos - x83d)) + ((x81d - x83d) * (mouseypos - y83d))) / (((y82d - y83d) * (x81d - x83d)) + ((x83d - x82d) * (y81d - y83d))));
    c8d = ((1 - a8d) - b8d);
    if (((((0 <= a1d) && (a1d <= 1)) && ((0 <= b1d) && (b1d <= 1))) && ((0 <= c1d) && (c1d <= 1)))) {
        similarity = 7;
    } else {
        if (((((0 <= a2d) && (a2d <= 1)) && ((0 <= b2d) && (b2d <= 1))) && ((0 <= c2d) && (c2d <= 1)))) {
            similarity = 6;
        } else {
            if (((((0 <= a3d) && (a3d <= 1)) && ((0 <= b3d) && (b3d <= 1))) && ((0 <= c3d) && (c3d <= 1)))) {
                similarity = 5;
            } else {
                if (((((0 <= a4d) && (a4d <= 1)) && ((0 <= b4d) && (b4d <= 1))) && ((0 <= c4d) && (c4d <= 1)))) {
                    similarity = 4;
                } else {
                    if (((((0 <= a5d) && (a5d <= 1)) && ((0 <= b5d) && (b5d <= 1))) && ((0 <= c5d) && (c5d <= 1)))) {
                        similarity = 3;
                    } else {
                        if (((((0 <= a6d) && (a6d <= 1)) && ((0 <= b6d) && (b6d <= 1))) && ((0 <= c6d) && (c6d <= 1)))) {
                            similarity = 2;
                        } else {
                            if (((((0 <= a7d) && (a7d <= 1)) && ((0 <= b7d) && (b7d <= 1))) && ((0 <= c7d) && (c7d <= 1)))) {
                                similarity = 1;
                            } else {
                                if (((((0 <= a8d) && (a8d <= 1)) && ((0 <= b8d) && (b8d <= 1))) && ((0 <= c8d) && (c8d <= 1)))) {
                                    similarity = 0;
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    thisExp.addData("Colour_2", Colour_2);
    thisExp.addData("similarity", similarity);
    thisExp.addData("response_time", mouse_5.mouseClock.getTime());
    
    // the Routine "response_prac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var responsefeedback;
var responsefeedback1;
var responseprac_feedbackComponents;
function responseprac_feedbackRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'responseprac_feedback'-------
    t = 0;
    responseprac_feedbackClock.reset(); // clock
    frameN = -1;
    routineTimer.add(4.000000);
    // update component parameters for each repeat
    if (((0 <= responsenumber) && (responsenumber <= 1))) {
        responsefeedback = `You selected ${responsenumber}`;
        responsefeedback1 = `${responsenumber} indicates you found the colours very similar`;
    }
    if (((2 <= responsenumber) && (responsenumber <= 3))) {
        responsefeedback = `You selected ${responsenumber}`;
        responsefeedback1 = `${responsenumber} indicates you found the colours similar`;
    }
    if (((4 <= responsenumber) && (responsenumber <= 5))) {
        responsefeedback = `You selected ${responsenumber}`;
        responsefeedback1 = `${responsenumber} indicates you found the colours different`;
    }
    if (((6 <= responsenumber) && (responsenumber <= 7))) {
        responsefeedback = `You selected ${responsenumber}`;
        responsefeedback1 = `${responsenumber} indicates you found the colours very different`;
    }
    
    text_55.setText(responsefeedback);
    text_56.setText(responsefeedback1);
    // keep track of which components have finished
    responseprac_feedbackComponents = [];
    responseprac_feedbackComponents.push(text_55);
    responseprac_feedbackComponents.push(text_56);
    
    responseprac_feedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function responseprac_feedbackRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'responseprac_feedback'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = responseprac_feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    if (((0 <= responsenumber) && (responsenumber <= 3))) {
        responsefeedback = `You selected ${responsenumber} indicating you found the colours are similar`;
    }
    if (((4 <= responsenumber) && (responsenumber <= 7))) {
        responsefeedback = `You selected ${responsenumber} indicating you found the colours are dissimilar`;
    }
    
    
    // *text_55* updates
    if (t >= 0.0 && text_55.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_55.tStart = t;  // (not accounting for frame time here)
      text_55.frameNStart = frameN;  // exact frame index
      
      text_55.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_55.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_55.setAutoDraw(false);
    }
    
    // *text_56* updates
    if (t >= 0.0 && text_56.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_56.tStart = t;  // (not accounting for frame time here)
      text_56.frameNStart = frameN;  // exact frame index
      
      text_56.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_56.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_56.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    responseprac_feedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function responseprac_feedbackRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'responseprac_feedback'-------
    responseprac_feedbackComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var pracnumbertext;
var summary_pracComponents;
function summary_pracRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'summary_prac'-------
    t = 0;
    summary_pracClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_10
    mouse_10.clicked_name = [];
    gotValidClick = false; // until a click is received
    rectangle_8.setFillColor(new util.Color(grey));
    pracnumbertext = `You have finished ${pracnumber} of 7 practice questions`;
    event.clearEvents();
    
    text_50.setText(pracnumbertext);
    // keep track of which components have finished
    summary_pracComponents = [];
    summary_pracComponents.push(mouse_10);
    summary_pracComponents.push(response1disk_10);
    summary_pracComponents.push(response3disk_10);
    summary_pracComponents.push(response5disk_10);
    summary_pracComponents.push(response7disk_10);
    summary_pracComponents.push(rectangle_8);
    summary_pracComponents.push(text_49);
    summary_pracComponents.push(text_50);
    
    summary_pracComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function summary_pracRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'summary_prac'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = summary_pracClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // *mouse_10* updates
    if (t >= 0.0 && mouse_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_10.tStart = t;  // (not accounting for frame time here)
      mouse_10.frameNStart = frameN;  // exact frame index
      
      mouse_10.status = PsychoJS.Status.STARTED;
      mouse_10.mouseClock.reset();
      prevButtonState = mouse_10.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_10.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      let buttons = mouse_10.getPressed();
      if (!buttons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = buttons;
        if (buttons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [rectangle_8]) {
            if (obj.contains(mouse_10)) {
              gotValidClick = true;
              mouse_10.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *response1disk_10* updates
    if (t >= 0.0 && response1disk_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response1disk_10.tStart = t;  // (not accounting for frame time here)
      response1disk_10.frameNStart = frameN;  // exact frame index
      
      response1disk_10.setAutoDraw(true);
    }

    
    // *response3disk_10* updates
    if (t >= 0.0 && response3disk_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response3disk_10.tStart = t;  // (not accounting for frame time here)
      response3disk_10.frameNStart = frameN;  // exact frame index
      
      response3disk_10.setAutoDraw(true);
    }

    
    // *response5disk_10* updates
    if (t >= 0.0 && response5disk_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response5disk_10.tStart = t;  // (not accounting for frame time here)
      response5disk_10.frameNStart = frameN;  // exact frame index
      
      response5disk_10.setAutoDraw(true);
    }

    
    // *response7disk_10* updates
    if (t >= 0.0 && response7disk_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response7disk_10.tStart = t;  // (not accounting for frame time here)
      response7disk_10.frameNStart = frameN;  // exact frame index
      
      response7disk_10.setAutoDraw(true);
    }

    
    // *rectangle_8* updates
    if (t >= 0.0 && rectangle_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rectangle_8.tStart = t;  // (not accounting for frame time here)
      rectangle_8.frameNStart = frameN;  // exact frame index
      
      rectangle_8.setAutoDraw(true);
    }

    
    // *text_49* updates
    if (t >= 0.0 && text_49.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_49.tStart = t;  // (not accounting for frame time here)
      text_49.frameNStart = frameN;  // exact frame index
      
      text_49.setAutoDraw(true);
    }

    
    // *text_50* updates
    if (t >= 0.0 && text_50.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_50.tStart = t;  // (not accounting for frame time here)
      text_50.frameNStart = frameN;  // exact frame index
      
      text_50.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    summary_pracComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function summary_pracRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'summary_prac'-------
    summary_pracComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // store data for thisExp (ExperimentHandler)
    const xys = mouse_10.getPos();
    const buttons = mouse_10.getPressed();
    psychoJS.experiment.addData('mouse_10.x', xys[0]);
    psychoJS.experiment.addData('mouse_10.y', xys[1]);
    psychoJS.experiment.addData('mouse_10.leftButton', buttons[0]);
    psychoJS.experiment.addData('mouse_10.midButton', buttons[1]);
    psychoJS.experiment.addData('mouse_10.rightButton', buttons[2]);
    if (mouse_10.clicked_name.length > 0) {
      psychoJS.experiment.addData('mouse_10.clicked_name', mouse_10.clicked_name[0]);}
    // the Routine "summary_prac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var special_trial_pracComponents;
function special_trial_pracRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'special_trial_prac'-------
    t = 0;
    special_trial_pracClock.reset(); // clock
    frameN = -1;
    routineTimer.add(0.250000);
    // update component parameters for each repeat
    // keep track of which components have finished
    special_trial_pracComponents = [];
    special_trial_pracComponents.push(text_36);
    
    special_trial_pracComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function special_trial_pracRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'special_trial_prac'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = special_trial_pracClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_36* updates
    if (t >= 0.0 && text_36.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_36.tStart = t;  // (not accounting for frame time here)
      text_36.frameNStart = frameN;  // exact frame index
      
      text_36.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.25 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_36.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_36.setAutoDraw(false);
    }
    if ((! ((pracnumber === catchtrialorderprac[0]) || (pracnumber === catchtrialorderprac[1])))) {
        continueRoutine = false;
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    special_trial_pracComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function special_trial_pracRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'special_trial_prac'-------
    special_trial_pracComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var catchtext;
var catch_pracComponents;
function catch_pracRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'catch_prac'-------
    t = 0;
    catch_pracClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_7
    mouse_7.clicked_name = [];
    gotValidClick = false; // until a click is received
    catchtext = `SPECIAL TRIAL PLEASE JUST CLICK AND HOLD ${catchnumberprac}`;
    event.clearEvents();
    
    text_32.setText(catchtext);
    rectangle_5.setFillColor(new util.Color(grey));
    // keep track of which components have finished
    catch_pracComponents = [];
    catch_pracComponents.push(mouse_7);
    catch_pracComponents.push(response1disk_7);
    catch_pracComponents.push(response3disk_7);
    catch_pracComponents.push(response5disk_7);
    catch_pracComponents.push(response7disk_7);
    catch_pracComponents.push(text_32);
    catch_pracComponents.push(rectangle_5);
    
    catch_pracComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function catch_pracRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'catch_prac'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = catch_pracClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // *mouse_7* updates
    if (t >= 0.0 && mouse_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_7.tStart = t;  // (not accounting for frame time here)
      mouse_7.frameNStart = frameN;  // exact frame index
      
      mouse_7.status = PsychoJS.Status.STARTED;
      mouse_7.mouseClock.reset();
      prevButtonState = mouse_7.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_7.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      let buttons = mouse_7.getPressed();
      if (!buttons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = buttons;
        if (buttons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [response1disk_7,response3disk_7,response5disk_7,response7disk_7]) {
            if (obj.contains(mouse_7)) {
              gotValidClick = true;
              mouse_7.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *response1disk_7* updates
    if (t >= 0.0 && response1disk_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response1disk_7.tStart = t;  // (not accounting for frame time here)
      response1disk_7.frameNStart = frameN;  // exact frame index
      
      response1disk_7.setAutoDraw(true);
    }

    
    // *response3disk_7* updates
    if (t >= 0.0 && response3disk_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response3disk_7.tStart = t;  // (not accounting for frame time here)
      response3disk_7.frameNStart = frameN;  // exact frame index
      
      response3disk_7.setAutoDraw(true);
    }

    
    // *response5disk_7* updates
    if (t >= 0.0 && response5disk_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response5disk_7.tStart = t;  // (not accounting for frame time here)
      response5disk_7.frameNStart = frameN;  // exact frame index
      
      response5disk_7.setAutoDraw(true);
    }

    
    // *response7disk_7* updates
    if (t >= 0.0 && response7disk_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response7disk_7.tStart = t;  // (not accounting for frame time here)
      response7disk_7.frameNStart = frameN;  // exact frame index
      
      response7disk_7.setAutoDraw(true);
    }

    if ((! ((pracnumber === catchtrialorderprac[0]) || (pracnumber === catchtrialorderprac[1])))) {
        continueRoutine = false;
    }
    
    
    // *text_32* updates
    if (t >= 0.0 && text_32.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_32.tStart = t;  // (not accounting for frame time here)
      text_32.frameNStart = frameN;  // exact frame index
      
      text_32.setAutoDraw(true);
    }

    
    // *rectangle_5* updates
    if (t >= 0.0 && rectangle_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rectangle_5.tStart = t;  // (not accounting for frame time here)
      rectangle_5.frameNStart = frameN;  // exact frame index
      
      rectangle_5.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    catch_pracComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var catchprac;
function catch_pracRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'catch_prac'-------
    catch_pracComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // store data for thisExp (ExperimentHandler)
    const xys = mouse_7.getPos();
    const buttons = mouse_7.getPressed();
    psychoJS.experiment.addData('mouse_7.x', xys[0]);
    psychoJS.experiment.addData('mouse_7.y', xys[1]);
    psychoJS.experiment.addData('mouse_7.leftButton', buttons[0]);
    psychoJS.experiment.addData('mouse_7.midButton', buttons[1]);
    psychoJS.experiment.addData('mouse_7.rightButton', buttons[2]);
    if (mouse_7.clicked_name.length > 0) {
      psychoJS.experiment.addData('mouse_7.clicked_name', mouse_7.clicked_name[0]);}
    mousexpos = mouse.getPos()[0];
    mouseypos = mouse.getPos()[1];
    x11d = (a - (b / 2));
    y11d = (a + (b / 2));
    x12d = (a + (b / 2));
    y12d = (a + (b / 2));
    x13d = (a - (b / 2));
    y13d = (a - (b / 2));
    a1d = ((((y12d - y13d) * (mousexpos - x13d)) + ((x13d - x12d) * (mouseypos - y13d))) / (((y12d - y13d) * (x11d - x13d)) + ((x13d - x12d) * (y11d - y13d))));
    b1d = ((((y13d - y11d) * (mousexpos - x13d)) + ((x11d - x13d) * (mouseypos - y13d))) / (((y12d - y13d) * (x11d - x13d)) + ((x13d - x12d) * (y11d - y13d))));
    c1d = ((1 - a1d) - b1d);
    x21d = (a - (b / 2));
    y21d = (a - (b / 2));
    x22d = (a + (b / 2));
    y22d = (a + (b / 2));
    x23d = (a + (b / 2));
    y23d = (a - (b / 2));
    a2d = ((((y22d - y23d) * (mousexpos - x23d)) + ((x23d - x22d) * (mouseypos - y23d))) / (((y22d - y23d) * (x21d - x23d)) + ((x23d - x22d) * (y21d - y23d))));
    b2d = ((((y23d - y21d) * (mousexpos - x23d)) + ((x21d - x23d) * (mouseypos - y23d))) / (((y22d - y23d) * (x21d - x23d)) + ((x23d - x22d) * (y21d - y23d))));
    c2d = ((1 - a2d) - b2d);
    x31d = (a - (b / 2));
    y31d = (- (a - (b / 2)));
    x32d = (a + (b / 2));
    y32d = (- (a - (b / 2)));
    x33d = (a + (b / 2));
    y33d = (- (a + (b / 2)));
    a3d = ((((y32d - y33d) * (mousexpos - x33d)) + ((x33d - x32d) * (mouseypos - y33d))) / (((y32d - y33d) * (x31d - x33d)) + ((x33d - x32d) * (y31d - y33d))));
    b3d = ((((y33d - y31d) * (mousexpos - x33d)) + ((x31d - x33d) * (mouseypos - y33d))) / (((y32d - y33d) * (x31d - x33d)) + ((x33d - x32d) * (y31d - y33d))));
    c3d = ((1 - a3d) - b3d);
    x41d = (a - (b / 2));
    y41d = (- (a - (b / 2)));
    x42d = (a + (b / 2));
    y42d = (- (a + (b / 2)));
    x43d = (a - (b / 2));
    y43d = (- (a + (b / 2)));
    a4d = ((((y42d - y43d) * (mousexpos - x43d)) + ((x43d - x42d) * (mouseypos - y43d))) / (((y42d - y43d) * (x41d - x43d)) + ((x43d - x42d) * (y41d - y43d))));
    b4d = ((((y43d - y41d) * (mousexpos - x43d)) + ((x41d - x43d) * (mouseypos - y43d))) / (((y42d - y43d) * (x41d - x43d)) + ((x43d - x42d) * (y41d - y43d))));
    c4d = ((1 - a4d) - b4d);
    x51d = (- (a + (b / 2)));
    y51d = (- (a + (b / 2)));
    x52d = (- (a - (b / 2)));
    y52d = (- (a - (b / 2)));
    x53d = (- (a - (b / 2)));
    y53d = (- (a + (b / 2)));
    a5d = ((((y52d - y53d) * (mousexpos - x53d)) + ((x53d - x52d) * (mouseypos - y53d))) / (((y52d - y53d) * (x51d - x53d)) + ((x53d - x52d) * (y51d - y53d))));
    b5d = ((((y53d - y51d) * (mousexpos - x53d)) + ((x51d - x53d) * (mouseypos - y53d))) / (((y52d - y53d) * (x51d - x53d)) + ((x53d - x52d) * (y51d - y53d))));
    c5d = ((1 - a5d) - b5d);
    x61d = (- (a + (b / 2)));
    y61d = (- (a + (b / 2)));
    x62d = (- (a - (b / 2)));
    y62d = (- (a - (b / 2)));
    x63d = (- (a + (b / 2)));
    y63d = (- (a + (b / 2)));
    a6d = ((((y62d - y63d) * (mousexpos - x63d)) + ((x63d - x62d) * (mouseypos - y63d))) / (((y62d - y63d) * (x61d - x63d)) + ((x63d - x62d) * (y61d - y63d))));
    b6d = ((((y63d - y61d) * (mousexpos - x63d)) + ((x61d - x63d) * (mouseypos - y63d))) / (((y62d - y63d) * (x61d - x63d)) + ((x63d - x62d) * (y61d - y63d))));
    c6d = ((1 - a6d) - b6d);
    x71d = (- (a + (b / 2)));
    y71d = (a + (b / 2));
    x72d = (- (a - (b / 2)));
    y72d = (a - (b / 2));
    x73d = (- (a + (b / 2)));
    y73d = (a - (b / 2));
    a7d = ((((y72d - y73d) * (mousexpos - x73d)) + ((x73d - x72d) * (mouseypos - y73d))) / (((y72d - y73d) * (x71d - x73d)) + ((x73d - x72d) * (y71d - y73d))));
    b7d = ((((y73d - y71d) * (mousexpos - x73d)) + ((x71d - x73d) * (mouseypos - y73d))) / (((y72d - y73d) * (x71d - x73d)) + ((x73d - x72d) * (y71d - y73d))));
    c7d = ((1 - a7d) - b7d);
    x81d = (- (a + (b / 2)));
    y81d = (a + (b / 2));
    x82d = (- (a - (b / 2)));
    y82d = (a + (b / 2));
    x83d = (- (a - (b / 2)));
    y83d = (a - (b / 2));
    a8d = ((((y82d - y83d) * (mousexpos - x83d)) + ((x83d - x82d) * (mouseypos - y83d))) / (((y82d - y83d) * (x81d - x83d)) + ((x83d - x82d) * (y81d - y83d))));
    b8d = ((((y83d - y81d) * (mousexpos - x83d)) + ((x81d - x83d) * (mouseypos - y83d))) / (((y82d - y83d) * (x81d - x83d)) + ((x83d - x82d) * (y81d - y83d))));
    c8d = ((1 - a8d) - b8d);
    if (((((0 <= a1d) && (a1d <= 1)) && ((0 <= b1d) && (b1d <= 1))) && ((0 <= c1d) && (c1d <= 1)))) {
        catchprac = 7;
        thisExp.addData("catchprac", catchprac);
    } else {
        if (((((0 <= a2d) && (a2d <= 1)) && ((0 <= b2d) && (b2d <= 1))) && ((0 <= c2d) && (c2d <= 1)))) {
            catchprac = 6;
            thisExp.addData("catchprac", catchprac);
        } else {
            if (((((0 <= a3d) && (a3d <= 1)) && ((0 <= b3d) && (b3d <= 1))) && ((0 <= c3d) && (c3d <= 1)))) {
                catchprac = 5;
                thisExp.addData("catchprac", catchprac);
            } else {
                if (((((0 <= a4d) && (a4d <= 1)) && ((0 <= b4d) && (b4d <= 1))) && ((0 <= c4d) && (c4d <= 1)))) {
                    catchprac = 4;
                    thisExp.addData("catchprac", catchprac);
                } else {
                    if (((((0 <= a5d) && (a5d <= 1)) && ((0 <= b5d) && (b5d <= 1))) && ((0 <= c5d) && (c5d <= 1)))) {
                        catchprac = 3;
                        thisExp.addData("catchprac", catchprac);
                    } else {
                        if (((((0 <= a6d) && (a6d <= 1)) && ((0 <= b6d) && (b6d <= 1))) && ((0 <= c6d) && (c6d <= 1)))) {
                            catchprac = 2;
                            thisExp.addData("catchprac", catchprac);
                        } else {
                            if (((((0 <= a7d) && (a7d <= 1)) && ((0 <= b7d) && (b7d <= 1))) && ((0 <= c7d) && (c7d <= 1)))) {
                                catchprac = 1;
                                thisExp.addData("catchprac", catchprac);
                            } else {
                                if (((((0 <= a8d) && (a8d <= 1)) && ((0 <= b8d) && (b8d <= 1))) && ((0 <= c8d) && (c8d <= 1)))) {
                                    catchprac = 0;
                                    thisExp.addData("catchprac", catchprac);
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    thisExp.addData("catchnumberprac", catchnumberprac);
    
    // the Routine "catch_prac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var summary2_pracComponents;
function summary2_pracRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'summary2_prac'-------
    t = 0;
    summary2_pracClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_6
    mouse_6.clicked_name = [];
    gotValidClick = false; // until a click is received
    response3disk_6.setPos([a, (- a)]);
    response3disk_6.setSize([b, b]);
    response7disk_6.setPos([(- a), a]);
    response7disk_6.setSize([b, b]);
    rectangle_4.setFillColor(new util.Color(grey));
    pracnumbertext = `You have finished ${pracnumber} of 7 practice questions`;
    event.clearEvents();
    if ((! ((pracnumber === catchtrialorderprac[0]) || (pracnumber === catchtrialorderprac[1])))) {
        continueRoutine = false;
    }
    
    text_31.setText(pracnumbertext);
    // keep track of which components have finished
    summary2_pracComponents = [];
    summary2_pracComponents.push(mouse_6);
    summary2_pracComponents.push(response1disk_6);
    summary2_pracComponents.push(response3disk_6);
    summary2_pracComponents.push(response5disk_6);
    summary2_pracComponents.push(response7disk_6);
    summary2_pracComponents.push(rectangle_4);
    summary2_pracComponents.push(text_30);
    summary2_pracComponents.push(text_31);
    
    summary2_pracComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function summary2_pracRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'summary2_prac'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = summary2_pracClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // *mouse_6* updates
    if (t >= 0.0 && mouse_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_6.tStart = t;  // (not accounting for frame time here)
      mouse_6.frameNStart = frameN;  // exact frame index
      
      mouse_6.status = PsychoJS.Status.STARTED;
      mouse_6.mouseClock.reset();
      prevButtonState = mouse_6.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_6.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      let buttons = mouse_6.getPressed();
      if (!buttons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = buttons;
        if (buttons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [rectangle_4]) {
            if (obj.contains(mouse_6)) {
              gotValidClick = true;
              mouse_6.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *response1disk_6* updates
    if (t >= 0.0 && response1disk_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response1disk_6.tStart = t;  // (not accounting for frame time here)
      response1disk_6.frameNStart = frameN;  // exact frame index
      
      response1disk_6.setAutoDraw(true);
    }

    
    // *response3disk_6* updates
    if (t >= 0.0 && response3disk_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response3disk_6.tStart = t;  // (not accounting for frame time here)
      response3disk_6.frameNStart = frameN;  // exact frame index
      
      response3disk_6.setAutoDraw(true);
    }

    
    // *response5disk_6* updates
    if (t >= 0.0 && response5disk_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response5disk_6.tStart = t;  // (not accounting for frame time here)
      response5disk_6.frameNStart = frameN;  // exact frame index
      
      response5disk_6.setAutoDraw(true);
    }

    
    // *response7disk_6* updates
    if (t >= 0.0 && response7disk_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response7disk_6.tStart = t;  // (not accounting for frame time here)
      response7disk_6.frameNStart = frameN;  // exact frame index
      
      response7disk_6.setAutoDraw(true);
    }

    
    // *rectangle_4* updates
    if (t >= 0.0 && rectangle_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rectangle_4.tStart = t;  // (not accounting for frame time here)
      rectangle_4.frameNStart = frameN;  // exact frame index
      
      rectangle_4.setAutoDraw(true);
    }

    if ((! ((pracnumber === catchtrialorderprac[0]) || (pracnumber === catchtrialorderprac[1])))) {
        continueRoutine = false;
    }
    
    
    // *text_30* updates
    if (t >= 0.0 && text_30.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_30.tStart = t;  // (not accounting for frame time here)
      text_30.frameNStart = frameN;  // exact frame index
      
      text_30.setAutoDraw(true);
    }

    
    // *text_31* updates
    if (t >= 0.0 && text_31.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_31.tStart = t;  // (not accounting for frame time here)
      text_31.frameNStart = frameN;  // exact frame index
      
      text_31.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    summary2_pracComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function summary2_pracRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'summary2_prac'-------
    summary2_pracComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // store data for thisExp (ExperimentHandler)
    const xys = mouse_6.getPos();
    const buttons = mouse_6.getPressed();
    psychoJS.experiment.addData('mouse_6.x', xys[0]);
    psychoJS.experiment.addData('mouse_6.y', xys[1]);
    psychoJS.experiment.addData('mouse_6.leftButton', buttons[0]);
    psychoJS.experiment.addData('mouse_6.midButton', buttons[1]);
    psychoJS.experiment.addData('mouse_6.rightButton', buttons[2]);
    if (mouse_6.clicked_name.length > 0) {
      psychoJS.experiment.addData('mouse_6.clicked_name', mouse_6.clicked_name[0]);}
    // the Routine "summary2_prac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_22_allKeys;
var beginComponents;
function beginRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'begin'-------
    t = 0;
    beginClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_22.keys = undefined;
    key_resp_22.rt = undefined;
    _key_resp_22_allKeys = [];
    // keep track of which components have finished
    beginComponents = [];
    beginComponents.push(space_19);
    beginComponents.push(text_46);
    beginComponents.push(key_resp_22);
    
    beginComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function beginRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'begin'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = beginClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *space_19* updates
    if (t >= 2 && space_19.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_19.tStart = t;  // (not accounting for frame time here)
      space_19.frameNStart = frameN;  // exact frame index
      
      space_19.setAutoDraw(true);
    }

    
    // *text_46* updates
    if (t >= 0.0 && text_46.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_46.tStart = t;  // (not accounting for frame time here)
      text_46.frameNStart = frameN;  // exact frame index
      
      text_46.setAutoDraw(true);
    }

    
    // *key_resp_22* updates
    if (t >= 0.0 && key_resp_22.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_22.tStart = t;  // (not accounting for frame time here)
      key_resp_22.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_22.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_22.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_22.clearEvents(); });
    }

    if (key_resp_22.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_22.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_22_allKeys = _key_resp_22_allKeys.concat(theseKeys);
      if (_key_resp_22_allKeys.length > 0) {
        key_resp_22.keys = _key_resp_22_allKeys[_key_resp_22_allKeys.length - 1].name;  // just the last key pressed
        key_resp_22.rt = _key_resp_22_allKeys[_key_resp_22_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    beginComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function beginRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'begin'-------
    beginComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_22.keys', key_resp_22.keys);
    if (typeof key_resp_22.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_22.rt', key_resp_22.rt);
        routineTimer.reset();
        }
    
    key_resp_22.stop();
    // the Routine "begin" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var Circle1_colour;
var Stim1_displayComponents;
function Stim1_displayRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'Stim1_display'-------
    t = 0;
    Stim1_displayClock.reset(); // clock
    frameN = -1;
    routineTimer.add(0.500000);
    // update component parameters for each repeat
    x = 1;
    y = 1;
    angle_1 = (Math.floor((Math.random() * ((30 - (- 30)) + 1))) + (- 30));
    angle_2 = (angle_1 + 180);
    theta_1 = (angle_1 * (pi / 180));
    theta_2 = (angle_2 * (pi / 180));
    deltax_1 = (radius_F * cos(theta_1));
    deltay_1 = (radius_F * sin(theta_1));
    deltax_2 = (radius_P * cos(theta_2));
    deltay_2 = (radius_P * sin(theta_2));
    a_1 = (x + deltax_1);
    b_1 = (y + deltay_1);
    a_2 = (x + deltax_2);
    b_2 = (y + deltay_2);
    if ((Colour1 === 1)) {
        Circle1_colour = [1, (- 1), (- 1)];
    } else {
        if ((Colour1 === 2)) {
            Circle1_colour = [1, 0.33, (- 1)];
        } else {
            if ((Colour1 === 3)) {
                Circle1_colour = [0.32, 1, (- 1)];
            } else {
                if ((Colour1 === 4)) {
                    Circle1_colour = [(- 1), 1, (- 1)];
                } else {
                    if ((Colour1 === 5)) {
                        Circle1_colour = [(- 1), 1, 0.33];
                    } else {
                        if ((Colour1 === 6)) {
                            Circle1_colour = [(- 1), 0.32, 1];
                        } else {
                            if ((Colour1 === 7)) {
                                Circle1_colour = [(- 1), (- 1), 1];
                            } else {
                                if ((Colour1 === 8)) {
                                    Circle1_colour = [0.33, (- 1), 1];
                                } else {
                                    if ((Colour1 === 9)) {
                                        Circle1_colour = [1, (- 1), 0.33];
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    if ((Ecc === "FF")) {
        circle1posx = a_1;
        circle1posy = b_1;
        circlesizeh = (2 * r_F);
        circlesizew = (2 * r_F);
    } else {
        if ((Ecc === "PF")) {
            circle1posx = a_2;
            circle1posy = b_2;
            circlesizeh = (2 * R_P);
            circlesizew = (2 * R_P);
        }
    }
    
    Circle_1.setPos([circle1posx, circle1posy]);
    Circle_1.setSize([circlesizew, circlesizeh]);
    Circle_1.setFillColor(new util.Color(Circle1_colour));
    Circle_1.setLineColor(new util.Color(Circle1_colour));
    // keep track of which components have finished
    Stim1_displayComponents = [];
    Stim1_displayComponents.push(Circle_1);
    Stim1_displayComponents.push(centre_cross4);
    
    Stim1_displayComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function Stim1_displayRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'Stim1_display'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = Stim1_displayClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Circle_1* updates
    if (t >= 0.0 && Circle_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Circle_1.tStart = t;  // (not accounting for frame time here)
      Circle_1.frameNStart = frameN;  // exact frame index
      
      Circle_1.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.25 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Circle_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Circle_1.setAutoDraw(false);
    }
    
    // *centre_cross4* updates
    if (t >= 0 && centre_cross4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      centre_cross4.tStart = t;  // (not accounting for frame time here)
      centre_cross4.frameNStart = frameN;  // exact frame index
      
      centre_cross4.setAutoDraw(true);
    }

    frameRemains = 0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (centre_cross4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      centre_cross4.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Stim1_displayComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Stim1_displayRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'Stim1_display'-------
    Stim1_displayComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    thisExp.addData("Colour1", Colour1);
    thisExp.addData("Ecc", Ecc);
    
    return Scheduler.Event.NEXT;
  };
}


var Circle2_colour;
var responseComponents;
function responseRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'response'-------
    t = 0;
    responseClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse
    mouse.clicked_name = [];
    gotValidClick = false; // until a click is received
    event.clearEvents();
    trialnumber = (trialnumber + 1);
    if ((Colour2 === 1)) {
        Circle2_colour = [1, (- 1), (- 1)];
    } else {
        if ((Colour2 === 2)) {
            Circle2_colour = [1, 0.33, (- 1)];
        } else {
            if ((Colour2 === 3)) {
                Circle2_colour = [0.32, 1, (- 1)];
            } else {
                if ((Colour2 === 4)) {
                    Circle2_colour = [(- 1), 1, (- 1)];
                } else {
                    if ((Colour2 === 5)) {
                        Circle2_colour = [(- 1), 1, 0.33];
                    } else {
                        if ((Colour2 === 6)) {
                            Circle2_colour = [(- 1), 0.32, 1];
                        } else {
                            if ((Colour2 === 7)) {
                                Circle2_colour = [(- 1), (- 1), 1];
                            } else {
                                if ((Colour2 === 8)) {
                                    Circle2_colour = [0.33, (- 1), 1];
                                } else {
                                    if ((Colour2 === 9)) {
                                        Circle2_colour = [1, (- 1), 0.33];
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    
    Circle_2.setSize([(15 * ratio_pxpermm), (15 * ratio_pxpermm)]);
    Circle_2.setFillColor(new util.Color(Circle2_colour));
    Circle_2.setLineColor(new util.Color(Circle2_colour));
    // keep track of which components have finished
    responseComponents = [];
    responseComponents.push(mouse);
    responseComponents.push(response1disk);
    responseComponents.push(response3disk);
    responseComponents.push(response5disk);
    responseComponents.push(response7disk);
    responseComponents.push(Circle_2);
    responseComponents.push(text_23);
    
    responseComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function responseRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'response'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = responseClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // *mouse* updates
    if (t >= 0.0 && mouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse.tStart = t;  // (not accounting for frame time here)
      mouse.frameNStart = frameN;  // exact frame index
      
      mouse.status = PsychoJS.Status.STARTED;
      mouse.mouseClock.reset();
      prevButtonState = mouse.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      let buttons = mouse.getPressed();
      if (!buttons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = buttons;
        if (buttons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [response1disk,response3disk,response5disk,response7disk]) {
            if (obj.contains(mouse)) {
              gotValidClick = true;
              mouse.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *response1disk* updates
    if (t >= 0.0 && response1disk.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response1disk.tStart = t;  // (not accounting for frame time here)
      response1disk.frameNStart = frameN;  // exact frame index
      
      response1disk.setAutoDraw(true);
    }

    
    // *response3disk* updates
    if (t >= 0.0 && response3disk.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response3disk.tStart = t;  // (not accounting for frame time here)
      response3disk.frameNStart = frameN;  // exact frame index
      
      response3disk.setAutoDraw(true);
    }

    
    // *response5disk* updates
    if (t >= 0.0 && response5disk.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response5disk.tStart = t;  // (not accounting for frame time here)
      response5disk.frameNStart = frameN;  // exact frame index
      
      response5disk.setAutoDraw(true);
    }

    
    // *response7disk* updates
    if (t >= 0.0 && response7disk.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response7disk.tStart = t;  // (not accounting for frame time here)
      response7disk.frameNStart = frameN;  // exact frame index
      
      response7disk.setAutoDraw(true);
    }

    
    // *Circle_2* updates
    if (t >= 0.0 && Circle_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Circle_2.tStart = t;  // (not accounting for frame time here)
      Circle_2.frameNStart = frameN;  // exact frame index
      
      Circle_2.setAutoDraw(true);
    }

    
    // *text_23* updates
    if (t >= 0.0 && text_23.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_23.tStart = t;  // (not accounting for frame time here)
      text_23.frameNStart = frameN;  // exact frame index
      
      text_23.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    responseComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function responseRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'response'-------
    responseComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // store data for thisExp (ExperimentHandler)
    const xys = mouse.getPos();
    const buttons = mouse.getPressed();
    psychoJS.experiment.addData('mouse.x', xys[0]);
    psychoJS.experiment.addData('mouse.y', xys[1]);
    psychoJS.experiment.addData('mouse.leftButton', buttons[0]);
    psychoJS.experiment.addData('mouse.midButton', buttons[1]);
    psychoJS.experiment.addData('mouse.rightButton', buttons[2]);
    if (mouse.clicked_name.length > 0) {
      psychoJS.experiment.addData('mouse.clicked_name', mouse.clicked_name[0]);}
    mousexpos = mouse.getPos()[0];
    mouseypos = mouse.getPos()[1];
    x11d = (a - (b / 2));
    y11d = (a + (b / 2));
    x12d = (a + (b / 2));
    y12d = (a + (b / 2));
    x13d = (a - (b / 2));
    y13d = (a - (b / 2));
    a1d = ((((y12d - y13d) * (mousexpos - x13d)) + ((x13d - x12d) * (mouseypos - y13d))) / (((y12d - y13d) * (x11d - x13d)) + ((x13d - x12d) * (y11d - y13d))));
    b1d = ((((y13d - y11d) * (mousexpos - x13d)) + ((x11d - x13d) * (mouseypos - y13d))) / (((y12d - y13d) * (x11d - x13d)) + ((x13d - x12d) * (y11d - y13d))));
    c1d = ((1 - a1d) - b1d);
    x21d = (a - (b / 2));
    y21d = (a - (b / 2));
    x22d = (a + (b / 2));
    y22d = (a + (b / 2));
    x23d = (a + (b / 2));
    y23d = (a - (b / 2));
    a2d = ((((y22d - y23d) * (mousexpos - x23d)) + ((x23d - x22d) * (mouseypos - y23d))) / (((y22d - y23d) * (x21d - x23d)) + ((x23d - x22d) * (y21d - y23d))));
    b2d = ((((y23d - y21d) * (mousexpos - x23d)) + ((x21d - x23d) * (mouseypos - y23d))) / (((y22d - y23d) * (x21d - x23d)) + ((x23d - x22d) * (y21d - y23d))));
    c2d = ((1 - a2d) - b2d);
    x31d = (a - (b / 2));
    y31d = (- (a - (b / 2)));
    x32d = (a + (b / 2));
    y32d = (- (a - (b / 2)));
    x33d = (a + (b / 2));
    y33d = (- (a + (b / 2)));
    a3d = ((((y32d - y33d) * (mousexpos - x33d)) + ((x33d - x32d) * (mouseypos - y33d))) / (((y32d - y33d) * (x31d - x33d)) + ((x33d - x32d) * (y31d - y33d))));
    b3d = ((((y33d - y31d) * (mousexpos - x33d)) + ((x31d - x33d) * (mouseypos - y33d))) / (((y32d - y33d) * (x31d - x33d)) + ((x33d - x32d) * (y31d - y33d))));
    c3d = ((1 - a3d) - b3d);
    x41d = (a - (b / 2));
    y41d = (- (a - (b / 2)));
    x42d = (a + (b / 2));
    y42d = (- (a + (b / 2)));
    x43d = (a - (b / 2));
    y43d = (- (a + (b / 2)));
    a4d = ((((y42d - y43d) * (mousexpos - x43d)) + ((x43d - x42d) * (mouseypos - y43d))) / (((y42d - y43d) * (x41d - x43d)) + ((x43d - x42d) * (y41d - y43d))));
    b4d = ((((y43d - y41d) * (mousexpos - x43d)) + ((x41d - x43d) * (mouseypos - y43d))) / (((y42d - y43d) * (x41d - x43d)) + ((x43d - x42d) * (y41d - y43d))));
    c4d = ((1 - a4d) - b4d);
    x51d = (- (a + (b / 2)));
    y51d = (- (a + (b / 2)));
    x52d = (- (a - (b / 2)));
    y52d = (- (a - (b / 2)));
    x53d = (- (a - (b / 2)));
    y53d = (- (a + (b / 2)));
    a5d = ((((y52d - y53d) * (mousexpos - x53d)) + ((x53d - x52d) * (mouseypos - y53d))) / (((y52d - y53d) * (x51d - x53d)) + ((x53d - x52d) * (y51d - y53d))));
    b5d = ((((y53d - y51d) * (mousexpos - x53d)) + ((x51d - x53d) * (mouseypos - y53d))) / (((y52d - y53d) * (x51d - x53d)) + ((x53d - x52d) * (y51d - y53d))));
    c5d = ((1 - a5d) - b5d);
    x61d = (- (a + (b / 2)));
    y61d = (- (a - (b / 2)));
    x62d = (- (a - (b / 2)));
    y62d = (- (a - (b / 2)));
    x63d = (- (a + (b / 2)));
    y63d = (- (a + (b / 2)));
    a6d = ((((y62d - y63d) * (mousexpos - x63d)) + ((x63d - x62d) * (mouseypos - y63d))) / (((y62d - y63d) * (x61d - x63d)) + ((x63d - x62d) * (y61d - y63d))));
    b6d = ((((y63d - y61d) * (mousexpos - x63d)) + ((x61d - x63d) * (mouseypos - y63d))) / (((y62d - y63d) * (x61d - x63d)) + ((x63d - x62d) * (y61d - y63d))));
    c6d = ((1 - a6d) - b6d);
    x71d = (- (a + (b / 2)));
    y71d = (a + (b / 2));
    x72d = (- (a - (b / 2)));
    y72d = (a - (b / 2));
    x73d = (- (a + (b / 2)));
    y73d = (a - (b / 2));
    a7d = ((((y72d - y73d) * (mousexpos - x73d)) + ((x73d - x72d) * (mouseypos - y73d))) / (((y72d - y73d) * (x71d - x73d)) + ((x73d - x72d) * (y71d - y73d))));
    b7d = ((((y73d - y71d) * (mousexpos - x73d)) + ((x71d - x73d) * (mouseypos - y73d))) / (((y72d - y73d) * (x71d - x73d)) + ((x73d - x72d) * (y71d - y73d))));
    c7d = ((1 - a7d) - b7d);
    x81d = (- (a + (b / 2)));
    y81d = (a + (b / 2));
    x82d = (- (a - (b / 2)));
    y82d = (a + (b / 2));
    x83d = (- (a - (b / 2)));
    y83d = (a - (b / 2));
    a8d = ((((y82d - y83d) * (mousexpos - x83d)) + ((x83d - x82d) * (mouseypos - y83d))) / (((y82d - y83d) * (x81d - x83d)) + ((x83d - x82d) * (y81d - y83d))));
    b8d = ((((y83d - y81d) * (mousexpos - x83d)) + ((x81d - x83d) * (mouseypos - y83d))) / (((y82d - y83d) * (x81d - x83d)) + ((x83d - x82d) * (y81d - y83d))));
    c8d = ((1 - a8d) - b8d);
    if (((((0 <= a1d) && (a1d <= 1)) && ((0 <= b1d) && (b1d <= 1))) && ((0 <= c1d) && (c1d <= 1)))) {
        similarity = 7;
    } else {
        if (((((0 <= a2d) && (a2d <= 1)) && ((0 <= b2d) && (b2d <= 1))) && ((0 <= c2d) && (c2d <= 1)))) {
            similarity = 6;
        } else {
            if (((((0 <= a3d) && (a3d <= 1)) && ((0 <= b3d) && (b3d <= 1))) && ((0 <= c3d) && (c3d <= 1)))) {
                similarity = 5;
            } else {
                if (((((0 <= a4d) && (a4d <= 1)) && ((0 <= b4d) && (b4d <= 1))) && ((0 <= c4d) && (c4d <= 1)))) {
                    similarity = 4;
                } else {
                    if (((((0 <= a5d) && (a5d <= 1)) && ((0 <= b5d) && (b5d <= 1))) && ((0 <= c5d) && (c5d <= 1)))) {
                        similarity = 3;
                    } else {
                        if (((((0 <= a6d) && (a6d <= 1)) && ((0 <= b6d) && (b6d <= 1))) && ((0 <= c6d) && (c6d <= 1)))) {
                            similarity = 2;
                        } else {
                            if (((((0 <= a7d) && (a7d <= 1)) && ((0 <= b7d) && (b7d <= 1))) && ((0 <= c7d) && (c7d <= 1)))) {
                                similarity = 1;
                            } else {
                                if (((((0 <= a8d) && (a8d <= 1)) && ((0 <= b8d) && (b8d <= 1))) && ((0 <= c8d) && (c8d <= 1)))) {
                                    similarity = 0;
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    thisExp.addData("Colour2", Colour2);
    thisExp.addData("Ecc", Ecc);
    thisExp.addData("similarity", similarity);
    thisExp.addData("response_time", mouse.mouseClock.getTime());
    thisExp.addData("trialnumber", trialnumber);
    
    // the Routine "response" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var trialnumbertext;
var response_2Components;
function response_2RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'response_2'-------
    t = 0;
    response_2Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_2
    mouse_2.clicked_name = [];
    gotValidClick = false; // until a click is received
    rectangle.setFillColor(new util.Color(grey));
    trialnumbertext = `You have finished ${trialnumber} of 324 questions`;
    event.clearEvents();
    
    text_24.setText(trialnumbertext);
    // keep track of which components have finished
    response_2Components = [];
    response_2Components.push(mouse_2);
    response_2Components.push(response1disk_2);
    response_2Components.push(response3disk_2);
    response_2Components.push(response5disk_2);
    response_2Components.push(response7disk_2);
    response_2Components.push(rectangle);
    response_2Components.push(text_25);
    response_2Components.push(text_24);
    
    response_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function response_2RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'response_2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = response_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // *mouse_2* updates
    if (t >= 0.0 && mouse_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_2.tStart = t;  // (not accounting for frame time here)
      mouse_2.frameNStart = frameN;  // exact frame index
      
      mouse_2.status = PsychoJS.Status.STARTED;
      mouse_2.mouseClock.reset();
      prevButtonState = mouse_2.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_2.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      let buttons = mouse_2.getPressed();
      if (!buttons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = buttons;
        if (buttons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [rectangle]) {
            if (obj.contains(mouse_2)) {
              gotValidClick = true;
              mouse_2.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *response1disk_2* updates
    if (t >= 0.0 && response1disk_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response1disk_2.tStart = t;  // (not accounting for frame time here)
      response1disk_2.frameNStart = frameN;  // exact frame index
      
      response1disk_2.setAutoDraw(true);
    }

    
    // *response3disk_2* updates
    if (t >= 0.0 && response3disk_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response3disk_2.tStart = t;  // (not accounting for frame time here)
      response3disk_2.frameNStart = frameN;  // exact frame index
      
      response3disk_2.setAutoDraw(true);
    }

    
    // *response5disk_2* updates
    if (t >= 0.0 && response5disk_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response5disk_2.tStart = t;  // (not accounting for frame time here)
      response5disk_2.frameNStart = frameN;  // exact frame index
      
      response5disk_2.setAutoDraw(true);
    }

    
    // *response7disk_2* updates
    if (t >= 0.0 && response7disk_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response7disk_2.tStart = t;  // (not accounting for frame time here)
      response7disk_2.frameNStart = frameN;  // exact frame index
      
      response7disk_2.setAutoDraw(true);
    }

    
    // *rectangle* updates
    if (t >= 0.0 && rectangle.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rectangle.tStart = t;  // (not accounting for frame time here)
      rectangle.frameNStart = frameN;  // exact frame index
      
      rectangle.setAutoDraw(true);
    }

    
    // *text_25* updates
    if (t >= 0.0 && text_25.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_25.tStart = t;  // (not accounting for frame time here)
      text_25.frameNStart = frameN;  // exact frame index
      
      text_25.setAutoDraw(true);
    }

    
    // *text_24* updates
    if (t >= 0.0 && text_24.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_24.tStart = t;  // (not accounting for frame time here)
      text_24.frameNStart = frameN;  // exact frame index
      
      text_24.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    response_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function response_2RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'response_2'-------
    response_2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // store data for thisExp (ExperimentHandler)
    const xys = mouse_2.getPos();
    const buttons = mouse_2.getPressed();
    psychoJS.experiment.addData('mouse_2.x', xys[0]);
    psychoJS.experiment.addData('mouse_2.y', xys[1]);
    psychoJS.experiment.addData('mouse_2.leftButton', buttons[0]);
    psychoJS.experiment.addData('mouse_2.midButton', buttons[1]);
    psychoJS.experiment.addData('mouse_2.rightButton', buttons[2]);
    if (mouse_2.clicked_name.length > 0) {
      psychoJS.experiment.addData('mouse_2.clicked_name', mouse_2.clicked_name[0]);}
    // the Routine "response_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var special_trialComponents;
function special_trialRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'special_trial'-------
    t = 0;
    special_trialClock.reset(); // clock
    frameN = -1;
    routineTimer.add(0.250000);
    // update component parameters for each repeat
    // keep track of which components have finished
    special_trialComponents = [];
    special_trialComponents.push(text_33);
    
    special_trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function special_trialRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'special_trial'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = special_trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_33* updates
    if (t >= 0.0 && text_33.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_33.tStart = t;  // (not accounting for frame time here)
      text_33.frameNStart = frameN;  // exact frame index
      
      text_33.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.25 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_33.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_33.setAutoDraw(false);
    }
    if (Catch === 0){
        continueRoutine = false
        }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    special_trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function special_trialRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'special_trial'-------
    special_trialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var catchnumber;
var catch_1Components;
function catch_1RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'catch_1'-------
    t = 0;
    catch_1Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_3
    mouse_3.clicked_name = [];
    gotValidClick = false; // until a click is received
    catchnumber = (Math.floor((Math.random() * ((7 - 0) + 1))) + 0);
    event.clearEvents();
    catchtext = `SPECIAL TRIAL PLEASE CLICK AND HOLD ${catchnumber}`;
    
    text_26.setText(catchtext);
    // keep track of which components have finished
    catch_1Components = [];
    catch_1Components.push(mouse_3);
    catch_1Components.push(response1disk_3);
    catch_1Components.push(response3disk_3);
    catch_1Components.push(response5disk_3);
    catch_1Components.push(response7disk_3);
    catch_1Components.push(text_26);
    catch_1Components.push(rectangle_2);
    
    catch_1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function catch_1RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'catch_1'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = catch_1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // *mouse_3* updates
    if (t >= 0.0 && mouse_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_3.tStart = t;  // (not accounting for frame time here)
      mouse_3.frameNStart = frameN;  // exact frame index
      
      mouse_3.status = PsychoJS.Status.STARTED;
      mouse_3.mouseClock.reset();
      prevButtonState = mouse_3.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_3.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      let buttons = mouse_3.getPressed();
      if (!buttons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = buttons;
        if (buttons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [response1disk_3,response3disk_3,response5disk_3,response7disk_3,]) {
            if (obj.contains(mouse_3)) {
              gotValidClick = true;
              mouse_3.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *response1disk_3* updates
    if (t >= 0.0 && response1disk_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response1disk_3.tStart = t;  // (not accounting for frame time here)
      response1disk_3.frameNStart = frameN;  // exact frame index
      
      response1disk_3.setAutoDraw(true);
    }

    
    // *response3disk_3* updates
    if (t >= 0.0 && response3disk_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response3disk_3.tStart = t;  // (not accounting for frame time here)
      response3disk_3.frameNStart = frameN;  // exact frame index
      
      response3disk_3.setAutoDraw(true);
    }

    
    // *response5disk_3* updates
    if (t >= 0.0 && response5disk_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response5disk_3.tStart = t;  // (not accounting for frame time here)
      response5disk_3.frameNStart = frameN;  // exact frame index
      
      response5disk_3.setAutoDraw(true);
    }

    
    // *response7disk_3* updates
    if (t >= 0.0 && response7disk_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response7disk_3.tStart = t;  // (not accounting for frame time here)
      response7disk_3.frameNStart = frameN;  // exact frame index
      
      response7disk_3.setAutoDraw(true);
    }

    if (Catch === 0){
        continueRoutine = false
        }
    
    // *text_26* updates
    if (t >= 0.0 && text_26.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_26.tStart = t;  // (not accounting for frame time here)
      text_26.frameNStart = frameN;  // exact frame index
      
      text_26.setAutoDraw(true);
    }

    
    // *rectangle_2* updates
    if (t >= 0.0 && rectangle_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rectangle_2.tStart = t;  // (not accounting for frame time here)
      rectangle_2.frameNStart = frameN;  // exact frame index
      
      rectangle_2.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    catch_1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var catchresponse;
function catch_1RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'catch_1'-------
    catch_1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // store data for thisExp (ExperimentHandler)
    const xys = mouse_3.getPos();
    const buttons = mouse_3.getPressed();
    psychoJS.experiment.addData('mouse_3.x', xys[0]);
    psychoJS.experiment.addData('mouse_3.y', xys[1]);
    psychoJS.experiment.addData('mouse_3.leftButton', buttons[0]);
    psychoJS.experiment.addData('mouse_3.midButton', buttons[1]);
    psychoJS.experiment.addData('mouse_3.rightButton', buttons[2]);
    if (mouse_3.clicked_name.length > 0) {
      psychoJS.experiment.addData('mouse_3.clicked_name', mouse_3.clicked_name[0]);}
    mousexpos = mouse.getPos()[0];
    mouseypos = mouse.getPos()[1];
    x11d = (a - (b / 2));
    y11d = (a + (b / 2));
    x12d = (a + (b / 2));
    y12d = (a + (b / 2));
    x13d = (a - (b / 2));
    y13d = (a - (b / 2));
    a1d = ((((y12d - y13d) * (mousexpos - x13d)) + ((x13d - x12d) * (mouseypos - y13d))) / (((y12d - y13d) * (x11d - x13d)) + ((x13d - x12d) * (y11d - y13d))));
    b1d = ((((y13d - y11d) * (mousexpos - x13d)) + ((x11d - x13d) * (mouseypos - y13d))) / (((y12d - y13d) * (x11d - x13d)) + ((x13d - x12d) * (y11d - y13d))));
    c1d = ((1 - a1d) - b1d);
    x21d = (a - (b / 2));
    y21d = (a - (b / 2));
    x22d = (a + (b / 2));
    y22d = (a + (b / 2));
    x23d = (a + (b / 2));
    y23d = (a - (b / 2));
    a2d = ((((y22d - y23d) * (mousexpos - x23d)) + ((x23d - x22d) * (mouseypos - y23d))) / (((y22d - y23d) * (x21d - x23d)) + ((x23d - x22d) * (y21d - y23d))));
    b2d = ((((y23d - y21d) * (mousexpos - x23d)) + ((x21d - x23d) * (mouseypos - y23d))) / (((y22d - y23d) * (x21d - x23d)) + ((x23d - x22d) * (y21d - y23d))));
    c2d = ((1 - a2d) - b2d);
    x31d = (a - (b / 2));
    y31d = (- (a - (b / 2)));
    x32d = (a + (b / 2));
    y32d = (- (a - (b / 2)));
    x33d = (a + (b / 2));
    y33d = (- (a + (b / 2)));
    a3d = ((((y32d - y33d) * (mousexpos - x33d)) + ((x33d - x32d) * (mouseypos - y33d))) / (((y32d - y33d) * (x31d - x33d)) + ((x33d - x32d) * (y31d - y33d))));
    b3d = ((((y33d - y31d) * (mousexpos - x33d)) + ((x31d - x33d) * (mouseypos - y33d))) / (((y32d - y33d) * (x31d - x33d)) + ((x33d - x32d) * (y31d - y33d))));
    c3d = ((1 - a3d) - b3d);
    x41d = (a - (b / 2));
    y41d = (- (a - (b / 2)));
    x42d = (a + (b / 2));
    y42d = (- (a + (b / 2)));
    x43d = (a - (b / 2));
    y43d = (- (a + (b / 2)));
    a4d = ((((y42d - y43d) * (mousexpos - x43d)) + ((x43d - x42d) * (mouseypos - y43d))) / (((y42d - y43d) * (x41d - x43d)) + ((x43d - x42d) * (y41d - y43d))));
    b4d = ((((y43d - y41d) * (mousexpos - x43d)) + ((x41d - x43d) * (mouseypos - y43d))) / (((y42d - y43d) * (x41d - x43d)) + ((x43d - x42d) * (y41d - y43d))));
    c4d = ((1 - a4d) - b4d);
    x51d = (- (a + (b / 2)));
    y51d = (- (a + (b / 2)));
    x52d = (- (a - (b / 2)));
    y52d = (- (a - (b / 2)));
    x53d = (- (a - (b / 2)));
    y53d = (- (a + (b / 2)));
    a5d = ((((y52d - y53d) * (mousexpos - x53d)) + ((x53d - x52d) * (mouseypos - y53d))) / (((y52d - y53d) * (x51d - x53d)) + ((x53d - x52d) * (y51d - y53d))));
    b5d = ((((y53d - y51d) * (mousexpos - x53d)) + ((x51d - x53d) * (mouseypos - y53d))) / (((y52d - y53d) * (x51d - x53d)) + ((x53d - x52d) * (y51d - y53d))));
    c5d = ((1 - a5d) - b5d);
    x61d = (- (a + (b / 2)));
    y61d = (- (a + (b / 2)));
    x62d = (- (a - (b / 2)));
    y62d = (- (a - (b / 2)));
    x63d = (- (a + (b / 2)));
    y63d = (- (a + (b / 2)));
    a6d = ((((y62d - y63d) * (mousexpos - x63d)) + ((x63d - x62d) * (mouseypos - y63d))) / (((y62d - y63d) * (x61d - x63d)) + ((x63d - x62d) * (y61d - y63d))));
    b6d = ((((y63d - y61d) * (mousexpos - x63d)) + ((x61d - x63d) * (mouseypos - y63d))) / (((y62d - y63d) * (x61d - x63d)) + ((x63d - x62d) * (y61d - y63d))));
    c6d = ((1 - a6d) - b6d);
    x71d = (- (a + (b / 2)));
    y71d = (a + (b / 2));
    x72d = (- (a - (b / 2)));
    y72d = (a - (b / 2));
    x73d = (- (a + (b / 2)));
    y73d = (a - (b / 2));
    a7d = ((((y72d - y73d) * (mousexpos - x73d)) + ((x73d - x72d) * (mouseypos - y73d))) / (((y72d - y73d) * (x71d - x73d)) + ((x73d - x72d) * (y71d - y73d))));
    b7d = ((((y73d - y71d) * (mousexpos - x73d)) + ((x71d - x73d) * (mouseypos - y73d))) / (((y72d - y73d) * (x71d - x73d)) + ((x73d - x72d) * (y71d - y73d))));
    c7d = ((1 - a7d) - b7d);
    x81d = (- (a + (b / 2)));
    y81d = (a + (b / 2));
    x82d = (- (a - (b / 2)));
    y82d = (a + (b / 2));
    x83d = (- (a - (b / 2)));
    y83d = (a - (b / 2));
    a8d = ((((y82d - y83d) * (mousexpos - x83d)) + ((x83d - x82d) * (mouseypos - y83d))) / (((y82d - y83d) * (x81d - x83d)) + ((x83d - x82d) * (y81d - y83d))));
    b8d = ((((y83d - y81d) * (mousexpos - x83d)) + ((x81d - x83d) * (mouseypos - y83d))) / (((y82d - y83d) * (x81d - x83d)) + ((x83d - x82d) * (y81d - y83d))));
    c8d = ((1 - a8d) - b8d);
    if (((((0 <= a1d) && (a1d <= 1)) && ((0 <= b1d) && (b1d <= 1))) && ((0 <= c1d) && (c1d <= 1)))) {
        catchresponse = 7;
    } else {
        if (((((0 <= a2d) && (a2d <= 1)) && ((0 <= b2d) && (b2d <= 1))) && ((0 <= c2d) && (c2d <= 1)))) {
            catchresponse = 6;
        } else {
            if (((((0 <= a3d) && (a3d <= 1)) && ((0 <= b3d) && (b3d <= 1))) && ((0 <= c3d) && (c3d <= 1)))) {
                catchresponse = 5;
            } else {
                if (((((0 <= a4d) && (a4d <= 1)) && ((0 <= b4d) && (b4d <= 1))) && ((0 <= c4d) && (c4d <= 1)))) {
                    catchresponse = 4;
                } else {
                    if (((((0 <= a5d) && (a5d <= 1)) && ((0 <= b5d) && (b5d <= 1))) && ((0 <= c5d) && (c5d <= 1)))) {
                        catchresponse = 3;
                    } else {
                        if (((((0 <= a6d) && (a6d <= 1)) && ((0 <= b6d) && (b6d <= 1))) && ((0 <= c6d) && (c6d <= 1)))) {
                            catchresponse = 2;
                        } else {
                            if (((((0 <= a7d) && (a7d <= 1)) && ((0 <= b7d) && (b7d <= 1))) && ((0 <= c7d) && (c7d <= 1)))) {
                                catchresponse = 1;
                            } else {
                                if (((((0 <= a8d) && (a8d <= 1)) && ((0 <= b8d) && (b8d <= 1))) && ((0 <= c8d) && (c8d <= 1)))) {
                                    catchresponse = 0;
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    thisExp.addData("catchresponse", catchresponse);
    thisExp.addData("catchnumber", catchnumber);
    thisExp.addData("Catch", Catch);
    thisExp.addData("response_time_catch", mouse_3.mouseClock.getTime());
    
    // the Routine "catch_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var response_sumComponents;
function response_sumRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'response_sum'-------
    t = 0;
    response_sumClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_11
    mouse_11.clicked_name = [];
    gotValidClick = false; // until a click is received
    rectangle_9.setFillColor(new util.Color(grey));
    trialnumbertext = `You have finished ${trialnumber} of 324 questions`;
    event.clearEvents();
    
    if (Catch === 0){
        continueRoutine = false
        }
    text_52.setText(trialnumbertext);
    // keep track of which components have finished
    response_sumComponents = [];
    response_sumComponents.push(mouse_11);
    response_sumComponents.push(response1disk_11);
    response_sumComponents.push(response3disk_11);
    response_sumComponents.push(response5disk_11);
    response_sumComponents.push(response7disk_11);
    response_sumComponents.push(rectangle_9);
    response_sumComponents.push(text_51);
    response_sumComponents.push(text_52);
    
    response_sumComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function response_sumRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'response_sum'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = response_sumClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // *mouse_11* updates
    if (t >= 0.0 && mouse_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_11.tStart = t;  // (not accounting for frame time here)
      mouse_11.frameNStart = frameN;  // exact frame index
      
      mouse_11.status = PsychoJS.Status.STARTED;
      mouse_11.mouseClock.reset();
      prevButtonState = mouse_11.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_11.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      let buttons = mouse_11.getPressed();
      if (!buttons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = buttons;
        if (buttons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [rectangle]) {
            if (obj.contains(mouse_11)) {
              gotValidClick = true;
              mouse_11.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *response1disk_11* updates
    if (t >= 0.0 && response1disk_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response1disk_11.tStart = t;  // (not accounting for frame time here)
      response1disk_11.frameNStart = frameN;  // exact frame index
      
      response1disk_11.setAutoDraw(true);
    }

    
    // *response3disk_11* updates
    if (t >= 0.0 && response3disk_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response3disk_11.tStart = t;  // (not accounting for frame time here)
      response3disk_11.frameNStart = frameN;  // exact frame index
      
      response3disk_11.setAutoDraw(true);
    }

    
    // *response5disk_11* updates
    if (t >= 0.0 && response5disk_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response5disk_11.tStart = t;  // (not accounting for frame time here)
      response5disk_11.frameNStart = frameN;  // exact frame index
      
      response5disk_11.setAutoDraw(true);
    }

    
    // *response7disk_11* updates
    if (t >= 0.0 && response7disk_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response7disk_11.tStart = t;  // (not accounting for frame time here)
      response7disk_11.frameNStart = frameN;  // exact frame index
      
      response7disk_11.setAutoDraw(true);
    }

    
    // *rectangle_9* updates
    if (t >= 0.0 && rectangle_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rectangle_9.tStart = t;  // (not accounting for frame time here)
      rectangle_9.frameNStart = frameN;  // exact frame index
      
      rectangle_9.setAutoDraw(true);
    }

    if (Catch === 0){
        continueRoutine = false
        }
    
    // *text_51* updates
    if (t >= 0.0 && text_51.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_51.tStart = t;  // (not accounting for frame time here)
      text_51.frameNStart = frameN;  // exact frame index
      
      text_51.setAutoDraw(true);
    }

    
    // *text_52* updates
    if (t >= 0.0 && text_52.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_52.tStart = t;  // (not accounting for frame time here)
      text_52.frameNStart = frameN;  // exact frame index
      
      text_52.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    response_sumComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function response_sumRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'response_sum'-------
    response_sumComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // store data for thisExp (ExperimentHandler)
    const xys = mouse_11.getPos();
    const buttons = mouse_11.getPressed();
    psychoJS.experiment.addData('mouse_11.x', xys[0]);
    psychoJS.experiment.addData('mouse_11.y', xys[1]);
    psychoJS.experiment.addData('mouse_11.leftButton', buttons[0]);
    psychoJS.experiment.addData('mouse_11.midButton', buttons[1]);
    psychoJS.experiment.addData('mouse_11.rightButton', buttons[2]);
    if (mouse_11.clicked_name.length > 0) {
      psychoJS.experiment.addData('mouse_11.clicked_name', mouse_11.clicked_name[0]);}
    // the Routine "response_sum" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var modify;
var survey1Components;
function survey1RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'survey1'-------
    t = 0;
    survey1Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    modify = false;
    copyText_1.text = '';
    // keep track of which components have finished
    survey1Components = [];
    survey1Components.push(copyText_1);
    survey1Components.push(question_4);
    survey1Components.push(submitanswer);
    
    survey1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


var textAdd;
function survey1RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'survey1'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = survey1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *copyText_1* updates
    if (t >= 0 && copyText_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      copyText_1.tStart = t;  // (not accounting for frame time here)
      copyText_1.frameNStart = frameN;  // exact frame index
      
      copyText_1.setAutoDraw(true);
    }

    let theseKeys = psychoJS.eventManager.getKeys({keyList: ['a', 'b', 'c', 'd','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','return','backspace','space']});
    if (theseKeys.length > 0) {  // at least one key was pressed
      textAdd = theseKeys[theseKeys.length-1]; 
      }
    
    
    
    
    if (textAdd === 'return') {
        textAdd = '';  // Add nothing
        continueRoutine = false;  // End routine (if that is what you want)
    } else if (textAdd === 'space') {
        textAdd = ' ';  // Add a space
    } else if (textAdd === 'backspace') {
        copyText_1.text = copyText_1.text.slice(0, -1);
        textAdd = undefined;
    } else if (textAdd !== undefined) {
        if (modify) {
            copyText_1.text = copyText_1.text + textAdd.toUpperCase();
            modify = false;
        } else {
            copyText_1.text = copyText_1.text + textAdd
        }
        textAdd = undefined;
    }
    
    
    // *question_4* updates
    if (t >= 0 && question_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      question_4.tStart = t;  // (not accounting for frame time here)
      question_4.frameNStart = frameN;  // exact frame index
      
      question_4.setAutoDraw(true);
    }

    
    // *submitanswer* updates
    if (t >= 0.0 && submitanswer.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      submitanswer.tStart = t;  // (not accounting for frame time here)
      submitanswer.frameNStart = frameN;  // exact frame index
      
      submitanswer.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    survey1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function survey1RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'survey1'-------
    survey1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData("answer1", copyText_1.text)
    copyText_1.setText('')  // empty the onscreen text ready for next input
    
    thisExp.addData("rt1", t);
    // the Routine "survey1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var survey2Components;
function survey2RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'survey2'-------
    t = 0;
    survey2Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    modify = false;
    copyText_2.text = '';
    // keep track of which components have finished
    survey2Components = [];
    survey2Components.push(copyText_2);
    survey2Components.push(question);
    survey2Components.push(submitanswer_2);
    
    survey2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function survey2RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'survey2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = survey2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *copyText_2* updates
    if (t >= 0 && copyText_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      copyText_2.tStart = t;  // (not accounting for frame time here)
      copyText_2.frameNStart = frameN;  // exact frame index
      
      copyText_2.setAutoDraw(true);
    }

    let theseKeys = psychoJS.eventManager.getKeys({keyList: ['a', 'b', 'c', 'd','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','return','backspace','space']});
    if (theseKeys.length > 0) {  // at least one key was pressed
      textAdd = theseKeys[theseKeys.length-1]; 
      }
    
    
    
    
    if (textAdd === 'return') {
        textAdd = '';  // Add nothing
        continueRoutine = false;  // End routine (if that is what you want)
    } else if (textAdd === 'space') {
        textAdd = ' ';  // Add a space
    } else if (textAdd === 'backspace') {
        copyText_2.text = copyText_2.text.slice(0, -1);
        textAdd = undefined;
    } else if (textAdd !== undefined) {
        if (modify) {
            copyText_2.text = copyText_2.text + textAdd.toUpperCase();
            modify = false;
        } else {
            copyText_2.text = copyText_2.text + textAdd
        }
        textAdd = undefined;
    }
    
    // *question* updates
    if (t >= 0 && question.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      question.tStart = t;  // (not accounting for frame time here)
      question.frameNStart = frameN;  // exact frame index
      
      question.setAutoDraw(true);
    }

    
    // *submitanswer_2* updates
    if (t >= 0.0 && submitanswer_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      submitanswer_2.tStart = t;  // (not accounting for frame time here)
      submitanswer_2.frameNStart = frameN;  // exact frame index
      
      submitanswer_2.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    survey2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function survey2RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'survey2'-------
    survey2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData("answer2", copyText_2.text)
    copyText_2.setText('')  // empty the onscreen text ready for next input
    
    thisExp.addData("rt2", t);
    // the Routine "survey2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var survey3Components;
function survey3RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'survey3'-------
    t = 0;
    survey3Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    modify = false;
    copyText_3.text = '';
    
    // keep track of which components have finished
    survey3Components = [];
    survey3Components.push(copyText_3);
    survey3Components.push(question_2);
    survey3Components.push(submitanswer_3);
    
    survey3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function survey3RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'survey3'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = survey3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *copyText_3* updates
    if (t >= 0 && copyText_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      copyText_3.tStart = t;  // (not accounting for frame time here)
      copyText_3.frameNStart = frameN;  // exact frame index
      
      copyText_3.setAutoDraw(true);
    }

    let theseKeys = psychoJS.eventManager.getKeys({keyList: ['a', 'b', 'c', 'd','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','return','backspace','space']});
    if (theseKeys.length > 0) {  // at least one key was pressed
      textAdd = theseKeys[theseKeys.length-1]; 
      }
    
    
    if (textAdd === 'return') {
        textAdd = '';  // Add nothing
        continueRoutine = false;  // End routine (if that is what you want)
    } else if (textAdd === 'space') {
        textAdd = ' ';  // Add a space
    } else if (textAdd === 'backspace') {
        copyText_3.text = copyText_3.text.slice(0, -1);
        textAdd = undefined;
    } else if (['lshift', 'rshift'].includes(textAdd)) {
        modify = true;
    } else if (textAdd !== undefined) {
        if (modify) {
            copyText_3.text = copyText_3.text + textAdd.toUpperCase();
            modify = false;
        } else {
            copyText_3.text = copyText_3.text + textAdd
        }
        textAdd = undefined;
    }
    
    // *question_2* updates
    if (t >= 0 && question_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      question_2.tStart = t;  // (not accounting for frame time here)
      question_2.frameNStart = frameN;  // exact frame index
      
      question_2.setAutoDraw(true);
    }

    
    // *submitanswer_3* updates
    if (t >= 0.0 && submitanswer_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      submitanswer_3.tStart = t;  // (not accounting for frame time here)
      submitanswer_3.frameNStart = frameN;  // exact frame index
      
      submitanswer_3.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    survey3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function survey3RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'survey3'-------
    survey3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData("answer3", copyText_3.text)
    copyText_3.setText('')  // empty the onscreen text ready for next input
    thisExp.addData("rt3", t);
    // the Routine "survey3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var survey_4Components;
function survey_4RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'survey_4'-------
    t = 0;
    survey_4Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    modify = false;
    copyText_4.text = '';
    // keep track of which components have finished
    survey_4Components = [];
    survey_4Components.push(copyText_4);
    survey_4Components.push(question_3);
    survey_4Components.push(submitanswer_4);
    
    survey_4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function survey_4RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'survey_4'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = survey_4Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *copyText_4* updates
    if (t >= 0 && copyText_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      copyText_4.tStart = t;  // (not accounting for frame time here)
      copyText_4.frameNStart = frameN;  // exact frame index
      
      copyText_4.setAutoDraw(true);
    }

    let theseKeys = psychoJS.eventManager.getKeys({keyList: ['a', 'b', 'c', 'd','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','return','backspace','space']});
    if (theseKeys.length > 0) {  // at least one key was pressed
      textAdd = theseKeys[theseKeys.length-1]; 
      }
    
    
    if (textAdd === 'return') {
        textAdd = '';  // Add nothing
        continueRoutine = false;  // End routine (if that is what you want)
    } else if (textAdd === 'space') {
        textAdd = ' ';  // Add a space
    } else if (textAdd === 'backspace') {
        copyText_4.text = copyText_4.text.slice(0, -1);
        textAdd = undefined;
    } else if (['lshift', 'rshift'].includes(textAdd)) {
        modify = true;
    } else if (textAdd !== undefined) {
        if (modify) {
            copyText_4.text = copyText_4.text + textAdd.toUpperCase();
            modify = false;
        } else {
            copyText_4.text = copyText_4.text + textAdd
        }
        textAdd = undefined;
    }
    
    // *question_3* updates
    if (t >= 0 && question_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      question_3.tStart = t;  // (not accounting for frame time here)
      question_3.frameNStart = frameN;  // exact frame index
      
      question_3.setAutoDraw(true);
    }

    
    // *submitanswer_4* updates
    if (t >= 0.0 && submitanswer_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      submitanswer_4.tStart = t;  // (not accounting for frame time here)
      submitanswer_4.frameNStart = frameN;  // exact frame index
      
      submitanswer_4.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    survey_4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function survey_4RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'survey_4'-------
    survey_4Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData("answer4", copyText_4.text)
    copyText_4.setText('')  // empty the onscreen text ready for next input
    thisExp.addData("rt4", t);
    // the Routine "survey_4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var survey5Components;
function survey5RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'survey5'-------
    t = 0;
    survey5Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    modify = false;
    copyText_5.text = '';
    // keep track of which components have finished
    survey5Components = [];
    survey5Components.push(copyText_5);
    survey5Components.push(question_5);
    survey5Components.push(submitanswer_5);
    
    survey5Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function survey5RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'survey5'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = survey5Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *copyText_5* updates
    if (t >= 0 && copyText_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      copyText_5.tStart = t;  // (not accounting for frame time here)
      copyText_5.frameNStart = frameN;  // exact frame index
      
      copyText_5.setAutoDraw(true);
    }

    let theseKeys = psychoJS.eventManager.getKeys({keyList: ['a', 'b', 'c', 'd','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','return','backspace','space']});
    if (theseKeys.length > 0) {  // at least one key was pressed
      textAdd = theseKeys[theseKeys.length-1]; 
      }
    
    
    if (textAdd === 'return') {
        textAdd = '';  // Add nothing
        continueRoutine = false;  // End routine (if that is what you want)
    } else if (textAdd === 'space') {
        textAdd = ' ';  // Add a space
    } else if (textAdd === 'backspace') {
        copyText_5.text = copyText_5.text.slice(0, -1);
        textAdd = undefined;
    } else if (['lshift', 'rshift'].includes(textAdd)) {
        modify = true;
    } else if (textAdd !== undefined) {
        if (modify) {
            copyText_5.text = copyText_5.text + textAdd.toUpperCase();
            modify = false;
        } else {
            copyText_5.text = copyText_5.text + textAdd
        }
        textAdd = undefined;
    }
    
    // *question_5* updates
    if (t >= 0 && question_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      question_5.tStart = t;  // (not accounting for frame time here)
      question_5.frameNStart = frameN;  // exact frame index
      
      question_5.setAutoDraw(true);
    }

    
    // *submitanswer_5* updates
    if (t >= 0.0 && submitanswer_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      submitanswer_5.tStart = t;  // (not accounting for frame time here)
      submitanswer_5.frameNStart = frameN;  // exact frame index
      
      submitanswer_5.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    survey5Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function survey5RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'survey5'-------
    survey5Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData("answer5", copyText_5.text)
    copyText_5.setText('')  // empty the onscreen text ready for next input
    thisExp.addData("rt5", t);
    // the Routine "survey5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var survey6Components;
function survey6RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'survey6'-------
    t = 0;
    survey6Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    modify = false;
    copyText_6.text = '';
    // keep track of which components have finished
    survey6Components = [];
    survey6Components.push(copyText_6);
    survey6Components.push(question_6);
    survey6Components.push(submitanswer_6);
    
    survey6Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function survey6RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'survey6'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = survey6Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *copyText_6* updates
    if (t >= 0 && copyText_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      copyText_6.tStart = t;  // (not accounting for frame time here)
      copyText_6.frameNStart = frameN;  // exact frame index
      
      copyText_6.setAutoDraw(true);
    }

    let theseKeys = psychoJS.eventManager.getKeys({keyList: ['a', 'b', 'c', 'd','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','return','backspace','space']});
    if (theseKeys.length > 0) {  // at least one key was pressed
      textAdd = theseKeys[theseKeys.length-1]; 
      }
    
    
    if (textAdd === 'return') {
        textAdd = '';  // Add nothing
        continueRoutine = false;  // End routine (if that is what you want)
    } else if (textAdd === 'space') {
        textAdd = ' ';  // Add a space
    } else if (textAdd === 'backspace') {
        copyText_6.text = copyText_6.text.slice(0, -1);
        textAdd = undefined;
    } else if (['lshift', 'rshift'].includes(textAdd)) {
        modify = true;
    } else if (textAdd !== undefined) {
        if (modify) {
            copyText_6.text = copyText_6.text + textAdd.toUpperCase();
            modify = false;
        } else {
            copyText_6.text = copyText_6.text + textAdd
        }
        textAdd = undefined;
    }
    
    // *question_6* updates
    if (t >= 0 && question_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      question_6.tStart = t;  // (not accounting for frame time here)
      question_6.frameNStart = frameN;  // exact frame index
      
      question_6.setAutoDraw(true);
    }

    
    // *submitanswer_6* updates
    if (t >= 0.0 && submitanswer_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      submitanswer_6.tStart = t;  // (not accounting for frame time here)
      submitanswer_6.frameNStart = frameN;  // exact frame index
      
      submitanswer_6.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    survey6Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function survey6RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'survey6'-------
    survey6Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData("answer6", copyText_6.text)
    copyText_6.setText('')  // empty the onscreen text ready for next input
    
    thisExp.addData("rt6", t);
    // the Routine "survey6" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var survey7Components;
function survey7RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'survey7'-------
    t = 0;
    survey7Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    modify = false;
    copyText_7.text = '';
    
    // keep track of which components have finished
    survey7Components = [];
    survey7Components.push(copyText_7);
    survey7Components.push(question_7);
    survey7Components.push(submitanswer_7);
    
    survey7Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function survey7RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'survey7'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = survey7Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *copyText_7* updates
    if (t >= 0 && copyText_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      copyText_7.tStart = t;  // (not accounting for frame time here)
      copyText_7.frameNStart = frameN;  // exact frame index
      
      copyText_7.setAutoDraw(true);
    }

    let theseKeys = psychoJS.eventManager.getKeys({keyList: ['a', 'b', 'c', 'd','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','return','backspace', 'space']});
    if (theseKeys.length > 0) {  // at least one key was pressed
      textAdd = theseKeys[theseKeys.length-1]; 
      }
    
    
    if (textAdd === 'return') {
        textAdd = '';  // Add nothing
        continueRoutine = false;  // End routine (if that is what you want)
    } else if (textAdd === 'space') {
        textAdd = ' ';  // Add a space
    } else if (textAdd === 'backspace') {
        copyText_7.text = copyText_7.text.slice(0, -1);
        textAdd = undefined;
    } else if (['lshift', 'rshift'].includes(textAdd)) {
        modify = true;
    } else if (textAdd !== undefined) {
        if (modify) {
            copyText_7.text = copyText_7.text + textAdd.toUpperCase();
            modify = false;
        } else {
            copyText_7.text = copyText_7.text + textAdd
        }
        textAdd = undefined;
    }
    
    // *question_7* updates
    if (t >= 0 && question_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      question_7.tStart = t;  // (not accounting for frame time here)
      question_7.frameNStart = frameN;  // exact frame index
      
      question_7.setAutoDraw(true);
    }

    
    // *submitanswer_7* updates
    if (t >= 0.0 && submitanswer_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      submitanswer_7.tStart = t;  // (not accounting for frame time here)
      submitanswer_7.frameNStart = frameN;  // exact frame index
      
      submitanswer_7.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    survey7Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function survey7RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'survey7'-------
    survey7Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData("answer7", copyText_7.text)
    copyText_7.setText('')  // empty the onscreen text ready for next input
    thisExp.addData("rt7", t);
    // the Routine "survey7" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(thisScheduler, loop) {
  // ------Prepare for next entry------
  return function () {
    if (typeof loop !== 'undefined') {
      // ------Check if user ended loop early------
      if (loop.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(loop);
        }
      thisScheduler.stop();
      } else {
        const thisTrial = loop.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(loop);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(trials) {
  return function () {
    psychoJS.importAttributes(trials.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
