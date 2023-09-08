# Import necessary libraries
import tkinter as tk  # Tkinter library for GUI
from tkinter import simpledialog, messagebox  # Dialog and message box modules
from PIL import Image, ImageTk  # Pillow library for image handling

# Define the BankingSystem class
class BankingSystem:
    def __init__(self, root):
        # Initialize the main window (root) and set its title
        self.root = root
        self.root.title("Banking System")

        # Example accounts and balances stored in a dictionary
        self.accounts = {"Alice": 1000, "Bob": 1500, "Eve": 2000}

        # Initialize variables to keep track of the current user and transaction history
        self.current_user = None
        self.transaction_history = []

        # Set the GUI background color
        self.root.configure(bg="#E1BEE7")  # Light purple background

        # Load and resize the background image
        image = Image.open("background_image.jpg")
        image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.ANTIALIAS)
        self.background_image = ImageTk.PhotoImage(image)

        # Create a label to display the background image
        self.background_label = tk.Label(root, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        # Load and resize the bank logo image
        image = Image.open("bank_logo.jpeg")
        image = image.resize((100, 100), Image.ANTIALIAS)
        self.bank_logo = ImageTk.PhotoImage(image)

        # Create a label to display the bank logo
        self.logo_label = tk.Label(root, image=self.bank_logo, bg="#E1BEE7")
        self.logo_label.pack(pady=10)

        # Create a label with a welcome message
        self.label = tk.Label(root, text="Welcome to the Banking System", font=("Helvetica", 16, "bold"), bg="pink", fg="purple")
        self.label.pack(pady=10)

        # Create a dropdown menu to select a user
        self.user_dropdown = tk.StringVar()
        self.user_dropdown.set("Select User")
        user_names = [*self.accounts.keys()]

        # Create an OptionMenu widget to display the user dropdown
        self.user_menu = tk.OptionMenu(root, self.user_dropdown, *user_names)
        self.user_menu.configure(bg="#800080", fg="white")
        self.user_menu["menu"].config(bg="#800080", fg="white")
        self.user_menu.pack(pady=5)

        # Create a login button with a callback to the login function
        self.login_button = tk.Button(root, text="Login", command=self.login, bg="pink", fg="purple", font=("Helvetica", 12, "bold"))
        self.login_button.pack(pady=5)

        # Create an account details button with a callback to the show_account_details function
        self.account_details_button = tk.Button(root, text="Account Details", command=self.show_account_details, bg="purple", fg="white", font=("Helvetica", 12, "bold"))
        self.account_details_button.pack(pady=5)

        # Create a deposit button with a callback to the deposit function
        self.deposit_button = tk.Button(root, text="Deposit", command=self.deposit, bg="pink", fg="black", font=("Helvetica", 12, "bold"))
        self.deposit_button.pack(pady=5)

        # Create a withdraw button with a callback to the withdraw function
        self.withdraw_button = tk.Button(root, text="Withdraw", command=self.withdraw, bg="purple", fg="white", font=("Helvetica", 12, "bold"))
        self.withdraw_button.pack(pady=5)

        # Create a label for the transaction history
        self.transaction_history_label = tk.Label(root, text="Transaction History:", bg="pink", fg="black", font=("Helvetica", 12, "bold"))
        self.transaction_history_label.pack(pady=5)

        # Create a listbox to display the transaction history
        self.transaction_listbox = tk.Listbox(root, font=("Helvetica", 12), bg="black", fg="white")
        self.transaction_listbox.pack(pady=5, padx=10)

    # Callback function to handle user login
    def login(self):
        selected_user = self.user_dropdown.get()
        if selected_user in self.accounts:
            self.current_user = selected_user
            self.update_transaction_listbox(f"Logged in as {self.current_user}")
        else:
            messagebox.showerror("Error", "User not found.")

    # Callback function to display account details
    def show_account_details(self):
        if self.current_user:
            messagebox.showinfo("Account Details", f"User: {self.current_user}\nBalance: ${self.accounts[self.current_user]}")
        else:
            messagebox.showerror("Error", "Please log in first.")

    # Callback function to handle depositing money
    def deposit(self):
        if self.current_user:
            amount = simpledialog.askinteger("Deposit", "Enter amount to deposit:", parent=self.root)
            if amount is not None and amount > 0:
                self.accounts[self.current_user] += amount
                self.update_transaction_listbox(f"Deposited ${amount}")
        else:
            messagebox.showerror("Error", "Please log in first.")

    # Callback function to handle withdrawing money
    def withdraw(self):
        if self.current_user:
            amount = simpledialog.askinteger("Withdraw", "Enter amount to withdraw:", parent=self.root)
            if amount is not None and amount > 0:
                if amount <= self.accounts[self.current_user]:
                    self.accounts[self.current_user] -= amount
                    self.update_transaction_listbox(f"Withdrew ${amount}")
                else:
                    messagebox.showerror("Error", "Insufficient balance!")
        else:
            messagebox.showerror("Error", "Please log in first.")

    # Function to update the transaction listbox
    def update_transaction_listbox(self, message):
        self.transaction_history.append(message)
        self.transaction_listbox.delete(0, tk.END)
        for item in self.transaction_history:
            self.transaction_listbox.insert(tk.END, item)

# Main entry point of the program
if __name__ == "__main__":
    # Create the main window (root)
    root = tk.Tk()
    # Create an instance of the BankingSystem class with the root window
    app = BankingSystem(root)
    # Start the main GUI event loop
    root.mainloop()
