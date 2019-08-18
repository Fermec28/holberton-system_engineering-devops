# task with puppet
exec { 'update_packages':
  command  => 'sudo apt-get update',
  provider => shell,
}
-> package {'nginx':
  ensure => present,
}
-> file_line { 'change line header':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => "location / {
add_header X-Served-By ${hostname};",
  match  => '^\tlocation / {',
}
-> exec { 'restart nginx':
  command  => 'sudo service nginx restart',
  provider => shell,
}
