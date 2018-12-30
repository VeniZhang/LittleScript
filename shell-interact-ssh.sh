#!/usr/bin/expect
#passwd=$(cat /passwd)
#echo $passwd
set ip [lindex $argv 0]
set passwd [lindex $argv 1]
#set passwd zdq
#set ip root@media
puts $ip
puts $passwd
spawn ssh-keygen
expect {
    "*id_rsa*" { send "\r"; exp_continue }
    "*passphrase*" { send "\r"; exp_continue }
    #"*again*" { send "\r" }
    "*Overwrite*" { send "n\r";exp_continue}
}
spawn ssh-copy-id $ip
expect {
    "*connecting*" {send "yes\r"; exp_continue}
    "*password*" {send "${passwd}\r"}
}
interact

#  设置  no-passwd login
