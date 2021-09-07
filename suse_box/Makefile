# Install dependencies in openSUSE
#
# FIRST: install 'make': sudo zypper install make
#
setup:
	sudo zypper -n update

git: setup
	sudo zypper -n install git

# https://github.com/pyenv/pyenv/wiki#suggested-build-environment
pyenv-bin-dependencies: setup
	sudo zypper -n install gcc automake bzip2 libbz2-devel xz xz-devel openssl-devel ncurses-devel \
	readline-devel zlib-devel tk-devel libffi-devel sqlite3-devel

k3s: setup
# https://kubernetes.io/docs/tutorials/clusters/apparmor/
	sudo zypper -n install apparmor-parser
	curl -sfL https://get.k3s.io | sh -s - --write-kubeconfig-mode 640
	# Set "root" group as vagrant's primary group, 
	# then logout/login again for the group change to take effect
	sudo usermod -g root vagrant

# https://github.com/pyenv/pyenv-installer
install: git pyenv-bin-dependencies k3s
	curl https://pyenv.run | bash
	echo "pyenv: Restart your shell so the path changes take effect: exec ${SHELL}"
	cat ./pyenv-activation >> ~/.profile



