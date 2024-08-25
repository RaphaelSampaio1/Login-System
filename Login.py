from tkinter import *
from tkinter import messagebox

class App:
    def __init__(self, root):
        self.root = root
        self.root.title('Login')
        self.root.geometry('925x500+300+200')
        self.root.configure(bg='white')
        self.root.resizable(False, False)
        
        # Load and keep a reference to the image
        self.bg_image = PhotoImage(file='login.png')
        self.create_login_frame()

    def create_login_frame(self):
        # Insert the background image
        Label(self.root, image=self.bg_image, bg='white').place(x=50, y=50)  # Image position

        # Create the frame for login
        self.frame = Frame(self.root, width=350, height=350, bg='white')
        self.frame.place(x=480, y=70)
        
        # Head text login
        heading = Label(self.frame, text='Sign In', fg='#57a1f8', bg='white', font=('Microsoft Yahei UI light', 23, 'bold'))
        heading.place(x=100, y=5)

        # Username entry for login
        self.user = Entry(self.frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI light', 11))
        self.user.place(x=30, y=80)
        self.user.insert(0, 'Username')
        self.user.bind('<FocusIn>', lambda e: self.on_enter(e, self.user, 'Username'))
        self.user.bind('<FocusOut>', lambda e: self.on_leave(e, self.user, 'Username'))
        Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=107)

        # Password entry for login
        self.code = Entry(self.frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI light', 11))
        self.code.place(x=30, y=150)
        self.code.insert(0, 'Password')
        self.code.bind('<FocusIn>', lambda e: self.on_enter(e, self.code, 'Password'))
        self.code.bind('<FocusOut>', lambda e: self.on_leave(e, self.code, 'Password'))
        Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=177)

        # Sign In button
        Button(self.frame, width=39, pady=7, text='Sign In', bg='#57a1f8', fg='white', border=0, cursor='hand2', command=self.signin).place(x=35, y=204)

        # Don't have an account label
        label = Label(self.frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft Yahei UI light', 9))
        label.place(x=75, y=270)

        # Sign Up button
        Button(self.frame, width=6, text='Sign Up', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=self.open_register_form).place(x=215, y=270)

    def on_enter(self, event, entry, placeholder):
        if entry.get() in [placeholder]:
            entry.delete(0, 'end')
        entry.config(show='*' if entry == self.code else '')

    def on_leave(self, event, entry, placeholder):
        if entry.get() == '':
            entry.insert(0, placeholder)
        entry.config(show='*' if entry == self.code else '')

    def signin(self):
        username = self.user.get()
        password = self.code.get()

        if username == 'admin' and password == '1234':
            screen = Toplevel(self.root)
            screen.title("App")
            screen.geometry('925x500+300+200')
            screen.config(bg='white')
            Label(screen, text=f'Welcome {username} !', bg='#fff', font=('Calibri(Body)', 50, 'bold')).pack(expand=True)
            screen.mainloop()
        elif username != 'admin' and password != '1234':
            messagebox.showerror("Invalid", "Invalid username and password")
        elif password != '1234':
            messagebox.showerror("Invalid", "Invalid password")
        elif username != 'admin':
            messagebox.showerror("Invalid", "Invalid username")

    def open_register_form(self):
        self.frame.destroy()  # Remove the login frame
        
        # Create the frame for register
        self.register_frame = Frame(self.root, width=350, height=550, bg='white')
        self.register_frame.place(x=480, y=70)

        # Head text register
        heading = Label(self.register_frame, text='Sign Up', fg='#57a1f8', bg='white', font=('Microsoft Yahei UI light', 23, 'bold'))
        heading.place(x=100, y=5)

        # Username entry for registration
        self.reg_user = Entry(self.register_frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI light', 11))
        self.reg_user.place(x=30, y=80)
        self.reg_user.insert(0, 'Username')
        Frame(self.register_frame, width=295, height=2, bg='black').place(x=25, y=107)
        self.reg_user.bind('<FocusIn>', lambda e: self.on_enter(e, self.reg_user, 'Username'))
        self.reg_user.bind('<FocusOut>', lambda e: self.on_leave(e, self.reg_user, 'Username'))

        # Password entry for registration
        self.reg_code = Entry(self.register_frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI light', 11))
        self.reg_code.place(x=30, y=150)
        self.reg_code.insert(0, 'Password')
        self.reg_code.bind('<FocusIn>', lambda e: self.on_enter(e, self.reg_code, 'Password'))
        self.reg_code.bind('<FocusOut>', lambda e: self.on_leave(e, self.reg_code, 'Password'))
        Frame(self.register_frame, width=295, height=2, bg='black').place(x=25, y=177)

        # Register button
        Button(self.register_frame, width=39, pady=7, text='Register', bg='#57a1f8', fg='white', border=0, cursor='hand2').place(x=35, y=300)

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
