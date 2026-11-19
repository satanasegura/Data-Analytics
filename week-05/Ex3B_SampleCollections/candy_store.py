candies = ("lollipops", "gummies", "gums")
flavors = ("cherry", "grape", "orange")

options = {
    f"{flavors[1]} {candies[0]}",
    f"{flavors[0]} {candies[2]}",
    f"{flavors[2]} {candies[1]}"

}
for _ in range(3):
    print("Today's candy options include:")
    print(options)