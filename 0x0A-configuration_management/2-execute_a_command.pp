# execute command from puppet
exec { 'killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin/'
}
