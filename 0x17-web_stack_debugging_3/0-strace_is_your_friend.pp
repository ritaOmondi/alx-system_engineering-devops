package { 'apache2':
  ensure => installed,
}

file { '/etc/apache2/sites-available/default.conf':
  ensure  => file,
  source  => 'puppet:///modules/apache/default.conf',
  require => Package['apache2'],
  notify  => Service['apache2'],
}

service { 'apache2':
  ensure     => running,
  enable     => true,
  hasstatus  => true,
  hasrestart => true,
  require    => File['/etc/apache2/sites-available/default.conf'],
}
