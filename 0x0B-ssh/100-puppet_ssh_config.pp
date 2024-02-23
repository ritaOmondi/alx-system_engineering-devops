# Puppet manifest to configure SSH client

file { '/root/.ssh/config':
  ensure  => present,
  mode    => '0600',
  content => "\
Host your_server_ip_here
    IdentityFile ~/.ssh/school
    PasswordAuthentication no\n",
}

