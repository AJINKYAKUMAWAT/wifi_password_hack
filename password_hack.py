import subprocess
import platform

def get_password(network_name):
    try:
        if platform.system() == 'Windows':
            result = subprocess.check_output(
                ['netsh', 'wlan', 'show', 'profile', network_name, 'key=clear'],
                stderr=subprocess.PIPE, text=True
            )
            password_index = result.find('Key Content')
            if password_index == -1:
                return 'Password not found'
            password_line = result[password_index:].split('\n')[0]
            password = password_line.split(': ')[1].strip()
            return password
        
        elif platform.system() == 'Darwin':
            result = subprocess.check_output(
                ['security', 'find-generic-password', '-wa', network_name],
                stderr=subprocess.PIPE, text=True
            )
            return result.strip()
        
        else:
            return 'Unsupported operating system'
    except subprocess.CalledProcessError:
        return 'Password not found'
    
    except Exception as e:
        return str(e)

network_name = 'Airtel_1561' # change wifi name
password = get_password(network_name)

if password:
    print(f'The wifi password for {network_name} is: {password}')
else:
    print('Password-1 not found')
