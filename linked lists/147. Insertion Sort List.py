def insertionSortList(head: Optional[ListNode]) -> Optional[ListNode]:
    def ll_to_arr(head):
        curr = head
        arr = []
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return arr

    # insertion sort
    nums = ll_to_arr(head)

    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1

        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = key
    # back to ll
    curr = head
    i = 0
    while curr:
        curr.val = nums[i]
        i += 1
        curr = curr.next
    return head
