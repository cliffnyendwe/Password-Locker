class Password:
    """
    clas that generates new instances of password
    """

    password_list = []

    def __init__(self,first_name,last_name,email,password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def save_password(self):
        """
        save_password method saves password objects into password_list
        """

        Password.password_list.append(self)

    def delete_password(self):
        """
        delete_password method deletes a saved password from the password_list
        """
        Password.password_list.remove(self)

    @classmethod
    def find_by_email(cls,email):
        '''
        method that takes in an email as,string returns a password that matches that email string
        
        
        Args:
            email:password to be searched
        Returns:
            Password of a person that matches the email
        '''

        for password in cls.password_list:
            if password.email == email:
                return password

    @classmethod
    def password_exist(cls,email):
        '''
        Method that checks if a password exists from the password list.
        Args:
            number: password to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for password in cls.password_list:

            if password.email == email:
               return True

        return False

    @classmethod
    def display_password(cls):
        '''
        method that returns the password list
        '''
        return cls.password_list

    



