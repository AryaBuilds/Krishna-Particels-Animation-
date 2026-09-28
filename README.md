# Smart Study Monitor (Web)

## Chalane ka tarika
1. Is folder mein terminal kholo: `python run.py`
2. Browser mein http://localhost:8000 khulega -> "Start Monitoring" dabao, camera allow karo.

(Camera ke liye `http://localhost` ya `https` zaroori hai — file par double-click se camera nahi chalega.)

## Online host karna ho
Poora folder Netlify / Vercel / GitHub Pages par upload kar do (https automatic milta hai).

## Kya badla
- Python + OpenCV + YOLO -> JavaScript: MediaPipe Face Landmarker (neend/face cover) + TensorFlow.js COCO-SSD (phone)
- Same logic aur same alarm priority: Face cover > Sleep > Phone
- Sliders se threshold aur delay adjust kar sakte ho
- Video browser se bahar nahi jata
