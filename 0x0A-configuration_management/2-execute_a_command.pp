exec { 'process kill killmenow':
  path    => '/user/bin',
  command => 'pkill -f killmenow'}
