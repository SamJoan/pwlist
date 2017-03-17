SSH Brute Force Passwords
=========================

As many people do, I have a honeypot listening on port 22 which keeps a record
of unauthorised login attempts. I wrote some scripts that analyse these attempts
and generate password lists by various metrics, this repository holds the
scripts as well as the output password lists. 

Not all of them are good. My favs so far:

* [Solid ~50k with all the common good passwords.](passwords/by_client/dbca281176103cd834e0a63b62429d8f.txt)

Password groupings implemented so far:

* [By IP and SSH client name](passwords/by_ip_and_client/summary.txt)
* [By IP](passwords/by_ip/summary.txt)
* [By SSH client name](passwords/by_client/summary.txt)

