class ListRecursion:
    def print_sentence(lst):
        if lst is None or " ":
            return lst
        if len(lst) ==1:
            print (lst[0] + ". " ) # end of the sentence, add a period and space.
        else:
            print(lst[0]+ " ", end=" ")
            ListRecursion.print_sentence(lst[1:])  # Recursive
        

    def reverse(lst):
        if lst is None or lst ==[]:
            return lst
        reversed = ListRecursion.reverse(lst[1:])
        return reversed + [lst[0]]
        

    def remove_every_other(lst):
        if lst is None or lst ==[]:
            return lst
        if len(lst) == 1:
            return lst
        removed = ListRecursion.remove_every_other(lst[2:])
        return [lst[0]] + removed
    
    def maximum(lst):
        if lst is None or lst == []:
            return lst
        if len(lst) ==1:
            return lst[0]
        max_lst = ListRecursion.maximum(lst[1:])
        if lst[0]> max_lst:
            return lst[0]
        else:
            return max_lst

if __name__ == "__main__":
   print_list = ListRecursion.print_sentence(['The', 'quick', 'brown', 'fox'])
   print(f"print: {print_list}")
   Reverse = ListRecursion.reverse([1,2,3,4,5])
   print(f'Reversed: {Reverse}')
   removed = ListRecursion.remove_every_other([1,2,3,4,5,6])
   print(removed)
   max_list = ListRecursion.maximum([1,100,300,2, 6000])
   print(f'max: {max_list}')