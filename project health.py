#creating the database
import pandas as pd
import matplotlib.pyplot as plt
import random

df1=pd.DataFrame([{'NAME':'Mr Lawrence Flynn','AGE':42,'GENDER':'Male','WEIGHT(in kg)':85,'HEIGHT(in cm)':171,'Chronic Issues':'Hypertension','Steps target(daily)':9000,'water target(daily)':10,'sleep hours':8,'active time(mins)':60},
                {'NAME':'Ms Linda Flynn' ,'AGE':40,'GENDER':'Female','WEIGHT(in kg)':72,'HEIGHT(in cm)':164,'Chronic Issues':'None','Steps target(daily)':9000,'water target(daily)':9,'sleep hours':8,'active time(mins)':60},
                {'NAME':'Phineas','AGE':11,'GENDER':'Male','WEIGHT(in kg)':25,'HEIGHT(in cm)':128,'Chronic Issues':'None','Steps target(daily)':10000,'water target(daily)':12,'sleep hours':9,'active time(mins)':90},
                {'NAME':'Ferb' ,'AGE':15,'GENDER':'Male','WEIGHT(in kg)':43,'HEIGHT(in cm)':145,'Chronic Issues':'None','Steps target(daily)':12000,'water target(daily)':11,'sleep hours':9,'active time(mins)':60},
                {'NAME':'Candace','AGE':28,'GENDER':'Female','WEIGHT(in kg)':41,'HEIGHT(in cm)':161,'Chronic Issues':'None','Steps target(daily)':11000,'water target(daily)':9,'sleep hours':7,'active time(mins)':70},
                {'NAME':'Mr Milo Murphy','AGE':20,'GENDER':'Male','WEIGHT(in kg)':60,'HEIGHT(in cm)':176,'Chronic Issues':'None','Steps target(daily)':13000,'water target(daily)':10,'sleep hours':7,'active time(mins)':80},
                {'NAME':'Ms melissa','AGE':26,'GENDER':'Female','WEIGHT(in kg)':45,'HEIGHT(in cm)':167,'Chronic Issues':'None','Steps target(daily)':11000,'water target(daily)':11,'sleep hours':8,'active time(mins)':70},
                {'NAME':'Isabella','AGE':8,'GENDER':'Female','WEIGHT(in kg)':21,'HEIGHT(in cm)':118,'Chronic Issues':'None','Steps target(daily)':14000,'water target(daily)':12,'sleep hours':10,'active time(mins)':120},
                {'NAME':'Mr Renold','AGE':72,'GENDER':'Male','WEIGHT(in kg)':70,'HEIGHT(in cm)':167,'Chronic Issues':'diabetes,arthritis,heart patient','Steps target(daily)':6000,'water target(daily)':7,'sleep hours':7,'active time(mins)':45},
                {'NAME':'Ms Kenna','AGE':65,'GENDER':'Male','WEIGHT(in kg)':65,'HEIGHT(in cm)':158,'Chronic Issues':'diabetes, hypertension, cervical spondylitis','Steps target(daily)':6000,'water target(daily)':8,'sleep hours':6,'active time(mins)':45}])
