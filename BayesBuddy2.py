
# A good friend lets you know when you are wrong
# A Bayesian Buddy tells you how likely that is.

# This program outputs the chance you are wrong given:
# Your guess (required), a base_rate of true/present/positive values (required), 
# And some measure of sensitivity or specificity

def predict_base_rate(guess, base_rate):
    print("Absent other information, I predict based on the base rate...")
    print("The chance the guess/result/diagnosis is wrong is: ") 
    if guess=="1":
        return round((1-float(base_rate)),2)
    else:
        return round((float(base_rate)),2)    

def get_output_sens(guess, base_rate, sensitivity):
    print("Based on the base-rate and sensitivity information...")
    print("The chance the guess/result/diagnosis is wrong is: ") 
    guess = float(guess)
    base_rate = float(base_rate)
    sensitivity = float(sensitivity)
    p1 = (base_rate * sensitivity) / ((base_rate * sensitivity) + ((1-base_rate)*(1-sensitivity)))
    return round((1-p1),2)   

def get_output_spec(guess, base_rate, specificity):
    print("Based on the base-rate specificity information...")
    print("The chance the guess/result/diagnosis is wrong is: ")  
    guess = float(guess)
    base_rate = float(base_rate)
    specificity = float(specificity)
    p0 = (base_rate * specificity) / ((base_rate * specificity) + ((1-base_rate)*(1-specificity)))
    return round((1-p0),2)

guess = input("What is your guess/result/diagnosis? Enter 1 for true/present/positive or 0 for false/negative/absent: ")
while True:
    if guess!="1" and guess!="0":
        print("Please enter a 1 or 0")
        guess = input("What is your guess/result/diagnosis? Enter 1 for true/present/positive or 0 for false/negative/absent: ")
    else:
        break
base_rate = input("What is the (prior) proportion of true/present/positive cases you would expect overall?: ")
while True:
    try:
        float(base_rate)
    except:
        print("Please enter a numeric value between 0 and 1") 
        base_rate = input("What is the (prior) proportion of true/present/positive cases you would expect overall?: ")
    else:
        if not float(base_rate) < 1 or not float(base_rate)> 0:
            print("Please enter a numeric value between 0 and 1") 
            base_rate = input("What is the (prior) proportion of true/present/positive cases you would expect overall?: ")
        else:
            break        
if guess=="1":
    sensitivity = input("If you have your prediction sensisitivity (proportion) enter it here, else hit return: ")
    if sensitivity != None and sensitivity != '':
        while True:
            try: 
                float(sensitivity)
            except:
                print("Please enter a numeric value between 0 and 1") 
                sensitivity = input("If you have your prediction sensisitivity (proportion) enter it here, else hit return: ")
            else:
                if not float(sensitivity) < 1 or not float(sensitivity)> 0:
                    print("Please enter a numeric value between 0 and 1") 
                    sensitivity = input("If you have your prediction sensisitivity (proportion) enter it here, else hit return: ")                    
                else:
                    print(get_output_sens(guess, base_rate, sensitivity))
                    raise SystemExit(0)
    else:
        fp_rate = input("If you have your false positive rate (proportion) enter it here, else hit return: ")
        if fp_rate != None and fp_rate != '':
            while True:
                try:
                    float(fp_rate)
                except:
                    print("Please enter a numeric value between 0 and 1")
                    fp_rate = input("If you have your false positive rate (proportion) enter it here, else hit return: ")
                else:
                    if not float(fp_rate) < 1 or not float(fp_rate)> 0:
                        print("Please enter a numeric value between 0 and 1")
                        fp_rate = input("If you have your false positive rate (proportion) enter it here, else hit return: ")                   
                    else:
                        sensitivity=1-float(fp_rate)
                        print(get_output_sens(guess, base_rate, sensitivity))
                        raise SystemExit(0)
        else:
            tp = input("If you have a count of correct true/present/positive predictions made, enter it here, else hit return: ")
            if tp==None or tp=='':
                print("More sensitivity information needed (e.g., tp and fp)")
                print(predict_base_rate(guess, base_rate))
                raise SystemExit(0)
            else:
                while True:
                    try:
                        float(tp)
                    except:
                        print("Please enter a numeric value")
                        tp = input("If you have a count of correct true/present/positive predictions made, enter it here, else hit return: ")
                    else:
                        break
            fp = input("If you have a count of INcorrect true/present/positive predictions made, enter it here, else hit return: ") 
            if fp==None or fp=='':
                print("More sensitivity information needed (e.g., tp and fp)")
                print(predict_base_rate(guess, base_rate))
                raise SystemExit(0)
            else:
                while True:
                    try:
                        float(fp)
                    except:
                        print("Please enter a numeric value")
                        fp = input("If you have a count of INcorrect true/present/positive predictions made, enter it here, else hit return: ")
                    else:                       
                        tp=float(tp)
                        fp=float(fp)
                        sensitivity = tp/(tp+fp)
                        print(get_output_sens(guess, base_rate, sensitivity))
                        raise SystemExit(0)

if guess=="0":
    specificity = input("If you have your prediction specificity (proportion) enter it here, else hit return: ")
    if specificity != None and specificity != '':
        while True:
            try: 
                float(specificity)
            except:
                print("Please enter a numeric value between 0 and 1") 
                specificity = input("If you have your prediction specificity (proportion) enter it here, else hit return: ")
            else:
                if not float(specificity) < 1 or not float(specificity)> 0:
                    print("Please enter a numeric value between 0 and 1") 
                    specificity = input("If you have your prediction specificity (proportion) enter it here, else hit return: ")                    
                else:
                    print(get_output_spec(guess, base_rate, specificity))
                    raise SystemExit(0)
    else:
        fn_rate = input("If you have your false negative rate (proportion) enter it here, else hit return: ")
        if fn_rate != None and fn_rate != '':
            while True:
                try:
                    float(fn_rate)
                except:
                    print("Please enter a numeric value between 0 and 1")
                    fn_rate = input("If you have your false negative rate (proportion) enter it here, else hit return: ")
                else:
                    if not float(fn_rate) < 1 or not float(fn_rate)> 0:
                        print("Please enter a numeric value between 0 and 1")
                        fn_rate = input("If you have your false negative rate (proportion) enter it here, else hit return: ")                   
                    else:
                        specificity=1-float(fn_rate)
                        print(get_output_spec(guess, base_rate, specificity))
                        raise SystemExit(0)
        else:
            tn = input("If you have a count of correct false/negative/absent predictions made, enter it here, else hit return: ")
            if tn==None or tn=='':
                print("More specificity information needed (e.g., tn and fn)")
                print(predict_base_rate(guess, base_rate))
                raise SystemExit(0)
            else:
                while True:
                    try:
                        float(tn)
                    except:
                        print("Please enter a numeric value")
                        tn = input("If you have a count of correct false/negative/absent predictions made, enter it here, else hit return: ")
                    else:
                        break
            fn = input("If you have a count of INcorrect false/negative/absent predictions made, enter it here, else hit return: ") 
            if fn==None or fn=='':
                print("More specificity information needed (e.g., tn and fn)")
                print(predict_base_rate(guess, base_rate))
                raise SystemExit(0)
            else:
                while True:
                    try:
                        float(fn)
                    except:
                        print("Please enter a numeric value")
                        fn = input("If you have a count of INcorrect false/negative/absent predictions made, enter it here, else hit return: ")
                    else:                       
                        tn=float(tn)
                        fn=float(fn)
                        specificity = tn/(tn+fn)
                        print(get_output_spec(guess, base_rate, specificity))
                        raise SystemExit(0)    