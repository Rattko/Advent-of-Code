function action_reward(action :: Union{Char, AbstractString}) :: Int32
    return only(action) - 'W'
end

function first_task() :: Int64
    function play_round(action_me :: AbstractString, action_opponent :: AbstractString) :: Int32
        diff = only(action_me) - only(action_opponent)

        if diff in [21, 24]
            # Win
            return 6
        elseif diff == 23
            # Draw
            return 3
        else
            # Loss
            return 0
        end
    end

    total_score = 0
    open("./input.txt") do file
        for line in eachline(file)
            opponent, me = split(line, " ")

            score = play_round(me, opponent) + action_reward(me)
            total_score += score
        end
    end

    return total_score
end

function second_task() :: Int64
    function play_round(
        action_opponent :: AbstractString, expected_result :: AbstractString
    ) :: Tuple{Char, Int32}
        action_opponent = only(action_opponent)

        if expected_result == "X"
            # Loss
            action_me = action_opponent + (Int(action_opponent + 22) in [88, 89, 90] ? 22 : 25)
            return action_me, 0
        elseif expected_result == "Y"
            # Draw
            return action_opponent + 23, 3
        else
            # Win
            action_me = action_opponent + (Int(action_opponent + 21) in [88, 89, 90] ? 21 : 24)
            return action_me, 6
        end
    end

    total_score = 0
    open("./input.txt") do file
        for line in eachline(file)
            opponent, result = split(line, " ")
            action_me, outcome = play_round(opponent, result)

            score = outcome + action_reward(action_me)
            total_score += score
        end
    end

    return total_score
end

println(first_task())
println(second_task())
