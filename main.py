class Node:
    def __init__(self, data=None, _next=None):
        self.data = data
        self._next = _next


class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def insert_at_back(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        else:
            count = self.head
            while count._next:
                count = count._next
            count._next = Node(data, None)

    def _print(self):
        count = self.head
        text = ''

        while count:
            text+=str(count.data)+'-->'
            count = count._next

        print(text)

    def make_linked_list(self, _list):
        self.head = None
        for element in _list:
            self.insert_at_back(element)

    def get_length(self):
        temp = self.head
        count = 0
        while temp:
            count+=1
            temp = temp._next
        return count

    def remove_at(self, index):
        if index == -1 or index > self.get_length():
            raise Exception('index error!')
        elif index == 0:
          self.head = self.head._next()
        else:
            count = 0
            temp = self.head
            while temp:
                if count == index-1:
                    temp._next = temp._next._next
                    break
                else:
                    temp = temp._next

    def insert_at_values(self, index, value):
        if index == -1 or index > self.get_length():
            raise Exceprion('index error')
        elif index == 0:
            self.insert_at_front(value)
        else:
            counter = 0
            temp = self.head
            while temp:
                if counter == index-1:
                    node = Node(value, temp._next)
                    temp._next = node
                    break
                temp = temp._next
                counter+=1
 
    def insert_after_values(self, data_after, data_insert):
        temp = self.head
        while temp:
            if temp.data == data_after:
                node = Node(data_insert, temp._next)
                temp._next = node
                break
            else:
                temp = temp._next
    
    def remove_by_value(self, data):
        temp = self.head
        flag = temp
        while temp:
            if temp.data == data:
                flag._next = flag._next._next
                break
            elif temp._next is None:
                print('no data!')
                break
            else:
                flag = temp
                temp = temp._next

if __name__ == '__main__':
    linked_list = Linkedlist()
    linked_list.make_linked_list(['banana', 'mango', 'grapes', 'orange'])
    linked_list.insert_after_values('mango', 'apple')
    linked_list._print()
    linked_list.remove_by_value('orange')
    linked_list._print()
    linked_list.remove_by_value('figs')
    linked_list._print()
