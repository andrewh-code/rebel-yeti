#!/usr/bin/shell 

# =====================
# ethereum setup
#
# =====================

# constants and global variables
PYTHON2_DIR=/usr/bin/python2
PYTHON3_DIR=/usr/bin/python3
PYTHON_PIP=/usr/bin/pip

# update Linux environment

# update 
apt-get -y update
if [ $? -ne 0 ]
then
    echo "env_setup.sh: Error: ${?} - Unable to update Linux environment"
    exit 1
fi

# upgrade
#apt-get -y upgrade
if [ $? -ne 0 ]
then
    echo "env_setup.sh: Error: ${?} - Unable to upgrade Linux environment"
    exit 1
fi

# install software properties
apt-get -y install software-properties-common
if [ $? -ne 0 ]
then
    echo "env_setup.sh: Error: ${?} - Unable to install software-properties-common"
    exit 1
fi

# check if python is installed
if [ ! -d "$PYTHON2_DIR" ]
then
    echo "env_setup.sh: Python 2.x not installed, installing Python"
    apt-get -y install python
    if [ $? -ne 0 ]
    then
        echo "env_setup.sh: Error: ${?} - Unable to install python"
    fi
fi

# check if python pip is installed (check for python3 pip)
if [ ! -d "$PYTHON_PIP" ]
then
    apt-get -y install python-pip 
    if [ $? -ne 0 ]
    then
        echo "env_setup.sh: Error: ${?} - Unable to install pip"
    fi
else
    # if pip is installed, upgrade it
    pip install --upgrade pip
    if [ $? -ne 0 ]
    then
	echo "env_setup.sh: Error: ${?} - Unable to upgrade pip"
    fi
fi

# install the python dev tools and build-essentials
apt-get -y install python-dev
if [ $? -ne 0 ]
then
    echo "env_setup.sh: Error: ${?} - Unable to install python-dev"
    exit 1
fi

apt-get -y install build-essential
if [ $? -ne 0 ]
then
    echo "env_setup.sh: Error: ${?} - Unable to install build-essentials"
    exit 1
fi


# install ethereum
# ========================================
add-apt-repository -y ppa:ethereum/ethereum
if [ $? -ne 0 ]
then
    echo "env_setup.sh: Error: ${?} - Unable to install ethereum reppository"
    exit 1
fi

add-apt-repository -y ppa:ethereum/ethereum-dev
if [ $? -ne 0 ]
then
    echo "env_setup.sh: Error: ${?} - Unable to install ethereum-dev repository"
    exit 1
fi

# run update to make sure dependencies are correct after adding eth repos or else install etheruem command won't work
apt-get update
if [ $? -ne 0 ]
then
    echo "env_setup.sh: Error: ${?} - Unable to update the machine for ethereum"
    exit 1
fi

# install ethereum
apt-get -y install ethereum
if [ $? -ne 0 ]
then
    echo "env_setup.sh: Error: ${?} - Unable to install ethereum"
    exit 1
fi

# install solidity compiler
apt-get -y install solc
if [ $? -ne 0 ]
then
    echo "env_setup.sh: Error: ${?} - Unable to install build-essentials"
    exit 1
fi


# install nodejs
# ==============================

# make sure to have at least nodejs version 6.0 installed or else testrpc won't install properly
# option to set nodejs 7?
curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
if [ $? -ne 0 ]
then
    echo "env_setup.sh: Error: ${?} - Unable to curl nodejs v6.0s"
    exit 1
fi

apt-get install nodejs
if [ $? -ne 0 ]
then
    echo "env_setup.sh: Error: ${?} - Unable to install nodejs"
    exit 1
fi

# install ethereum testrpc (good luck, so many problems with this)
npm install -g ethereumjs-testrpc
# provide a funky if statement here

# install truffle
npm install -g truffle
if [ $? -ne 0 ]
then
    echo "env_setup.sh: Error: ${?} - Unable to install truffle"
    exit 1
fi

