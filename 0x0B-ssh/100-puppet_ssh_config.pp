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
    ensure => 'file',
    owner => 'vagrant',
    group => 'vagrant',
    mode => '0600',
    content   => "

-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAACmFlczI1Ni1jdHIAAAAGYmNyeXB0AAAAGAAAABCnxyUkIh
f49NSy5j1dffXoAAAAEAAAAAEAAAIXAAAAB3NzaC1yc2EAAAADAQABAAACAQDL7XIY7cTZ
q4dHnv9TTJ0Zwzzm3plyt2OD4PFbpnSgbvPL4a7CnWmcCMO8i2YH1byso1VXso93fycCNn
I6IyF54p6GMLavw0xX6lG0E26aYXfmAZOh4PdsflRXXbmRMNdkbDEBSgHa/6XnU7lTqshx
Qq0Am5kHL41IjSeohg5a0ZGlPf0TmVQyGDqLtiat1gZAtzw1yknHUSIKzZ7IspvYaT+6Na
eMqpfellsnnaGAvlldeiqd/AWqwo1XMNcqPaZw1gTjV4GElPtjZjdWfZvAI8csrhmI9OVC
0OO4UgQz1cEEGhHbjIYZdzb3tBfLI0ODxuCSuxfbY3wtLTB0OsuauuiGZ5rQdHnhI+KEzL
+y5qTLq6K03lCBg74nob/o5tL3NH4Cfo0q+ivMiwTmSa75L2lUkXAK9X0lw1yYVuCVF3B+
/jYZG18EcfmFghAANJZZm0wvMaZFNwL+wWJmsR5XYGV1/r4Xx/oZYWnkR1qaqPaLbF3SHK
Wh23JPjEQSfxO3V9rFe4BF8VSGsjFz0p4Bp0fN0oh46FEFUfNyPpOU9oWWWE
kP2bN6GE6v/gV2IzFgBATBKEL97K+hpEGAfcikV7Th+MjXQLRPW1DCLv/DonYAbNqwm1NV
izfcL+djH3tKiAHpbuysC5F/fY+gwV82YVHmH55znCM0LYfKfVAjwiw8Lynqzi4B1DeBgN
r/kTY4EhkWOzfsdYGGEco/lqfdE0b4cyjUqpBb9wAZwINy0Z2dSvF93ewYFOtFgIUDKosm
FgKz1RWUKWnSC0YTs583XVWMM1eHMcPR+6Ktvwgf56flAh1ypOCAW/bABF9VeUuNcu+NaQ
BsqIVmDXFzO+5to9FTGnAV5SuKcxkY8BltkTNCLShLZyetEHw71HI9Vv/oIquDgnAIoDW8
XwnBMYPW3PpLM1B4SIRsG59CHnCKaopTo3vyRht27aTdST2H8E/BzpUyicESdIW/H4HQ0c
n7VocUPYNmOlXbgvfFX/8qmzpgj80euERbGTp6hlvVhNUvLp4ZEzWU+blqjb4LXCdamqZO
xDMpeCaj/nf7HiPJ2h/RO355rrxjBwXxezi+59VkGKBSqb5BCZsMW8L9ZzYsgmXsG0A+/0
2xy7FGz9j37i1V1PNIAX1JdTRqBc5chNV6LGrAkzPqkrox/IJGYnTwoSaL5N5qMztpYbyy
zF
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
-----END OPENSSH PRIVATE KEY7----	
	 IdentityFile ~/.ssh/school
	
	",
}
