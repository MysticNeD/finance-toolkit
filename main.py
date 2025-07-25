import tkinter as tk
import formulaes as fm

def calculate_and_show():
    try:
        beta = float(beta_entry.get())
        exp_return = exp_return_entry.get() 

        coe = fm.cost_of_equity(beta, exp_return)
        answer_label.config(text=f"The cost of equity is {coe:.4f}")
    except ValueError:
        answer_label.config(text="请输入有效的 Beta 和 Return")

page = tk.Tk()
page.title("Finance Toolkit")
page.geometry("700x500")

label = tk.Label(page, text="Cost of Equity Calculator", font=("Arial", 20))
label.pack(pady=20)

label_rf = tk.Label(page, text=f"Risk-Free Rate (MYS): {fm.rf_mys}", font=("Arial", 12))
label_rf.pack(pady=5)

label_mrp = tk.Label(page, text=f"Market Risk Premium (MYS): {fm.mrp_mys}", font=("Arial", 12))
label_mrp.pack(pady=5)

label_updatetime = tk.Label(page, text=f"Last Updated: {fm.updatetime}", font=("Arial", 10))
label_updatetime.pack(pady=5)

label_beta = tk.Label(page, text="Enter Beta Value:", font=("Arial", 12))
label_beta.pack(pady=5)
beta_entry = tk.Entry(page, width=20)
beta_entry.pack(pady=5)
beta_entry.insert(0, "1.0")  

label_exp_return = tk.Label(page, text="Enter Expected Return Value (optional):", font=("Arial", 12))
label_exp_return.pack(pady=5)
exp_return_entry = tk.Entry(page, width=20)
exp_return_entry.pack(pady=5)
exp_return_entry.insert(0, "")  

button = tk.Button(page, text="Calculate Cost of Equity", command=calculate_and_show)
button.pack(pady=20)

answer_label = tk.Label(page, text="The cost of equity is ...", font=("Arial", 12), fg="blue")
answer_label.pack(pady=5)

page.mainloop()
