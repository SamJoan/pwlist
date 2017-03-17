from .common import *
from sqlite3 import Connection

def attempts_sorted_get(conn: Connection, group_by: str) -> list:
    """
    @return (ip, ssh_client_version, nb_auth_attempts)
    """

    query = """select ip, c.version, count(distinct a.password) as nb_auth from auth
    as a left join sessions as s on a.session = s.id left join clients as c on
    s.client = c.id group by %s having nb_auth > 1000 order by nb_auth desc""" % (group_by)
    
    attempts_sorted = list(conn.execute(query))

    return attempts_sorted

def sess_filter_get(conn: Connection, query: str, params: tuple) -> str:
    sessions = conn.execute(query, params)

    session_ids = [session[0] for session in sessions]
    sess_filter = "(\"" + "\",\"".join(session_ids) + "\")"

    return sess_filter

def passwords_write(conn: Connection, out_path: str, hsh: str, where: str, query_params: tuple) -> None:
    sess_filter = sess_filter_get(conn, """select s.id from sessions as s left
            join clients as c on s.client = c.id where """ + where, query_params)

    passwords = pw_uniq([password[0] for password in conn.execute("select password from \
        auth where session in " + sess_filter)])

    pw_write(out_path + hsh + ".txt", passwords)

def by_ip_and_client(conn : Connection, out_path : str):
    sessions = attempts_sorted_get(conn, "c.id, ip")
    for ip, client_name, _ in sessions:
        try:
            file_uid = ip + client_name
        except TypeError:
            file_uid = ip

        hsh = md5(file_uid)

        passwords_write(conn, out_path, hsh, "ip = ? and c.version = ?", (ip,
            client_name))

    pw_dir_summary(out_path)

def by_client(conn: Connection, out_path: str) -> None:
    sessions = attempts_sorted_get(conn, "c.id")
    for _, client_name, _ in sessions:
        if client_name:
            hsh = md5(client_name)
        else:
            continue

        passwords_write(conn, out_path, hsh, "c.version = ?", (client_name,) )

    pw_dir_summary(out_path)
        
def by_ip(conn: Connection, out_path: str) -> None:
    sessions = attempts_sorted_get(conn, "ip")
    for ip, _, _ in sessions:
        hsh = md5(ip)
        passwords_write(conn, out_path, hsh, "ip = ?", (ip,) )

    pw_dir_summary(out_path)
