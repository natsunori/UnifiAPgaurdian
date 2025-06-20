#!/usr/bin/expect -f
log_user 0	;
exp_internal 0	; 	
spawn ssh -oHostKeyAlgorithms=+ssh-rsa {username}@192.168.1.95 "reboot"
expect "password:"
send "{enter password here}\r"
interact
