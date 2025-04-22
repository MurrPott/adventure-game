class Item():
    def __init__(self,item_name):
        name = item_name
        description = None
        role = None

    def set_description(self, item_description):
        self.description = item_description

    def get_description(self):
        return self.description

    def describe(self):
        print(self.description)

    def set_name(self):
        self.name = self.item_name

    def get_name(self):
        return self.name

    def set_role(self,role):
        self.role = role

    def get_role(self):
        return self.role

    def print_role(self):
        print(self.role)


