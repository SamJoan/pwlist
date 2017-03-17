SSH Brute Force Passwords
=========================

As many people do, I have a honeypot listening on port 22 which keeps a record
of unauthorised login attempts. I wrote some scripts that analyse these attempts
and generate password lists by various metrics, this repository holds the
scripts as well as the output password lists. 

Not all of them are good. My favs so far:

* [~20k lines](passwords/by_ip_and_client/4fd9c95b5289889270725ce9f9e7edbd.txt)
* [~6k lines](passwords/by_ip_and_client/a3c26961ba5d2cb395e56f8f2d190aa1.txt)

Password groupings implemented so far:

* [By IP and SSH Client name](passwords/by_ip_and_client/summary.txt)

