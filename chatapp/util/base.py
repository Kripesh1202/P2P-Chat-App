"""Basic utils functions"""

import configparser

class MsgLog():
    """Class to write and get Message Logs"""
    def __init__(self) -> None:
        pass


    def write_log(self, name, text):
        """Write Message Logs to file"""
        with open(file=r"chatapp\msg_data\msg_log.txt", \
                mode='a+', encoding='utf-8') as msg_log:
            msg_log.write(name+':'+text)


    def get_log(self):
        """Get Message Logs from file"""
        with open(file=r"chatapp\msg_data\msg_log.txt", \
                mode='r+', encoding='utf-8') as msg_log:
            msg_data=msg_log.readlines()
            return msg_data
        
    def clear_log(self):
        """Clear all message logs from file"""
        with open(file=r"chatapp\msg_data\msg_log.txt", \
                  mode='w', encoding='utf-8') as msg_log:
            msg_log.write('')



class ConfigFile():
    """Class to write and get config info"""
    def __init__(self) -> None:
        self.conf = configparser.ConfigParser()


    def write_partner_config(self, name, ip):
        """Write to partner config"""
        with open(file=r'chatapp\util\config.ini', \
                mode='w+', encoding='utf-8') as wc:
            self.conf['PARTNER']['NAME'] = name
            self.conf['PARTNER']['IP'] = ip
            self.conf['PARTNER']['CONTENT'] = '1'
            self.conf.write(wc)


    def get_partner_config(self):
        """Get from partner config"""
        self.conf.read(r'chatapp\util\config.ini')
        return self.conf['PARTNER']
    

    def write_user_config(self, name):
        """Write to user config"""
        with open(file=r'chatapp\util\config.ini', \
                mode='w+', encoding='utf-8') as wc:
            self.conf['SELF']['NAME'] = name
            self.conf['SELF']['CONTENT'] = '1'
            self.conf.write(wc)


    def get_user_config(self):
        """Get from user config"""
        self.conf.read(r'chatapp\util\config.ini')
        return self.conf['SELF']
    

    def get_all_config(self):
        """Get both user and parnter config"""
        self.conf.read(r'chatapp\util\config.ini')
        return self.conf    


    def clear_config(self):
        """Clear config file"""
        with open(file=r'chatapp\util\config.ini', \
                mode='w+', encoding='utf-8') as wc:
            self.conf['PARTNER']['CONTENT'] = '0'
            self.conf['PARTNER']['NAME'] = ''
            self.conf['PARTNER']['IP'] = ''
            self.conf.write(wc)
        