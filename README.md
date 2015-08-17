FUNCTION
===
This script is used to plot the ndnSIM simulation result
It will generate a pdf file after finish plotting


PREREQUIRMENT
===
The script has been tested on Ubuntu

###Ubuntu
There are some dependencies have to be downloaded:

    sudo apt-get install python gnuplot gnuplot-x11 python-gnuplot

USAGE
===
Type

    python plot.py OPTIONS DATA_TYPE TRACING_RESULT_FILE OUT_FILE_NAME

or change permission before using

    chmod u+x plot.py

and use it directly

    ./plot.py OPTIONS DATA_TYPE TRACING_RESULT_FILE OUT_FILE_NAME

for OPTIONS:
  * L3 - Plot the result of L3RateTracer 
  * L2 - Plot the result of L2Tracer
  * app - Plot the result of AppDelayTracer

for DATA_TYPE please enter:
  * **Packets**, **Kilobytes**, **PacketsRaw** or **KilobytesRaw** for L3RateTracer and L2Tracer
  * **DelayS**, **DelayUS**, **RetxCount** or **HopCount** for AppDelayTracer
