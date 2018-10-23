import boto
from boto.ec2.regioninfo import RegionInfo
import time
from subprocess import call


import sys


class confidential:
    private_id = 'ee3c641bc6ae46e89398bb4f4258a5aa'
    private_key = '9740aae8f5fc452587d2ede0aef974e7'


def authentication(id, key):
    region = RegionInfo(name='melbourne', endpoint='nova.rc.nectar.org.au')
    ec2_connection = boto.connect_ec2(aws_access_key_id=id ,
                                aws_secret_access_key=key ,
                                is_secure=True,
                                region=region,
                                port=8773,
                                path='/services/Cloud',
                                validate_certs=False)
    print("AUTH SUCCESS")
    return ec2_connection


def createInstance(ec2_connection, image_id, type):

    reservation = ec2_connection.run_instances(
        image_id, key_name='ykl1', instance_type=type, security_groups=['new','ssh'], placement='melbourne-qh2')

    instance = reservation.instances[0]
    print("INSTANCE CREATED")
    return instance

# this method returns all the running instances details

def instance_status(ec2_connection):
    reservations = ec2_connection.get_all_instances()
    instances = []
    instances = [i for r in reservations for i in r.instances]
    for i in instances:
        print('Instance {} is {}'.format(i.id, i.state))


# this method return a list of running instances
# And check whether all the instances have been set up

def getInstances(ec2_connection):
    reservations = ec2_connection.get_all_instances()
    instances = []
    instances = [i for r in reservations for i in r.instances]
    for i in instances:
        print('Instance {} is {}'.format(i.id, i.state))

    return instances


def security_groups(ec2_connection):
    gp = ec2_connection.get_all_security_groups()
    print(gp)

# this function will generate a host file for the ansible playbook to read


def hostFile(IP):
    with open("host", "w+") as f:
        counter = 0
        for ip in IP:
            if counter == 0:
                f.write("[masterdbnode]\r\n")
                f.write("%s ansible_user=ubuntu\r\n" % ip)
                f.write("\r\n")
                f.write("[dbservers]\r\n")
                f.write("%s ansible_user=ubuntu\r\n" % ip)
                counter = counter + 1
            else:
                f.write("%s ansible_user=ubuntu\r\n" % ip)


def replaceIP(IP):

# replace IP address in setup1.sh
    string1 = "declare REPLACE_nodes=(115.146.85.214 115.146.84.193)"

    string2 = (
        "declare nodes=(%s %s)" % ( IP[0], IP[1]))

    string3 = "/Users/liuyongkang/Desktop/project/venv/shell/setup1.sh"

    call(["rpl", string1, string2, string3])

    print("REPLACED setup1.sh")

#  replace IP address in setup2.sh
    string1 = "declare REPLACE_nodes=(115.146.85.214 115.146.84.193)"

    string2 = (
        "declare nodes=(%s %s)" % (IP[0], IP[1]))

    string3 = "/Users/liuyongkang/Desktop/project/venv/shell/setup2.sh"

    call(["rpl", string1, string2, string3])

    print("REPLACED setup2.sh")


def wait(sec):
    while sec > 0:
        print(str(sec) + '     \r')
        sec -= 1
        time.sleep(1)
