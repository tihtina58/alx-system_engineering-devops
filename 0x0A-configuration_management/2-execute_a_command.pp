# create a manifest that kills a process

exec { 'kill killmenow process':
   command   => 'pkill killmenow',
   provider  => 'shell',
}