FROM centos:7

RUN yum update -y && yum clean all
RUN yum -y install epel-release

# Node.js install
RUN yum install -y nodejs

# Nginx install
RUN yum install -y nginx

EXPOSE 80

# Nginx start
CMD ["nginx", "-g", "daemon off;"]