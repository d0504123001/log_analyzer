def list_hours():
    path =  r'C:\Users\esti7\network_traffic.log'
    with open(path, 'r') as f:
        hours =list( map(lambda line:int(line.strip().split(" ")[1].split(':')[0]),f))
    return hours
