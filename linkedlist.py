class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0 # To find the list length in another way

        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.

        Run Time (Best and worst): O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""

        items = [] # O(1) only one step to do this
        # Start at head node
        current_node = self.head  # O(1) only one step to do this
        # Loop until node is None, meaning at the end
        while current_node != None:   # O(n) loop through all of the list
            items.append(current_node.data) # O(1) only one step to do this
            # Now the node is equal to the node.next to move to the next item, also, last step current_node points to None
            current_node = current_node.next  # O(1) only one step to do this
        return items   # O(1) only one step to do this

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        """Run time(Best and Worst): O(1) because only have to check once wether the head exists """

        # Checking wether the head exists
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        # TODO: Running time: O(???) Why and under what conditions?
        Run time(Best and Worst): O(n) because have to go through all of the nodes to get the number of items in list
        OR Run Time(Best and Worst Case) = O(1) because just returning the size property"""

        # TODO: Loop through all nodes and count one for each

        # count = 0
        # # Set current node to point to head node, rememeber self.head points to a Node object, which has data and next
        # current_node = self.head

        # # Iterate through all the list until current_node is not None, because if none then last item
        # while current_node is not None: # Meaning the head exists
        #     current_node = current_node.next # This is only possible becauase not None, so must/can have .next property
        #     count += 1
        # return count

        # Can just return self.count as alternate way of finding length
        return self.size

    def append(self, item):
        """Insert the given item at the tail of this linked list."""
        # TODO: Running time: O(???) Why and under what conditions?
        """
        Run time(Best and Worst): O(1) because the tail can be accessed in one step"""

        # TODO: Create new node to hold given item
        # TODO: Append node after tail, if it exists

        new_node = Node(item) # Create a new Node object with the specified item

        if self.tail is not None:
            # Appending node after tail, if tail exists, and tail currently points at None
            self.tail.next = new_node # Note! Can only do this if tail is NOT None, meaning it exists
            self.tail = new_node # Update the self.tail to the newly last node, updating the tail
            self.size += 1
        else:
            self.head = new_node # If no tail then set the self.head to point to newly created Node object
            self.tail = new_node # And self.tail also equals this newly created node
            self.size += 1

    def prepend(self, item):
        """Insert the given item at the head of this linked list."""
        # TODO: Running time: O(???) Why and under what conditions?

        """Run time(Best and Worst): O(1) because like head, the head can be accessed in one step"""

        # TODO: Create new node to hold given item
        # TODO: Prepend node before head, if it exists

        new_node = Node(item)

        if self.head != None:
            new_node.next = self.head # Remember self.head is a Node object
            self.head = new_node # Updates head to be this new node
            self.size += 1
        else:
            self.tail = new_node # Sets/assigns head to be this new node
            self.head = new_node # Sets/assigns tail to be this new node
            self.size += 1

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality."""

        # TODO: Best case running time: O(???) Why and under what conditions?
        # TODO: Worst case running time: O(???) Why and under what conditions?
        """
        Run time(Best Case): O(1), becuse if you let lucky you can find it running just once
        Run time(Worst Case): O(n), becuase you have to go every single one"""

        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function

        current_node = self.head

        # Check make sure there's a list, when current node changes to tail.next that equals to None, while loop terminates
        while current_node != None:
            if quality(current_node.data) == True:
                return current_node.data
            else:
                current_node = current_node.next

        return None # To catch if item doesn't exist in list

    def replace(self, list_item, new_item):
        """Replaces an item in the list with a new item"""
        """Run time(Worst): O(n) because have to go through the entire list"""
        """Run time(Best): O(1) because found on first instance"""

        current_node = self.head

        while current_node is not None:
            if current_node.data == list_item: # If the data in the node is found in list.
                current_node.data = new_item # Sets the current_node data to be the new stuff
                return
            else:
                current_node.current_node.next # To change pointer to next node

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError."""
        """TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?
        Run time(Best Case): O(1), beacuse finds it after the head pointer, item can be deleted by running just once
        Run time(Worst Case): O(n), becuase you have to go every single one to find it and delete"""

        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))

        previous_node = None
        current_node = self.head

        if self.is_empty():
            raise ValueError('Item not found: {}'.format(item))

        elif self.head == self.tail: # If there is only one node in the list
            if current_node.data == item:
                self.head = None # This to delete both the pointers of head and tail, because only have one node in entire list
                self.tail = None
                self.size -= 1
            else:
                raise ValueError('Item not found: {}'.format(item)) # If item is not in one item list

        else:
            while current_node is not None: # To traverse through list, tail(end) points to None
                # If the item found in list to be removed, then executed
                if current_node.data == item:
                    if previous_node is None: # To remove item at the head cause head doesn't have previous node
                        self.head = current_node.next # Resets so head points to the node right after head
                        self.size -= 1
                        # if current_node == self.tail: # To remove at the tail
                        #     self.tail = previous_node
                    # Removing item from tail(current_node), b/c tail.next points to None
                    elif current_node.next is None:
                        previous_node.next = None # Then deletes previous node's next pointer
                        self.tail = previous_node # Update tail to point to the previous node
                        self.size -= 1
                    # To remove item that is not tail or head
                    else:
                        previous_node.next = current_node.next # Update previous pointer's next to current's next
                        current_node = None # To delete current node, when something = None is delete
                        self.size -= 1
                    return # Finished deleting
                # If item not yet found so moving to next node
                else:
                    previous_node = current_node
                    current_node = current_node.next

            raise ValueError('Item not found: {}'.format(item)) # To make sure the item is in the list after going through the list



def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
