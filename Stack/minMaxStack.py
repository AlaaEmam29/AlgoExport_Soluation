class MinMaxStack:
    def __init__(self):
        self.items = []
    def peek(self):
        # Write your code here.
        if self.is_empty():
            return 
        return self.items[-1]['num']

    def pop(self):
        # Write your code here.
        if self.is_empty():
            return 
        return self.items.pop()['num']

    def push(self, number):
        min_num = number
        max_num = number
        if not self.is_empty():
            min_num = min(self.items[-1]['min'] , number)
            max_num = max(self.items[-1]['max'], number)
        self.items.append({'num': number
                            ,'min': min_num
                            ,'max': max_num
                            })

    def getMin(self):
        # Write your code here.
        return self.items[-1]['min']
    def getMax(self):
        # Write your code here.
        return self.items[-1]['max']
    
    def is_empty(self):
        return not self.items