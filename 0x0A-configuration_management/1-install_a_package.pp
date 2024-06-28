# install flask package

exec{ 'flask_install':
  command => '/usr/bin/pip3 install flask',
  }
