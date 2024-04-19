# installs Flask version 2.1.0
exec { 'Flask':
  command => '/usr/bin/pip3 -y install Flask -v 2.1.0',
}