FROM centos:8

RUN yum update -y && yum clean all

# Apache install
RUN yum install -y httpd
RUN yum install -y python3

EXPOSE 80

CMD ["/usr/sbin/httpd","-D","FOREGROUND"]