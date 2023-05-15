import csv
import random

def generate_users(num_users):
    users = []
    for i in range(1, num_users + 1):
        username = f"user{i}"
        password = f"password{i}"
        email = f"user{i}@example.com"
        name = f"User {i}"
        users.append([username, password, email, name])
    return users

def write_to_csv(users, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['username', 'password', 'email', 'name'])
        writer.writerows(users)

if __name__ == "__main__":
    num_users = 100
    users = generate_users(num_users)
    write_to_csv(users, 'users.csv')
    print(f"{num_users} users generated and saved to users.csv")