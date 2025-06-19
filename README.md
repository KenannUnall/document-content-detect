# Document Content Detect

This project uses a YOLO-based object detection model to detect document content in images. It can process multiple document images in batch and outputs both the detection results to the screen and saves the result images.

## Features

- Document content detection with YOLO model
- Batch processing of multiple images
- Visualization and saving of results

## Requirements

- Python 3.8+
- [Ultralytics YOLO](https://docs.ultralytics.com/)
- Required packages: `pip install ultralytics`

## Usage

1. **Add Model Weights:**  
   Place the `weights/best.pt` file in the `weights` folder of your project. You can download the model weights from [here](https://huggingface.co/Kenan-Unal/document-content-detect).

2. **Add Images:**  
   Add the images you want to process to the `docs` folder and list their filenames in the `docs_path` list in the script.

3. **Run the Script:**  
   Execute the following command in your terminal:
   ```bash
   python document-detection.py
   ```

4. **Results:**  
   - Detected boxes and classes will be printed in the terminal.
   - Result images will be saved in the `result` folder.

## File Descriptions

- `document-detection.py`: Main detection script.
- `weights/best.pt`: Trained YOLO model weights.
- `docs/`: Folder containing the images to be tested.
- `result/`: Folder where the result images will be saved.

## Contribution

If you would like to contribute, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. 