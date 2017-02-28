import subprocess

p = subprocess.Popen("arp-scan -l", stdout=subprocess.PIPE, shell=True)
(output,err) = p.communicate()
p_status = p.wait()

print(output.decode("utf-8"))


if "b8:27:eb:16:28:91" in output:
    print(True)
