# create a manifest that kills a process named killmenow.

exec { 'process kill killmenow':
  path     => ['/user/bin', '/bin', '/usr/sbin', '/sbin'],
  command  => 'pkill -f killmenow'}
