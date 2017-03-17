from common import *

def by_ip_and_client(conn, out_path):
    query = """select ip, c.version, count(distinct a.id) as nb_auth from auth
    as a left join sessions as s on a.session = s.id left join clients as c on
    s.client = c.id group by c.id order by nb_auth desc"""

    for ip, client_name, _ in conn.execute(query):
        try:
            file_uid = ip + client_name
        except TypeError:
            file_uid = ip

        hsh = md5(file_uid)

        sessions = conn.execute("""select s.id from sessions as s left join clients
        as c on s.client = c.id where ip = ? and c.version = ?""", (ip, client_name))

        sessions = [session[0] for session in sessions]
        sess_filter = "(\"" + "\",\"".join(sessions) + "\")"

        passwords = pw_uniq([password[0] for password in conn.execute("select password from \
            auth where session in " + sess_filter)])

        pw_write(out_path + hsh + ".txt", passwords)

    pw_dir_summary(out_path)

