# creates a manifest that kills a process named killmenow.

exec { 'kill killmenow process':
  command  => 'pkill killmenow',
  provider => 'shell',
}