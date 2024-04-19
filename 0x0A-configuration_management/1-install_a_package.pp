#!/usr/bin/pup
# install a specific version of Flask (2.1.0)
package { 'Werkzeu':
  ensure   => '2.0.0',
  provider => 'pip3',
}
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
