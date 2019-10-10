#change limit
exec { 'change hard':
    command  => "sed -i 's/holberton hard nofile 5/holberton hard nofile 1001/'\
    	     	 /etc/security/limits.conf",
    provider => shell
}
-> exec { 'soft hard':
    command  => "sed -i 's/holberton soft nofile 4/holberton soft nofile 1001/'\
    	     	 /etc/security/limits.conf",
    provider => shell
}
-> exec { 'restart':
  command  => 'sysctl -p',
  provider => shell
}