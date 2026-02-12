def load_file():
    path = r'C:\Users\esti7\network_traffic.log'
    with open(path, 'r') as f:
        return [line.strip().split(',') for line in f]
def output_ip_external():
    ip_list_external = []
    for item in load_file():
        src_ip = item[1]
        if not src_ip.startswith('10.' ) and not src_ip.startswith('192.168') :
            ip_list_external.append(src_ip)
    return ip_list_external
def port_sensitive():
    list_port_sensitive = []
    for item in load_file():
        port = item[3]
        if port == '22' or port == '3389' or port == '23':
            list_port_sensitive.append(item)
    return list_port_sensitive
def return_packet_large():
    list_packet_large = []
    for item in load_file():
        packet = item[5]
        if int(packet) > 5000:
            list_packet_large.append(item)
    return list_packet_large

def traffic_labeling():
    traffic_label = []
    for item in load_file():
        size = int(item[5])
        label = 'LARGE' if size > 5000 else 'NORMAL'
        traffic_label.append([label]+item)
    return traffic_labeling
