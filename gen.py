from os import mkdir
from os.path import isfile
from pwlistgen.common import c, tidy_mod
from pwlistgen.modules import *
import sqlite3

OUT_PATH = "passwords/"
DB_PATH = "/tmp/cowrie.db"
ENABLED_MODS = [
    by_client,
    by_ip,
    by_ip_and_client,
]

def get_db() -> sqlite3.Connection:
    if not isfile(DB_PATH):
        print("[+] DB doesn't exist, getting.")
        c("scp honeypot:/home/cowrie/cowrie/cowrie.db /tmp/")
    else:
        print("[+] using %s" % DB_PATH)

    return sqlite3.connect(DB_PATH)

if __name__ == "__main__":
    conn = get_db()
    for mod in ENABLED_MODS:
        mod_name = mod.__name__
        mod_path = OUT_PATH + mod_name + "/"

        print("[+] Running module '%s' -> %s" % (tidy_mod(mod_name), mod_path))
        try:
            mkdir(mod_path)
        except OSError:
            pass

        mod(conn, mod_path)

    print("[+] done")

