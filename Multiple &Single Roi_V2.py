import cv2
import numpy as np

# Global variables
points = []
rects = []
roi_count = 0
poly_count = 0
    
def roi_selection(mode):
    global points, rects, roi_count, poly_count

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
       

        elif mode == "polyline":
            if key == 13:  # 'Enter' key pressed
                if len(points) > 1:
                    cv2.polylines(img, [np.array(points)], isClosed=True, color=(0, 255, 0), thickness=2)
                    poly_count += 1
                    print(f"Poly_{poly_count}:", points)
                   
                    points = []

        if key == 27 or exit_flag:  # Escape key or exit flag set
            break
            
    cv2.destroyAllWindows()
roi_selection(mode="rect")
