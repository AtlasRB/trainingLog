#Imports
from tabulate import tabulate

#Creating the dataframe
dates1 = {} #An empty data frame which will be added to.
dates2 = {} #An empty data frame which will be added to.
dates3 = {} #An empty data frame which will be added to.


#1/12/23
title = 'Arms'
headers = ['Set One', 'Set Two', 'To Failure']

workout1 = [['12*22.5kg','8*25kg','7*27.5kg'],
            ['12*22.5kg','8*25kg','--------'],
            ['12*22.5kg','8*25kg','--------'],
            ['12*22.5kg','8*25kg','--------']]
table1 = 'Overhead\n\n' + tabulate(workout1, headers, tablefmt="pretty", showindex="never")

workout2 = [['12*21.25kg','8*26.25kg','5*31.25kg'],
            ['12*21.25kg','8*26.25kg','---------'],
            ['12*21.25kg','8*26.25kg','---------'],
            ['12*21.25kg','8*26.25kg','---------']]
table2 = '2A Curls\n\n' + tabulate(workout2, headers, tablefmt="pretty", showindex="never")

workout3 = [['12*8kg','8*10.5kg','6*13kg'],
            ['12*8kg','8*10.5kg','------'],
            ['12*8kg','8*10.5kg','------'],
            ['12*8kg','8*10.5kg','------']]
table3 = '1A Curls\n\n' + tabulate(workout3, headers, tablefmt="pretty", showindex="never")

notes = 'Keep strict Overhead form.' #Notes
dates1['1/12/23'] = [title, table1, table2, table3, notes] #Line to add to the datframe


title = 'Back'
headers = ['Set One', 'Set Two', 'To Failure']

workout1 = [['12*30kg','8*35kg','6*40kg'],
            ['12*30kg','8*35kg','------'],
            ['12*30kg','8*35kg','------'],
            ['12*30kg','8*35kg','------']]
table1 = 'Backrows\n\n' + tabulate(workout1, headers, tablefmt="pretty", showindex="never")

notes = '' #Notes
dates2['1/12/23'] = [title, table1, notes] #Line to add to the datframe



#4/12/23
title = 'Chest'
headers = ['Set One', 'Set Two', 'To Failure']

workout1 = [['12*40kg','8*45kg','4*50kg'],
            ['12*40kg','8*45kg','------'],
            ['12*40kg','8*45kg','------'],
            ['12*40kg','8*45kg','------']]
table1 = 'Bench Press\n\n' + tabulate(workout1, headers, tablefmt="pretty", showindex="never")

workout2 = [['12*22.5kg','8*27.5kg','5*32.5kg'],
            ['12*22.5kg','8*27.5kg','--------'],
            ['12*22.5kg','8*27.5kg','--------'],
            ['12*22.5kg','8*27.5kg','--------']]
table2 = 'Inclined\n\n' + tabulate(workout2, headers, tablefmt="pretty", showindex="never")

notes = '' #Notes
dates1['4/12/23'] = [title, table1, table2, notes] #Line to add to the datframe


title = 'Legs'
headers = ['Set One', 'Set Two', 'To Failure']

workout1 = [['12*45kg','8*50kg','12*55kg'],
            ['12*45kg','8*50kg','-------'],
            ['12*45kg','8*50kg','-------'],
            ['12*45kg','8*50kg','-------']]
table1 = 'Squats\n\n' + tabulate(workout1, headers, tablefmt="pretty", showindex="never")

workout2 = [['25*30kg','20*40kg','--------'],
            ['25*30kg','20*40kg','--------'],
            ['25*30kg','20*40kg','--------'],
            ['25*30kg','20*40kg','--------']]
table2 = 'Calf Dips\n\n' + tabulate(workout2, headers, tablefmt="pretty", showindex="never")

notes = 'Increase squat weight increments to 45kg set 1 - 55kg set 2 - 65kg to failure.' #Notes
dates2['4/12/23'] = [title, table1, table2, notes] #Line to add to the datframe



#8/12/23
title = 'Arms'
headers = ['Set One', 'Set Two', 'To Failure']

workout1 = [['12*22.5kg','8*25kg','7*27.5kg'],
            ['12*22.5kg','8*25kg','--------'],
            ['12*22.5kg','8*25kg','--------'],
            ['12*22.5kg','8*25kg','--------']]
