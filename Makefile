#
# Makefile to operate the vagrant box
#

# setup:
# 	vagrant init ubuntu/bionic64

lint:
	vagrant validate
	
start:
	vagrant up

sync-files:
	vagrant rsync-auto

ssh:
	vagrant ssh

stop:
	vagrant halt

clean:
	# vagrant destroy
	@echo "cleanup did not remove the \'box\' from your computer!"
	vagrant box list
	@echo "To remove the box run: vagrant box remove [box_name]"
