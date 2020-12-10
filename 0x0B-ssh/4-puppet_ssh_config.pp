#set up client SSH configuration file so that you can connect to a server without typing a password
file_line {  'adding_no_passw_config':
  path      => '/etc/ssh/ssh_config',
  ensure    => true,
  line      => '
  PasswordAuthentication no\n
  IdentityFile ~/.ssh/holberton',
}
