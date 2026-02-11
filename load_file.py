def load_file():
    path = r'C:\Users\esti7\network_traffic.log'
    with open(path, 'r') as f:
        return [line.strip().split(',') for line in f]
g