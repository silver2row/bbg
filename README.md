# Motor Bridge Cape addition for the BeagleBone Green Wireless...

    The software for MotorBridge.py was typed up by a different person. That info. is listed in
    that specific file. I did have help from this page online to start the software example(s).

git clone github.com/Seeed-Studio/MotorBridgeCapeforBBG_BBB/blob/master/tests/DCMotorTest.py

...

So...if you are using your MotorBridge.py library w/ the Motor Bridge Cape, use uMove.py or
DCMotorTest.py to run your favorite bunch of motors. I personally have two geared motors for the software 
example listed here as "uMove.py" under MBC. MBC, as you guessed it, stands for Motor Bridge
Cape.

Oh and you now need to install this:

    pip3 install smbus2

Change your ideas accordingly. You can see the changes in the source of the MotorBridge.py file.
And...

Change line 302 in smbus2.py to:

    filepath = "/dev/i2c-2".format(bus)

...

If you need assistance w/ set up or breakdown of the BBG for your Motor Bridge Cape, either
look to me or find another route. Godspeed!

    https://github.com/Seeed-Studio/MotorBridgeCapeforBBG_BBB/blob/master/BBG_MotorBridgeCape/MotorBridge.py

Seth

If you need to be assisted w/ any ideas belonging to this page, let me know. Outside of that, enjoy! I may be
adding new content soon. I will keep everyone updated.

` uname -r ` : 5.10.59-ti-r22

and...

` cat /etc/dogtag ` : BeagleBoard.org Debian Bullseye IoT Image 2021-10-02

Oh and...

    1. sudo apt install python3-venv
    2. python3 -m venv <your directory> # for instance, <your directory> can be Frost or Forth or whatever...
    3. cd <your directory> && source bin/activate
    4. pip3 install smbus2
    5. 'change line 302' in /lib/python3.7/site-packages/smbus2/smbus2.py
        a. from what it is in the current file to filepath = "/dev/i2c-2".format(bus)
    6. alter MotorBridge.py to use smbus2.py, i.e. look in the MotorBridge.py file for ideas...
    7. Type up awesome source!

