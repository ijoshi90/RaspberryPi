echo "Capturing photo..."
raspistill -o /home/pi/Camera_Captures/`date +"%Y%m%d%H%M%S"`.jpg
echo "Photo is saved as /home/pi/Camera_Captures/"
