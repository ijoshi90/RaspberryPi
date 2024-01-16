echo "Capturing photo..."
imageName="/home/pi/Camera_Captures/`date +"%Y%m%d%H%M%S"`.jpg"
#raspistill -o $imageName
libcamera-still -r -o $imageName
echo "Photo can be found here $imageName"
