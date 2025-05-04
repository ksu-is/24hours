import tkinter as tk
from tkinter import messagebox, Menu, IntVar, Menubutton

user_info = {}

# Create main window
root = tk.Tk()
root.title("24Hrs +")
root.geometry("300x450")

# Frame for sign-up screen
frame_signup = tk.Frame(root)
frame_signup.pack(pady=20)

tk.Label(frame_signup, text="Full Name:").pack()
entry_name = tk.Entry(frame_signup)
entry_name.pack()

tk.Label(frame_signup, text="Phone Number:").pack()
entry_phone = tk.Entry(frame_signup)
entry_phone.pack()

tk.Label(frame_signup, text="Email Address:").pack()
entry_email = tk.Entry(frame_signup)
entry_email.pack()

tk.Label(frame_signup, text="Password:").pack()
entry_signup_password = tk.Entry(frame_signup, show="*")
entry_signup_password.pack()

tk.Label(frame_signup, text="Confirm Password:").pack()
entry_confirm_password = tk.Entry(frame_signup, show="*")
entry_confirm_password.pack()

tk.Label(frame_signup, text="School/Occupation:").pack()
entry_school_occupation = tk.Entry(frame_signup)
entry_school_occupation.pack()

# Menu creation function
def create_menu(window, user_name):
    menubutton = Menubutton(window, text="≡", relief="raised", direction="below")
    menubutton.menu = Menu(menubutton, tearoff=0)
    menubutton["menu"] = menubutton.menu

    menubutton.menu.add_command(label="Home", command=lambda: open_home_page(user_name))
    menubutton.menu.add_command(label="Stats", command=lambda: open_stats_page(user_name))
    menubutton.menu.add_command(label="Bio", command=lambda: open_bio_page(user_name))

    menubutton.pack(pady=10)

# Page functions
def open_home_page(name):
    home = tk.Toplevel(root)
    home.title("Home Page")
    home.geometry("300x400")
    tk.Label(home, text=f"Welcome, {name}!", font=("Helvetica", 18)).pack(pady=20)
    tk.Button(home, text="Exit", command=home.destroy).pack(pady=10)
    create_menu(home, name)

def open_stats_page(name): 
    def calculate_breaks():
        try:
            hours = float(entry_hours.get())
            if hours <= 0:
                raise ValueError

            if hours == 1:
                result.set("Take a 10-minute break after 1 hour.")
            elif hours == 2:
                result.set("Take a 10-minute break after each hour (2 breaks total).")
            elif hours == 3:
                result.set("Take a 15-minute break after every 90 minutes.")
            elif hours >= 4:
                breaks = int(hours)  # One break every 60 minutes
                result.set(f"Take a 15-minute break every 60 minutes. Total breaks: {breaks}")
            else:
                result.set("Custom: Consider a short break every 60-90 minutes.")

        except ValueError:
            result.set("Please enter a valid number of hours.")

    stats = tk.Toplevel(root)
    stats.title("Stats Page")
    stats.geometry("300x400")

    tk.Label(stats, text="Statistics Page", font=("Helvetica", 18)).pack(pady=10)

    # Input for study hours
    tk.Label(stats, text="Enter your study hours:").pack()
    entry_hours = tk.Entry(stats)
    entry_hours.pack(pady=5)

    # Output display
    result = tk.StringVar()
    tk.Button(stats, text="Calculate Breaks", command=calculate_breaks).pack(pady=10)
    tk.Label(stats, textvariable=result, wraplength=250, justify="left").pack(pady=5)

    # Close button
    tk.Button(stats, text="Close", command=stats.destroy).pack(pady=10)

    # Menu
    create_menu(stats, name)

def open_bio_page(name):
    bio = tk.Toplevel(root)
    bio.title("Bio Page")
    bio.geometry("300x400")
    
    tk.Label(bio, text="Bio", font=("Helvetica", 18)).pack(pady=20)
    tk.Label(bio, text=f"Name: {user_info.get('name', 'N/A')}").pack()
    tk.Label(bio, text=f"Phone: {user_info.get('phone', 'N/A')}").pack()
    tk.Label(bio, text=f"Email: {user_info.get('email', 'N/A')}").pack()
    tk.Label(bio, text=f"School/Occupation: {user_info.get('occupation', 'N/A')}").pack()
    
    tk.Button(bio, text="Close", command=bio.destroy).pack(pady=10)
    create_menu(bio, name)

# Sign-up logic
def signup():
    global user_info
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    pw = entry_signup_password.get()
    confirm_pw = entry_confirm_password.get()
    occupation = entry_school_occupation.get()

    if pw != confirm_pw:
        messagebox.showerror("Error", "Passwords do not match!")
        return

    if len(pw) < 5 or not any(c.isupper() for c in pw):
        messagebox.showerror("Error", "Password must be at least 5 characters and contain at least one uppercase letter.")
        return

    if name and phone and email and pw and occupation:
        user_info["name"] = name
        user_info["phone"] = phone
        user_info["email"] = email
        user_info["occupation"] = occupation
        
        print("Sign Up:", name, phone, email, occupation)
        messagebox.showinfo("Sign Up", "Sign Up Successful!")
        open_home_page(name)
    else:
        messagebox.showerror("Error", "Please fill in all fields!")

# Sign-up button
tk.Button(frame_signup, text="Create Account", command=signup, width=15).pack(pady=15)

# Run the app
root.mainloop()

    