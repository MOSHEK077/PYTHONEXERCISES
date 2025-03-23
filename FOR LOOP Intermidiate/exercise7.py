"""Example 1: Analyzing Delivery Times
You have a list of delivery times (in minutes) and you want to calculate the average delivery time,
the number of deliveries that were late (assuming a delivery is considered late if it takes more than 30 minutes),
and the fastest and slowest delivery times."""
# List of delivery times in minutes
delivery_times = [25,32,18,45,29,50,20,30,28,35,22]

#Initialize variable 
total_time = 0 
late_deliveries = 0
fastest_delivery = float('inf')
slowest_delivery = float('-inf')
#iterate through the list of delivery times 
for time in delivery_times:
    total_time += time
    if time > 30 :
        late_deliveries += 1
    if time < fastest_delivery :
        fastest_delivery = time
    if time > slowest_delivery :
        slowest_delivery = time
    
average_time = total_time / len(delivery_times)
print("Average Delivery Time : {:.2f} minutes".format(average_time))
print("Number of late deliveries:",late_deliveries)
print("Fastest Delivery Time:", fastest_delivery, "minutes") 
print("Slowest Delivery Time:", slowest_delivery, "minutes")