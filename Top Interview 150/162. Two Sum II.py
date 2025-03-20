def twoSum(numbers, target):
    pointerHigher = 0
    pointerLower = len(numbers) - 1
    for i in range(len(numbers)):
        if numbers[pointerHigher] + numbers[pointerLower] == target:
            return [pointerHigher + 1, pointerLower + 1]
        if numbers[pointerHigher] + numbers[pointerLower] > target:
            pointerLower -= 1
        else: 
            pointerHigher += 1
