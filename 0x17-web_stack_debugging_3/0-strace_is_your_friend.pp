# replace phpp for php

exec { 'fix wrong name php':
    command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
    path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
    # path    => [ '/usr/local/bin/', '/bin/' ],  # alternative syntax
  }