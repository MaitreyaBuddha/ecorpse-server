# For the good of all beings.

SHELL:=/bin/bash

export MONGO_USERNAME:=userroot
export MONGO_PASSWORD:=rootpassword
service:
	docker-compose up --build ecorpse

shell:
	docker-compose --build run ecorpse sh

TAG:=kellyjokes/ecorpse:latest
restart:
	docker-compose restart ecorpse

testPost:
	curl -v \
	--header "Content-Type: application/json" \
	--data '{"username":"xyz","password":"xyz"}' \
	localhost:5000/submit

register:
	curl -v \
	localhost:5000/register?name=kelly\&email=k@j.c

test:
	docker-compose run ecorpse python3 test.py

testGetFoo:
	curl http://ec2-3-101-36-252.us-west-1.compute.amazonaws.com:5000/static/foo.txt

ssh:
	ssh -i /Users/kelly/Downloads/ecorpsessh.pem ubuntu@ec2-3-101-36-252.us-west-1.compute.amazonaws.com

upload:
	zip -r ../ecorpse .
	scp -i /Users/kelly/Downloads/ecorpsessh.pem ../ecorpse.zip ubuntu@ec2-3-101-36-252.us-west-1.compute.amazonaws.com:projects/ecorpse
	ssh -i /Users/kelly/Downloads/ecorpsessh.pem ubuntu@ec2-3-101-36-252.us-west-1.compute.amazonaws.com
