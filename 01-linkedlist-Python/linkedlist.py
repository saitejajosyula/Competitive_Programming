"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        # Your code goes here

        current = self.head

        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
        # if self.head == None:
        #     newNode = Element(new_element)
        #     self.head = newNode
        # else:
        #     current = self.head
        #     while current.next:
        #         current = current.next
            
        #     current.next = new_element
        #     # self.__sizeof__ = self.__sizeof__ + 1

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        # Your code goes here
        current = self.head

        for i in range(1, position):

            if current.value == None:
                return None
            else:
                current = current.next
        return current.value
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        # Your code goes here

        if position == 1:
            #     prev_next = self.head
            #     new_element.next = prev_next
            #     self.head = new_element
            #     return
            
            # current = self.head
            # for i in range(1, position):

            #     prev_next = current.next
            #     new_element.next = prev_next
            #     current.next = new_element

            newNode = Element(new_element)

            newNode.next = self.head
            
            self.head = newNode
        
        elif position == self.__sizeof__:
            self.append(self.value)
        else:

            current = self.head
            count = 0
            while current != None:

                if count == position - 2:
                    break
                else:
                    count = count + 1
                    current = current.next

            newNode = Element(self.value)
            newNode.next = current.next
            current.next = newNode

        
    
    
    def delete(self, value):
        """Delete the first node with a given value."""
        # Your code goes here
        
        if self.head.value == value:

            further_next = self.head.next
            self.head = further_next
            return
        
        current = self.head

        while current.next is not None:
            if current.next.value == value:
                further_next = current.next.next 
                current.next = further_next
                return
            else:
                current = current.next