df1.to_csv('C:/Users/Jayantika/Desktop/ip.csv')
df=pd.read_csv('C:/Users/Jayantika/Desktop/ip.csv')
#welcoming the cutomer
print('             ***********************************')
print('                    HEALTHY Life-Track!!                    ')
print('             ***********************************')
print('(Lets pledge to make ourselves better for a better future of our own)')
print()
condn=input('Already a member of Healthy Life-Track?? ')
if condn=='yes' or condn=='Yes':
    print()
    print('                   WELCOME BACK!!')
    name=input('enter your username: ')
    password=input('enter the password: ')
    if name in df.values and password=='984532':
        index = df.index
        check_name = df["NAME"] == name
        a= index[check_name]
        a= a.tolist()
        string = [str(integer) for integer in a]
        list_string = "".join(string)
        string_integer = int(list_string)
        print()
        print('------------------------------------------------')
        print('HERE IS YOUR PERSONAL INFORMATION: ', end='\n')
        print('------------------------------------------------')
        print(df.loc[string_integer,:])
        print('------------------------------------------------')
        #modifying personal information
        mod=input("Do you want to make some modifications in your personal information? (yes/no) :")
        print()
        if mod=='yes' or mod=='Yes':
            print('what do u want to change(weight/height)?')
            change=input('->')
            if change=='weight':
                print('enter your new weight(in kg): ')
                n_wt=int(input('->')) 
                o_wt= df.at[string_integer,'WEIGHT(in kg)'] 
                df.replace({o_wt:n_wt}, inplace=True) 
                print()
                print('YOUR DETAILS HAVE BEEN MODIFIED') 
                print()
                print('Now we may proceed!')
                
            elif change=='height': 
                print('enter your new height(in cm): ') 
                n_ht=int(input('->')) 
                o_ht= df.at[string_integer,'HEIGHT(in cm)'] 
                df.replace({o_ht:n_ht}, inplace=True)
                print()
                print('YOUR DETAILS HAVE BEEN MODIFIED') 
                print()
                print('Now we may proceed!')
        else: 
            print('Cool!! we may proceed then.')
        
        #modifying targets
        print('---------------------------------------------')   
        d_mod=input("Do you want to make some modifications in your Daily Targets? (yes/no): ")
        if d_mod=='yes' or d_mod=='Yes':
            print('what do u want to change(steps/water/sleep/active time)?')
            t_change=input('->')
            if t_change=='steps':
                print('enter your new steps target(daily): ')
                n_st=int(input('->')) 
                o_st= df.at[string_integer,'Steps target(daily)'] 
                df.replace({o_st:n_st}, inplace=True) 
                print('the changes have been made') 
                print('Now we may proceed!')
            elif t_change=='water': 
                print('enter your new water target: ') 
                n_wt=int(input('->')) 
                o_wt= df.at[string_integer,'water target(daily)'] 
                df.replace({o_wt:n_wt}, inplace=True) 
                print('the changes have been made') 
                print('Now we may proceed!')
            
            elif t_change=='sleep': 
                print('enter your new sleep hours: ') 
                n_slt=int(input('->')) 
                o_slt= df.at[string_integer,'sleep hours'] 
                df.replace({o_slt:n_slt}, inplace=True) 
                print('the changes have been made') 
                print('Now we may proceed!')
                
            elif t_change=='active time': 
                print('enter your new active time: ') 
                n_at=int(input('->')) 
                o_at= df.at[string_integer,'active time(mins)'] 
                df.replace({o_at:n_at}, inplace=True) 
                print('the changes have been made') 
                print('Now we may proceed!')
        else: 
            print('Cool!! we may proceed then.')
        
        print('-----------------------------------------------')
        #display the modified table
        print()   
        display=input('Do you want to see the modified information?(yes/no): ')
        print()
        if display=='yes':
            print(df.loc[string_integer,:]) 
            print()
        else:
            print('ok then, lets continue!')
        print('-----------------------------------------------')
        
        #weekly analysis
        print()
        print('Do you want to have weekly analysis?(yes/no): ')
        w_ana=input('->')
        li1=[]
        li2=[]
        li3=[]
        li4=[]
        days=['Day 1','Day 2','Day 3','Day 4','Day 5','Day 6','Day 7']
        
        if w_ana=='yes':
            print('1. water intake')
            print('2. steps')
            print('3. sleep hrs')
            print('4. active time')
            w_ch=input('Which one do you want to see? (choose 2 numbers at most): ')
            print()
            
            if w_ch=='1' or w_ch=='1 and 2' or w_ch=='1 and 3' or w_ch=='1 and 4':
                print('--------------------------------------------------')
                print('ENTER your water intake per day')
                print()
                for x in range(1,8):
                    print('Day',x,': ',end='')
                    a=int(input())
                    li1.append(a)
                avg1=(sum(li1))/7
                print()
                print('THE AVG FOR THE WEEK IS: ',avg1)
                print()
                age= df.at[string_integer,'AGE']
                check_water= df.at[string_integer,'water target(daily)']
                #check_avg
                if age<60 and 8<avg1<12:
                    print('Good work!! Keep it up.') 
                elif age>60 and 6<avg1<8:
                    print('Good work!! Keep it up.') 
                else: 
                    print('Your avg weekly water intake should be improved','the range is: ','->8-12 glasses for below 60yrs of age','->6-8 glasses for above 60yrs of age',sep='\n')  
                #check_target
                print()
                if age<60 and 8<check_water<12:
                    print('also we can say that your set daily target is alright so make sure u follow it!') 
                elif age>60 and 6<check_water<8:
                    print('also we can say that your set daily target is alright so make sure u follow it! ') 
                else: 
                    print('hey buddy! lets keep a better target for better results')
                #graph
                plt.bar(days,li1)  
                plt.xlabel('Days of the week')  
                plt.ylabel('values per week')  
                print() 
                print('           LETS HAVE A LOOK ON THE GRAPH AS WELL')  
                plt.show()
                
            
            if w_ch=='2' or w_ch=='2 and 3' or w_ch=='1 and 2' or w_ch=='2 and 4':
                print('--------------------------------------------------')
                print('ENTER your steps per day')
                print()
                for x in range(1,8):
                    print('Day',x,': ',end='')
                    a=int(input())
                    li2.append(a)
                avg2=(sum(li2))/7
                print('avg of the week is: ',avg2)
                age= df.at[string_integer,'AGE']
                check_steps= df.at[string_integer,'Steps target(daily)']
                if check_steps>6000:
                    print('your set target is alright!')
                else:
                    print('lets keep a better target for better results.')
                if age<30 and 8000<avg2:
                    print('Good work!! Keep it up.')
                elif 30>age>60 and 7000<avg2:
                    print('good work!! Keep it up.')
                elif age>60 and 5000<avg2:
                    print('Good work!! Keep it up.') 
                else: 
                    print('your steps in a day should be little more!! need somemore hardwork to stay fit.',sep='\n')  
                plt.bar(days,li2)  
                plt.xlabel('Days of the week')  
                plt.ylabel('values per week')  
                print() 
                print('YOU CAN ALSO SEE THE GRAPH FOR THE SAME')  
                plt.show()
                print('-----------------------------------------------')
            
            if w_ch=='3' or w_ch=='2 and 3' or w_ch=='1 and 3' or w_ch=='3 and 4':
                print('--------------------------------------------------')
                print('ENTER your sleep hours per day')
                print()
                for x in range(1,8):
                    print('Day',x,': ',end='')
                    a=int(input())
                    li3.append(a) 
                avg3=(sum(li3))/7
                print()
                print('THE AVG FOR THIS WEEK IS: ',avg3)
                age= df.at[string_integer,'AGE']
                check_sl= df.at[string_integer,'sleep hours']
                print()
                if age<60 and 10>check_sl>6:
                    print('Your set target is perfect') 
                elif age>=60 and 5<check_sl:
                    print('Your set target is perfect') 
                else: 
                    print('lets keep a better target for better results')
                if age<60 and 5>avg3:
                    print('Good work!! Keep it up.') 
                elif age>60 and 6<avg3<8:
                    print('Good work!! Keep it up.') 
                else: 
                    print('BUT your sleep schedule should be improved.Remeber sleep is the best meditation ;)',sep='\n')  
                plt.bar(days,li3)  
                plt.xlabel('Days of the week')  
                plt.ylabel('values per week')  
                print() 
                print('            LETS HAVE A LOOK ON THE GRAPH AS WELL')  
                plt.show()
                print('-----------------------------------------------')
            
            if w_ch=='4' or w_ch=='1 and 4' or w_ch=='2 and 4' or w_ch=='3 and 4':
                print('--------------------------------------------------')
                print('ENTER your active time per day')
                print()
                for x in range(1,8):
                    print('Day',x,': ',end='')
                    a=int(input())
                    li4.append(a) 
                avg=(sum(li4))/7
                print('avg of the week is: ',avg)
                age= df.at[string_integer,'AGE']
                check_act= df.at[string_integer,'active time(mins)']
                if age<60 and avg>60:
                    print('Your set target is alright') 
                elif age>60 and avg>40:
                    print('Your set target is alright') 
                else: 
                    print('lets improve the active time for better results!')
                if age<60 and 8<avg<12:
                    print('Good work!! Keep it up.') 
                elif age>60 and 6<avg<8:
                    print('Good work!! Keep it up.') 
                else: 
                    print('your water intake should be improved','the range is: ','8-12 glasses for below 60yrs of age','6-8 glasses for above 60yrs of age',sep='\n')  
                plt.bar(days,li4)  
                plt.xlabel('Days of the week')  
                plt.ylabel('values per week')  
                print() 
                print('YOU CAN ALSO SEE THE GRAPH FOR THE SAME')  
                plt.show()
                print('-----------------------------------------------')
        else:
            print('aah! u seem confident lets proceed')
        print()
        print('-----------------------------------------------')
        yn=input('Lets run a quick daily analysis, would u like to?(yes/no): ')
        
        if yn=='yes':
            print('Now enter the Values')
            print()
            print('1. Blood Pressure -> ')
            bp_s=float(input('enter systolic(upper value) ->'))
            bp_d=float(input('enter diastolic(lower value) ->'))
            
            blood_sugar=float(input('2. blood sugar(RBS-random blood sugar before bed) -> ')) 
            bt=float(input('3. body temperature -> ')) 
            pr=int(input('4. pulse rate -> '))
            sp=int(input('5. spo2 levels -> '))
            print()
            print('--------------------------------------------------')
            print('Here is your report:')
            print('--------------------------------------------------')
            #BP
            if 60<=bp_d<=80 and 90<=bp_s<=120:
                print('BP: normal')
                print('normal range is:systolic 90-120, diastolic 60-80 ')
                print()
            else:
                print('BP: out of range')
                print('normal range is:systolic 90-120, diastolic 60-80')
                print()
            #blood sugar
            if 90<blood_sugar<120:
                print('Blood sugar: normal')
                print('normal range is: before meals or after waking up=80-120')
                print('                 before bed=100-140')
                print()
            else:
                print('blood sugar: out of range')
                print('normal range is: before meals or after waking up=80-120')
                print('                 before bed=100-140')
                print()
            #body temperature
            if 97.4<=bt<=99.3:
                print('Body temp: normal')
                print('normal range is:97.4-99.3')
                print()
            else:
                print('body temp: out of range')
                print('normal range is:97.4-99.3')
                print()
            #pulse rate
            if 94<pr<100:
                print('pulse rate: normal')
                print('normal range is:94-100')
                print()
            else:
                print('pulse rate: out of range')
                print('normal range is:94-100')
                print()
            #spo2
            if 94<=sp<=99:
                print('spo2 level: normal')
                print('normal range is: 94-99')
                print()    
            else:
                print('pulse rate: its out of range')
                print('normal range is: 94-99')
                print() 
        else:
            print('you seem confuident enough')
        print('-----------------------------------------------')
        
        #BMI check
        bmi=input('Lastly would you like to check your BMI? ')
        if bmi=='yes':
            wt=df.at[string_integer,'WEIGHT(in kg)']
            ht=df.at[string_integer,'HEIGHT(in cm)']
            ht_m=ht/100
            cal=wt/(ht_m)**2
            print('Your BMI value is: ',cal)
            if cal<=18.5:
                print('you are underweight. Pls take proper meals as specified by your nutritionist')
            elif 18.5<=cal<=24.9:
                print('wohoo!! your BMI is in normal range')
            elif 25<=cal<=29.9:
                print('u are overwight. pls dont forget your daily fitness routine!!')
            elif cal>=30:
                print('You are obese. pls consult a doctor and take proper steps')
        else:
            print('ok we may proceed then!!')
        print('-----------------------------------------------')
        
        #tips
        print('So as we come to an end lets have  amazing Bonus TIP for today!!')
        tip=random.choice(['Don’t drink sugar calories as sugary drinks are among the most fattening items you can put into your body.',
                           'Eat nuts, despite being high in fat, nuts are incredibly nutritious and healthy but make sure there is a limit :)',
                           'Eat fatty fish, it is a great source of high-quality protein and healthy fat.',
                           'Get enough sleep,the importance of getting enough quality sleep cannot be overstated.',
                           'Drink some water, especially before meals, drinking enough water can have numerous benefits.',
                           'Avoid bright lights before sleep. When you’re exposed to bright lights in the evening, it may disrupt your production of the sleep hormone melatonin',
                           'Take vitamin D3 if you don’t get much sun exposure. Sunlight is a great source of vitamin D.',
                           'Do some cardio. Doing aerobic exercise, also called cardio, is one of the best things you can do for your mental and physical health.'])
        print()
        print('So the tip of the day for u is: ')
        print(tip)
        print('-----------------------------------------------')
        
        #feedback
        #doctor check ups
    else:
        print('either password or username is incorrect.pls check')
    
else:
    print()
    print('Join Healthy LIfe-track to get the best tips and keep a check!!')
    print('contact:+919676829891 for more details')

# reminder abt regular doctor check ups feedback 
