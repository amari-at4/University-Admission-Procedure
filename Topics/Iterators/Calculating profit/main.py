print("\n".join([" ".join([month, str(revenue - cost)]) for month, revenue, cost in zip(months, revenues, costs)]))
