import socket
import time
import random
from scapy.all import traceroute

# 1. Ping Host (Latency Measurement)
def ping_host(host, port=80):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        start = time.time()
        s.connect((host, port))
        end = time.time()
        print(f"\n[✓] Ping to {host}:{port} = {(end - start) * 1000:.2f} ms")
        s.close()
    except Exception as e:
        print(f"\n[x] Failed to connect to {host}:{port} – {e}")

# 2. Simulate Packet Loss
def simulate_packet_loss(count=10, loss_rate=0.2):
    print("\nSimulating Packet Loss:")
    lost = 0
    for i in range(count):
        if random.random() < loss_rate:
            print(f"Packet {i+1}: ❌ Lost")
            lost += 1
        else:
            print(f"Packet {i+1}: ✅ Received")
    print(f"\nTotal Lost: {lost}/{count}")

# 3. Run Traceroute
def run_traceroute(host):
    print(f"\nTraceroute to {host}:")
    try:
        res, _ = traceroute([host], maxttl=20)
        res.show()
    except Exception as e:
        print(f"[x] Traceroute failed: {e}")

# 4. Main
if __name__ == "__main__":
    print("📡 Welcome to NetProbe – Simple TCP/IP Analyzer")
    target = input("Enter hostname or IP (e.g., google.com): ").strip()

    ping_host(target)
    simulate_packet_loss()
    run_traceroute(target)
