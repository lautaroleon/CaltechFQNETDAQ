# TimingBone
OTSDAQ Custom Plugin

This is a simple plugin for the OTSDAQ to be able to run any command line command on "START" and "STOP".

THIS_IP : set it to the ip address of the computer that this code is running on.
COMMUNICATION_PORT: set it to the port that you configured for this module in OTSDAQ

On receiving the "START" command, this plugin will execute on the command line the string given by the variable "command".

On receiving the "STOP" command, this plugin will write the word "stop" to the file located at /tmp/RunFile.txt. The executable that is called by the "command" string must be able to check this file and stop data acquisition when it reads the word "stop" in that file. 

On receiving the "CONFIGURE" command, this plugin currently doesn't do anything. But it can be change to execute a different command line script if desired.

