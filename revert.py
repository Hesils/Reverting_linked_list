class LinkedNode:
    def __init__(self, value, link):
        self.value = value
        self.link = link

def createLinkedListe():
    head = None
    act = None
    act = LinkedNode(2, None)
    head = LinkedNode(1, act)
    for i in range(10):
        tmp = LinkedNode(i + 3, None)
        act.link = tmp
        act = tmp
    return head

def printLinkedListe(head):
    tmp = head
    while tmp.link != None:
        print("value : " + str(tmp.value))
        tmp = tmp.link

def revertLinkedListe(head):
    pass

def main():
    head = createLinkedListe()
    printLinkedListe(head)

if __name__ == "__main__":
    main()