'''Module 2: Individual Programming Assignment 1'''

def savings(gross_pay, tax_rate, expenses):

    tax_deduction = int(gross_pay * tax_rate)
    take_home_pay = gross_pay - tax_deduction - expenses
    
    return take_home_pay

def material_waste(total_material, material_units, num_jobs, job_consumption):
    total_consumed = num_jobs * job_consumption
    remaining_material = total_material - total_consumed
    
    material_waste = str(remaining_material) + material_units
    
    return material_waste

def interest(principal, rate, periods):
    rate = float(rate/100)
    interest = principal * rate * periods
    final_value = principal + interest
    
    return final_value

def body_mass_index(weight, height):
    
    weight_kg = weight * 0.45359237

    height_ft, height_in = height
    height_m = (int(height_ft) * 0.3048) + (int(height_in) * 0.0254)

    body_mass_index = weight_kg/(height_m**2)
    body_mass_index = format(body_mass_index,".2f")

    return body_mass_index

while(True):
    print("\nSelect a Computational Function")
    print("[1] Savings")
    print("[2] Material Waste")
    print("[3] Interest")
    print("[4] Body Mass Index")

    select = None

    while(True):
        select = int(input(">> "))
        if not(select <= 4 and select >= 1):
            print("\n[SYSTEM]: Please input a number from the available options.")
        else:
            break

    if select == 1:  
        print("\n[FUNCTION: SAVINGS]")
        print("\nInput the Gross Pay | E.g. 12500")
        while(True):
            gross_pay = int(input(">> "))
            if not(gross_pay >= 0):
                print("\n[SYSTEM]: Please input a number greater than or equal to 0.")
            else:
                break
        print("\nInput the Tax Rate | E.g. 0.13")
        while(True):
            tax_rate = float(input(">> "))
            if not(tax_rate < 1 and tax_rate > 0):
                print("\n[SYSTEM]: Please input a number between 0 and 1.")
            else:
                break
        print("\Input the Expenses | E.g. 3400")
        while(True):
            expenses = int(input(">> "))
            if not(expenses >= 0):
                print("\n[SYSTEM]: Please input a number greater than or equal to 0.")
            else:
                break
        print("\nCentavos Remaining: " + str(savings(gross_pay, tax_rate, expenses)) + '\u00a2')
    
    elif select == 2:
        print("\n[FUNCTION: MATERIAL WASTE]")
        print("\nInput the Total Material | E.g. 97000")
        while(True):
            total_material = int(input(">> "))
            if not(total_material >= 0):
                print("\n[SYSTEM]: Please input a number greater than or equal to 0.")
            else:
                break
        print("\nInput the Material Unit | E.g. Kg, Lbs, or L")
        while(True):
            material_units = str(input(">> "))
            if not(type(material_units) == str):
                print("\n[SYSTEM]: Please input a string.")
            else:
                break
        print("Input the Number of Jobs | E.g. 13")
        while(True):
            num_jobs = int(input(">> "))
            if not(num_jobs >= 0):
                print("\n[SYSTEM]: Please input a number greater than or equal to 0.")
            else:
                break
        print("Input the Job Consumption | E.g. 710")
        while(True):
            job_consumption = int(input(">> "))
            if not(job_consumption >= 0):
                print("\n[SYSTEM]: Please input a number greater than or equal to 0.")
            else:
                break
        print("\nRemaining Materials: " + material_waste(total_material, material_units, num_jobs, job_consumption))
   
    elif select == 3:
        print("\n[FUNCTION: INTEREST]")
        print("Input the Principal | E.g. 3600")
        while(True):
            principal = int(input(">> "))
            if not(principal >= 0):
                print("\n[SYSTEM]: Please input a number greater than or equal to 0.")
            else:
                break
        print("Input the rate | E.g. 3% or 0.3")
        while(True):
            rate = input(">> ")
            if(rate.endswith('%')):
                rate = rate.replace("%", "")
                rate = float(int(rate)/100)
                if not(rate >= 0):
                        print("\n[SYSTEM]: Please input a percentage greater than or equal to 0.")
                else:
                    break
            else:
                try:
                    rate = float(rate)
                    if not(rate >= 0):
                        print("\n[SYSTEM]: Please input a number greater than or equal to 0.")
                    else:
                        break
                except ValueError:
                    print("\n[SYSTEM]: Please input a percentage or decimal.")
        print("Input the Periods")
        while(True):
            periods = input(">> ")
            if not(periods >= 0):
                print("\n[SYSTEM]: Please input a number greater than or equal to 0.")
            else:
                break
        print("\Final Investment Value: " + str(interest(principal, rate, periods)))
    
    elif select == 4:
        print("\nYou've selected BODY MASS INDEX.")
        print("Input the Weight (in pounds)")
        while(True):
            weight = float(input(">> "))
            if not(weight >= 0):
                print("\n[SYSTEM]: Please input a number greater than or equal to 0.")
            else:
                break
        print("Input the Height (in feet and inches) | Ex. 4'10")
        while(True):
            height = str(input(">> "))
            if not(type(height) == str):
                print("\n[SYSTEM]: Please input the right format.")
            else:
                break
        height_list = height.split("'")
        bmi = body_mass_index(weight, height_list)
        print("\nBody Mass Index: " + (str(bmi)))
        if (bmi < 18.5):
            print("Category: Underweight")
        elif (bmi >= 18.5 and bmi <= 24.9):
            print("Category: Healthy Weight")
        elif (bmi >= 25.0 and bmi <= 29.9):
            print("Category: Overweight")
        elif (bmi > 30.0):
            print("Category: Obesity")

    print("\nInitiate program execution once more?")
    print("[1] Yes")
    print("[2] No")
    
    while(True):
        select = int(input(">> "))
        if not(select <= 2 and select >= 1):
            print("\nPlease input a number from the available options.")
        else:
            break

    if(select == 1):
        continue
    elif(select == 2):
        break