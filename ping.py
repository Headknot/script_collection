import subprocess

def ping_test(hostname, pingstatus=""):
    """Sends one ping message and returns exit code"""
    cmd = ['ping', '-n', '1', hostname]

    response = subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE).communicate()[0]
    response = response.decode("utf-8")

    if "Ping request could not find host" in response:
        pingstatus = "Down"
    else:
        pingstatus = "Up"
    return pingstatus

print(ping_test("8.8.8.8"))