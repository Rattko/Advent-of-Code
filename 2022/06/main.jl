function main(window_size :: Int64) :: Int64
    open("./input.txt") do file
        line = readline(file)

        for i in range(1, length(line))
            window = line[i:i + window_size - 1]

            if length(window) == length(Set(window))
                return i + window_size - 1
            end
        end
    end
end

println(main(4))
println(main(14))
