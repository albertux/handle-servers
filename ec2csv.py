#!/usr/bin/env python

from boto.ec2 import EC2Connection

csv_file = open('instances.csv','w+')

csv_file.write("public_dns_name,instance_id,ip,state")
csv_file.flush()


def process_instance_list(connection):
    map(build_instance_list,connection.get_all_instances())

def build_instance_list(reservation):
    map(write_instances,reservation.instances)

def write_instances(instance):
        if instance.public_dns_name is '':
        name = "None"
    else:
        name = instance.public_dns_name
    csv_file.write("%s,%s,%s,%s\n"%(name,instance.id,instance.ip_address,instance.state))
    csv_file.flush()

if __name__=="__main__":
    connection = EC2Connection()
    process_instance_list(connection)
    csv_file.close()

