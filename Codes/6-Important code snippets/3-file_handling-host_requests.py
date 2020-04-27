def hostsInfo(filename):
    hosts_info = []
    hosts = []
    unique_hosts = set()

    #Reading from file
    file_read = open(filename, mode = 'r')
    lines = file_read.readlines()

    #Processing data
    for line in lines:
        hosts_info.append(line)

    for host in hosts_info:
        h = host.split(" ")
        hosts.append(h[0])
        unique_hosts.add(h[0])
        
        
    #Writing to file
        file_write = open("records_"+filename, mode = 'w')

        for u in sorted(unique_hosts):
            request_count = str(hosts.count(u))
            file_write.write(u + " " + request_count)
            file_write.write("\n")

    
        
    



if __name__ == "__main__":
    hostsInfo("hostsinfo.txt")
