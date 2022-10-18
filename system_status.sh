clear
echo "---------------------------------------------"
echo
echo "Temperature : "$(vcgencmd measure_temp)
echo
echo "Core Voltage : "$(vcgencmd measure_volts core)
echo
echo "GPU Memory : "$(vcgencmd get_mem gpu)
echo
echo "CPU Memory : "$(vcgencmd get_mem arm)
echo
echo "Camera Status : "$(vcgencmd get_camera)
echo
echo "---------------------------------------------"
