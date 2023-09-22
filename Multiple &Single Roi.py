import cv2
import numpy as np
import json
import os

# Global variables
points = []
rects = []
roi_count = 0
poly_count = 0
json_filename = "roi_data.json"

if os.path.exists(json_filename):
    os.remove(json_filename)
    
def roi_selection(mode):
    global points, rects, roi_count, poly_count

    def save_to_json(data):
        with open(json_filename, "w") as f:
            json.dump(data, f, indent=4)
            
    def load_from_json():
        if os.path.exists(json_filename):
            with open(json_filename, "r") as f:
                content = f.read()
                if content:
                    try:
                        return json.loads(content)
                    except json.JSONDecodeError:
                        return {}
        return {}

    def click_event(event, x, y, flags, param):
        global points
        if mode == "polyline":
            if event == cv2.EVENT_LBUTTONDOWN:
                points.append((x, y))
                cv2.circle(img, (x, y), 5, (0, 0, 255), -1)

    img = cv2.imread('image.jpg', 1)
    if img is None:
        img = np.zeros((720, 1280, 3), np.uint8)
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.setMouseCallback('image', click_event)

    exit_flag = False
    while True:
        if mode == "rect":
            cv2.putText(img, "1- Select a rectangle and press Enter to confirm", (30, 50), 
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4)

            cv2.putText(img, "2- Press Escape to end the function", (80, 120), 
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4)
    
        elif mode == "polyline":
            cv2.putText(img, "Press Enter to close the polygon", (30, 50), 
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4)

            cv2.putText(img, "Press Escape to end the function", (80, 120), 
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4)
            
        cv2.imshow('image', img)
        key = cv2.waitKey(100) & 0xFF 

        if mode == "rect":
            roi = cv2.selectROI("image", img, False, True)
            if roi == (0, 0, 0, 0):
                exit_flag = True
                break
            x, y, w, h = roi
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
            roi_data = (x, y, w, h)
            rects.append(roi_data)
            roi_count += 1
            print(f"ROI_{roi_count}:", roi_data)
                
            data = load_from_json()
            data[f"ROI_{roi_count}"] = roi_data
            save_to_json(data)

        elif mode == "polyline":
            if key == 13:  # 'Enter' key pressed
                if len(points) > 1:
                    cv2.polylines(img, [np.array(points)], isClosed=True, color=(0, 255, 0), thickness=2)
                    poly_count += 1
                    print(f"Poly_{poly_count}:", points)
                    
                    data = load_from_json()
                    data[f"Poly_{poly_count}"] = points
                    save_to_json(data)
                    points = []

        if key == 27 or exit_flag:  # Escape key or exit flag set
            break
            
    cv2.destroyAllWindows()
roi_selection(mode="polyline")
