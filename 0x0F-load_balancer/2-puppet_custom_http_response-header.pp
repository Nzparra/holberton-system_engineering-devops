# creating a custom HTTP header response
exec {'e0':
  command  => 'sudo apt-get update -y',
  path     => ['/usr/bin', 's/bin', '/bin', '/usr/sbin'],
  provider => 'shell',
  return   => [0,1]}

exec { 'e1':
  require  => Exec['e0'],
  command  => 'sudo apt-get install nginx -y',
  path     => ['/usr/bin', 's/bin', '/bin', '/usr/sbin'],
  provider => 'shell',
  return   => [0,1]}

exec { 'e2':
  require  => Exec['e1'],
  command  => 'sudo sed -i "s/server_name _;/server_name _;\n\tadd_header X-Served-By \$hostname;/" /etc/nginx/sites-enabled/default',
  path     => ['/usr/bin', 's/bin', '/bin', '/usr/sbin'],
  provider => 'shell',
  return   => [0,1]}

exec { 'e3':
  require  => Exec['e2'],
  command  => 'sudo service nginx start',
  path     => ['/usr/bin', 's/bin', '/bin', '/usr/sbin'],
  provider => 'shell',
  return   => [0,1]}
