#!/bin/bash

set -e

# Check if the script is run as root
if [ "$EUID" -ne 0 ]; then
    echo "This script must be run as root. Please use sudo." >&2
    exit 1
fi

if [ -d /tmp/archlive ]; then
	sudo rm -rfv /tmp/archlive
fi

echo "########################################################"
echo "########################################################"
echo "########################################################"
echo "########################################################"

packages_file="/tmp/archlive/packages.x86_64"

# Packages to add to the archiso profile packages
packages=(
	gcc
	git
	pkgconfig
	python
	python-pip
	python-build
	python-setuptools
	python-wheel
	python-simple-term-menu
	python-pyparted
)

mkdir -p /tmp/archlive/airootfs/root/archinstall-git
cp -r . /tmp/archlive/airootfs/root/archinstall-git

cat <<- _EOF_ | tee /tmp/archlive/airootfs/root/.zprofile
	echo
	echo
	echo -e "\033[1;34mSetting keyboard layout to be-latin1 for azerty keyboard \033[0m"
	loadkeys be-latin1
	echo
	echo -e "\033[1;32mCreating alias: 'archinstall becomes archinstall --advanced' \033[0m"
	alias archinstall="archinstall --advanced"
	echo

	# Prompt to continue
	echo -e "\033[1;33mPress any key to continue...\033[0m"
	read input
	
	cd archinstall-git
	rm -rf dist

	python -m build --wheel --no-isolation
	pip install dist/archinstall*.whl --break-system-packages

	echo "This is an unofficial ISO for development and testing of archinstall. No support will be provided."
	echo "This ISO was built from Git SHA $GITHUB_SHA"
	echo "Type archinstall to launch the installer."
_EOF_

pacman --noconfirm -S archiso

cp -r /usr/share/archiso/configs/releng/* /tmp/archlive

sed -i /archinstall/d "$packages_file"

# Add packages to the archiso profile packages
for package in "${packages[@]}"; do
	echo "$package" >> "$packages_file"
done

cp pacman.conf /tmp/archlive

find /tmp/archlive
cd /tmp/archlive

mkarchiso -v -w work/ -o out/ ./
