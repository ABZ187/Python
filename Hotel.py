roomdict = {"101": False, "102": False, "103": True, "104": False, "105": True, "201": True, "202": True, "203": True,
            "204": True, "205": True}

A_class = ["101", "102", "201", "202"]
AP_class = ["103", "104"]
P_class = ["203", "204"]
G_class = ["105", "205"]

roomarray = ["101", "102", "103", "104", "105", "201", "202", "203", "204", "205"]

def availroom():
    rno = input("Enter room no. to check availability\t")
    if rno in roomarray:
        if not roomdict[rno]:
            accommodation = int(input(f"Room no {rno} is available, Press 1 , enter for accommodation "))
            if accommodation == 1:
                roomdict[rno]=True
            bill(rno)
        else:
            print(f"Room  no. {rno} not available.")


def bill(rno):
    numberOfDays = int(input("Enter the number days you want to stay "))
    if rno in A_class:
        amount = numberOfDays * 6000 * 1.09
        print(f"Total bill for {numberOfDays} days in A class is USD {amount}")
    if rno in AP_class:
        amount = numberOfDays * 5000 * 1.09
        print(f"Total bill for {numberOfDays} days in A class Premium is USD {amount}")
    if rno in P_class:
        amount = numberOfDays * 4000 * 1.09
        print(f"Total bill for {numberOfDays} days in Premium class is USD {amount}")
    if rno in G_class:
        amount = numberOfDays * 3000 * 1.09
        print(f"Total bill for {numberOfDays} days in Gold class is USD {amount}")


availroom()
