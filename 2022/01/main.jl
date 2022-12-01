function main() :: Tuple{Int64, Int64}
    calories_per_elf = Int32[]

    open("./input.txt") do file
        total_calories = 0

        for line in eachline(file)
            if line == ""
                push!(calories_per_elf, total_calories)
                total_calories = 0

                continue
            end

            total_calories += parse(Int32, line)
        end
    end

    calories_cumsum = cumsum(sort(calories_per_elf, rev=true))

    return calories_cumsum[1], calories_cumsum[3]
end

println(main())
