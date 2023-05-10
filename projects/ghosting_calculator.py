###CODE STARTS HERE. 
total_number_of_messages=3000000
total_number_of_hours_between_first_message_and_last=500000
number_of_hours_since_last_message=1 
total_number_of_people_you_have_messaged=4
total_number_who_ended_up_ghosting=3

###################################################################
tot_ghost_prob=total_number_who_ended_up_ghosting/total_number_of_people_you_have_messaged

ghost_rate_prior=1/total_number_of_hours_between_first_message_and_last
msg_rate=total_number_of_messages/total_number_of_hours_between_first_message_and_last

import numpy as np

## Probability of no messages between t1 and t2, assuming no ghosting.
def no_msg(t1,t2):
    return np.exp(-msg_rate*(t2-t1))

## Probability of no ghosting between t1 and t2
def no_ghost(t1,t2):
    return (tot_ghost_prob*np.exp(-ghost_rate_prior *(t2-t1)) + (1-tot_ghost_prob))

#Probability of ghosting happening between t1 and t2
def ghost(t1,t2):
    return 1-no_ghost(t1,t2)

#probability of receiving no messages betweem t1 and t2 and also being ghosted between t1 and t2
def no_msg_and_ghost(t1,t2):
    z=0
    # for each small interval in the time range, we compute probability that we were *not* ghosted up that point, received *no* messages to that point,
    #  and *did* get ghosted in next interval 
    for i in range(t2-t1):
        z+=no_ghost(t1,t1+i-1)*no_msg(t1,t1+i-1)*ghost(t1+i-1,t1+i)
    return z

#probability of receiving no messages between t1 and t2, given that ghosting happened between t1 and t2.
def no_msg_given_ghost(t1,t2):
    return no_msg_and_ghost(t1,t2)/ghost(t1,t2)

#probability of receiving no messages between t1 and t2, and not being ghosted between t1 and t2
def no_msg_and_no_ghost(t1,t2):
    return no_msg(t1,t2)*no_ghost(t1,t2)

#probability of receiving no messages between t1 and t2
def no_msg_tot(t1,t2):
    return no_msg_and_no_ghost(t1,t2)+no_msg_and_ghost(t1,t2)

#probability of being ghosted between t1 and t2, assuming no messages between t1 and t2
def ghost_given_no_msg(t1,t2):
    return no_msg_given_ghost(t1,t2)*ghost(t1,t2)/no_msg_tot(t1,t2)

p=ghost_given_no_msg(total_number_of_hours_between_first_message_and_last,total_number_of_hours_between_first_message_and_last+number_of_hours_since_last_message)
#p=ghost_given_no_msg(10,20)

print("probability you have been ghosted is:",p)