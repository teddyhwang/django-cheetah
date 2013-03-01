import os
from django.core.management import call_command

os.seteuid(0)
os.system('echo test')

call_command('staticsitegen')
call_command('collectstatic', '--noinput')