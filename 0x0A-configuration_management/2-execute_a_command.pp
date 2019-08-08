# execute command from puppet
exec { 'killmenow':
  command  => 'pkill killmenow',
  provider => shell,
}
