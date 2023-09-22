
# ROI Selection Tool

This tool allows the user to select and save Regions of Interest (ROIs) from an image in two modes: rectangle and polyline. The selected ROIs are saved to a JSON file for future reference.

## Features

1. Two ROI selection modes:
   - **Rectangle**: Enables the user to select rectangular ROIs.
   - **Polyline**: Enables the user to create polygonal ROIs by selecting points on the image.

2. Real-time feedback on the image for ROI selection.
3. Data persistence through a JSON file (`roi_data.json`), which saves the selected ROIs.

## Prerequisites

- Python 3.x
- OpenCV (`cv2`)
- Numpy

## Usage

1. Download or clone this repository.
2. Place your desired image named `image.jpg` in the same directory.
3. Run the script:

For Rectangle mode:
```bash
python your_script_name.py --mode rect
```

For Polyline mode:
```bash
python your_script_name.py --mode polyline
```

4. Follow the on-screen instructions for selecting ROIs.
5. Selected ROIs will be saved to `roi_data.json`.

## How it works

1. The code checks if the `roi_data.json` file exists and deletes it if found.
2. The user is presented with an image window where they can select ROIs based on the mode.
3. The selected ROIs are displayed on the image in real-time and saved to the JSON file.
4. The user can exit the ROI selection process by pressing the `Escape` key.

## Limitations

1. Currently supports only one image named `image.jpg`.
2. The image window size is hardcoded.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
