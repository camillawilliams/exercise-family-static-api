
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members =  [{
            "id":3, 
            'first_name':"Camilla",  
            'last_name': "williams", 
            'age':22, 
            'lucky_numbers':[7, 5, 77]
            }] 
        
    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        return self._members.append(member)

    def delete_member(self, id):
        # fill this method and update the return
       for index in range(len(self._members)):
        if id == self._members[index].id:
            removed = self._members.pop(index)
            return removed
#  if the id equals (==) what is in the self._members list
# we are searching the the id in the list and then pop method takes it out and returns/shows what it took out
    def get_member(self, id):
        # fill this method and update the return
        for index in range(len(self._member)):
         if id == self._members[i].id:
            return self._members[i]

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
