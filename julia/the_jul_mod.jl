using JSON

out = Dict("payload" => 313)

open("jldata.json", "w") do f
    write(f, JSON.json(out))
end