table1 = 'Overhead\n\n' + tabulate(workout1, headers, tablefmt="pretty", showindex="never")

workout2 = [['12*21.25kg','8*26.25kg','8*31.25kg'],
            ['12*21.25kg','8*26.25kg','---------'],
            ['12*21.25kg','8*26.25kg','---------'],
            ['12*21.25kg','8*26.25kg','---------']]
table2 = '2A Curls\n\n' + tabulate(workout2, headers, tablefmt="pretty", showindex="never")

workout3 = [['12*8kg','8*10.5kg','6*13kg'],
            ['12*8kg','8*10.5kg','------'],
            ['12*8kg','8*10.5kg','------'],
            ['12*8kg','8*10.5kg','------']]
table3 = '1A Curls\n\n' + tabulate(workout3, headers, tablefmt="pretty", showindex="never")

notes = 'Keep strict Overhead form.\nIncrease 2A curls by 2.5kg' #Notes
dates1['8/12/23'] = [title, table1, table2, table3, notes] #Line to add to the datframe


title = 'Back'
headers = ['Set One', 'Set Two', 'To Failure']

workout1 = [['12*30kg','8*35kg','6*40kg'],
            ['12*30kg','8*35kg','------'],
            ['12*30kg','8*35kg','------'],
            ['12*30kg','8*35kg','------']]
table1 = 'Backrows\n\n' + tabulate(workout1, headers, tablefmt="pretty", showindex="never")

notes = '' #Notes
dates2['8/12/23'] = [title, table1, notes] #Line to add to the datframe



#12/12/23
title = 'Chest'
headers = ['Set One', 'Set Two', 'To Failure']

workout1 = [['12*40kg','8*45kg','5*50kg'],
            ['12*40kg','8*45kg','------'],
            ['12*40kg','8*45kg','------'],
            ['12*40kg','7*45kg','------']]
table1 = 'Bench Press\n\n' + tabulate(workout1, headers, tablefmt="pretty", showindex="never")

workout2 = [['12*22.5kg','8*27.5kg','8*32.5kg'],
            ['12*22.5kg','8*27.5kg','--------'],
            ['12*22.5kg','8*27.5kg','--------'],
            ['12*22.5kg','8*27.5kg','--------']]
table2 = 'Inclined\n\n' + tabulate(workout2, headers, tablefmt="pretty", showindex="never")

notes = 'Adjust Inclined angle by 30°.\nIncrease inclined weight by 2.5kg.' #Notes
dates1['12/12/23'] = [title, table1, table2, notes] #Line to add to the datframe


title = 'Legs'
headers = ['Set One', 'Set Two', 'To Failure']

workout1 = [['12*45kg','8*55kg','8*65kg'],
            ['12*45kg','8*55kg','------'],
            ['12*45kg','8*55kg','------'],
            ['12*45kg','8*55kg','------']]
table1 = 'Squats\n\n' + tabulate(workout1, headers, tablefmt="pretty", showindex="never")

workout2 = [['25*30kg','20*40kg','--------'],
            ['25*30kg','20*40kg','--------'],
            ['25*30kg','20*40kg','--------'],
            ['25*30kg','20*40kg','--------']]
table2 = 'Calf Dips\n\n' + tabulate(workout2, headers, tablefmt="pretty", showindex="never")

notes = 'Increase squat weight by 5kg.' #Notes
dates2['12/12/23'] = [title, table1, table2, notes] #Line to add to the datframe



#14/12/23
title = 'Abs'
headers = ['Set One', 'Set Two', 'To Failure']

workout1 = [['15*10kg','10*15kg','------'],
            ['15*10kg','10*15kg','------'],
            ['15*10kg','10*15kg','------'],
            ['15*10kg','10*15kg','------']]
table1 = 'Declined Sit Ups\n\n' + tabulate(workout1, headers, tablefmt="pretty", showindex="never")

notes = '' #Notes
dates1['14/12/23'] = [title, table1, notes] #Line to add to the datframe


title = 'Shoulders'
headers = ['Set One', 'Set Two', 'To Failure']

