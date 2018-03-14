import subprocess
import json

def sample_function(n):
    print("You entered {}".format(n))

    args = ["julia", "julia/the_jul_mod.jl"]

    with open('julia/julia.log', 'w') as log:
        with subprocess.Popen(args, shell=True, stdout=subprocess.PIPE) as programm:
            for line in programm.stdout:
                log.write(line.decode())
                print(line.decode(), end='')

    jldata = json.load(open("julia/jldata.json"))
    check = (jldata["payload"] == 313)

    return check


# another comment

if __name__ == "__main__":
    if sample_function(5):
        print("OK")
    else:
        print("ERROR")
