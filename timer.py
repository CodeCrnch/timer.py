import time


def countdown(user_time):
   while user_time >= 1:
       mins, secs = divmod(user_time, 60)
       timer = "{:02d}:{:02d}".format(mins, secs)
       print(timer, end="\r \n")
       time.sleep(1)
       user_time -= 1
   print("Subscribe!")


if __name__ == "__main__":
   
   user_time = int(input("Add the time in seconds: "))
   countdown(user_time)
