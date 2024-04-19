#!/usr/bin/pup
# install a specific version of Flask (2.1.0)
package { 'werkzeug':
  ensure   => '2.0.2',
  provider => 'pip3',
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
