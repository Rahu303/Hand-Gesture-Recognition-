import cv2
import mediapipe as mp
import pyautogui
import platform
import numpy as np

# Detect OS
system_os = platform.system()

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.9, min_tracking_confidence=0.9, max_num_hands=1)
cap = cv2.VideoCapture(0)

screen_w, screen_h = pyautogui.size()
prev_index_x = None
prev_index_y = None
smooth_factor = 3  # Enhanced smoothing for better control

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)
    h, w, _ = frame.shape
    
    # Display AR-based Instructions for New Users
    cv2.putText(frame, "Hand Gesture Guide:", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.putText(frame, "- Swipe Left: Previous Slide", (30, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(frame, "- Swipe Right: Next Slide", (30, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(frame, "- Two Fingers Point: Click", (30, 140), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(frame, "- One Finger Point: Cursor", (30, 170), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Extract key finger tip positions
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
            wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]

            index_x, index_y = int(index_tip.x * w), int(index_tip.y * h)
            middle_x, middle_y = int(middle_tip.x * w), int(middle_tip.y * h)
            
            # Cursor tracking with one finger pointing towards the camera
            cursor_x = int(np.interp(index_x, (0, w), (0, screen_w)))
            cursor_y = int(np.interp(index_y, (0, h), (0, screen_h)))
            pyautogui.moveTo(cursor_x, cursor_y, duration=0.01)
            
            # Click detection (Point with Two Fingers Close Together)
            if abs(index_x - middle_x) < 20 and abs(index_y - middle_y) < 20:
                pyautogui.click()
                cv2.putText(frame, "Click", (index_x, index_y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                
            # Backward gesture (Swipe Left with One Finger)
            if prev_index_x and (prev_index_x - index_x) > 50:
                pyautogui.press('left')
                cv2.putText(frame, "Back", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            
            # Forward gesture (Swipe Right with One Finger)
            if prev_index_x and (index_x - prev_index_x) > 50:
                pyautogui.press('right')
                cv2.putText(frame, "Forward", (w-150, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
            
            # Store previous index finger position for next frame comparison
            prev_index_x = index_x
            prev_index_y = index_y
    
    cv2.imshow("Hand Gesture Control", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
