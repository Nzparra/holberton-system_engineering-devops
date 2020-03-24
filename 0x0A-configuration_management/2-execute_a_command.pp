# create a manifest that kills a process named killmenow.

exec { 'process kill killmenow':
  path    => '/user/bin',
  command => 'pkill -f killmenow'}
