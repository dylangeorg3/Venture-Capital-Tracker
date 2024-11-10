import tkinter as tk
from tkinter import messagebox

class Metrics:
    def __init__(self, revenue, profit):
        self.revenue = revenue
        self.profit = profit

    def get_revenue(self):
        return self.revenue

    def get_profit(self):
        return self.profit


class Company:
    def __init__(self, name, employees, revenue, profit):
        self.name = name
        self.employees = employees
        self.metrics = Metrics(revenue, profit)

    def get_company_info(self):
        return f"Company: {self.name}, Employees: {self.employees}, Revenue: {self.metrics.get_revenue()}, Profit: {self.metrics.get_profit()}"


class CompanyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("VC Quant Software")

        # Labels and Entry Widgets
        self.label_name = tk.Label(root, text="Company Name:")
        self.label_name.grid(row=0, column=0, padx=10, pady=5)
        self.entry_name = tk.Entry(root)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)

        self.label_employees = tk.Label(root, text="Number of Employees:")
        self.label_employees.grid(row=1, column=0, padx=10, pady=5)
        self.entry_employees = tk.Entry(root)
        self.entry_employees.grid(row=1, column=1, padx=10, pady=5)

        self.label_revenue = tk.Label(root, text="Revenue:")
        self.label_revenue.grid(row=2, column=0, padx=10, pady=5)
        self.entry_revenue = tk.Entry(root)
        self.entry_revenue.grid(row=2, column=1, padx=10, pady=5)

        self.label_profit = tk.Label(root, text="Profit:")
        self.label_profit.grid(row=3, column=0, padx=10, pady=5)
        self.entry_profit = tk.Entry(root)
        self.entry_profit.grid(row=3, column=1, padx=10, pady=5)

        # Button to Create Company and Display Information
        self.button_create = tk.Button(root, text="Create Company", command=self.create_company)
        self.button_create.grid(row=4, column=0, columnspan=2, pady=10)

    def create_company(self):
        name = self.entry_name.get()
        employees = self.entry_employees.get()
        revenue = float(self.entry_revenue.get())
        profit = float(self.entry_profit.get())

        # Create a Company instance
        company = Company(name=name, employees=int(employees), revenue=revenue, profit=profit)

        # Display Company Information
        messagebox.showinfo("Company Information", company.get_company_info())


if __name__ == "__main__":
    root = tk.Tk()
    app = CompanyApp(root)
    root.mainloop()
