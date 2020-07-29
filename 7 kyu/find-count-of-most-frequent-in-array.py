#Complete the function to find the count of the most frequent item of an array. You can assume that input is an array of integers. For an empty array return 0

def most_frequent_item_count(collection):
    counter = 0
    
    if len(collection) == 0:
        return 0;
    else:
        for i in collection: 
            curr_frequency = collection.count(i) 
            if(curr_frequency > counter): 
                counter = curr_frequency 
                
    return counter