# installing Flask using  the package puppet-lint
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

#updating the werkzeug library
#package { 'werkzeug':
 # ensure   => '2.0.2',
  #provider => 'pip3',
#}
