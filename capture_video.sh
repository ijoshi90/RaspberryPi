# Input needed - argument 1 with time in seconds
echo "Capturing photo..."
captureTime=$(($1 * 100))
imageName="/home/pi/Camera_Captures/`date +"%Y%m%d%H%M%S"`.mp4"
#raspistill -o $imageName
libcamera-vid -t $captureTime -o $imageName --save-pts timestamps.txt
echo "Video can be found here $imageName"
