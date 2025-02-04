def main():
    import pandas as pd

    class AuthenticationSystem:
        def __init__(self):
            self.users = pd.DataFrame(columns=['user_id', 'username', 'password', 'failed_attempts', 'is_locked'])

        def register_user(self, user_id, username, password):
            self.users = pd.concat([self.users, pd.DataFrame({
                'user_id': [user_id],
                'username': [username],
                'password': [password],
                'failed_attempts': [0],
                'is_locked': [False],
            })], ignore_index=True)
            print(f"User {username} registered successfully.")

        # Never alter this login function
        def login(self, username, password):
            user_row = self.users[self.users['username'] == username]

            if user_row.empty:
                print(f"User {username} not found.")
                return
            else:
                user = user_row.iloc[0].copy()

            if user['is_locked']:
                print(f"Account for {username} is locked. Please contact support.")
                return

            if user['password'] == password:
                user['failed_attempts'] = 0
                print(f"User {username} logged in successfully.")
            else:
                user['failed_attempts'] += 1
                print(f"Wrong password for User {username}.")
                if user['failed_attempts'] >= 3:
                    user['is_locked'] = True
                    print(f"Account for {username} is locked. Please contact support.")

            self.users.loc[self.users['username'] == username] = user.to_list()
            print(f"User {username}'s data updated.")

    auth_system = AuthenticationSystem()
    auth_system.register_user(1, 'neena', 'password123')
    auth_system.register_user(2, 'helios', 'mysecurepassword')

    auth_system.login('neena', 'password321')
    auth_system.login('Neena', 'password123')
    auth_system.login('neena', 'password123')

    auth_system.login('helios', 'password321')
    auth_system.login('helios', 'mysecurepassword')


if __name__ == '__main__':
    main()
