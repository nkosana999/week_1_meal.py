def main():
    time = input("What time is it? ")
    return convert(time)



def convert(time):
    time = time.split(":")
    x = int(time[0])

    if  7 <= x <= 8:
        print("breakfast time")
    elif 12 <= x <= 13:
        print("lunch time")
    elif 18 <= x <= 19:
        print("dinner time")
    else:
        None


if __name__ == "__main__":
    main()
