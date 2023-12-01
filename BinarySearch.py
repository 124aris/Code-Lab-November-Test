# A List is provided with the values:
# List = [-947, -836, -298, -265, -165, 157, 264, 265, 271, 429, 518, 714, 836, 926]
# Write a program code for the implementation of a Function BinarySearch() which takes
# “SearchValue” and the list as arguments, and return the index of the search value, if
# found. If the search value is not in the list, the function should print out an appropriate message and return -1.
# *Write program in file BinarySearch.py*

def BinarySearch(SearchValue, Array):
    Low = 0;
    High = len(Array) - 1;
    while Low <= High:
        Mid = (Low + High) // 2;
        if Array[Mid] == SearchValue:
            return Mid;
        elif Array[Mid] < SearchValue:
            Low = Mid + 1;
        else:
            High = Mid - 1;
    print(f"{SearchValue} Not Found In The List.");
    return -1;

MyList = [-947, -836, -298, -265, -165, 157, 264, 265, 271, 429, 518, 714, 836, 926];
ValueToSearch = int(input('Value To Search:'));
Result = BinarySearch(ValueToSearch, MyList);
if Result != -1:
    print(f"{ValueToSearch} Found At Index: {Result}");