# Define the resource type for the SSH client configuration file
file_line { 'Turn off passwd auth':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
}

# Declare the identity file in global ssh configuration
file_line { 'Declare identity file':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile /home/vagrant/.ssh/school',
}