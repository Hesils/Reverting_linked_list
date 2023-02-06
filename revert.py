class LinkedNode:
    def __init__(self, value, link):
        self.value = value
        self.link = link

def createLinkedListe(len):
    head = None
    act = None
    act = LinkedNode(2, None)
    head = LinkedNode(1, act)
    for i in range(len - 2):
        tmp = LinkedNode(i + 3, None)
        act.link = tmp
        act = tmp
    return head

def printLinkedListe(head):
    tmp = head
    while tmp != None:
        print("value : " + str(tmp.value))
        tmp = tmp.link

def reverseListe(head):
    prev = None
    current = head
    while current:
        next = current.link
        current.link = prev
        prev = current
        current = next
    return prev
    

def main():
    head = createLinkedListe(100)
    printLinkedListe(head)
    print("\n\n")
    reversed = reverseListe(head)
    printLinkedListe(reversed)

if __name__ == "__main__":
    main()