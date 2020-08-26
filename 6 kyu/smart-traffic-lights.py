# Your friend Bob is working as a taxi driver. After working for a month he is frustrated in the city's traffic lights.
# He asks you to write a program for a new type of traffic light. It is made so it turns green for the road with the most congestion.

# Example: There are 42 cars waiting on 27th ave. There are 72 cars waiting on 3rd st.
# Since there are more cars on 3rd st, the light turn green for that street.

# You don't need to worry about the process of detecting cars yet.

class SmartTrafficLight():
    def __init__(self, st1, st2):
        self.firststreet = st1[1]
        self.firststreetcars = st1[0]
        self.secondstreet = st2[1]
        self.secondstreetcars = st2[0]
    def turngreen(self):
        if (self.firststreetcars > self.secondstreetcars):
            self.firststreetcars = 0
            return self.firststreet
        elif (self.secondstreetcars > self.firststreetcars):
            self.secondstreetcars = 0
            return self.secondstreet
        else:
            return None
