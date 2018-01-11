import subprocess

def sample_function(n):
    print("You entered {}".format(n))

    args = ["julia", "julia/the_jul_mod.jl"]

    with open('julia/julia.log', 'w') as log:
        with subprocess.Popen(args, shell=True, stdout=subprocess.PIPE) as programm:
            for line in programm.stdout:
                log.write(line.decode())
                print(line.decode(), end='')

    return True


if __name__ == "__main__":
    sample_function(5)
