from users.models import User
 
dummy_data = [
        {'first_name': 'Alice', 'last_name': 'Williams', 'email': 'alice.williams@example.com'},
        {'first_name': 'Charlie', 'last_name': 'Brown', 'email': 'charlie.brown@example.com'},
        {'first_name': 'Eva', 'last_name': 'Johnson', 'email': 'eva.johnson@example.com'},
        {'first_name': 'David', 'last_name': 'Miller', 'email': 'david.miller@example.com'},
        {'first_name': 'Sophie', 'last_name': 'Clark', 'email': 'sophie.clark@example.com'},
        {'first_name': 'Michael', 'last_name': 'Davis', 'email': 'michael.davis@example.com'},
        {'first_name': 'Olivia', 'last_name': 'Taylor', 'email': 'olivia.taylor@example.com'},
        {'first_name': 'Samuel', 'last_name': 'Moore', 'email': 'samuel.moore@example.com'},
        {'first_name': 'Emily', 'last_name': 'Hill', 'email': 'emily.hill@example.com'},
        {'first_name': 'Daniel', 'last_name': 'Wright', 'email': 'daniel.wright@example.com'},
            ]

for index,user in enumerate(dummy_data):
        u = User(first_name=dummy_data[index]['first_name'],last_name=dummy_data[index]['last_name'],email=dummy_data[index]['email'])
        u.save()