workout1 = [['15*4.5kg','10*5.5kg','------'],
            ['15*4.5kg','10*5.5kg','------'],
            ['15*4.5kg','10*5.5kg','------'],
            ['15*4.5kg','10*5.5kg','------']]
table1 = 'Side Lateral Raises\n\n' + tabulate(workout1, headers, tablefmt="pretty", showindex="never")

notes = '' #Notes
dates2['14/12/23'] = [title, table1, notes] #Line to add to the datframe



#15/12/23
title = 'Arms'
headers = ['Set One', 'Set Two', 'To Failure']

workout1 = [['12*22.5kg','8*25kg','8*27.5kg'],
            ['12*22.5kg','8*25kg','--------'],
            ['12*22.5kg','8*25kg','--------'],
            ['12*22.5kg','8*25kg','--------']]
table1 = 'Overhead\n\n' + tabulate(workout1, headers, tablefmt="pretty", showindex="never")

workout2 = [['12*23.75kg','8*28.75kg','8*33.75kg'],
            ['12*23.75kg','8*28.75kg','---------'],
            ['12*23.75kg','8*28.75kg','---------'],
            ['12*23.75kg','8*28.75kg','---------']]
table2 = '2A Curls\n\n' + tabulate(workout2, headers, tablefmt="pretty", showindex="never")

notes = '' #Notes
dates1['15/12/23'] = [title, table1, table2, notes] #Line to add to the datframe


title = 'Back'
headers = ['Set One', 'Set Two', 'To Failure']

workout1 = [['10','8','--'],
            ['10','8','--'],
            ['10','8','--'],
            ['10','8','--']]
table1 = 'Pullups\n\n' + tabulate(workout1, headers, tablefmt="pretty", showindex="never")

notes = '' #Notes
dates2['15/12/23'] = [title, table1, notes] #Line to add to the datframe



#18/12/23
title = 'Chest'
headers = ['Set One', 'Set Two', 'To Failure']

workout1 = [['12*40kg','8*45kg','5*50kg'],
            ['12*40kg','8*45kg','------'],
            ['12*40kg','7*45kg','------'],
            ['12*40kg','7*45kg','------']]
table1 = 'Bench Press\n\n' + tabulate(workout1, headers, tablefmt="pretty", showindex="never")

workout2 = [['12*25kg','8*30kg','7*35kg'],
            ['12*25kg','8*30kg','------'],
            ['12*25kg','8*30kg','------'],
            ['12*25kg','8*30kg','------']]
table2 = 'Inclined\n\n' + tabulate(workout2, headers, tablefmt="pretty", showindex="never")

notes = '' #Notes
dates1['18/12/23'] = [title, table1, table2, notes] #Line to add to the datframe


title = 'Legs'
headers = ['Set One', 'Set Two', 'To Failure']

workout1 = [['12*50kg','8*60kg','6*70kg'],
            ['12*50kg','8*60kg','------'],
            ['12*50kg','8*60kg','------'],
            ['12*50kg','8*60kg','------']]
table1 = 'Squats\n\n' + tabulate(workout1, headers, tablefmt="pretty", showindex="never")

notes = '' #Notes
dates2['18/12/23'] = [title, table1, notes] #Line to add to the datframe



#21/12/23
title = 'Abs'
headers = ['Set One', 'Set Two', 'To Failure']

workout1 = [['15*10kg','10*15kg','------'],
            ['15*10kg','10*15kg','------'],
            ['15*10kg','10*15kg','------'],
            ['15*10kg','10*15kg','------']]
table1 = 'Declined Sit Ups\n\n' + tabulate(workout1, headers, tablefmt="pretty", showindex="never")

notes = '' #Notes
dates1['21/12/23'] = [title, table1, notes] #Line to add to the datframe


title = 'Shoulders'
headers = ['Set One', 'Set Two', 'To Failure']

workout1 = [['15*4.5kg','10*5.5kg','------'],
            ['15*4.5kg','10*5.5kg','------'],
            ['15*4.5kg','10*5.5kg','------'],
            ['15*4.5kg','10*5.5kg','------']]
table1 = 'Side Lateral Raises\n\n' + tabulate(workout1, headers, tablefmt="pretty", showindex="never")

