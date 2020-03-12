import urllib.request
import os
import ssl

## Prevent 'SSL: CERTIFICATE_VERIFY_FAILED' errors when using the urllib module
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

lst = ['admin_login', 'cgi-bin', 'admin.php', 'src', 'main', 'public', 'admin', 'dev', 'phpmyadmin', 'config', 'users', 'news', 'ftp', 'contact', 'admin.html', 'about', 'supersecretpath']
def simpleProbe(lst):
    url = input("URL TO PROBE: ") 
    for path in lst:
        try:
            response = urllib.request.urlopen(url + path)
            content = response.read().decode('utf-8')
    
            print('\nVALID PATH FOUND!' + '/' + path)
            print('########################################')
            print('PROCEEDING TO SCRAPE FOR CONTACT INFORMATION.')
            print('########## ' + url + path + ' ##########')
            print('')

            email_pattern = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}")
            phone_pattern = re.compile(r"(\d{3}[-\.\s]\d{3}[-\.\s]\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]\d{4}|\d{3}[-\.\s]\d{4})")
            
            phonenums = re.findall(phone_pattern,content)            
            print('The following phone numbers were found:\n')
            for val in phonenums:
                print(val)
            print('')
            
            emails = re.findall(email_pattern,content)
            print('The following email addresses were found:\n')
            for val in emails:
                print(val)
            print('')
            
        except urllib.error.HTTPError:
            print('Unable to find or access /' + path)
            
        except:
            print('Other error encountered. Did you remember the / at the end of your URL? (https://www.example.com/')

simpleProbe(lst)

