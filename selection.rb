# Traverse over and then swap
def selection_sort(list)
  list.each do |item|
    min_index = list.index(item)

    for matcher in ((min_index + 1)..(list.length - 1)) do
      if list[matcher] < list[min_index]
        min_index = matcher
      end
    end

    tmp = list[min_index]
    list[min_index] = item
    list[list.index(item)] = tmp
  end  
end

# printing out the desired output
list = [5, 7, 14, 3, 13, 10, 4, 15, 6, 8, 11, 1, 9, 12, 2]
puts selection_sort(list)
