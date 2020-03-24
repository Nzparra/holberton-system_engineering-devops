# create a manifest that kills a process named killmenow.
exec { 'kill process':
    path     => ['/usr/bin', '/bin', '/usr/sbin', '/sbin'],
    command  => 'pkill killmenow',
    provider => 'shell' }
