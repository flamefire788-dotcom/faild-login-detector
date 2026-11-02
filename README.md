
# Failed Login Detector

A Python script that reads an SSH-style log, counts failed and
successful logins per IP, and flags suspicious ones.

## What it detects
- ALERT: an IP with many failed logins (possible brute force)
- CRITICAL: an IP that failed many times and then logged in successfully

## What I learned
- Reading and filtering log files
- Using dictionaries as counters
- Why repeated failed logins on port 22 (SSH) suggest brute force
- Debugging a logic bug (IP was only set on failed lines)

## How to run
python3 count.py

## Note
Uses a fake log with example IPs. No real systems involved.
