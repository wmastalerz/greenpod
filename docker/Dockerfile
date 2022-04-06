FROM    centos:latest
# Fix Error: Failed to download metadata for repo 'appstream': Cannot prepare internal mirrorlist: No URLs in mirrorlist
RUN     cd /etc/yum.repos.d/
RUN     sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
RUN     sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*
RUN     yum update -y
RUN     yum install httpd -y
CMD     /usr/sbin/httpd -DFOREGROUND
EXPOSE  80
RUN     yum install python3 -y
RUN     cd /usr/bin && ln -s python3 python
RUN     pip3 install setuptools_rust
RUN     pip3 install --upgrade pip
RUN     pip3 install ansible
RUN     pip3 install kubernetes
RUN     mkdir /etc/ansible/
RUN     touch /inventory.txt
RUN     yum install net-tools -y
RUN     yum install vim -y
RUN     dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm -y
RUN     yum install sshpass -y
RUN     yum install openssh-clients -y
COPY    ./ansible.cfg   /etc/ansible/ansible.cfg
