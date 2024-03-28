#1

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
common_items=our_routes.intersection(competitor_routes)
print(common_items)

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
difference_set=our_routes.difference(competitor_routes)
print(difference_set)

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
difference_set2=competitor_routes.difference(our_routes)
print(difference_set2)

#2

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
unique_id=set(customer_ids)
print(unique_id)