notes = '' #Notes
dates2['21/12/23'] = [title, table1, notes] #Line to add to the datframe



#22/12/23
title = 'Arms'
headers = ['Set One', 'Set Two', 'To Failure']

workout1 = [['12*16.25kg','8*21.25kg','8*26.25kg'],
            ['12*16.25kg','8*21.25kg','---------'],
            ['12*16.25kg','8*21.25kg','---------'],
            ['12*16.25kg','8*21.25kg','---------']]
table1 = 'Skull Crushers\n\n' + tabulate(workout1, headers, tablefmt="pretty", showindex="never")

workout2 = [['12*23.75kg','8*28.75kg','8*33.75kg'],
            ['12*23.75kg','8*28.75kg','---------'],
            ['12*23.75kg','8*28.75kg','---------'],
            ['12*23.75kg','8*28.75kg','---------']]
table2 = '2A Curls\n\n' + tabulate(workout2, headers, tablefmt="pretty", showindex="never")

notes = 'Replaced Overhead with Skull Crushers.\nIncrease Skull Crusher weight by 2.5kg.\nIncresae 2A Curl weight by 2.5kg.' #Notes
dates1['22/12/23'] = [title, table1, table2, notes] #Line to add to the datframe


title = 'Back'
headers = ['Set One', 'Set Two', 'To Failure']

workout1 = [['12*30kg','8*35kg','11*40kg'],
            ['12*30kg','8*35kg','-------'],
            ['12*30kg','8*35kg','-------'],
            ['12*30kg','8*35kg','-------']]
table1 = 'Backrows\n\n' + tabulate(workout1, headers, tablefmt="pretty", showindex="never")

workout2 = [['10','--','--'],
            [' 8','--','--'],
            [' 6','--','--'],
            [' 6','--','--']]
table2 = 'Pullups\n\n' + tabulate(workout1, headers, tablefmt="pretty", showindex="never")

notes = 'Increase Backrows weight to:\nSet one - 30kg\nSet two - 40kg\nTo Failure - 50kg' #Notes
dates2['22/12/23'] = [title, table1, table2, notes] #Line to add to the datframe



#27/12/23
title = 'Legs'
headers = ['Set One', 'Set Two', 'To Failure']

workout1 = [['12*50kg','8*60kg','6*70kg'],
            ['12*50kg','8*60kg','------'],
            ['12*50kg','8*60kg','------'],
            ['12*50kg','8*60kg','------']]
table1 = 'Squats\n\n' + tabulate(workout1, headers, tablefmt="pretty", showindex="never")

notes = '' #Notes
dates1['27/12/23'] = [title, table1, notes] #Line to add to the datframe



#28/12/23
title = 'Arms'
headers = ['Set One', 'Set Two', 'To Failure']

workout1 = [['12*18.75kg','8*23.75kg','3*28.75kg'],
            ['12*18.75kg','8*23.75kg','---------'],
            ['12*18.75kg','8*23.75kg','---------'],
            ['12*18.75kg','8*23.75kg','---------']]
table1 = 'Skull Crushers\n\n' + tabulate(workout1, headers, tablefmt="pretty", showindex="never")

workout2 = [['12*26.25kg','8*31.25kg','4*36.25kg'],
            ['12*26.25kg','8*31.25kg','---------'],
            ['12*26.25kg','8*31.25kg','---------'],
            ['12*26.25kg','8*31.25kg','---------']]
table2 = '2A Curls\n\n' + tabulate(workout2, headers, tablefmt="pretty", showindex="never")

notes = 'Replaced Overhead with Skull Crushers.\nIncrease Skull Crusher weight by 2.5kg.\nIncresae 2A Curl weight by 2.5kg.' #Notes
dates1['28/12/23'] = [title, table1, table2, notes] #Line to add to the datframe


title = 'Back'
headers = ['Set One', 'Set Two', 'To Failure']

workout1 = [['10','--','--'],
            [' 8','--','--'],
            [' 6','--','--'],
            [' 6','--','--']]
table1 = 'Pullups\n\n' + tabulate(workout1, headers, tablefmt="pretty", showindex="never")

notes = '' #Notes
dates2['28/12/23'] = [title, table1, notes] #Line to add to the datframe