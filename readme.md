# Basketball Shot Tracker (Taco Inspiration)

Personal Project for tracking the made and missed basketball shots

## Steps Taken to build

### Collect and Process Data
1. Took video footage of myself shooting around in a basketball gym
2. Parsed out each frame of the video using [VideoProc Converter]([url](https://www.videoproc.com/))
3. Annotated Over 2000 images labeling basketball, person, net, etc. Using [LabelImg]([url](https://github.com/HumanSignal/labelImg)https://github.com/HumanSignal/labelImg)

### Train Model Using Labeled Image Data
1. Followed [theAIGuy's Google Colab Notebook]([url](https://colab.research.google.com/drive/1Mh2HP_Mfxoao6qNFbhfV3u28tG8jAVGk)https://colab.research.google.com/drive/1Mh2HP_Mfxoao6qNFbhfV3u28tG8jAVGk) to train model and output weights
2. Exported Output Weights

### Implement Weights into YOLO and OPENCV Code
1. Pysource has a [great tutorial]([url](https://www.youtube.com/watch?v=GgGro5IV-cs&ab_channel=Pysource)https://www.youtube.com/watch?v=GgGro5IV-cs&ab_channel=Pysource) to get started
2. Using OpenCV, opened a new video that you want the code to run object recognition on
3. Utilized YOLO to generate bounding boxes and confidence levels for the basketball images
4. Wrote logic for capturing shot count
