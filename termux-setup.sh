#!/bin/bash

echo "[ INF ] Installation started... [INF]"
echo "[ INF ] Installing requirements.txt [ INF ]"
pip3 install -r requirements.txt
if [ $? -eq 0 ]; then
    echo "[i] Sucessfully installed requirements [i]"
else
    echo "Unable to install the packages please try to manually install the packages."
    echo "Try the following command"
    echo "pip install -r requirements.txt"
    exit
fi
cp hijacker.py /data/data/com.termux/files/usr/bin/hijacker
if [ $? -eq 0 ]; then
    echo "The tool has been installed now run hijacker -h to see the help menu."
    echo "Happy hacking!"
else
    echo "Unable to make a binary file of the tool."
    echo "Please run the following command."
    echo "cp hijacker.py /data/data/com.termux/files/usr/bin/hijacker"
fi
