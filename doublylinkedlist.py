class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __repr__(self) -> str:
        if self.head is None:
            return "[]"
        else:
            last = self.head

            return_string = f"[{last.value}"

            while last.next:
                last = last.next
                return_string += f", {last.value}"
            return_string += "]"

            return return_string
        
    def __contains__(self, value):
        last = self.head
        while last is not None:
            if last.value == value:
                return True
            last = last.next
        return False

    def __len__(self):
        last = self.head
        counter = 0
        while last is not None:
            counter += 1
            last = last.next
        return counter

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            self.size = 1
        else:
            last_node = Node(value)
            last_node.previous = self.tail
            self.tail.next = last_node
            self.tail = last_node
            self.size += 1
        
    def prepend(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            first_node = Node(value)
            first_node.next = self.head
            self.head.previous = first_node
            self.head = first_node
            self.size += 1

    def insert(self, value, index):
        self.size += 1

        if index == 0:
            self.prepend(value)
        else:
            if self.head is None:
                raise ValueError("Index out of bounds")
            else:
                last = self.head

                for i in range(index-1):
                    if last.next is None:
                        raise ValueError("Index out of bounds")
                    last = last.next

                new_node = Node(value)
                new_node.next = last.next
                new_node.previous = last
                if last.next is not None:
                    last.next.previous = new_node
                last.next = new_node

    def delete(self, value):
        last = self.head

        if last is not None:
            self.size -= 1
            if last.value == value:
                self.head = last.next
            else:
                while last.next:
                    if last.next.value == value:
                        if last.next.next is not None:
                            last.next.next.previous = last
                        last.next = last.next.next
                        break
                    last = last.next

    def pop(self, index):
        if self.head is None:
            raise ValueError("Index out of bounds")
        else:
            self.size -= 1
            last = self.head

            for i in range(index-1):
                if last.next is None:
                    raise ValueError("Index out of bounds")
                last = last.next
            
            if last.next is None:
                raise ValueError("Index out of bounds")
            else:
                if last.next.next is not None:
                    last.next.next.previous = last
                last.next = last.next.next

    def get(self, index):
        if self.head is None:
            raise ValueError("Index out of bounds")
        else:
            last = self.head
            for i in range(index-1):
                if last.next is None:
                    raise ValueError("Index out of bounds")
                last = last.next
            return last.value

    def get_size(self):
        return f"size:  {self.size}"


if __name__ == "__main__":
    ll = LinkedList()

    ll.append(10)
    ll.insert(5, 1)
    ll.insert(19, 1)
    ll.insert(23, 1)
    ll.insert(99, 1)
    ll.insert(14, 1)
    ll.insert(35, 1)
    ll.insert(86, 1)

    ll.prepend(100)

    ll.insert(200, 1)

    ll.delete(18)

    ll.pop(1)

    print(ll)
    print(ll.get(1))
    print(99 in ll)
    print(880 in ll)
    print(200 in ll)
    print(ll.get_size())