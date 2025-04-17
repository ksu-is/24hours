import tkinter as tk

# Creating the main window
root = tk.Tk()
root.title("24Hrs +")
root.geometry("300x200")  # Set a reasonable size

# Creating heading label
heading_label = tk.Label(root, text="Welcome to 24Hrs +!", font=("Helvetica", 24))
heading_label.pack(pady=10)

# Creating a sub-heading
sub_heading = tk.Label(root, text="Do you have an account?", font=("Helvetica", 12))
sub_heading.pack()

# Function to open login window
def open_login():
    top = tk.Toplevel(root)  # Create a new top-level window
    top.geometry("250x150")
    top.title("Login")
    
    log_page = tk.Label(top, text="Login Page", font=("Helvetica", 16))
    log_page.pack(pady=20)

# Function for sign-up 
def open_signup():
    top = tk.Toplevel(root)
    top.geometry("250x150")
    top.title("Sign Up")
    
    signup_page = tk.Label(top, text="Sign Up Page", font=("Helvetica", 16))
    signup_page.pack(pady=20)

# Creating buttons
yes_button = tk.Button(root, text="Yes!", command=open_login)
yes_button.pack(pady=5)

no_button = tk.Button(root, text="No", command=open_signup)
no_button.pack(pady=5)



# Making the sign-up button
sign_up = tk.Button(root, text="SignUp", command=signup)
sign_up.pack()

#making login buttion
def login():
    print("Hello")

# Making the sign-up button
log_in = tk.Button(root, text="Login", command=login)
log_in.pack()

# Running the main loop
root.mainloop()