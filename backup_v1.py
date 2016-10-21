#!/usr/bin/python

import os
import time

source = ['/home/hp/test']

target_dir = '/home/hp/backup/'

target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command = "zip -qr '%s' %s" % (target,' '.join(source))

if os.system(zip_command) == 0:
	print 'Successful backup to',target
else:
	print 'Backup Failed'
