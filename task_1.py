class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def insertion_sort(self):
        if not self.head or not self.head.next:
            return

        sorted_head = None
        current = self.head

        while current:
            next_node = current.next
            if not sorted_head or current.data <= sorted_head.data:
                current.next = sorted_head
                sorted_head = current
            else:
                search_node = sorted_head
                while search_node.next and search_node.next.data < current.data:
                    search_node = search_node.next
                current.next = search_node.next
                search_node.next = current
            current = next_node

        self.head = sorted_head


def merge_sorted_lists(list1, list2):
    dummy = Node()
    current = dummy
    current1 = list1.head
    current2 = list2.head

    while current1 and current2:
        if current1.data <= current2.data:
            current.next = current1
            current1 = current1.next
        else:
            current.next = current2
            current2 = current2.next
        current = current.next

    if current1:
        current.next = current1
    if current2:
        current.next = current2

    result = LinkedList()
    result.head = dummy.next
    return result


def main():
    llist_1 = LinkedList()
    llist_2 = LinkedList()

    # Наповнюємо перший список
    llist_1.insert_at_beginning(7)
    llist_1.insert_at_beginning(11)
    llist_1.insert_at_beginning(15)
    llist_1.insert_at_end(20)
    llist_1.insert_at_end(27)

    # Наповнюємо другий список
    llist_2.insert_at_beginning(12)
    llist_2.insert_at_beginning(6)
    llist_2.insert_at_beginning(21)

    print("Зв'язний список:")
    llist_1.print_list()

    # Видалення вузла
    llist_1.delete_node(11)
    print("\nПісля видалення вузла з даними 11:")
    llist_1.print_list()

    # Пошук елемента
    print("\nШукаємо елемент 15:")
    element = llist_1.search_element(15)
    if element:
        print(element.data)

    # Реверсування списку
    llist_1.reverse()
    print("\nРеверсований список:")
    llist_1.print_list()

    # Сортування обох списків
    llist_1.insertion_sort()
    print("\nВідсортований список 1:")
    llist_1.print_list()

    llist_2.insertion_sort()
    print("\nВідсортований список 2:")
    llist_2.print_list()

    # Злиття двох відсортованих списків
    merged_list = merge_sorted_lists(llist_1, llist_2)
    print("\nОб'єднаний список:")
    merged_list.print_list()


if __name__ == "__main__":
    main()