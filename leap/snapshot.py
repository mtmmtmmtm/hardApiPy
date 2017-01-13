import LeapAPI.Leap as lp, sys, thread, time
from LeapAPI.Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
import numpy as np
from matplotlib import pyplot
#import pandas as pd

class SampleListener(lp.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']
    timeOld = 0
    x_ = np.eye(1, 16)
    time_Cooldown = 1000000

    def on_init(self, controller):
        print ("Initialized")

    def on_connect(self, controller):
        print ("Connected")

        # Enable gestures
        controller.enable_gesture(lp.Gesture.TYPE_CIRCLE);
        controller.enable_gesture(lp.Gesture.TYPE_KEY_TAP);
        controller.enable_gesture(lp.Gesture.TYPE_SCREEN_TAP);
        controller.enable_gesture(lp.Gesture.TYPE_SWIPE);

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print ("Disconnected")

    def on_exit(self, controller):
        print ("Exited")

    def on_frame(self, controller):
        frame = controller.frame()
        if(str(frame.hands[0]) !="Invalid Hand"):
            x = np.eye(1, 16)
            normal = frame.hands[0].palm_normal
            direction = frame.hands[0].direction
            arm = frame.hands[0].arm
            finger = frame.hands[0].fingers
            x[0][0]=direction.pitch * lp.RAD_TO_DEG #
            x[0][1]=direction.pitch * lp.RAD_TO_DEG
            x[0][2]=direction.yaw * lp.RAD_TO_DEG
            x[0][3]=arm.wrist_position[0] #
            x[0][4]=arm.wrist_position[1]
            x[0][5]=arm.wrist_position[2]
            i = 6
            for finger in frame.hands[0].fingers:
                #for b in range(0, 4):
                    for j in range(0, 2):
                        x[0][i] = finger.bone(2).direction[j]
                        i += 1


            #
           # sys.stdout.write('\rf =' + str(x)) #x[0][7]
            #sys.stdout.flush()1

            if frame.timestamp-self.timeOld > self.time_Cooldown:
                print(str(x-self.x_) + "\n") #print error
                self.x_ = x
                self.timeOld=frame.timestamp
        else:
            self.timeOld = frame.timestamp
        #for hand in frame.hands:
        #    print()

def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = lp.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()
