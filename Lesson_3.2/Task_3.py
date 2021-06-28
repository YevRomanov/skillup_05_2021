def task_3(side, sign, fill):
    space = " "
    if fill:
        for i in range(side):
            print(sign*side)
    else: 
        print(sign*side)
        for i in range(side-2):
            print(sign + space*(side-2) + sign)
        print(sign*side)

task_3(side=10, sign="*", fill=False)

# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********

# **********
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# **********
