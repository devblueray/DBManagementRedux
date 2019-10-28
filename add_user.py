class AddUserToGroup:

    def __init__(self, user):
        self.user = user
    
    def check_for_existing_password(self):
        response = self.table.get_item({Key='user': self.user})
        try: 
            if self.user in response['Item']['user']:
                return True
            else:
                return False

    def create_user_with_existing_password(self):
        pass

    def create_user_with_random_password(self):
        pass

    def remove_password_from_db(self):
        pass

    def check_database_for_user(self):
        pass

    def convert_long_username(self):
        if len(self.origuser) <= 16:
            return self.origuser
        split_name = self.origuser.split('.')
        if len(split_name) > 2:
            middle_name = [names for names in split_name[1:-1]][0]
            split_name = self.origuser.split('.')
            short_name = f'{split_name[0]}.{middle_name[0]}.{split_name[-1]}'
            if len(short_name) <= 16:
                self.create_tag(short_name)
                return short_name
        else:
            short_name = f'{split_name[0][0]}.{split_name[-1]}'
            if len(short_name) <= 16:
                self.create_tag(short_name)
                return short_name

    def create_iam_tag(self, short_name):
        self.iam.tag_user(
            UserName=self.origuser,
            Tags=[{
                'Key': 'db_user',
                'Value': short_name
            }])

    def _log(self)
