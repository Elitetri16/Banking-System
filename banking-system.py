import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk

class BankingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Banking System")

        self.accounts = {"Alice": 1000, "Bob": 1500, "Eve": 2000}  # Example accounts and balances

        self.current_user = None
        self.transaction_history = []

        # Set a colorful and interactive color scheme
        self.root.configure(bg="#E1BEE7")  # Light purple background
        image = Image.open("background_image.jpg")  
        image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.ANTIALIAS)
        self.background_image = ImageTk.PhotoImage(image)
        self.background_label = tk.Label(root, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        image = Image.open("bank_logo.jpeg")  
        image = image.resize((100, 100), Image.ANTIALIAS)
        self.bank_logo = ImageTk.PhotoImage(image)
        self.logo_label = tk.Label(root, image=self.bank_logo, bg="#E1BEE7")
        self.logo_label.pack(pady=10)

        self.label = tk.Label(root, text="Welcome to the Banking System", font=("Helvetica", 16, "bold"), bg="pink", fg="purple")
        self.label.pack(pady=10)

        self.user_dropdown = tk.StringVar()
        self.user_dropdown.set("Select User")
        user_names = [*self.accounts.keys()]

        self.user_menu = tk.OptionMenu(root, self.user_dropdown, *user_names)
        self.user_menu.configure(bg="#800080", fg="white")
        self.user_menu["menu"].config(bg="#800080", fg="white")
        self.user_menu.pack(pady=5)

        self.login_button = tk.Button(root, text="Login", command=self.login, bg="pink", fg="purple", font=("Helvetica", 12, "bold"))
        self.login_button.pack(pady=5)

        self.account_details_button = tk.Button(root, text="Account Details", command=self.show_account_details, bg="purple", fg="white", font=("Helvetica", 12, "bold"))
        self.account_details_button.pack(pady=5)

        self.deposit_button = tk.Button(root, text="Deposit", command=self.deposit, bg="pink", fg="black", font=("Helvetica", 12, "bold"))
        self.deposit_button.pack(pady=5)

        self.withdraw_button = tk.Button(root, text="Withdraw", command=self.withdraw, bg="purple", fg="white", font=("Helvetica", 12, "bold"))
        self.withdraw_button.pack(pady=5)

        self.transaction_history_label = tk.Label(root, text="Transaction History:", bg="pink", fg="black", font=("Helvetica", 12, "bold"))
        self.transaction_history_label.pack(pady=5)

        self.transaction_listbox = tk.Listbox(root, font=("Helvetica", 12), bg="black", fg="white")
        self.transaction_listbox.pack(pady=5, padx=10)

    def login(self):
        selected_user = self.user_dropdown.get()
        if selected_user in self.accounts:
            self.current_user = selected_user
            self.update_transaction_listbox(f"Logged in as {self.current_user}")
        else:
            messagebox.showerror("Error", "User not found.")

    def show_account_details(self):
        if self.current_user:
            messagebox.showinfo("Account Details", f"User: {self.current_user}\nBalance: ${self.accounts[self.current_user]}")
        else:
            messagebox.showerror("Error", "Please log in first.")

    def deposit(self):
        if self.current_user:
            amount = simpledialog.askinteger("Deposit", "Enter amount to deposit:", 
                                             parent=self.root, foreground="light green")
            if amount is not None and amount > 0:
                self.accounts[self.current_user] += amount
                self.update_transaction_listbox(f"Deposited ${amount}")
        else:
            messagebox.showerror("Error", "Please log in first.")

    def withdraw(self):
        if self.current_user:
            amount = simpledialog.askinteger("Withdraw", "Enter amount to withdraw:", 
                                             parent=self.root, foreground="light green")
            if amount is not None and amount > 0:
                if amount <= self.accounts[self.current_user]:
                    self.accounts[self.current_user] -= amount
                    self.update_transaction_listbox(f"Withdrew ${amount}")
                else:
                    messagebox.showerror("Error", "Insufficient balance!")
        else:
            messagebox.showerror("Error", "Please log in first.")

    def update_transaction_listbox(self, message):
        self.transaction_history.append(message)
        self.transaction_listbox.delete(0, tk.END)
        for item in self.transaction_history:
            self.transaction_listbox.insert(tk.END, item)

if __name__ == "__main__":
    root = tk.Tk()
    app = BankingSystem(root)
    root.mainloop()
