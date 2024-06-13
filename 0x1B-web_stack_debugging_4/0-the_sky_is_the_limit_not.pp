# Increases the amount of traffic an Nginx server can handle.

# Increase the ULIMIT of the default file
exec { 'increase-nginx-ulimit':
  command => 'sed -i "s/^ULIMIT=.*$/ULIMIT=4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/:/usr/bin/',
  unless  => 'grep -q "^ULIMIT=4096$" /etc/default/nginx',
} ->

# Restart Nginx
exec { 'nginx-reload':
  command => 'systemctl reload nginx || service nginx reload',
  path    => '/usr/local/bin/:/bin/:/usr/sbin/:/usr/bin/',
  subscribe => Exec['increase-nginx-ulimit'],
}
