
def Reading_Logs(file):
    file = open('log.txt', 'r')
    lst_lines = file.readlines()
    lst_output = []
    for log in lst_lines:
        lst_output.append(log.split())
    return lst_output

def parsing_Logs(lst_output):
    IPs = []
    URIs = []
    AccessMethods = []
    UserAgents = []
    i = 0
    for log in lst_output:
        IPs.append(log[0])
        AccessMethods.append(log[5][1:])
        URIs.append(log[6])
        UserAgents.append(' '.join(log[11:-1]))
        print(" IP: "+IPs[i]+" Access Method: "+AccessMethods[i]+" URI: "+URIs[i]+" UserAgents: "+UserAgents[i])
        i=i+1
    return IPs, URIs, AccessMethods, UserAgents

if __name__ == "__main__":
    lst_output = OpenLogs('log.txt')
    IPs ,URIs, AccessMethods , UserAgents = parseLogs(lst_output)

     #getting unique IPS & URLS
    UIPs = set(IPs)
    UURIs = set(URIs)
    UAccessMeth	ods = set(AccessMethods)