import socket
from tqdm import tqdm

def check_port_status(host, port):
  try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.settimeout(2)
      s.connect((host,port))
      return "open"
  except ConnectionRefusedError:
    return 'closed'
  except socket.timeout:
    return 'filtered'

def scan_ports(host):
  start_port = 79
  end_port = 8080
  open_ports = []
  print(f"scanning ports on {host} from {start_port} to {end_port} ...")
  with tqdm(total=end_port-start_port, desc="Scanning ports", unit="port") as pbar:
    for port in range(start_port, end_port+1):
      status = check_port_status(host, port)
      if status == 'open' or status == "filtered":
        open_ports.append([port,status])
      pbar.update(1)
  return open_ports

if __name__ == "__main__":
  host = "192.168.234.6"
  open_ports = scan_ports(host)
  if open_ports:
    print("Open ports on the machine:")
    for port,status in open_ports:
      print(f"Port {port} : {status}")
  else:
    print("No open ports found on this machine.")