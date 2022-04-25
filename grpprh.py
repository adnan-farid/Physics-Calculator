equationType = input('Please enter what type of equation you would like to use by typing "Force" or "BryanEquation":')

#defining inputs for variables in the force equation and defining the units for each variable
if equationType == 'Force':
    force = input('Please enter the force value or type "unknown" if you want to solve for it:')
    mass = input('Please enter the mass value or type "unknown" if you want to solve for it:')
    acceleration = input('Please enter the acceleration value or type "unknown" if you want to solve for it:')
elif equationType != 'Force' or equationType != "Bryan's Equation":
    print('Please enter a valid equation type.')
if equationType == 'Force':
    unitF = input('Please enter the unit of force you would like (type "N" for Newtons):')
    unitM = input('Please enter the unit of mass you would like (type "g" for grams, and "kg" for kilograms):')
    unitA = input('Please enter the unit of acceleration you would like (type "ms" for meters per second squared or "kms" '
                  'for kilometers per second squared):')
#calculations if the user wants to solve for force
if force == 'unknown' and unitM == 'kg' and unitA == 'ms' and unitF == 'N':
    force = float(mass) * float(acceleration)
    print('The force is equal to'+ ' ' + str(force) + ' '+ 'Newtons.')
elif force == 'unknown' and unitM == 'g' and unitA == 'ms' and unitF == 'N':
    force = (float(mass) * float(acceleration)) / 1000
    print('The force is equal to'+ ' ' + str(force) + ' '+ 'Newtons.')
elif force == 'unknown' and unitM == 'kg' and unitA == 'kms' and unitF == 'N':
    force = (float(mass)*float(acceleration)) * 1000
    print('The force is equal to' + ' ' + str(force) + ' ' + 'Newtons.')
elif force == 'unknown' and unitM == 'g' and unitA == 'kms'and unitF == 'N':
    force = float(mass)*float(acceleration)
    print('The force is equal to' + ' ' + str(force) + ' ' + 'Newtons.')
#Calculations if the user wants to solve for mass
elif mass == 'unknown' and unitM =='g' and unitA == 'ms' and unitF == 'N':
    mass = (float(force)/float(acceleration)) * 1000
    print('The mass is equal to' + ' ' + str(mass) + ' ' + 'grams.')
elif mass == 'unknown' and unitM == 'g' and unitA == 'kms' and unitF == 'N':
    mass = (float(force)/float(acceleration))
    print('The mass is equal to' + ' ' + str(mass) + ' ' + 'grams.')
elif mass == 'unknown' and unitM == 'kg' and unitA == 'ms' and unitF == 'N':
    mass = (float(force)/float(acceleration))
    print('The mass is equal to' + ' ' + str(mass) + ' ' + 'kilograms.')
elif mass == 'unknown' and unitM == 'kg' and unitA == 'kms' and unitF == 'N':
    mass = (float(force)/float(acceleration)) / 1000
    print('The mass is equal to' + ' ' + str(mass) + ' ' + 'kilograms.')
#Calculations if the user wants to solve for acceleration
elif acceleration == 'unknown' and unitM == 'g' and unitA == 'ms' and unitF == 'N':
    acceleration == (float(force)/float(mass)) * 1000
    print('The acceleration is equal to' + ' ' + str(acceleration) + ' ' + 'meters per second squared.')
elif acceleration == 'unknown' and unitM == 'g' and unitA == 'kms' and unitF == 'N':
    acceleration = (float(force)/float(mass))
    print('The acceleration is equal to' + ' ' + str(acceleration) + ' ' + 'kilometers per second squared.')
elif acceleration == 'unknown' and unitM == 'kg' and unitA == 'ms' and unitF == 'N':
    acceleration = (float(force)/float(mass))
    print('The acceleration is equal to' + ' ' + str(acceleration) + ' ' + 'meters per second squared.')
elif acceleration == 'unknown' and unitM == 'kg' and unitA == 'kms' and unitF == 'N':
    acceleration = (float(force)/float(mass)) / 1000
#in case an invalid string value or float number/integer is entered
else:
    print('Please recheck your values into the calculator (make sure you do not include spaces or unnecessary capitaliza'
          'tion nor units).')