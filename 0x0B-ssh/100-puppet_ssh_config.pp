# Define the resource type for the SSH client configuration file
  file { '/home/vagrant/.ssh/config':
    ensure => 'file',
    owner => 'vagrant',
    group => 'vagrant',
    mode => '0600',
    content => "
	Host server1 
    	    HostName 174.129.54.166
            Port 22
            IdentityFile  ~/.ssh/school
            PasswordAuthentication no
     ",
}

# Define the resource type for the private key file
  file { '/home/vagrant/.ssh/school':
    ensure => 'present',
    owner => 'vagrant',
    group => 'vagrant',
    mode => '0600',
}
