#! python3
# Author: George Gao, gaojz017@163.com
# 根据工资计算所得税以及到手的金额。本脚本以北京为例，
# Beijing
msg = "Your salary is %s.\nYou should pay %s.\nYou have %s."
condition = 1
while True:
    salary = input("Please Input Your Salary（￥）\nPress any alphabet to quit ：")

    if salary.isdigit():
        condition == 1
        salary = int(salary)
    else:
        break
    if salary <= 3500:
        print("The tax point is 3500. You don't need to pay taxes.")
    else:
        # delet_s：差额，实际工资减去起征点
        delet_s = salary - 3500
        if delet_s <= 1500:
            taxes = delet_s * 0.03
            income = salary - taxes
            print(msg % (str(salary), str(taxes), str(income)))
        elif 1500 < delet_s <= 4500:
            delet_s = delet_s - 1500
            taxes = delet_s * 0.1 + 1500 * 0.03
            income = salary - taxes
            print(msg % (str(salary), str(taxes), str(income)))
        elif 4500 < delet_s <= 9000:
            delet_s = delet_s - 4500
            taxes = delet_s * 0.2 + 4500 * 0.1 + 1500 * 0.03
            income = salary - taxes
            print(msg % (str(salary), str(taxes), str(income)))
        elif 9000 < salary <= 35000:
            delet_s = delet_s - 9000
            taxes = delet_s * 0.25 + 9000 * 0.2 + 4500 * 0.1 + 1500 * 0.03
            income = salary - taxes
            print(msg % (str(salary), str(taxes), str(income)))
        elif 35000 < salary <= 55000:
            delet_s = delet_s - 35000
            taxes = delet_s * 0.3 + 35000 * 0.25 + 9000 * 0.2 + 4500 * 0.1 + 1500 * 0.03
            income = salary - taxes
            print(msg % (str(salary), str(taxes), str(income)))
        elif 55000 < salary <= 85000:
            delet_s = delet_s - 55000
            taxes = delet_s * 0.35 + 55000 * 0.3 + 35000 * 0.25 + 9000 * 0.2 + 4500 * 0.1 + 1500 * 0.03
            income = salary - taxes
            print(msg % (str(salary), str(taxes), str(income)))
        else:
            delet_s = delet_s - 85000
            taxes = delet_s * 0.45 + 85000 * 0.35 + 55000 * 0.3 + 35000 * 0.25 + 9000 * 0.2 + 4500 * 0.1 + 1500 * 0.03
            income = salary - taxes
            print(msg % (str(salary), str(taxes), str(income)))
