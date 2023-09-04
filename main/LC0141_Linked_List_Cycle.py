from typing import Optional

from main.ListNode import ListNode


class LC0141_Linked_List_Cycle:
  def hasCycle(self, head: Optional[ListNode]) -> bool:
    lists = set()
    temp = head
    while temp is not None:
      if temp in lists:
        return True
      lists.add(temp)
      temp = temp.next

    return False
