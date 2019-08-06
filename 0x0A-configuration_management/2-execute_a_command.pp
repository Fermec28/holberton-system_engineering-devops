# execute command from puppet
exec { 'killmenow':
  command => '/usr/bin/pkill killmenow'
}
