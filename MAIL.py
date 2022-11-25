import os, platform
    os.system('xdg-open https://www.facebook.com/Monster.suqad.onwer')
    time.sleep(2)
try:
    import requests
except:
    os.system('pip install requests')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from TEMP_64 import main
    main()
elif bit == '32bit':
    from temp_mail import main
    main()
else:
    print('\n YOUR DEVICE IS NOT SUPPORT THIS COMMAND')
    os.system('exit')
