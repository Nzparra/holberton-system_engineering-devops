# Install Nginx

exec {'install':
  provider => shell,
  command  => 'apt-get update ; apt-get install nginx -y ; service nginx start',
}
