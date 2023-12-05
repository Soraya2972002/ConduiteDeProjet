import os
import platform
import subprocess
from tqdm import tqdm

def ping(host):
    if platform.system().lower() == "windows":
        response = subprocess.run(['ping', '-n', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    else:
        response = subprocess.run(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return response.stdout

def scan_network(ip_range):
    active_machines = []
    total_machines = 55
    with tqdm(total=total_machines, desc="Scanning network", unit="host") as pbar:
        for i in range(1, total_machines):
            target_ip = f"{ip_range}.{i}"
            if "1 received" in ping(target_ip):
                active_machines.append(target_ip)
            pbar.update(1)

    return active_machines

if __name__ == "__main__":
    network = "192.168.234"  # Change this to your network's IP range

    active_machines = scan_network(network)

    if active_machines:
        print("Active machines on the network:")
        for machine in active_machines:
            print(machine)
    else:
        print("No active machines found on the network.")