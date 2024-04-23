# Puppet manifest to install and configure Nginx on a web server

# Update package lists to get the latest versions of packages
exec { 'apt-update':
  command => '/usr/bin/apt-get update',
  path    => '/usr/bin',
}

# Install Nginx package if it's not already installed
package { 'nginx':
  ensure => installed,
  require => Exec['apt-update'],
}

# Allow incoming HTTP traffic through the firewall for Nginx
firewall { 'Nginx HTTP':
  proto  => 'tcp',
  dport  => 80,
  action => 'accept',
}

# Write "Hello World!" to the default HTML file served by Nginx
file { '/var/www/html/index.nginx-debian.html':
  content => 'Hello World!',
}

# Configure Nginx to redirect /redirect_me to another page
file_line { 'nginx-redirect':
  path  => '/etc/nginx/sites-available/default',
  line  => '    location /redirect_me {',
  match => 'server_name _;',
  after => true,
}

file_line { 'nginx-redirect-return':
  path  => '/etc/nginx/sites-available/default',
  line  => '        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;',
  match => 'location /redirect_me {',
  after => true,
}

# Create a custom 404 page with the string "Ceci n'est pas une page"
file { '/var/www/html/error_404.html':
  content => "Ceci n'est pas une page",
}

# Configure Nginx to use the custom 404 page
file_line { 'nginx-custom-404':
  path  => '/etc/nginx/sites-available/default',
  line  => '          error_page 404 /error_404.html;',
  match => 'server_name _;',
  after => true,
}

file_line { 'nginx-custom-404-location':
  path  => '/etc/nginx/sites-available/default',
  line  => '          location = /error_404.html {',
  match => 'error_page 404 /error_404.html;',
  after => true,
}

# Start the Nginx service
service { 'nginx':
  ensure => running,
  enable => true,
}
