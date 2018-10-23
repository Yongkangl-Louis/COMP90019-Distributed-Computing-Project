from prepare import *


connect_ec2 = authentication(confidential.private_id, confidential.private_key)


print("Create instances")
numberofInstance = 2
UBUNTU_16_04_LTS = 'ami-190a1773'

for i in range(0, numberofInstance):
    instance = createInstance(connect_ec2, UBUNTU_16_04_LTS, 'm1.medium')


all = connect_ec2.get_all_reservations()
for id, reser in enumerate(all):
    print('{}\t{}\t{}'.format(id, reser.id, reser.instances))

instances = getInstances(connect_ec2)

# check the status of each instance
for i in instances:
    count = 0
    i.update()
    if(i.state == 'running'):
        continue
    while (i.state != 'running' and count <= 30):
        i.update()
        print('Instance {} is {}'.format(i.id, i.state))
        time.sleep(5)
        count = count+1


print("ALL instances are ready \n")
print('\n------ IP addresses ------\n')

IP = []
for i in instances:
    print(i.id + ':' + i.private_ip_address)
    IP.append(i.private_ip_address)

hostFile(IP)
print("Host IP file write success")

# zip the package
call(["zip", "-r", "zip.zip", "zip/"])

# replace IP address in shell script
print("/n")
replaceIP(IP)
print("Process in replacing IP address in shell")
print("/n")

wait(60)


# run the ansible-playbook
call(["ansible-playbook", "install.yml",
      "--private-key=cloud.pem", "-i", "host"])

print("playbook has ran")
