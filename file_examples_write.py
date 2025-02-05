# lets create a diary
with open("diary.txt", "w") as fp:
    while True:
        text = input("how do you feel today? type q to quit): ")
        if text == "q":
            break
        fp.write(f"{text}\n") # these are the same : fp.write(text + "\n")

with open("diary.txt", "a") as fp:   # la a hace algo pero no se
    while True:
        text = input("how do you feel today? type q to quit): ")
        if text == "q":
            break
        fp.write(f"{text}\n") # these are the same : fp.write(text + "\n")



