#set up client SSH configuration file so that you can connect to a server without typing a password
file_line {  'passw_no_autentication':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}
file_line {  'passw_direction':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/holberton',
}
