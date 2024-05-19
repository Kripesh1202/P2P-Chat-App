from .chat import Chatapp as chat
from .util import base as b

import customtkinter

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
import  sys
=======
>>>>>>> a80bc70172e467c43b5fb15c755f6fb94644041f
=======
import  sys
>>>>>>> c71df84 (updated exception errors)
=======
import  sys
=======
>>>>>>> a80bc70172e467c43b5fb15c755f6fb94644041f
>>>>>>> origin/main
import threading



customtkinter.set_appearance_mode(mode_string="system")
customtkinter.set_default_color_theme(color_string="green")


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> c71df84 (updated exception errors)
=======
>>>>>>> origin/main

class MessageFrame(customtkinter.CTkTextbox):
    """Message Frame to Display Received and Send Messages"""
    def __init__(self, master):  #font=customtkinter.CTkFont()
        super().__init__(master, width=507, height=320)  #font
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> origin/main
=======
class MessageFrame(customtkinter.CTkTextbox):
    """Message Frame to Display Received and Send Messages"""
    def __init__(self, master):  #font=customtkinter.CTkFont()
        super().__init__(master, width=500, height=270)  #font
>>>>>>> a80bc70172e467c43b5fb15c755f6fb94644041f
<<<<<<< HEAD
=======
>>>>>>> c71df84 (updated exception errors)
=======
>>>>>>> origin/main
        # self.configure(state = "disabled")
        self.pack(pady=50)



class MainFrame(customtkinter.CTk):
    """Main Frame Class for Chat GUI"""
    def __init__(self):
        super().__init__()
        self.title('P2P Chatapp')
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> origin/main
        self.geometry('700x520')
        self.resizable(0,0)
=======
        self.geometry('700x500')
>>>>>>> a80bc70172e467c43b5fb15c755f6fb94644041f
<<<<<<< HEAD
=======
        self.geometry('700x520')
        self.resizable(0,0)
>>>>>>> c71df84 (updated exception errors)
=======
>>>>>>> origin/main



class ChatFrame:
    """Class for initializing Chat frame"""
    def __init__(self):
        self.app = None
        self.entry = ''
        self.msg_frame = ''
        self.name = ''
        self.parter_name = ''
        self.parter_ip = ''
        self.index = 0.0
        self.client_obj = ''
        self.server_obj = ''
        self.config_file = b.ConfigFile()
        self.msg_log = b.MsgLog()
        self.lock = threading.Lock()


    def get_username(self):
        """Input dialogbox to get user name"""
        userinfo = customtkinter.CTkInputDialog(text="Enter your user name", title='User Info')
        self.name = userinfo.get_input()
        print(self.name)
        self.config_file.write_user_config(name=self.name)


    def get_partner_info(self):
        """Get partner name and ip"""
        print('Getting user info')
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> c71df84 (updated exception errors)
=======
>>>>>>> origin/main
        while True:
            try:
                get_info = customtkinter.CTkInputDialog(text="Enter your partner ip and name. Eg <name>:<ip>", \
                                                        title='Partner user Info')
                self.parter_name, self.parter_ip = get_info.get_input().split(':')
                self.config_file.write_partner_config(name=self.parter_name, ip=self.parter_ip)
                break
            except AttributeError:
                pass
            except ValueError:
                pass
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> origin/main
=======
        get_info = customtkinter.CTkInputDialog(text="Enter your partner ip and name. Eg <name>:<ip>", \
                                                title='Partner user Info')
        self.parter_name, self.parter_ip = get_info.get_input().split(':')
        self.config_file.write_partner_config(name=self.parter_name, ip=self.parter_ip)
>>>>>>> a80bc70172e467c43b5fb15c755f6fb94644041f
<<<<<<< HEAD
=======
>>>>>>> c71df84 (updated exception errors)
=======
>>>>>>> origin/main


    def insert_textbox(self):
        """Insert Message to TextBox"""
        self.msg_frame = MessageFrame(master=self.app)
        if msg_data := self.msg_log.get_log():
            for msg_meta in msg_data:
                msg_name, msg_text = msg_meta.split(':')
                # self.msg_frame.insert(str(self.index), text=f"{msg_name} :\t{msg_text}")
                self.msg_frame.insert(customtkinter.END, text=f"{msg_name} :\t{msg_text}")
                self.index += 1.0
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> c71df84 (updated exception errors)
=======
>>>>>>> origin/main
        self.msg_frame.configure(state = 'disabled')


    def get_from_entry(self, event=None):
        """Get data from Entry and writes to message logs"""
        try:
            self.msg_frame.configure(state = "normal")
            text = self.entry.get()+'\n'
            # self.msg_frame.insert(self.index,  text=f"{self.name} :\t{text}")
            self.msg_frame.insert(customtkinter.END,  text=f"{self.name} :\t{text}")
            self.msg_frame.configure(state = "disabled")
            self.client_obj.send_data(data=text)
            self.msg_log.write_log(self.name, text)
            self.entry.delete('0', customtkinter.END)
        except OSError:
            pass

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> origin/main
=======


    def get_from_entry(self):
        """Get data from Entry and writes to message logs"""
        text = self.entry.get()+'\n'
        # self.msg_frame.insert(self.index,  text=f"{self.name} :\t{text}")
        self.msg_frame.insert(customtkinter.END,  text=f"{self.name} :\t{text}")
        self.client_obj.send_data(data=text)
        self.msg_log.write_log(self.name, text)
        self.entry.delete('0', customtkinter.END)
