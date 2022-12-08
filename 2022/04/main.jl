function main() :: Tuple{Int32, Int32}
    total_overlap, partial_overlap = 0, 0
    open("./input.txt") do file
        for line in eachline(file)
            a, b, c, d = parse.(Int, split(line, [',', '-']))
            first, second = Set(a:b), Set(c:d)

            # Check if one is a subset of another
            if first <= second || second <= first
                total_overlap += 1
            end

            if ! isempty(intersect(first, second))
                partial_overlap += 1
            end
        end
    end

    return total_overlap, partial_overlap
end

println(main())
