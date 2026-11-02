counts = {}
success = {}
with open("auth.log") as f:
    for line in f:
        ip = line.split()[-1]
        if "Failed" in line:
            counts[ip] = counts.get(ip,0)+1
        elif "Successful" in line:
            success[ip] = success.get(ip,0)+1
THRESHOLD = 3
for ip, count in counts.items():
    if count >= THREESHOLD:
        print("ALERT:", ip, count, "failed logins (possible brute force)")
    else:
        print("ok:", ip, count, "failed logins")
print("Failed:" ,counts)          
print("Successful:", success)
