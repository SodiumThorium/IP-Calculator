#Pseudo IP
ipPseudoAddress = input("Pseudo IP first part ")
ipPseudoAddress1 = input("Pseudo IP second part ")
ipPseudoAddress2 = input("Pseudo IP third part ")
ipPseudoAddress3 = input("Pseudo IP fourth part ")

calculate = int(ipPseudoAddress3) + int(int(0o1))
calculate1 = int(calculate) + int(int(0o1))
ourRouter1 = str(ipPseudoAddress) + "." + str(ipPseudoAddress1) + "." + str(ipPseudoAddress2) + "." + str(calculate)
ourRouter2 = str(ipPseudoAddress) + "." + str(ipPseudoAddress1) + "." + str(ipPseudoAddress2) + "." + str(calculate1)
print("")
print("Ipaddress for our main router is AKA WAN Gateway " + str(ourRouter1))
print("Ipaddress for management router is AKA WAN " + str(ourRouter2) + " with gateway of " + str(ourRouter1))
print("")

# Work out the public IP
ipAddress = input("IP first part ")
ipAddress1 = input("IP second part ")
ipAddress2 = input("IP third part ")
ipAddress3 = input("IP fourth part ")

subNet = input("Subnet ")
subNet1 = input("Subnet ")
subNet2 = input("Subnet ")
subNet3 = input("Subnet ")

cCalculate = int(ipAddress3) + int(int(0o1))
cCalculate1 = int(cCalculate) + int(int(0o1))
oOurRouter1 = str(ipAddress) + "." + str(ipAddress1) + "." + str(ipAddress2) + "." + str(cCalculate)
oOurRouter2 = str(ipAddress) + "." + str(ipAddress1) + "." + str(ipAddress2) + "." + str(cCalculate1)


test = str(ipPseudoAddress) + "." + str(ipPseudoAddress1) + "." + str(ipPseudoAddress2) + "." + (str(calculate1))
test2 = str(ipAddress) + "." + str(ipAddress1) + "." + str(ipAddress2) + "." + (str(ipAddress3))

print("")
print("Ipaddress for management router is aka LAN " + str(oOurRouter1))
print("Ipaddress for Customer router is aka DHCP " + str(oOurRouter2) + " with gateway of " + str(oOurRouter1))
print("")
print("ip route: " + test2 + " " + subNet + "." + subNet1 + "." + subNet2 + "." + subNet3 + " " +  test)

input("hit any key when done")