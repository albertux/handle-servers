#!/bin/bash
for region in eu-west-1 sa-east-1 us-east-1 ap-northeast-1  us-west-2 us-west-1 us-west-1 ap-southeast-1  ap-southeast-2
do 
	ec2-describe-instances --region $region | cut -f 4 | grep ec2 >> aws_instances.txt 
done
