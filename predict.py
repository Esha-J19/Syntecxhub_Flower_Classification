import joblib

model = joblib.load("flower_model.pkl")

while True:

    print("\nFlower Classification")
    print("1. Predict Flower")
    print("2. Exit")

    choice = input("Choose an option: ")

    if choice == "1":

        sl = float(input("Sepal Length: "))
        sw = float(input("Sepal Width: "))
        pl = float(input("Petal Length: "))
        pw = float(input("Petal Width: "))

        pred = model.predict([[sl, sw, pl, pw]])

        print(f"\nPredicted Flower: {iris.target_names[pred[0]]}")

    elif choice == "2":
        print("Exited")
        break

    else:
        print("Invalid choice")