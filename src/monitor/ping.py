import subprocess

def ping_host(host, timeout=5):
    result = subprocess.run(
        ["ping",
         "-c",
         "1",
         host
         ],
        capture_output=True,
        text=True
    )
    if result.returncode == 0:
        return True
    elif result.returncode == 1:
        return False
    return result
