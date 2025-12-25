
🧙 Harry Potter Invisible Cloak (White Cloak Version)
A fun Computer Vision project inspired by Harry Potter’s Invisibility Cloak, built using Python and OpenCV.
This program makes a white-colored cloak invisible in real time by replacing it with the captured background from the webcam feed.
✨ How It Works
The program first captures the static background (without the person in frame).
It continuously reads webcam frames.
Converts each frame to HSV color space.
Detects white-colored regions (cloak).
Applies morphological operations to remove noise.
Replaces the cloak area with the background, creating the invisibility illusion.
🛠️ Tech Stack
Python
OpenCV (cv2)
NumPy
Webcam / Camera module
📂 Project Structure
Copy code

├── invisible_cloak.py
├── README.md
▶️ How to Run
1️⃣ Install Dependencies
Copy code
Bash
pip install opencv-python numpy
2️⃣ Run the Script
Copy code
Bash
python invisible_cloak.py
🎥 Usage Instructions
Run the program.
Move out of the camera frame when prompted (to capture background).
Wear a white cloth or cloak.
Stand in front of the camera and enjoy the invisibility effect.
Press ESC to exit.
⚙️ Key Parameters
Copy code
Python
lower_white = np.array([0, 0, 200])
upper_white = np.array([180, 50, 255])
These HSV values detect white color.
You can adjust them based on lighting conditions.
🧠 Concepts Used
HSV Color Space
Color Masking
Bitwise Operations
Morphological Transformations
Real-Time Video Processing
🚀 Future Enhancements
Support for multiple cloak colors
Auto lighting calibration
Background re-capture button
Performance optimization
🪄 Inspired By
✨ Harry Potter’s Invisibility Cloak
✨ Computer Vision magic with OpenCV# Invisible-Cloak