>>>>>>> a80bc70172e467c43b5fb15c755f6fb94644041f
<<<<<<< HEAD
=======
>>>>>>> c71df84 (updated exception errors)
=======
>>>>>>> origin/main

    def recv_to_entry(self):
        """Display received message in textbox"""
        while True:
            try:
                if msg := self.server_obj.recv_data():
                    # self.lock.acquire(True)
                    # self.msg_frame.insert(index=self.index, text=f"{self.parter_name} :\t{msg}")
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> origin/main
                    self.msg_frame.configure(state = "normal")
                    self.msg_frame.insert(index=customtkinter.END, text=f"{self.parter_name} :\t{msg}")
                    self.msg_frame.configure(state = "disabled")
=======
                    self.msg_frame.insert(index=customtkinter.END, text=f"{self.parter_name} :\t{msg}")
>>>>>>> a80bc70172e467c43b5fb15c755f6fb94644041f
<<<<<<< HEAD
=======
                    self.msg_frame.configure(state = "normal")
                    self.msg_frame.insert(index=customtkinter.END, text=f"{self.parter_name} :\t{msg}")
                    self.msg_frame.configure(state = "disabled")
>>>>>>> c71df84 (updated exception errors)
=======
>>>>>>> origin/main
                    self.index+=1
                    self.msg_log.write_log(name=self.parter_name, text=msg)
                    # self.lock.release()
            except AttributeError:
                pass
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> c71df84 (updated exception errors)
=======
>>>>>>> origin/main
            except EOFError:
                pass


    def exit_conv(self):
        """Exit from the conversation"""
        self.client_obj.close_sock()
        self.server_obj.close_server_sock()
        self.app.destroy()
        self.msg_log.clear_log()
        self.config_file.clear_config()
        self.init_frame()

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> origin/main
=======


>>>>>>> a80bc70172e467c43b5fb15c755f6fb94644041f
<<<<<<< HEAD
=======
>>>>>>> c71df84 (updated exception errors)
=======
>>>>>>> origin/main

    def check_partnerinfo(self):
        """Checks for partner info"""
        while True:
            conf = self.config_file.get_partner_config()
            if bool(int(conf['CONTENT'])):
                return conf['NAME']
            self.get_partner_info()

    def check_userinfo(self):
        """Check for user info"""
        while True:
            conf = self.config_file.get_user_config()
            if bool(int(conf['CONTENT'])):
                return conf['NAME']
            self.get_username()


    def init_frame(self):
        """Initialize Main Frame with widgets"""
        self.name = self.check_userinfo()
        self.parter_name = self.check_partnerinfo()
        self.app = MainFrame()
        self.insert_textbox()
        self.chat = chat()

        text_msg = customtkinter.StringVar()
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> c71df84 (updated exception errors)
=======
>>>>>>> origin/main
        self.entry = customtkinter.CTkEntry(master=self.app, width=378, height= 35, textvariable=text_msg, \
                                            placeholder_text="Message")
        self.entry.place(x=121, y=390)
        self.app.bind('<Return>', func=self.get_from_entry)

        send_btn = customtkinter.CTkButton(master=self.app, text="Send", \
                                             width=78, height=35, command=self.get_from_entry)
        send_btn.place(x=510, y=390)
        # send_btn.pack(pady=30)

        exit_btn = customtkinter.CTkButton(master=self.app, width=75, height= 30, text="Exit", \
                                           command=self.exit_conv)
        exit_btn.place(x=472, y=40)
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> origin/main
=======
        self.entry = customtkinter.CTkEntry(master=self.app, textvariable=text_msg, placeholder_text="Message")
        self.entry.pack()
        btn = customtkinter.CTkButton(master=self.app, text="submit", command=self.get_from_entry)
        btn.pack(pady=30)
>>>>>>> a80bc70172e467c43b5fb15c755f6fb94644041f
<<<<<<< HEAD
=======
>>>>>>> c71df84 (updated exception errors)
=======
>>>>>>> origin/main

        init_serv_thread = threading.Thread(target=self.chat.init_server, daemon=True)
        init_client_thread = threading.Thread(target=self.chat.init_client, daemon=True)
        recv_thread = threading.Thread(target=self.recv_to_entry, daemon=True)
        init_serv_thread.start()
        init_client_thread.start()
        self.server_obj = self.chat.return_server_obj()
        self.client_obj = self.chat.return_client_obj()
        recv_thread.start()
        self.app.mainloop()
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> origin/main
        self.msg_log.clear_log()
        self.config_file.clear_config()
        sys.exit()
=======
        self.client_obj.close_sock()
        self.server_obj.close_server_sock()
>>>>>>> a80bc70172e467c43b5fb15c755f6fb94644041f
<<<<<<< HEAD
=======
        self.msg_log.clear_log()
        self.config_file.clear_config()
        sys.exit()
>>>>>>> c71df84 (updated exception errors)
=======
>>>>>>> origin/main
