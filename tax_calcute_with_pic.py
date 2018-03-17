#! python3
# Author: George Gao, gaojz017@163.com
import  matplotlib.pyplot as plt
import pygal

# Beijing
def tex_calcute(salary):
    """
    salary: income before paying taxes
    income: real income
    taxes: taxes should pay
    """
    if salary <= 3500:
        print("The tax point is 3500. You don't need to pay taxes.")
    else:
        # delet_s：差额，实际工资减去起征点
        delet_s = salary - 3500
        if delet_s <= 1500:
            taxes = delet_s * 0.03
            income = salary - taxes
        elif 1500 < delet_s <= 4500:
            delet_s = delet_s - 1500
            taxes = delet_s * 0.1 + 1500 * 0.03
            income = salary - taxes
        elif 4500 < delet_s <= 9000:
            delet_s = delet_s - 4500
            taxes = delet_s * 0.2 + 4500 * 0.1 + 1500 * 0.03
            income = salary - taxes
        elif 9000 < salary <= 35000:
            delet_s = delet_s - 9000
            taxes = delet_s * 0.25 + 9000 * 0.2 + 4500 * 0.1 + 1500 * 0.03
            income = salary - taxes
        elif 35000 < salary <= 55000:
            delet_s = delet_s - 35000
            taxes = delet_s * 0.3 + 35000 * 0.25 + 9000 * 0.2 + 4500 * 0.1 + 1500 * 0.03
            income = salary - taxes
        elif 55000 < salary <= 85000:
            delet_s = delet_s - 55000
            taxes = delet_s * 0.35 + 55000 * 0.3 + 35000 * 0.25 + 9000 * 0.2 + 4500 * 0.1 + 1500 * 0.03
            income = salary - taxes
        else:
            delet_s = delet_s - 85000
            taxes = delet_s * 0.45 + 85000 * 0.35 + 55000 * 0.3 + 35000 * 0.25 + 9000 * 0.2 + 4500 * 0.1 + 1500 * 0.03
            income = salary - taxes

        return  {'salary': income}

# calcute salary, taxes and income
x_axes = []
y_axes = []
for i in range(8000, 25000, 500):
    moneys = tex_calcute(i)
    x_axes.append(i)

    for k in moneys.keys():
        v_income = moneys[k]
        y_axes.append(v_income)
print(x_axes)
print(y_axes)
line_chart = pygal.Line()
line_chart._title = "Salary and real income"
line_chart.x_labels = map(str, x_axes)
line_chart.add('income', y_axes)
line_chart.render_to_file('salary_income.svg')
