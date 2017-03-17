from subprocess import check_output
import hashlib

def c(cmd):
    out = check_output(cmd, shell=True)
    return out

def tidy_mod(mod_name):
    name = mod_name.replace('_', ' ')
    return name

def md5(input):
    m = hashlib.md5()
    m.update(input)

    return m.hexdigest()

def pw_uniq(passwords):
    seen = {}
    new_pw = []
    for pw in passwords:
        if not pw in seen:
            seen[pw] = True
        else:
            continue

        new_pw.append(pw)

    return new_pw

def pw_write(filename, passwords):
    print("[+] Writing %s" % filename)
    with open(filename, 'w') as fh:
        for pw in passwords:
            fh.write(pw + "\n")

def pw_dir_summary(dir_path):
    wc_out = c("wc -l %s* | head -n -1 | sort -rn | grep -v summary.txt" % dir_path)
    with open(dir_path + "summary.txt", 'w') as fh:
        fh.write(wc_out)
