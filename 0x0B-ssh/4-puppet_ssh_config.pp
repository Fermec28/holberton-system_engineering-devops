# modify ssh config with puppet
file { '/etc/ssh/ssh_config':
  ensure => present,
}
file_line { 'change auth type':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
  match  => '^PasswordAuthentication.*$',
}
file_line { 'set identity file':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/holberton',
  match  => '^IdentityFile.$',
}
