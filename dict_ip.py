from load_file_sfiting_data import load_file

def num_of_inquiries():
    dict_inquiries = {}
    for item in load_file():
        ip = item [1]
        if ip not in dict_inquiries:
            dict_inquiries[ip] = 1
        else:
            dict_inquiries[ip] += 1
    return dict_inquiries
def port_mapping():
    dict_mapping = {}
    for item in load_file():
        port = int (item[3])
        protocol = item[4]
        dict_mapping [port]  = protocol
    return dict_mapping

def type_suspicion():
    type_suspicion_dict = {}
    for item in load_file():
        sour_ip = item[1]
        port = item[3]
        size = int(item[5])
        time = item[0]
        hour = int(time.split(" ")[1].split(":")[0])
        if sour_ip not in type_suspicion_dict:
            type_suspicion_dict[sour_ip] = set()
        if not sour_ip.startswith('10.') and not sour_ip.startswith('192.168'):
            type_suspicion_dict[sour_ip].add("EXTERNAL_IP")
        if port in ('22', '3389', '23'):
            type_suspicion_dict[sour_ip].add("SENSITIVE_PORT")
        if size > 5000:
            type_suspicion_dict[sour_ip].add("LARGE_PACKET")
        if hour < 6:
            type_suspicion_dict[sour_ip].add("NIGHT_ACTIVITY")
    for sour_ip in type_suspicion_dict:
        type_suspicion_dict[sour_ip] = list(type_suspicion_dict[sour_ip])
    return type_suspicion_dict
def filter_suspicion(type_suspicion_dict):
    filter_suspicion_dict = {}
    for (key ,val) in type_suspicion_dict.items():
        if len(val) >= 3:
            filter_suspicion_dict[key] =  val
    return filter_suspicion_dict

