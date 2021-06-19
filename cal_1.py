#function 1 extracts the words onto an array

def word_get(filename):
    fileObj = open(filename, "r")  # opens the file in read mode
    word_array = fileObj.read().split()  # puts the file into an array
    wordcount = len(word_array)  # gives the length of the array, useful for while loop
    return word_array

#print(word_get("text.txt"))


def date_get(word_array):

    wordcount = len(word_array)    #gives the length of the array, useful for while loop
#    print(wordcount) #total amount of words

    a = 0                       #loop/index controller
    tf_array = []               #empty array for adding the indices of TRUE/FALSE array positions.
    while a < wordcount:        #a starts at 0 but wordcount starts at 1
         if word_array[a] == "TRUE" or word_array[a] == "FALSE":   #abusing checkbox format
            tf_array.append(a)                                     #position is added to array
#            print("Test" + str(a))                                 #debugging step, to make sure while loop and if is enterd
            a += 1
         else:
            a += 1


#    print(tf_array)        #debugging, check array is correct

    tf_array_length = len(tf_array)
#    print("tf_array_length:")
#    print(tf_array_length)
    print("loop 1 exited")  # debugging step for loop 1
#i want to pull out dates (1 less than T/F array pos)




    b = 0  #while loop 2 controller
    date_position_array = []
    while b < tf_array_length:
        one_less = tf_array[b] - 1
        date_position_array.append(one_less)
        b += 1
#    print("one_less_array:")
#    print(one_less_array)      #debugging step
    print("loop 2 exited")     #debugging step for loop 2 success

    c = 0  #while loop 3 controller
    date_str_array = []
    api_datetime_array = []
    while c < tf_array_length:
        date_position = date_position_array[c]     #pulls out each individual number of date position from array
        date_str = word_array[date_position]     #refers back to original word array to pull out the date
        api_date_time = datetime_convert(date_str)   #calls upon def1 to convert the date string into
                                                    #google api compatible dates
#        print("variable test " + str(api_date_time))   #debugging step
        date_str_array.append(date_str)
        api_datetime_array.append(api_date_time)

        c+=1
#    print(api_datetime_array)               #prints api compatible str array
#    print(date_str_array)                   #debugging step to see if dates are right
    print("loop 3 exited")                  #debugging for loop 3

    # end of the line, will return api compatible dates (like return 0;)

    return api_datetime_array, date_position_array

def datetime_convert(date_str):
    #datetime is called upon in loop 3 on def 2.


    from datetime import datetime

    date_month = date_str   #variable imported from function 2 via fn input
    year = "/21"
    time = " 09:00:00"

    date_time_str = date_month + year + time
#    print("test" + date_time_str)       debugging step

    date_time_obj = datetime.strptime(date_time_str, '%d/%m/%y %H:%M:%S')
    date_time_test = date_time_obj.strftime("%y-%m-%dT%H:%M:%S")
    API_datetime = str(date_time_test) + "+10:00"
#    print(API_datetime)
#    print(date_time_obj)            #debugging step

    return API_datetime

def desc_get(word_array1,date_pos_array):
#debugging steps
#    print("test " + str(word_array1))
#    print("test "+ str(date_pos_array))
    no_events = len(date_pos_array)
    a = 0
    b = 0
    prev_date = 0
    event_str = ""
    event_array = []
    while (a < no_events):
        date_location = date_pos_array[a]
        while(prev_date<date_location):
            event_str += word_array1[prev_date] + " "
            prev_date+=1
        prev_date = date_location + 2
        a+=1
        event_array.append(event_str)
        event_str = ""
#    print(event_array)





    return event_array




#SUMMARY UP TO LOOP 3:
    #api_datetime_array is an array that contains the dates in a format that's compatible
    #with gcal API.

    #loop 1 abuses the TRUE/FALSE and arrays them
    #loop 2 simply arrays 1 less than loop 1 to obtain date position.
    #loop 3
        #first uses loop2 to index and retrieve date strings from the original statement
        #then calls upon function 1 to convert the date string (08/06) to GCAL API compatible strings.

#THINGS TO DO:
    #extract the description
    #if the "date" in front of TRUE/FALSE is not given, or ASAP give special conditions.
        #if else before loop 3?



    #    print(wordcount) #total amount of words






wordarray = word_get("text.txt")
api_datetime_array, date_position_array = date_get(wordarray)
#print(date_position_array)
print(api_datetime_array)

event_array = desc_get(wordarray,date_position_array)
print(event_array)
#puts extracted words into array for def 2 and 3
#print(read_file("text.txt"))
#from def 2 extracts array of gcal compatible dates











