function read_towers(lines :: Vector{String}) :: Vector{Vector{Char}}
    towers = [Char[] for _ in range(1, 10)]

    for line in lines[1:8]
        for (i, char) in enumerate(line[2:4:end])
            if char != ' '
                append!(towers[i], char)
            end
        end
    end

    return towers
end

function first_task() :: String
    local towers :: Vector{Vector{Char}}

    open("./input.txt") do file
        lines = readlines(file)
        towers = read_towers(lines)

        for line in lines[11:end]
            amount, from, to = filter(!=(nothing), tryparse.(Int, split(line, ' ')))

            for _ in range(1, amount)
                crate = popfirst!(towers[from])
                pushfirst!(towers[to], crate)
            end
        end
    end

    return String([tower[1] for tower in towers if length(tower) > 0])
end

function second_task() :: String
    local towers :: Vector{Vector{Char}}

    open("./input.txt") do file
        lines = readlines(file)
        towers = read_towers(lines)

        for line in lines[11:end]
            amount, from, to = filter(!=(nothing), tryparse.(Int, split(line, " ")))

            crates = towers[from][1:amount]
            towers[to] = [crates; towers[to]]
            towers[from] = towers[from][amount + 1:end]
        end
    end

    return String([tower[1] for tower in towers if length(tower) > 0])
end

println(first_task())
println(second_task())
