# NetProbe
# 🛰️ NetProbe – TCP/IP Analyzer Tool

NetProbe is a lightweight Python-based command-line tool to analyze basic TCP/IP networking behavior. It combines latency checks, packet loss simulation, and traceroute functionality into a single script.

## 🚀 Features

- ✅ **Latency Measurement** – Ping any host and measure response time (TCP handshake based).
- ✅ **Packet Loss Simulation** – Simulates how often packets are dropped during transmission.
- ✅ **Traceroute** – Visualize the route taken by packets to reach the destination.
- ⚙️ Built using `socket` and `scapy` libraries.

---


```bash
$ python3 netprobe.py
📡 Welcome to NetProbe – Simple TCP/IP Analyzer
Enter hostname or IP (e.g., google.com): google.com

[✓] Ping to google.com:80 = 48.23 ms

Simulating Packet Loss:
Packet 1: ✅ Received
Packet 2: ❌ Lost
...
Total Lost: 3/10

Traceroute to google.com:
1  192.168.1.1
2  10.0.0.1
...
