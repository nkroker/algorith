# Reference for learning
#
# check this video: https://youtu.be/lk9AK-ZB4U0?list=PLx2fZyxEuihJ5qBT79H7Mxf3z2E-IoEj0
# Rearguard is the key

def insertion_sort(numbers)
  for runner in (1...numbers.length) do
    swap = numbers[runner]
    rear_guard = runner - 1

    while rear_guard >= 0 && swap < numbers[rear_guard] do
      numbers[rear_guard+1] = numbers[rear_guard]
      rear_guard -= 1
    end

    numbers[rear_guard+1] = swap
  end

  numbers
end



nums = [5, 2, 4, 6, 1, 3]

result = insertion_sort(nums)
puts result
