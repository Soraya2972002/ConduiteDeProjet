from scapy.all import IP, ICMP, sr1

def send_icmp_packet(target_ip):
    # Create an ICMP Echo Request packet
    packet = IP(dst=target_ip) / ICMP()

    # Send the packet and receive a response
    response = sr1(packet, timeout=2, verbose=False)

    # Print the response details
    if response:
        response.show()
        return response
    else :
        return None

def detect_os(dest_ip):
    # Send ICMP Echo Request
    response = send_icmp_packet(target_ip)
    if response == None:
        print(f"No response received from {target_ip}")
        return

    # Receive ICMP Echo Reply
    ttl = response[IP].ttl

    # Analyze the TTL value to make an educated guess about the OS
    if ttl is not None:
        if ttl <= 64:
            print(f"The host {dest_ip} is likely running a Unix-like operating system.")
        elif ttl > 64:
            print(f"The host {dest_ip} is likely running a Windows operating system.")
        else:
            print(f"OS detection for {dest_ip} failed.")
    else:
        print(f"Failed to receive ICMP reply from {dest_ip}.")

if __name__ == "__main__":
    target_ip = "192.168.48.54"  # Replace with the target IP address

    detect_os(target_ip)