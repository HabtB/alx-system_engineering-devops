# This puppet script substitutes the type 'phpp' with 'php'
exec { 'fix_wordpress_config/typo error':
  command => '/usr/bin/env sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path    => '/bin:/usr/bin',
  onlyif  => '/usr/bin/test -f /var/www/html/wp-settings.php',
}
