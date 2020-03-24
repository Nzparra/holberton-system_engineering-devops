# create a manifest that kills a process named killmenow.

exec { 'process_kill':
    path    => ['/user/bin', '/bin', '/usr/sbin', '/sbin'],
    command => 'pkill killmenow'}
