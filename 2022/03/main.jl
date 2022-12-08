function get_priority(char :: Char) :: Int32
    return findfirst(item -> item == char, ['a':'z'; 'A':'Z'])
end

function first_task() :: Int32
    total_priorities = 0
    open("./input.txt") do file
        for line in eachline(file)
            half = div(length(line), 2)
            first, second = Set(line[1:half]), Set(line[half+1:end])

            total_priorities += get_priority(collect(intersect(first, second))[1])
        end
    end

    return total_priorities
end

function second_task() :: Int32
    total_priorities = 0
    open("./input.txt") do file
        lines = readlines(file)

        for (first, second, third) in zip(lines[1:3:end], lines[2:3:end], lines[3:3:end])
            first, second, third = Set(first), Set(second), Set(third)

            total_priorities += get_priority(collect(intersect(first, second, third))[1])
        end
    end

    return total_priorities
end

println(first_task())
println(second_task())
