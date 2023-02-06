import cv2
import mediapipe as mp
from cvzone.HandTrackingModule import HandDetector

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles         #initialisation des modules 
mp_hands = mp.solutions.hands


class HandTracking:
    def __init__(self):
        self.hand_tracking = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
#        self.detector = HandDetector(detectionCon=0.8, maxHands=1)
        self.cap = cv2.VideoCapture(0)

        self.hand_x = 0
        self.hand_y = 0                     #coordonnées 
        self.axis_x = 0
        self.axis_y = 0
        
        self.results = None
        self.hand_closed = False
        

    def scan_hands(self):
        _, self.frame = self.cap.read() #initialiser la cam
        self.frame.shape        
        self.frame = cv2.cvtColor(cv2.flip(self.frame, 1), cv2.COLOR_BGR2RGB)   #mettre un filtre 
        self.frame.flags.writeable = False                                      
        
        self.results = self.hand_tracking.process(self.frame)

        #mettre le filtre sur la cam
        self.frame.flags.writeable = True
        self.frame = cv2.cvtColor(self.frame, cv2.COLOR_RGB2BGR)

        self.hand_closed = False

        if self.results.multi_hand_landmarks:
            for hand_landmarks in self.results.multi_hand_landmarks:
                x, y = hand_landmarks.landmark[9].x, hand_landmarks.landmark[9].y

                self.hand_x = int(x * self.axis_x)
                self.hand_y = int(y * self.axis_y)                                  #pour chaque point de la main

                y_close = hand_landmarks.landmark[12].y

                if y < y_close and y < hand_landmarks.landmark[0].y:            #fermer la main
                    self.hand_closed = True

                mp_drawing.draw_landmarks(
                    self.frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,                                      #optimisation
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style()
                    )
        cv2.imshow("Camera Baker Adventure", self.frame)     #afficher la caméra
        
hand_tracking = HandTracking()