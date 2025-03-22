Hand Gesture Recognition AI project:  

# Hand Gesture Recognition AI for Slide Navigation & Cursor Control  

🚀 **An AI-powered hand tracking system that enables touchless control of presentations and cursor movements using real-time gestures.**  

## **🔹 Features**  
✅ **Move Cursor with One Finger** – Point your **index finger** at the camera to control the mouse.  
✅ **Click with Two Fingers** – Touch **index and middle fingers together** to perform a click.  
✅ **Slide Navigation with One Finger Swipe** –  
   - Swipe **left** to go **backward** in a presentation.  
   - Swipe **right** to go **forward** in a presentation.  
✅ **Real-Time AR-Based Instructions** – Displays on-screen guidance for first-time users.  
✅ **High Accuracy & Smooth Tracking** – Uses **advanced hand detection & smoothing techniques** for ultra-responsive gestures.  

---

## **📌 How It Works**  
1. **Hand Tracking with AI:**  
   - Uses **MediaPipe Hands** to detect and track **finger movements** in real-time.  
   - Identifies **finger tips** and maps them to screen coordinates.  

2. **Gesture Recognition & Execution:**  
   - **Cursor movement**: Maps **index finger** position to screen.  
   - **Click detection**: Detects when **index & middle fingers** are close.  
   - **Slide navigation**: Detects **left & right swipes** to control presentations.  

3. **Real-Time Feedback:**  
   - **Displays guidance text** to help users interact seamlessly.  

---

## **💻 Installation**  
### **🔹 Prerequisites**  
- Python **3.7+**  
- Webcam (Built-in or External)  

### **🔹 Install Required Libraries**  
```sh
pip install opencv-python mediapipe pyautogui numpy
```

---

## **🚀 Usage**  
1️⃣ **Run the Script:**  
```sh
python hand_gesture_ai.py
```
2️⃣ Ensure your **webcam** is on.  
3️⃣ **Control your screen using gestures:**  
   - **Move cursor:** Point one finger.  
   - **Click:** Touch two fingers together.  
   - **Swipe left/right:** Change slides in PowerPoint/Google Slides.  
4️⃣ Press **'q'** to exit.  

---

## **🎯 Use Cases**  
✔ **Hands-Free Slide Navigation** (PowerPoint, Google Slides, Keynote)  
✔ **Touchless Mouse Control** for accessibility and smart interfaces  
✔ **AI-Powered Gesture-Based Interactions**  

---

## **🔧 Troubleshooting**  
❗ If gestures are unresponsive, try increasing brightness for better hand detection.  
❗ Ensure the webcam is positioned properly for **optimal hand visibility**.  
❗ Restart the script if tracking is **laggy**.  

---

## **📜 License**  
🔹 Open-source under the **MIT License**. Feel free to modify and improve it!  

---

🚀 **Enjoy the futuristic, hands-free interaction experience!** 🖐️💡
